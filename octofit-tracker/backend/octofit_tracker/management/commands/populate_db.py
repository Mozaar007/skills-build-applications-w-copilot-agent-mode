from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Elliot Alderson'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', name='Dade Murphy'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Sleep Token'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team_blue = Team(name='Blue Team', members=users[:3])
        team_gold = Team(name='Gold Team', members=users[3:])
        team_blue.save()
        team_gold.save()

        # Create activities
        activities = [
            Activity(user=users[0], description='Cycling for 1 hour', date='2025-04-29T10:00:00Z'),
            Activity(user=users[1], description='Crossfit for 2 hours', date='2025-04-29T12:00:00Z'),
            Activity(user=users[2], description='Running for 1.5 hours', date='2025-04-29T14:00:00Z'),
            Activity(user=users[3], description='Strength training for 30 minutes', date='2025-04-29T16:00:00Z'),
            Activity(user=users[4], description='Swimming for 1.25 hours', date='2025-04-29T18:00:00Z'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team_blue, score=300),
            Leaderboard(team=team_gold, score=250),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(user=users[0], type='Cycling', duration=60),
            Workout(user=users[1], type='Crossfit', duration=120),
            Workout(user=users[2], type='Running', duration=90),
            Workout(user=users[3], type='Strength', duration=30),
            Workout(user=users[4], type='Swimming', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))