from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=120)
    password = forms.CharField(label='Hasło', max_length=120, widget=forms.PasswordInput)


class RegisterUserForm(forms.Form):
    username = forms.CharField(label='Login', max_length=120)
    password = forms.CharField(label='Hasło', max_length=120, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Powtórz hasło', max_length=120, widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail")