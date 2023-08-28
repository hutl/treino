# Generated by Django 4.2.4 on 2023-08-28 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='preco',
        ),
        migrations.AddField(
            model_name='produto',
            name='descrição',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='produto',
            name='preço',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd',
            field=models.PositiveIntegerField(),
        ),
    ]
