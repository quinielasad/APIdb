from django.contrib import admin

# Register your models here.
from principal.models import Jornada, Partido

admin.site.register(Jornada)
admin.site.register(Partido)