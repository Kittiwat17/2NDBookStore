from django import forms

class register(form.Form):
    username = form.CharField()
    password1 = form.IntegerField()
    password2 = form.IntegerField()
    email = form.EmailField()
    phone = form.CharField()

