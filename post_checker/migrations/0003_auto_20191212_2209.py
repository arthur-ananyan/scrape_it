# Generated by Django 3.0 on 2019-12-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_checker', '0002_auto_20191212_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]