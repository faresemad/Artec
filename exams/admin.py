from django.contrib import admin
from .models import MCQExam, DigitalDrawingExam, HandDrawingExam, PracticeDrawingExam


@admin.register(MCQExam)
class MCQExamAdmin(admin.ModelAdmin):
    list_display = ("question", "option1", "option2", "option3", "answer", "college")
    list_filter = ("question", "college")


@admin.register(DigitalDrawingExam)
class DigitalDrawingExamAdmin(admin.ModelAdmin):
    list_display = ("question", "task_description", "college")
    list_filter = ("question", "college")


@admin.register(HandDrawingExam)
class HandDrawingExamAdmin(admin.ModelAdmin):
    list_display = ("question", "task_description", "college")
    list_filter = ("question", "college")


@admin.register(PracticeDrawingExam)
class PracticeDrawingExamAdmin(admin.ModelAdmin):
    list_display = ("question", "task_description", "college")
    list_filter = ("question", "college")
