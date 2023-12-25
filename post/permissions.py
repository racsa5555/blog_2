from rest_framework.permissions import BasePermission

class PostStaffPermission(BasePermission):
    """
    Permission check for staff status.
    """

    def has_permission(self, request, view):
        # Проверяем, является ли пользователь персоналом (staff)
        return request.user.is_staff