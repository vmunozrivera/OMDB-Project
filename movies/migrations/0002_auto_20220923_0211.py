# Generated by Django 3.2.6 on 2022-09-23 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title', 'year']},
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='tittle',
            new_name='title',
        ),
    ]
