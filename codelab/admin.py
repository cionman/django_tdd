from django.contrib import admin

# Register your models here.
from codelab.models import Codelab, CodelabDetail


@admin.register(Codelab)
class CodelabAdmin(admin.ModelAdmin):
    pass


@admin.register(CodelabDetail)
class CodelabDetailAdmin(admin.ModelAdmin):
    pass
