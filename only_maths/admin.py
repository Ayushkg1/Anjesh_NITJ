from django.contrib import admin

# Register your models here.
from .models import Chapter, Contact, Material

admin.site.register(Chapter)
admin.site.register(Contact)
admin.site.register(Material)