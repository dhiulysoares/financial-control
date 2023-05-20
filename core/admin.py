from django.contrib import admin

from core.models import BankAccount, Transaction, Purchase, Invoice, CreditCard


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "purpose", "balance"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "date", "value", "transaction_type", "description"]
    list_filter = ["transaction_type"]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["id", "buy_date", "description", "price", "total_parcels", "pay_date"]


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["purchase", "total_price", "pay_date"]
    list_filter = ["pay_date"]


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ["invoice", "limit"]
