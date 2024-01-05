from django.db import models

# Create your models here.
class Registration(models.Model):
    choice_type = (
        ('S', 'Student'),
        ('E', 'Employee'),
        ('Ex', 'Extern'),
    )
    public_type = models.CharField(max_length=2, choices=choice_type)
    registration = models.CharField(max_length=11)
    