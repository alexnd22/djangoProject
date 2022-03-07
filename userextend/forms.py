from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, CheckboxInput

from userextend.models import UserExtend


class UserExtendForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'is_adult', 'username']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Enter your phone', 'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Enter your address', 'class': 'form-control'})

        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter password confirmation'
