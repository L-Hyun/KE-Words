# Generated by Django 4.0.2 on 2022-04-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='고유번호')),
                ('word_id', models.IntegerField(default=0, verbose_name='단어 교유번호')),
                ('user_id', models.IntegerField(default=0, verbose_name='유저 고유번호')),
            ],
        ),
    ]
