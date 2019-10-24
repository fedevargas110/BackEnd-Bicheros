from django.contrib import admin
from .models import *

# Register your models here.
class ItemPhotoAdmin(admin.TabularInline):
  model = Photo
  extra = 1

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
  list_display = ('name','species','date_founded','race')
  list_filter = ('name','species')
  inlines = [ItemPhotoAdmin]

@admin.register(Monto)
class MontoAdmin(admin.ModelAdmin):
  list_display = ('date','amount','type')
  list_filter = ('date',)

admin.site.register(CAP)
admin.site.register(Donacion)
@admin.register(Veterinaria)
class VeterinariaAdmin(admin.ModelAdmin):
  list_display = ('name','address','phone')
  list_filter = ('name','address')

admin.site.register(Photo)
admin.site.register(HistorialM)