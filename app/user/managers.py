from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ Manager for user """

    def create_user(
            self, email,
            first_name=None, last_name=None, password=None):
        """Create a new user"""
        if not email:
            raise ValueError('User must have an email id')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """ Create and save a new superuser with given details"""
        user = self.create_user(
            email,
            first_name,
            last_name,
            password
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
