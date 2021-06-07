from mptt.models import MPTTModel, TreeForeignKey
from django.db import models

# Create your models here.


class Project(models.Model):
    DESIGN_TYPES = (
        ('platdak', 'Platdak'),
        ('gen4', 'Gen 4'),
        ('wind', 'Wind Net'),
    )
    name = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    areaManager = models.CharField(max_length=100)
    designType = models.CharField(max_length=30, choices=DESIGN_TYPES)
    sections = models.IntegerField(default=1)
    lowMaintananceCheck = models.BooleanField(default=True, blank=True)
    folderUrl = models.URLField()
    infoUrl = models.URLField()

    def __str__(self) -> str:
        return self.name


class Measurement(models.Model):
    blockArea = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    blockOmtrek = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    blockLengte = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    blockBreedte = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    blockRy = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    blockDwars = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    blockHoeke = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    blockHeight = models.DecimalField(default=0, max_digits=6, decimal_places=2)


class Section(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='measurement')
