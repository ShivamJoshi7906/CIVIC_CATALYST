from django.db import models
from django.conf import settings

class Issue(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    CATEGORY_CHOICES = (
        ('Road', 'Roads & Maintenance'),
        ('Electricity', 'Electricity & Power'),
        ('Water', 'Water Supply & Sewage'),
        ('Garbage', 'Garbage & Sanitation'),
        ('Traffic', 'Traffic & Transport'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='issues/', blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reported_issues')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_issues', limit_choices_to={'role': 'Staff'})
    
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    estimated_completion = models.DateField(null=True, blank=True)
    completion_proof = models.ImageField(upload_to='proofs/', null=True, blank=True)
    
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    report_id = models.CharField(max_length=20, unique=True, editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.report_id:
            import string
            import random
            from django.utils.crypto import get_random_string
            while True:
                # Generate a random ID like CIV-1A2B3D4E
                new_id = f"CIV-{''.join(random.choices(string.ascii_uppercase + string.digits, k=8))}"
                if not Issue.objects.filter(report_id=new_id).exists():
                    self.report_id = new_id
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.report_id} - {self.title} - {self.status}"
