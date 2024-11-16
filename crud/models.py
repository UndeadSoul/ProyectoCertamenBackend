from django.db import models

# Create your models here.


class Post(models.Model):
    post_title=models.CharField(max_length=40)
    post_subtitle=models.CharField(max_length=80)
    post_description=models.TextField()
    post_image=models.ImageField()
    post_creator=models.TextField()
    post_created=models.DateTimeField(auto_now_add=True)
    post_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Titulo: "+self.post_title

class Chef(models.Model):
    chef_name=models.CharField(max_length=40)
    chef_description=models.TextField()
    chef_position=models.CharField(max_length=30)
    chef_photo=models.ImageField()

    def __str__(self):
        return "Nombre: "+self.chef_name

class MasaDisp(models.Model):
    type=models.CharField(max_length=100,verbose_name="tipo")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="Masa"
        verbose_name_plural="Masas"
    
    def __str__(self):
        return self.type
    
class Contenido(models.Model):
    name=models.CharField(max_length=100,verbose_name="nombre")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="Contenido"
        verbose_name_plural="Contenidos"
    
    def __str__(self):
        return self.name
    
class Pizza(models.Model):
    pizza_name=models.CharField(max_length=40)
    pizza_description=models.TextField()
    pizza_image=models.ImageField()
    pizza_price=models.CharField(max_length=10)
    Contain=models.ManyToManyField(Contenido,verbose_name="Contenido")
    dough=models.ManyToManyField(MasaDisp,verbose_name="Masa")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")

    def __str__(self):
        return "Nombre: "+self.pizza_name