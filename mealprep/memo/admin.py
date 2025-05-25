from django.contrib import admin
from .models import PreparedItem

@admin.register(PreparedItem)
class PreparedItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'prepared_date', 'expiry_date')
