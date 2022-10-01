from django.contrib import admin

# Register your models here.

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'city', 'state', 'country', 'date_created', 'date_updated')
    # list_filter = ('date_created', 'date_updated')
    # search_fields = ('name', 'email', 'phone', 'address', 'city', 'state', 'country')
    list_per_page = 25
