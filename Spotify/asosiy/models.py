from django.db import models

# Create your models here.

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=30)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=35)

    def __str__(self):
        return self.ism


class Albom(models.Model):
    nom = models.CharField(max_length=30)
    sana = models.DateField()
    rasm = models.URLField(null=True,blank=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.qoshiqchi.ism}"

class Qoshiq(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=20)
    davomiylik = models.DurationField(null=True,blank=True)
    fayl = models.URLField(null=True,blank=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.albom.qoshiqchi.ism}"