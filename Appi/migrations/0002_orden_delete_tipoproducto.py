# Generated by Django 4.1.5 on 2023-04-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='tipoproducto',
        ),
    ]