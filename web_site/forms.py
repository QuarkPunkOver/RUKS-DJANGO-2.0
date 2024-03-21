from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "sign__input", 'placeholder': 'Email'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': "sign__input", 'placeholder': 'Имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "sign__input", 'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "sign__input", 'placeholder': 'Подтвердите пароль'}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'sign__input', 'placeholder': 'Пароль'}))


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(
            attrs={'autocomplete': 'email', 'class': 'sign__input', 'placeholder': 'Enter your Email'})
    )


class SetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'sign__input', 'placeholder': 'New password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'sign__input', 'placeholder': 'Repeat password'}),
    )
