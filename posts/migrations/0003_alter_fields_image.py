# Generated by Django 4.1.1 on 2022-10-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_fields_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
