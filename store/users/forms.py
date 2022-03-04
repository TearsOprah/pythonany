from dataclasses import field
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')

    # def __init__(self, *args, **kwargs):
    #     super(UserLoginForm, self).__init__(*args, **kwargs)
    #     for field_name, filed in self.fields.items():
    #         filed.widget.attrs['class'] = 'form-control py-4'


class UserRegistrationForm(UserCreationForm):

    number_of_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'number_of_phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'


class UserProfileForm(UserChangeForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))

    number_of_phone = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))

    delivery_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите адрес доставки'}))

    class Meta:
        model = User
        fields = ('username', 'number_of_phone', 'delivery_address')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'