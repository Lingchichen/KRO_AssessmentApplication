# Generated by Django 2.0.2 on 2018-05-02 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kro', '0021_projectmilestonedevelopmentstepstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmilestonedevelopmentstepstatus',
            name='growth_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kro.GrowthClass'),
            preserve_default=False,
        ),
    ]
