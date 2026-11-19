from django.db import models

class Profesor(models.Model):
    clave_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    reporte = models.DateField(null=True, blank=True)
    materia = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.correo})"

class Materia(models.Model):
    clave_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    # Relación con Profesor (también puedes usar CharField si lo prefieres aislado)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    clave_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    semestre = models.IntegerField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    materias = models.ManyToManyField(Materia, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Semestre {self.semestre}"

class ReporteAlumno(models.Model):
    clave_reporte = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='reportes')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='reportes_emitidos')
    tipo_reporte = models.CharField(max_length=100)
    fecha = models.DateField()
    observaciones = models.TextField()

    def __str__(self):
        return f"Reporte #{self.clave_reporte} - {self.alumno.nombre} ({self.fecha})"
