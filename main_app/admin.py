from django.contrib import admin
from .models import Pokemon, Berries, Item
# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Berries)
admin.site.register(Item)