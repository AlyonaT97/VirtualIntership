# Generated by Django 4.2.7 on 2023-11-23 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perevals', '0003_alter_perevals_level_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevals',
            name='level_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='perevals.level'),
        ),
    ]
