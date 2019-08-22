from django.contrib import admin
from .models import *

# Register your models here.
class ItemPhotoAdmin(admin.TabularInline):
  model = Photo
  extra = 1

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
  list_display = ('name','gender')
  inlines = [ItemPhotoAdmin]



admin.site.register(Monto)
admin.site.register(CAP)
admin.site.register(Donacion)
admin.site.register(Veterinaria)
admin.site.register(Photo)