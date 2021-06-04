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
