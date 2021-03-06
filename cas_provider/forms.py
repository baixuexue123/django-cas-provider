# -*- coding: utf-8 -*-
from django import forms

from .utils import create_login_ticket


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)
    lt = forms.CharField(widget=forms.HiddenInput, initial=create_login_ticket)

    def __init__(self, service=None, renew=None, gateway=None, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.request = request
        if service is not None:
            self.fields['service'] = forms.CharField(widget=forms.HiddenInput, initial=service)
