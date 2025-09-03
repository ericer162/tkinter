from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor= models.CharField(max_length=100)
    ano_publicaçao = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo