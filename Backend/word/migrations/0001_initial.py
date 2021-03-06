# Generated by Django 4.0.2 on 2022-04-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='고유번호')),
                ('word', models.CharField(default='', max_length=50, verbose_name='단어')),
                ('korean_mean', models.CharField(default='', max_length=255, verbose_name='한국어 뜻')),
                ('english_mean', models.CharField(default='', max_length=255, verbose_name='영어 뜻')),
                ('is_korean', models.BooleanField(default=False, verbose_name='단어 종류')),
            ],
        ),
    ]
