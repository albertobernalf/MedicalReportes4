from django.contrib import admin

from django import forms

# Register your models here.

from Administracion.models import Mae_Reportes , Mae_GrupoReportes, Mae_RepUsuarios, Mae_RepParametros, Mae_TiposCampo, Imhotep_SedesReportes
from Administracion.forms import Mae_ReportesForm


#@admin.register(Mae_ReportesAdmin)
class mae_ReportesAdmin(admin.ModelAdmin):

    list_display  = ("id","mae_gruporeportes","nom_reporte","descripcion","cuerpo_sql", "encabezados","excel","pdf","csv", "estadoreg")
    search_fields = ("id","nom_reporte","descripcion","cuerpo_sql", "encabezados", "excel","pdf","csv", "estadoreg")
    # Filtrar
    list_filter = ("mae_gruporeportes","nom_reporte","descripcion", "excel","pdf","csv", "estadoreg")

    form = Mae_ReportesForm


class mae_GrupoReportesAdmin(admin.ModelAdmin):

    list_display  = ("id","nom_grupo","estadoreg")
    search_fields = ("id","nom_grupo","estadoreg")
    # Filtrar
    list_filter = ("id","nom_grupo","estadoreg")



class mae_RepUsuariosAdmin(admin.ModelAdmin):
    list_display = ("cod_sede","mae_reportes", "cod_usuario", "estadoreg")
    search_fields = ("cod_sede","mae_reportes",  "cod_usuario", "estadoreg")
    # Filtrar


    list_filter = ("cod_sede", "mae_reportes",  "cod_usuario",  "estadoreg")

class mae_RepParametrosAdmin(admin.ModelAdmin):
    list_display = ("id", "mae_reportes","parametro","parametro_texto","mae_tiposcampo",  "estadoreg")
    search_fields =("id", "mae_reportes","parametro","parametro_texto","mae_tiposcampo",  "estadoreg")
    # Filtrar

    list_filter = ( "mae_reportes","parametro_texto", "estadoreg")

class mae_TiposCampoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields =("id", "nombre")
    # Filtrar

    list_filter = ("id", "nombre")

class imhotep_SedesReportesAdmin(admin.ModelAdmin):
        list_display = ("id", "codreg_sede", "nom_sede","codreg_ips","direccion","telefono","departamento","municipio")
        search_fields = ("id", "codreg_sede", "nom_sede","codreg_ips","direccion","telefono","departamento","municipio")
        # Filtrar

        list_filter = ("id", "codreg_sede", "nom_sede","codreg_ips","direccion","telefono","departamento","municipio")



admin.site.register(Mae_Reportes, mae_ReportesAdmin)
admin.site.register(Mae_GrupoReportes, mae_GrupoReportesAdmin)
admin.site.register(Mae_RepUsuarios, mae_RepUsuariosAdmin)
admin.site.register(Mae_RepParametros, mae_RepParametrosAdmin)
admin.site.register(Mae_TiposCampo, mae_TiposCampoAdmin)
admin.site.register(Imhotep_SedesReportes, imhotep_SedesReportesAdmin)

