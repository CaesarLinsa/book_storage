# Generated by Django 3.1 on 2020-08-26 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='contry',
            new_name='country',
        ),
    ]
