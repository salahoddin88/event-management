from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'phone',
            'profile_picture',
        ]
        widgets = {
            'profile_picture': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        """ Add Class : form-control to every fields """
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg form-control-solid mb-3 mb-lg-0',
                'placeholder':  (f'{str(field.replace("_", " "))}').title(),
                'autocomplete' : 'off'
            })



class UpdatePasswordForm(PasswordChangeForm):
    
    def __init__(self, *args, **kwargs):
        """ Add Class : form-control to every fields """
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder':  f'Enter {str(field.replace("_", " "))}',
                'required' : False
            })



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'profile_picture'
        ]
        widgets = {
            'profile_picture': forms.FileInput(),
        }
    
    def __init__(self, *args, **kwargs):
        """ Add Class : form-control to every fields """
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder':  str(field.capitalize().replace("_", " ")) + '...',
            })

