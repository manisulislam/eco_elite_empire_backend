from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('You must provide a valid email address'))

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        if not first_name:
            raise ValueError(_('The First Name must be provided'))
        if not last_name:
            raise ValueError(_('The Last Name must be provided'))
        if email:
            email=self.normalize_email(email)
            self.email_validator(email)
            # normalize the email address by lowercasing the domain
        else:
            raise ValueError(_('The Email must be provided'))
        if not password:
            raise ValueError(_('The Password must be provided'))

        
        user = self.model(
            first_name=first_name,
            last_name=last_name, 
            email=email, 
            **extra_fields)
        user.set_password(password)
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
       
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        if email:
            email=self.normalize_email(email)
            self.email_validator(email)
            # normalize the email address by lowercasing the domain
        else:
            raise ValueError(_('The Email must be provided'))
        if not password:
            raise ValueError(_('The Password must be provided'))

        user=self.create_user(
            first_name,
            last_name,
            email,
            password,
            **extra_fields)
        
        
        user.save()
        return user