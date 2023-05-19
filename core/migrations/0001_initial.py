# Generated by Django 4.2.1 on 2023-05-19 23:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('purpose', models.CharField(blank=True, choices=[('education', 'Educação'), ('essencial_costs', 'Custos essenciais'), ('free', 'Livre'), ('credit_account', 'Conta dos créditos'), ('reserve', 'Reserva')], max_length=200, null=True, verbose_name='Propósito')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome')),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Saldo')),
                ('input_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Percentual de entrada')),
            ],
            options={
                'verbose_name': 'Conta bancária',
                'verbose_name_plural': 'Contas bancárias',
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('movement_type', models.CharField(blank=True, choices=[('input', 'Entrada'), ('output', 'Saída')], max_length=200, null=True, verbose_name='Tipo de movimentação')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Data de recebimento')),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor recebido')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição')),
                ('destiny', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destiny', to='core.bankaccount', verbose_name='Destino')),
                ('origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='core.bankaccount', verbose_name='Origem')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
    ]
