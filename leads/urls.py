from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    
    # FUNC BASED PATHS
    # path("", views.index, name="index"),
    
    # path("leads", views.leadPage, name="leads"),
    # path("leads/<int:pk>/", views.leadDetailPage, name="lead-detail"),
    # path("create-lead/", views.createLead, name="create-lead"),
    # path("leads/<int:pk>/update/", views.updateLead, name="update-lead"),
    # path("leads/<int:pk>/delete/", views.deleteLead, name="delete-lead"),
    
    # CLASS-BASED VIEWS PATHS
    path("", views.IndexView.as_view(), name="index"),
    path("leads/", views.LeadsPageView.as_view(), name="leads"),
    path("leads/<int:pk>/", views.LeadDetailView.as_view(), name="lead-detail"),
    path("create-lead/", views.LeadCreateView.as_view(), name="create-lead"),    
    path("leads/<int:pk>/update/", views.LeadUpdateView.as_view(), name="update-lead"),    
    path("leads/<int:pk>/delete/", views.LeadDeleteView.as_view(), name="delete-lead"),    
    
]
