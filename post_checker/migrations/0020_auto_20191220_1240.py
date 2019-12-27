# Generated by Django 3.0.1 on 2019-12-20 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_checker', '0019_auto_20191219_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='general_link',
        ),
        migrations.RemoveField(
            model_name='post',
            name='page_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='page_img_link',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.CharField(blank=True, max_length=200)),
                ('page_author', models.CharField(max_length=100)),
                ('general_link', models.CharField(max_length=200)),
                ('page_img_link', models.CharField(max_length=400)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post_checker.Page'),
            preserve_default=False,
        ),
    ]
