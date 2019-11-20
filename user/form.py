from django import forms
from django.contrib import auth
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class':'form-control', "placeholder"
                                                                          :"请输入用户名"}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder"
                                                                          :"请输入密码"}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is  None:
            raise forms.ValidationError('用户名或密码不正确')
        self.cleaned_data["user"] = user
        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=30, min_length=3,
                               widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"请输入用户名"}))
    password = forms.CharField(label="密码", min_length=6,
                               widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder":"请输入密码"}))
    password2 = forms.CharField(label="再输入一次密码", min_length=6,
                               widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder":"请再次输入密码"}))
    email = forms.EmailField(label="邮箱",
                             widget=forms.EmailInput(attrs={'class':'form-control', "placeholder":"邮箱"}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('用户已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email

    def clean_password2(self):
        password = self.cleaned_data["password"]
        password2 = self.cleaned_data["password2"]
        if password != password2:
            raise forms.ValidationError("两次输入的密码不一致")
        return password2


class ChangeNickNameForm(forms.Form):
    nickname = forms.CharField(label="昵称", max_length=30, min_length=3,
                               widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"请输入昵称"}))

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ChangeNickNameForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data["user"] = self.user
        else:
            raise forms.ValidationError('用户未登录')
        return self.cleaned_data

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname'].strip()
        if len(nickname) < 2:
            raise forms.ValidationError('必须包含多余两个的非空格字符')
        return nickname