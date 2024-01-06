from django.contrib import admin
from .models import Lead, Agent


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'age']


@admin.register(Agent)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['user']


