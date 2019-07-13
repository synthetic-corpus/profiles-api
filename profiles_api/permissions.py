from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow User to edit their own profile """

    def has_object_permission(self, request, view, obj):
        """ Check if user is attempting to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        """ Does the Requester ID match the ID of the Object in Question? """
        """ If True, this request will allow the requester to make all changes. """
        
        return obj.id == request.user.id