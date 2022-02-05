from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, CharField, PasswordInput
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = EmailField()
    password1= CharField(label='Contraseña', widget=PasswordInput)
    password2= CharField(label='Repetir contraseña', widget=PasswordInput)
   
class Meta:
    model = User
    fields = ['username', 'email', 'passsword1', 'password2']
    help_texts = {k: '' for k in fields}