from django.shortcuts import render, redirect
from .forms import ProfesorForm, MateriaForm, AlumnoForm, ReporteAlumnoForm
from .models import ReporteAlumno

def registrar_profesor(request):
    form = ProfesorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registrar_profesor')
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Profesor'})

def registrar_materia(request):
    form = MateriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registrar_materia')
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Materia'})

def registrar_alumno(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registrar_alumno')
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Registrar Alumno'})

def crear_reporte(request):
    form = ReporteAlumnoForm(request.POST or None)
    reportes = ReporteAlumno.objects.all()
    if form.is_valid():
        form.save()
        return redirect('crear_reporte')
    return render(request, 'formulario.html', {
        'form': form,
        'titulo': 'Generar Reporte de Alumno',
        'reportes': reportes
    })
