from django.test import TestCase
from .models import Team, UserProfile, Activity, LeaderboardEntry, Workout

class OctofitModelsTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', universe='Test')
        self.user = UserProfile.objects.create(name='Clark Kent', hero_alias='Superman', email='superman@octofit.com', team=self.team)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.universe, 'Test')

    def test_user_creation(self):
        self.assertEqual(self.user.hero_alias, 'Superman')
        self.assertEqual(self.user.team, self.team)

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, activity_type='Flight', duration_minutes=60, calories_burned=1000)
        self.assertEqual(activity.user, self.user)
        self.assertEqual(activity.activity_type, 'Flight')

    def test_leaderboard_entry_creation(self):
        entry = LeaderboardEntry.objects.create(user=self.user, points=100, rank=1)
        self.assertEqual(entry.user, self.user)
        self.assertEqual(entry.rank, 1)

    def test_workout_creation(self):
        workout = Workout.objects.create(user=self.user, title='Kryptonian Strength', difficulty='Advanced', focus_area='Strength', recommended_minutes=45)
        self.assertEqual(workout.user, self.user)
        self.assertEqual(workout.title, 'Kryptonian Strength')
