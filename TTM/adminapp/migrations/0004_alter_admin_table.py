# Generated by Django 5.0 on 2024-01-04 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_admin_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='admin',
            table='ttmadmin_table',
        ),
    ]