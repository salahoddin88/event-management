from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpassword',
        )

    def test_user_creation(self):
        # Test that the user was created successfully
        self.assertEqual(self.test_user.email, 'testuser@example.com')
        self.assertTrue(self.test_user.check_password('testpassword'))

    def test_user_authentication(self):
        # Test user authentication
        user = get_user_model().objects.get(email='testuser@example.com')
        self.assertTrue(user.is_authenticated)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_user_deletion(self):
        # Test user deletion
        user_count_before_delete = get_user_model().objects.count()
        self.test_user.delete()
        user_count_after_delete = get_user_model().objects.count()
        self.assertEqual(user_count_before_delete - 1, user_count_after_delete)
