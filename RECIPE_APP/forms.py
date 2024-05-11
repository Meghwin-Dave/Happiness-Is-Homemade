from django import forms

class addrec(forms.Form):
    username=forms.CharField()
    recipename=forms.CharField()
    dietlabel=forms.CharField()
    cuisine=forms.CharField()
    dish=forms.CharField()
    ingredients=forms.CharField()
    health=forms.CharField()
    image=forms.FileField()