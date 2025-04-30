from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import get_test_data

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        test_data = get_test_data()

        # Populate users
        user_instances = {}
        for user_data in test_data['users']:
            user = User.objects.create(**user_data)
            user_instances[user.email] = user

        # Populate teams
        for team_data in test_data['teams']:
            team = Team.objects.create(name=team_data['name'])
            if 'members' in team_data:
                for member_email in team_data['members']:
                    if member_email in user_instances:
                        team.members.add(user_instances[member_email])

        # Populate activities
        for activity_data in test_data['activities']:
            if activity_data['user'] is not None and activity_data['user'] in user_instances:
                activity_data['user'] = user_instances[activity_data['user']]
                Activity.objects.create(**activity_data)

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            if leaderboard_data['user'] is not None and leaderboard_data['user'] in user_instances:
                leaderboard_data['user'] = user_instances[leaderboard_data['user']]
                Leaderboard.objects.create(**leaderboard_data)

        # Populate workouts
        for workout_data in test_data['workouts']:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))