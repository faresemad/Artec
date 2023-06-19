from django.contrib import admin

from .models import College, CollegeDepartment


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("name", "logo", "payment_code")
    list_filter = ("name", "payment_code")


@admin.register(CollegeDepartment)
class CollegeDepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "subtitle", "image")
    list_filter = ("name", "subtitle")
