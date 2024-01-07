from typing import Any
from django.db import models

# Create your models here.
class Registration(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    choice_type = (
        ('S', 'Estudante'),
        ('E', 'Funcionário'),
        ('Ex', 'Externo'),
    )

    public_type = models.CharField(max_length=2, choices=choice_type)
    matriculation = models.CharField(max_length=11) # matricula
    cpf = models.CharField(max_length=11)