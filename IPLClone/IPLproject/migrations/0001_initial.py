# Generated by Django 2.2.1 on 2019-06-17 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('city', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('team1', models.CharField(max_length=64)),
                ('team2', models.CharField(max_length=64)),
                ('toss_winner', models.CharField(max_length=64)),
                ('toss_decision', models.CharField(max_length=64)),
                ('result', models.CharField(max_length=64)),
                ('dl_applied', models.IntegerField()),
                ('winner', models.CharField(max_length=64)),
                ('win_by_runs', models.IntegerField()),
                ('win_by_wickets', models.IntegerField()),
                ('player_of_match', models.CharField(max_length=64)),
                ('venue', models.CharField(max_length=64)),
                ('umpire1', models.CharField(max_length=64)),
                ('umpire2', models.CharField(max_length=64)),
                ('umpire3', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inning', models.IntegerField()),
                ('batting_team', models.CharField(max_length=64)),
                ('bowling_team', models.CharField(max_length=64)),
                ('over', models.IntegerField()),
                ('ball', models.IntegerField()),
                ('batsman', models.CharField(max_length=64)),
                ('non_striker', models.CharField(max_length=64)),
                ('bowler', models.CharField(max_length=64)),
                ('is_super_over', models.IntegerField()),
                ('wide_runs', models.IntegerField()),
                ('bye_runs', models.IntegerField()),
                ('legbye_runs', models.IntegerField()),
                ('noball_runs', models.IntegerField()),
                ('penalty_runs', models.IntegerField()),
                ('batsman_runs', models.IntegerField()),
                ('extra_runs', models.IntegerField()),
                ('total_runs', models.IntegerField()),
                ('player_dismissed', models.CharField(max_length=64)),
                ('dismissal_kind', models.CharField(max_length=64)),
                ('fielder', models.CharField(max_length=64)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IPLproject.Match')),
            ],
        ),
    ]
