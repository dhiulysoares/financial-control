import datetime
import uuid

from django.db import models
from model_utils import Choices


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Id")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        abstract = True


class BankAccount(BaseModel):

    PURPOSE_CHOICES = Choices(
        ("education", "EDUCATION", "Educação"),
        ("essencial_costs", "ESSENCIAL_COSTS", "Custos essenciais"),
        ("free", "FREE", "Livre"),
        ("credit_account", "CREDIT_ACCOUNT", "Conta dos créditos"),
        ("reserve", "RESERVE", "Reserva")
    )

    purpose = models.CharField(max_length=200, choices=PURPOSE_CHOICES, null=True, blank=True, verbose_name="Propósito")
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nome")
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Saldo")
    input_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Percentual de entrada")

    class Meta:
        verbose_name = "Conta bancária"
        verbose_name_plural = "Contas bancárias"

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    TRANSACTION_CHOICES = Choices(
        ("input", "INPUT", "Entrada"),
        ("output", "OUTPUT", "Saída"),
    )
    transaction_type = models.CharField(verbose_name="Tipo de transação", max_length=200, choices=TRANSACTION_CHOICES, null=True, blank=True)
    date = models.DateField(verbose_name="Data da transação", null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor transacionado", null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"

    def __str__(self):
        return self.transaction_type


class CreditCard(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Nome do cartão / Beneficiário")

    limit = models.DecimalField(verbose_name="limite", max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Cartão de crédito"
        verbose_name_plural = "Cartões de crédito"

    def __str__(self):
        return self.name


class Invoice(BaseModel):
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cartão de Crédito")
    total_price = models.DecimalField(verbose_name="Preço total da fatura", max_digits=10, decimal_places=2, default=0)
    pay_date = models.DateField(verbose_name="Data de vencimento", null=True, blank=True)

    class Meta:
        verbose_name = "Fatura"
        verbose_name_plural = "Faturas"

    def __str__(self):
        return str(self.pay_date)


class Purchase(BaseModel):
    PAYMENT_CHOICES = Choices(
        ("in_cash", "IN_CASH", "À vista"),
        ("installments", "INSTALLMENTS", "Parcelado"),
        ("period", "PERIOD", "A prazo")
    )
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name="Fatura")
    description = models.CharField(verbose_name="Descrição da compra", max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço", default=0)
    buy_date = models.DateField(verbose_name="Data da compra", default=datetime.date.today)
    pay_date = models.DateField(verbose_name="Data de vencimento", null=True, blank=True)
    total_parcels = models.IntegerField(verbose_name="Número de parcelas", default=1)
    payment_form = models.CharField(verbose_name="Forma de pagamento", max_length=200, null=True, blank=True, choices=PAYMENT_CHOICES)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return self.description
