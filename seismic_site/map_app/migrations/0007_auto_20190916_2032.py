# Generated by Django 2.2.4 on 2019-09-16 20:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('map_app', '0006_auto_20190916_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='numar_cadastral',
            new_name='nr_cadastral',
        ),
    ]