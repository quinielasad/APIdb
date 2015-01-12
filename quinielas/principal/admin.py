from django.contrib import admin

# Register your models here.
from principal.models import Jornada, Partido, Perfil, ApuestaPartido

admin.site.register(Jornada)
admin.site.register(Partido)
admin.site.register(Perfil)
admin.site.register(ApuestaPartido)