from django.db import models
from django.urls import reverse

# Create your models here.
SNACKS = (
    ('O', 'Oran Berry'),
    ('C', 'Cheri Berry'),
    ('P', 'Pecha Berry'),
    ('R', 'Rawst Berry'),
    ('I', 'Iapapa Berry')
)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

class Berries(models.Model):
    date = models.DateField('Snack Date')
    snack = models.CharField(
        max_length=1,
        choices=SNACKS,
        default=SNACKS[0][0]
        )
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_snack_display()} on {self.date}"
    class Meta:
        ordering = ['-date']