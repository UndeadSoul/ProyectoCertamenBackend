from django import forms
class contactForm(forms.Form):
    name=forms.CharField(label="Nombre y apellido", required=True,min_length=5,max_length=40,widget=forms.TextInput(attrs=
    {'class':'form-control', 'placeholder':'Your name'}))

    email=forms.EmailField(label="Correo electrónico", required=True,max_length=100,widget=forms.EmailInput(attrs=
    {'class':'form-control', 'placeholder':'Your email'}))

    subject=forms.CharField(label="Asunto", required=True,max_length=100,widget=forms.TextInput(attrs=
    {'class':'form-control', 'placeholder':'Subject'}))

    message=forms.CharField(label="Mensaje",required=True,widget=forms.Textarea(attrs=
    {'class':'form-control', 'placeholder':'Your message...','rows':5}))


