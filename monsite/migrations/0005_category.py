# Generated by Django 4.2.5 on 2023-10-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsite', '0004_blogpost_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
