from django.contrib import admin

from core.models import BankAccount, Movement


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "purpose", "balance"]


@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ["id", "date", "value", "movement_type", "origin", "destiny", "description"]
    list_filter = ["movement_type"]
