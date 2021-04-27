from django import forms
from .models import *
from m1 import maths


MATH_SYMBOL = {
    1: "+",
    2: "-",
    3: "*",
    4: '/',
}

#
# STATUSES = (
#     (1, 'Parent'),
#     (2, 'Kid'),
# )
#


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=120)
    password = forms.CharField(label='Hasło', max_length=120, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input'


class RegisterUserForm(forms.Form):
    username = forms.CharField(label='Login', max_length=120)
    password = forms.CharField(label='Hasło', max_length=120, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Powtórz hasło', max_length=120, widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail")

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input'


class NewKidForm(forms.Form):
    username = forms.CharField(label='Login', max_length=120)
    password = forms.CharField(label='Hasło', max_length=120, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Powtórz hasło', max_length=120, widget=forms.PasswordInput)


#
# class UserForm(forms.Form):
#     username = forms.CharField(label='Login', max_length=120)
#     password = forms.CharField(label='Hasło', max_length=120, widget=forms.PasswordInput)
#     repeat_password = forms.CharField(label='Powtórz hasło', max_length=120, widget=forms.PasswordInput)
#     email = forms.EmailField(label="E-mail")
#
#
class EditKidsProfileForm(forms.Form):
    username = forms.CharField(label='login')
    profile_picture = forms.ImageField(label='Zdjęcie profilowe')

    class Meta:
        model = ProfileKid
        fields = ['username', 'profile_picture']

    @property
    def profile(self):
        return f'{self.profile_picture}'



class ProfileParentForm(forms.Form):
    username = forms.CharField()
    # profile_picture = forms.ImageField()
    # points_counter = forms.IntegerField()
    # available_points = forms.IntegerField()


