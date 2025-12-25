from django.contrib import admin
from .models import Reservoir

@admin.register(Reservoir)
class ReservoirAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude")
    search_fields = ("name",)
