import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'civic.settings')
django.setup()

from users.models import CustomUser

# Admin Details
email = 'admin@civic.com'
password = 'admin123'
username = 'admin'

if not CustomUser.objects.filter(email=email).exists():
    try:
        user = CustomUser.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name='Admin',
            last_name='User',
            role='Admin'
        )
        print(f"Successfully created admin user: {email}")
    except Exception as e:
        print(f"Error creating admin user: {e}")
else:
    print(f"Admin user {email} already exists.")
