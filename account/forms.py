from django.forms import Widget, TextInput
from django.contrib.auth.forms import UserCreationForm
# forms.py

from django.contrib.auth.models import User



class BootstrapTextInput(TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})
        kwargs['attrs'].update({'class': 'form-control'})
        super().__init__(*args, **kwargs)


# forms.py

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = BootstrapTextInput()
        self.fields['email'].widget = BootstrapTextInput()
        self.fields['password1'].widget = BootstrapTextInput()
        self.fields['password2'].widget = BootstrapTextInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

