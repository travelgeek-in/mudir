from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Global permission check for user type admin.
    """
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == 3
        else:
            return False


class IsProvider(permissions.BasePermission):
    """
    Global permission check for user type admin.
    """
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == 3
        else:
            return False


class IsLoggedIn(permissions.BasePermission):
    """
    Global permission check for user type admin.
    """
    def has_permission(self, request, view):
        if hasattr(request.user, 'role'):
            return request.user.role == 3
        else:
            return False
