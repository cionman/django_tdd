from django.contrib import admin

from til.models import Til


@admin.register(Til)
class TilAdmin(admin.ModelAdmin):
    pass