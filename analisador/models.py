from django.db import models

# Create your models here.

class AnaliseCurriculo(models.Model):
    nome_vaga = models.CharField(max_length=250)
    curriculo = models.FileField(upload_to='curriculos/')
    analise = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.nome_vaga} - {self.criado_em: %Y-%m-%d}"
