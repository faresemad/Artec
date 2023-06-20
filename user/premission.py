from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == "user"


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == "student_review"


class IsApproved(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == "student_approved"


class IsRejected(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == "student_rejected"
