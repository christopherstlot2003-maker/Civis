from django.db import models

class Civilisation(models.Model):
    nom=models.CharField(max_length=200)
    epoque=models.CharField()
    Description=models.TextField()

    def __str__(self):
        return self.nom 


class Chef(models.Model):
    nom=models.CharField(max_length=200)
    epoque=models.CharField()
    image=models.URLField(blank=True,null=True) 
    Description=models.TextField()
    civilisation=models.ForeignKey(Civilisation,on_delete=models.CASCADE) 

    def __str__(self):
        return self.nom 

