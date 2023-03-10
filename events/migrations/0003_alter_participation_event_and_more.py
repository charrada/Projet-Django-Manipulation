# Generated by Django 4.1.5 on 2023-01-31 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='personne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]