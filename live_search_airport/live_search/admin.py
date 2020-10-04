from django.contrib import admin

from live_search.models import Airport


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('id', 'iata', 'city', 'country')
