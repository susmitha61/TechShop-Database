import unittest
from entity.services.user_service import access_sensitive_info
from entity.exceptions.authentication_exception import AuthenticationException
from entity.exceptions.authorization_exception import AuthorizationException

# Mock User Class
class MockUser:
    def __init__(self, is_authenticated, has_permission):
        self.is_authenticated = is_authenticated
        self.has_permission = has_permission

class TestUserAuthentication(unittest.TestCase):
    def test_access_without_authentication(self):
        user = MockUser(is_authenticated=False, has_permission=lambda x: False)
        with self.assertRaises(AuthenticationException):
            access_sensitive_info(user)

    def test_access_without_authorization(self):
        user = MockUser(is_authenticated=True, has_permission=lambda x: False)
        with self.assertRaises(AuthorizationException):
            access_sensitive_info(user)

    def test_access_with_authorization(self):
        user = MockUser(is_authenticated=True, has_permission=lambda x: True)
        try:
            access_sensitive_info(user)  # Should not raise an exception
        except (AuthenticationException, AuthorizationException):
            self.fail("access_sensitive_info raised an exception for an authorized user.")
