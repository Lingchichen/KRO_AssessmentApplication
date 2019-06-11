# Generated by Django 2.0.2 on 2018-03-15 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kro', '0005_meetingsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('BOOKKEEPING_PROGRESS_REPORT', 'Bookkeeping progress report - AP / AR'), ('BUDGET_VS_ACTUAL_REPORT', 'Budget vs Actual report'), ('BOOKKEEPTING_SUCCESS_CHALLENGES_OPPORTUNITIES', 'Bookkeeping - Success / Challenges / Opportunities')], default='BOOKKEEPING_PROGRESS_REPORT', max_length=255)),
                ('review_financials', models.BooleanField()),
                ('review_success_challenge', models.BooleanField()),
                ('review_project', models.BooleanField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='meetingsection',
            old_name='section_title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='meetingtopic',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kro.MeetingSection'),
        ),
    ]
