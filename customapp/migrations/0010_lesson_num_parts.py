# Generated by Django 3.2.6 on 2021-08-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customapp', '0009_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='num_parts',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
