from django.db import models

# Create your models here.
class Materia(models.Model):
    clave_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    clave_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    semestre = models.IntegerField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    materias = models.ManyToManyField(Materia)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Profesor(models.Model):
    clave_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    reporte = models.DateField()
    materia = models.CharField(max_length=100)
    correo = models.EmailField()
    materias_impartidas = models.ManyToManyField(Materia)
    alumnos = models.ManyToManyField(Alumno)

    def __str__(self):
        return self.nombre



class ReporteAlumno(models.Model):
    clave_reporte = models.AutoField(primary_key=True)
    tipo_reporte = models.CharField(max_length=100)
    fecha = models.DateField()
    observaciones = models.TextField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_reporte} - {self.fecha}"
