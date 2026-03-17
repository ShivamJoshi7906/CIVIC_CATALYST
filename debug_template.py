import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'civic.settings')
django.setup()

from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from issues.models import Issue

User = get_user_model()

try:
    factory = RequestFactory()
    request = factory.get('/dashboard/')
    request.user = User.objects.first() or User(username='test', email='test@example.com')
    
    # Needs session for messages
    from django.contrib.sessions.middleware import SessionMiddleware
    middleware = SessionMiddleware(lambda x: None)
    middleware.process_request(request)
    request.session.save()
    
    # Needs messages
    from django.contrib.messages.middleware import MessageMiddleware
    middleware = MessageMiddleware(lambda x: None)
    middleware.process_request(request)

    issues = [
        Issue(title='Test Issue', status='Pending', category='Road', description='Test', reported_by=request.user),
    ]
    
    context = {'my_issues': issues}
    # render_to_string with request to trigger context processors
    rendered = render_to_string('dashboard/user.html', context, request=request)
    print("Template rendered successfully!")
except Exception as e:
    print(f"Error rendering template: {e}")
    import traceback
    traceback.print_exc()
