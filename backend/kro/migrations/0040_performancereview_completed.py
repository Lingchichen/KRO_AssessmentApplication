# Generated by Django 2.0.2 on 2018-07-17 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kro', '0039_remove_projectmilestonedevelopmentstepstatus_growth_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='performancereview',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
