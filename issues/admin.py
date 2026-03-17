from django.contrib import admin
from .models import Issue

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'reported_by', 'assigned_to', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')
