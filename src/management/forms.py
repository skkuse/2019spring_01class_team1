from django import forms

class UploadDocumentForm(forms.Form):
    file = forms.FileField()
    image = forms.ImageField()


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length = 15)
    files = forms.FileField(widget=forms.ClearableFileInput(attrs = {'multiple': True}))
    