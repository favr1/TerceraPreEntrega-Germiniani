from django import forms

class auto_registro(forms.Form):
    marca = forms.CharField(max_length=50, help_text="")
    modelo = forms.CharField(max_length=50, help_text="")
    reparacion = forms.CharField(max_length=500, help_text="")
    precio = forms.IntegerField()

class mecanico_registro(forms.Form):
    nombre = forms.CharField(max_length=50, help_text="")
    apellido = forms.CharField(max_length=50, help_text="")
    especializacion = forms.CharField(max_length=150, help_text="")

class pieza_registro(forms.Form):
    nombre = forms.CharField(max_length=50, help_text="")
    precio = forms.IntegerField()
    cantidad = forms.IntegerField()