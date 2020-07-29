from django import forms


class DangerForm(forms.Form):
    data = forms.CharField()