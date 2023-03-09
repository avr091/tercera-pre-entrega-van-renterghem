from django import forms

class PistolaFormulario(forms.Form):

    nombre=forms.CharField(max_length=30)
    fps=forms.IntegerField()

class AsaltoFormulario (forms.Form):
    nombre=forms.CharField(max_length=30)
    tipo=forms.CharField(max_length=30)
    fps=forms.IntegerField()


class DmrFormulario (forms.Form):
    nombre=forms.CharField(max_length=30)
    tipo=forms.CharField(max_length=30)
    fps=forms.IntegerField()
