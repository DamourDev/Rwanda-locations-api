from django.db import models

# Create your models here.

class Province(models.Model):

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10,  null=True, blank=True)

    def __str__(self):
        return self.name
    

class District(models.Model):

    name = models.CharField(max_length=20)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Sector(models.Model):

    name = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class Cell(models.Model):

    name = models.CharField(max_length=20)
    sector = models.ForeignKey(Sector,on_delete=models.CASCADE)
    code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
    


class Village(models.Model):

    name = models.CharField(max_length=20)
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
    code = models.CharField(max_length=10,  null=True, blank=True)

    def __str__(self):
        return self.name


