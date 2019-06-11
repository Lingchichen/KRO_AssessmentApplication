# Generated by Django 2.0.2 on 2018-05-02 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kro', '0019_challenge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('problem', models.TextField()),
                ('opportunity_or_gains', models.TextField()),
                ('estimated_budget', models.IntegerField()),
                ('budget_approved', models.BooleanField()),
                ('stall_alert', models.BooleanField()),
                ('budget_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kro.Department')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kro.Company')),
                ('growth_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kro.GrowthClass')),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kro.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('problem', models.TextField()),
                ('opportunity_or_gains', models.TextField()),
                ('estimated_budget', models.IntegerField()),
                ('goals', models.CharField(max_length=255)),
                ('budget_approved', models.BooleanField()),
                ('stall_alert', models.BooleanField()),
                ('budget_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kro.Department')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kro.Company')),
                ('growth_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kro.GrowthClass')),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kro.Meeting')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kro.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('NEW', 'New'), ('ACTIVE', 'Active'), ('ON_HOLD', 'On Hold'), ('CLOSED', 'Closed')], default='NEW', max_length=255)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kro.Project'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kro.Team'),
        ),
    ]
