from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Issue
from django.contrib.auth import get_user_model
from django.db.models import Avg, F, ExpressionWrapper, DurationField
from django.utils import timezone
from django.contrib import messages

User = get_user_model()

def home_view(request):
    total_issues = Issue.objects.count()
    completed_issues = Issue.objects.filter(status='Completed').count()
    resolution_rate = (completed_issues / total_issues * 100) if total_issues > 0 else 0
    
    # Calculate Avg Response Time
    completed_issues_qs = Issue.objects.filter(status='Completed', completed_at__isnull=False)
    avg_time = "N/A"
    if completed_issues_qs.exists():
        # MongoDB backend might not support aggregate duration directly efficiently depending on version
        # But we try standard Django ORM approach
        annotated = completed_issues_qs.annotate(
            duration=ExpressionWrapper(F('completed_at') - F('created_at'), output_field=DurationField())
        )
        avg_duration = annotated.aggregate(Avg('duration'))['duration__avg']
        if avg_duration:
            hours = int(avg_duration.total_seconds() / 3600)
            avg_time = f"{hours}h"
    
    context = {
        'issues_reported': total_issues,
        'resolution_rate': round(resolution_rate, 1),
        'avg_response_time': avg_time,
        'active_citizens': User.objects.count(),
    }
    return render(request, 'home.html', context)

def how_it_works_view(request):
    return render(request, 'how_it_works.html')

@login_required
def dashboard_view(request):
    user = request.user
    
    if user.role == 'Admin':
        context = {
            'user': user,
            'total_issues': Issue.objects.count(),
            'pending_issues': Issue.objects.filter(status='Pending').count(),
            'resolved_issues': Issue.objects.filter(status='Completed').count(),
            'assigned_issues': Issue.objects.filter(status__in=['Assigned', 'In Progress']),
            'recent_issues': Issue.objects.all().order_by('-created_at')[:5],
            'users_count': User.objects.count(),
            'staff_count': User.objects.filter(role='Staff').count(),
            'all_users': User.objects.all().order_by('-date_joined'),
        }
        return render(request, 'dashboard/admin.html', context)
    
    elif user.role == 'Staff':
        context = {
            'user': user,
            'assigned_issues': Issue.objects.filter(assigned_to=user, status__in=['Assigned', 'In Progress']),
            'completed_issues': Issue.objects.filter(assigned_to=user, status='Completed'),
        }
        return render(request, 'dashboard/staff.html', context)
    
    else: # User
        context = {
            'user': user,
            'my_issues': Issue.objects.filter(reported_by=user).order_by('-created_at'),
        }
        return render(request, 'dashboard/user.html', context)

@login_required
def update_issue_status_view(request, pk):
    # Need to import get_object_or_404
    from django.shortcuts import get_object_or_404
    
    issue = get_object_or_404(Issue, pk=pk)
    user = request.user
    
    # Permission Check
    if user.role == 'User' and issue.reported_by != user:
        messages.error(request, "You are not authorized to manage this issue.")
        return redirect('dashboard')
        
    staff_members = User.objects.filter(role='Staff')
    
    if request.method == 'POST':
        if user.role == 'Admin':
            assigned_to_id = request.POST.get('assigned_to')
            status = request.POST.get('status')
            proof = request.FILES.get('completion_proof')
            
            if assigned_to_id:
                try:
                    staff = User.objects.get(id=assigned_to_id)
                    issue.assigned_to = staff
                    if issue.status == 'Pending':
                        issue.status = 'Assigned'
                except User.DoesNotExist:
                    pass
            elif 'assigned_to' in request.POST: # Handle unassigning
                issue.assigned_to = None
                
            if status:
                old_status = issue.status
                issue.status = status
                if status == 'Completed' and old_status != 'Completed':
                    if not proof:
                        messages.error(request, "Please upload completion proof before marking as Completed.")
                        issue.status = old_status
                        return render(request, 'manage_issue.html', {'issue': issue, 'staff_members': staff_members})
                    issue.completion_proof = proof
                    issue.completed_at = timezone.now()
            
            if proof and status != 'Completed':
                issue.completion_proof = proof
                
            issue.save()
            messages.success(request, f"Issue #{issue.report_id} updated successfully.")
            return redirect('dashboard')
            
        elif user.role == 'Staff' and (issue.assigned_to == user or issue.assigned_to is None):
            status = request.POST.get('status')
            proof = request.FILES.get('completion_proof')
            
            if status:
                old_status = issue.status
                issue.status = status
                if status == 'Completed' and old_status != 'Completed':
                    if not proof:
                        messages.error(request, "Please upload completion proof.")
                        issue.status = old_status
                        return render(request, 'manage_issue.html', {'issue': issue, 'staff_members': staff_members})
                    issue.completion_proof = proof
                    issue.completed_at = timezone.now()
            
            if proof and status != 'Completed':
                issue.completion_proof = proof
                
            issue.save()
            messages.success(request, "Status updated successfully.")
            return redirect('dashboard')
            
    return render(request, 'manage_issue.html', {'issue': issue, 'staff_members': staff_members})

@login_required
def report_issue_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        location = request.POST.get('location')
        image = request.FILES.get('image')
        
        if title and description and category and location:
            Issue.objects.create(
                title=title,
                description=description,
                category=category,
                location=location,
                image=image,
                reported_by=request.user
            )
            messages.success(request, 'Issue reported successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill all fields.')
            
    return render(request, 'report_issue.html')

def issue_list_view(request):
    issues = Issue.objects.filter(status__in=['Pending', 'Assigned', 'In Progress']).order_by('-created_at')
    return render(request, 'issue_list.html', {'issues': issues})

def map_view(request):
    return render(request, 'view_map.html')

def issues_json_view(request):
    from django.http import JsonResponse
    issues = Issue.objects.all()
    data = []
    for issue in issues:
        data.append({
            'id': str(issue.id),
            'title': issue.title,
            'location': issue.location,
            'status': issue.status,
            'category': issue.category,
            'description': issue.description,
            'latitude': str(issue.latitude) if issue.latitude else None,
            'longitude': str(issue.longitude) if issue.longitude else None,
            'report_id': issue.report_id,
            'reported_by': issue.reported_by.get_full_name() or issue.reported_by.email
        })
    return JsonResponse(data, safe=False)

def about_us_view(request):
    resolved = Issue.objects.filter(status='Completed').count()
    # Round down to nearest 5 for the display e.g. 12→10, 28→25, 106→105
    resolved_display = (resolved // 5) * 5
    return render(request, 'about_us.html', {
        'resolved_count': resolved,
        'resolved_display': resolved_display,
    })
