# Generated by Django 5.1.4 on 2024-12-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='result_away_team_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='result_home_team_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
