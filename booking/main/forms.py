from dataclasses import fields

from django import forms
from django.contrib.auth.models import User


class register_form(forms.ModelForm):
    username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'input wide', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={'class':'input wide', 'placeholder': 'Password'}))
    # password = forms.CharField(max_length=10)
    # first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input wide'}))
    # last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input wide'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'input wide', 'placeholder': 'tester001@hotmail.com'}))
    phone = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'input wide', 'placeholder': '0888888888'}))
    class Meta:
        model=User
        fields = ('username','password','email', 'phone')

    def clean(self):
        clean_data = super().clean()
        username = clean_data.get('username')
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            self.add_error('username', 'มีชื่อผู้ใช้ในระบบแล้ว')
