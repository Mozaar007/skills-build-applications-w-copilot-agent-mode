from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        activity = Activity.objects.create(user=user, description="Test Activity", date="2025-04-29")
        self.assertEqual(activity.description, "Test Activity")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Test Team")
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User")
        workout = Workout.objects.create(user=user, type="Running", duration=30)
        self.assertEqual(workout.type, "Running")