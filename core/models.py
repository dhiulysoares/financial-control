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


class Movement(BaseModel):
    MOVEMENT_CHOICES = Choices(
        ("input", "INPUT", "Entrada"),
        ("output", "OUTPUT", "Saída"),
    )
    movement_type = models.CharField(max_length=200, choices=MOVEMENT_CHOICES, null=True, blank=True, verbose_name="Tipo de movimentação")
    origin = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="origin", null=True, blank=True, verbose_name="Origem")
    destiny = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="destiny", null=True, blank=True, verbose_name="Destino")
    date = models.DateTimeField(verbose_name="Data de recebimento", null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor recebido", null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
