# Generated by Django 4.0.2 on 2022-04-04 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='id',
            new_name='word_id',
        ),
    ]
