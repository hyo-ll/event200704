from django import forms

class AllmemberForm(forms.Form):
    name = forms.CharField(label='name', required=False)
    mail = forms.CharField(label='mail', required=False)
    age = forms.IntegerField(label='age', required=False)

