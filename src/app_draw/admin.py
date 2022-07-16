from django.contrib import admin

from . import models

admin.site.register(models.Winner, admin.ModelAdmin)
admin.site.register(models.Draw, admin.ModelAdmin)
