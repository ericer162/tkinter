from django.db import models

class UsuarioAutorizado(models.Model):
    nome = models.CharField(max_length=100)
    identificacao = models.CharField(max_length=50, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.identificacao})"

class RegistroAcesso(models.Model):
    usuario = models.ForeignKey(UsuarioAutorizado, on_delete=models.SET_NULL, null=True)
    identificacao_tentativa = models.CharField(max_length=50)
    data_tentativa = models.DateTimeField(auto_now_add=True)
    acesso_permitido = models.BooleanField(default=False)

    def __str__(self):
        status = "Permitido" if self.acesso_permitido else "Negado"
        return f"{self.identificacao_tentativa} - {status} - {self.data_tentativa}"