# Generated by Django 5.1.1 on 2024-09-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='icon',
            field=models.CharField(default='default.png', max_length=100, verbose_name='Icon'),
        ),
    ]