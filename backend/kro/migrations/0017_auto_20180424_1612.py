# Generated by Django 2.0.2 on 2018-04-24 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kro', '0016_meetingprogressnotes_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingprogressnotes',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kro.MeetingTopic'),
        ),
    ]
