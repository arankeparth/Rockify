# Generated by Django 3.2.6 on 2021-08-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0007_posters'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='difficulty_level',
            field=models.CharField(default='hard', max_length=100),
            preserve_default=False,
        ),
    ]