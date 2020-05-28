from django import forms
from django.contrib.auth.models import User
from login_app.models import UserInfo


class userform(forms.ModelForm):
    class Meta():
        model = User
        fields = {'username','email','password'}


class userinfo_form(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = {'facebook_id' , 'profile_img'}
