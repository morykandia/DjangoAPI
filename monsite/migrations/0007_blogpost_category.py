# Generated by Django 4.2.5 on 2023-10-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsite', '0006_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(to='monsite.category'),
        ),
    ]