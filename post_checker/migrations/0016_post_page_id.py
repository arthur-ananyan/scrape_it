# Generated by Django 3.0 on 2019-12-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_checker', '0015_post_page_img_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='page_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]