# Generated by Django 5.0.3 on 2024-03-21 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningLogApp', '0003_assunto_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='assunto',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
