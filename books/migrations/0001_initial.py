# Generated by Django 5.0.4 on 2024-05-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/cars')),
            ],
        ),
    ]
