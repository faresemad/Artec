from django.contrib import admin
from .models import (
    Student,
    McqAnswer,
    HandDrawingAnswer,
    DigitalDrawingAnswer,
    PracticeDrawingAnswer,
    StudentResults,
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "national_id",
        "phone_number",
        "college",
        "up_to_level",
    )
    list_filter = ("full_name", "national_id", "phone_number", "college")


@admin.register(McqAnswer)
class McqAnswerAdmin(admin.ModelAdmin):
    list_display = ("student", "question", "answer", "is_correct", "score")
    list_filter = ("student", "question", "answer")


@admin.register(HandDrawingAnswer)
class HandDrawingAnswerAdmin(admin.ModelAdmin):
    list_display = ("student", "hand_draw", "answer", "score")
    list_filter = ("student", "hand_draw", "answer")


@admin.register(DigitalDrawingAnswer)
class DigitalDrawingAnswerAdmin(admin.ModelAdmin):
    list_display = ("student", "digital_draw", "answer", "score")
    list_filter = ("student", "digital_draw", "answer")


@admin.register(PracticeDrawingAnswer)
class PracticeDrawingAnswerAdmin(admin.ModelAdmin):
    list_display = ("student", "practice_draw", "answer", "score")
    list_filter = ("student", "practice_draw", "answer")


@admin.register(StudentResults)
class ResultsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "mcq_result",
        "digital_art_result",
        "hand_drawing_result",
        "trial_result",
        "up_to_level",
    )
    list_filter = ("user",)
