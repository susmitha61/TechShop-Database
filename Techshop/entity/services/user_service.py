from entity.exceptions.authentication_exception import AuthenticationException
from entity.exceptions.authorization_exception import AuthorizationException

def access_sensitive_info(user):
    if not user.is_authenticated:
        raise AuthenticationException("User must be logged in to access this information.")
    if not user.has_permission("view_sensitive_info"):
        raise AuthorizationException("User does not have permission to view this information.")
