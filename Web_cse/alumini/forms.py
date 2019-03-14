from django import forms


class Nameform(forms.Form):
    First_name = forms.CharField(max_length=50)
    Last_name = forms.CharField(max_length=30)
    batchId = forms.IntegerField()
