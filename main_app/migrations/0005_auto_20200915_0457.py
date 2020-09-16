# Generated by Django 3.1.1 on 2020-09-15 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0004_auto_20200914_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='comment'),
        ),
    ]