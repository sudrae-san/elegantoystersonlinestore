# Generated by Django 4.2 on 2023-05-08 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_account_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='active',
        ),
    ]
