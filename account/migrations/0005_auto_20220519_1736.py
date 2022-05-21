# Generated by Django 3.2.13 on 2022-05-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additional',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='specialization',
            name='degree',
        ),
        migrations.AddField(
            model_name='specialization',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='useradditional',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='userlanguages',
            name='degree',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userspecialization',
            name='degree',
            field=models.FloatField(blank=True, null=True),
        ),
    ]