
from django.db import models


class Voo(models.Model):
    idVoo = models.IntegerField(primary_key=True)
    volumeinicialAgua = models.DecimalField(max_digits=6, decimal_places=2)
    pressaoInicial = models.DecimalField(max_digits=6, decimal_places=2)
    pesoFoguete = models.DecimalField(max_digits=6, decimal_places=2)
    pressaoBomba = models.DecimalField(max_digits=6, decimal_places=2)
    anguloLancamento = models.DecimalField(max_digits=6, decimal_places=2)
    duracaoSegundos = models.PositiveSmallIntegerField()


class Instante(models.Model):
    idInstante = models.IntegerField(primary_key=True)
    tempo = models.TimeField()
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    altitude = models.DecimalField(max_digits=6, decimal_places=2)
    idVoo = models.ForeignKey(Voo, on_delete=models.CASCADE)

class Eixo(models.Model):
    idEixo = models.IntegerField(primary_key=True)
    angulo = models.DecimalField(max_digits=4, decimal_places=2)
    velocidade = models.DecimalField(max_digits=4, decimal_places=2)
    aceleracao = models.DecimalField(max_digits=4, decimal_places=2)
    tipoEixo = models.CharField(max_length=1)
    idInstante = models.ForeignKey(Instante, on_delete=models.CASCADE)

    

    
