from django.contrib import admin
from .models import College, CollegeDepartment

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'payment_code')
    search_fields = ('name', 'payment_code')

@admin.register(CollegeDepartment)
class CollegeDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subtitle', 'image')
    search_fields = ('name', 'subtitle')