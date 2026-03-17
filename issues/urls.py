from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('report/', views.report_issue_view, name='report_issue'),
    path('issues/', views.issue_list_view, name='issue_list'),
    path('update-status/<str:pk>/', views.update_issue_status_view, name='update_issue_status'),
    path('map/', views.map_view, name='view_map'),
    path('issues-json/', views.issues_json_view, name='issues_json'),
    path('about-us/', views.about_us_view, name='about_us'),
    path('', views.home_view, name='home'),
]
