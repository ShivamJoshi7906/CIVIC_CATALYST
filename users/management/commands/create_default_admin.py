from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a default admin user'

    def handle(self, *args, **kwargs):
        email = 'admin@civic.com'
        password = 'admin123'
        
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                username='admin',
                email=email,
                password=password,
                role='Admin'
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin user: {email}'))
        else:
            self.stdout.write(self.style.WARNING(f'Admin user {email} already exists'))
