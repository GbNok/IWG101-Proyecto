# Generated by Django 3.2.9 on 2021-12-07 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estudio_mate', '0005_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solution',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudio_mate.problem'),
        ),
    ]
