from django.contrib import admin
from .models import Student, McqAnswer, HandDrawingAnswer, DigitalDrawingAnswer, PracticeDrawingAnswer, StudentResults

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'national_id', 'phone_number', 'college')
    search_fields = ('full_name', 'national_id', 'phone_number', 'college')

@admin.register(McqAnswer)
class McqAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'question', 'answer', 'is_correct')
    search_fields = ('student', 'question', 'answer')

@admin.register(HandDrawingAnswer)
class HandDrawingAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'hand_draw', 'answer')
    search_fields = ('student', 'hand_draw', 'answer')

@admin.register(DigitalDrawingAnswer)
class DigitalDrawingAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'digital_draw', 'answer')
    search_fields = ('student', 'digital_draw', 'answer')

@admin.register(PracticeDrawingAnswer)
class PracticeDrawingAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'practice_draw', 'answer')
    search_fields = ('student', 'practice_draw', 'answer')

admin.site.register(StudentResults)