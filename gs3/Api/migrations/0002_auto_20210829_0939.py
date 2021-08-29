# Generated by Django 3.2.6 on 2021-08-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='marks',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='student',
            name='Class',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='School',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]