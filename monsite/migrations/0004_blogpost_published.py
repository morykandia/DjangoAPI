# Generated by Django 4.2.5 on 2023-10-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsite', '0003_remove_blogpost_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
