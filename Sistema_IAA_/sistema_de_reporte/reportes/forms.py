from django import forms
from .models import Profesor, Materia, Alumno, ReporteAlumno

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'reporte', 'materia', 'correo']
        widgets = {
            'reporte': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'materia': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'profesor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'profesor': forms.Select(attrs={'class': 'form-select'}),
        }

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'semestre', 'correo', 'telefono', 'materias']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'materias': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class ReporteAlumnoForm(forms.ModelForm):
    class Meta:
        model = ReporteAlumno
        fields = ['alumno', 'profesor', 'tipo_reporte', 'fecha', 'observaciones']
        widgets = {
            'alumno': forms.Select(attrs={'class': 'form-select'}),
            'profesor': forms.Select(attrs={'class': 'form-select'}),
            'tipo_reporte': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
