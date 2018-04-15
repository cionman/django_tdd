from django.contrib import admin

from toy.models import Toy


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    pass

