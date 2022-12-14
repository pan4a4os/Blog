# Generated by Django 4.1.1 on 2022-10-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('phone_number', models.CharField(null=False, blank=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(verbose_name='Some information:')),
                ('type', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('status', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=None, null=True, blank=True)),
                ('created', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
