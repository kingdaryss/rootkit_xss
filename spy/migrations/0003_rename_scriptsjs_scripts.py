# Generated by Django 4.1.7 on 2023-03-04 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spy', '0002_spylogs_insert_date_alter_scriptsjs_script'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ScriptsJs',
            new_name='Scripts',
        ),
    ]
