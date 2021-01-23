# Generated by Django 3.1.4 on 2021-01-18 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0004_auto_20210116_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_date',
            field=models.DateTimeField(null=True),
        ),
    ]