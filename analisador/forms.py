from django import forms

class CurriculoUploadForm(forms.Form):
    nome_vaga = forms.CharField(max_length=250, label='Vaga')
    curriculo = forms.FileField(label='Curriculo em pdf')
