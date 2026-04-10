from django.core.management.base import BaseCommand

from octofit_tracker.models import (
    Activity,
    LeaderboardEntry,
    Team,
    UserProfile,
    Workout,
)


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing test data...')
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        team_dc = Team.objects.create(name='Team DC', universe='DC')

        self.stdout.write('Creating users...')
        users = [
            UserProfile.objects.create(
                name='Peter Parker',
                hero_alias='Spider-Man',
                email='spiderman@octofit.com',
                team=team_marvel,
            ),
            UserProfile.objects.create(
                name='Tony Stark',
                hero_alias='Iron Man',
                email='ironman@octofit.com',
                team=team_marvel,
            ),
            UserProfile.objects.create(
                name='Bruce Wayne',
                hero_alias='Batman',
                email='batman@octofit.com',
                team=team_dc,
            ),
            UserProfile.objects.create(
                name='Diana Prince',
                hero_alias='Wonder Woman',
                email='wonderwoman@octofit.com',
                team=team_dc,
            ),
        ]

        self.stdout.write('Creating activities...')
        Activity.objects.bulk_create(
            [
                Activity(user=users[0], activity_type='Web Swinging Cardio', duration_minutes=45, calories_burned=520),
                Activity(user=users[1], activity_type='Arc Reactor HIIT', duration_minutes=35, calories_burned=460),
                Activity(user=users[2], activity_type='Night Patrol Run', duration_minutes=50, calories_burned=540),
                Activity(user=users[3], activity_type='Amazon Strength Circuit', duration_minutes=40, calories_burned=500),
            ]
        )

        self.stdout.write('Creating leaderboard entries...')
        LeaderboardEntry.objects.bulk_create(
            [
                LeaderboardEntry(user=users[3], points=980, rank=1),
                LeaderboardEntry(user=users[2], points=940, rank=2),
                LeaderboardEntry(user=users[0], points=910, rank=3),
                LeaderboardEntry(user=users[1], points=870, rank=4),
            ]
        )

        self.stdout.write('Creating workout recommendations...')
        Workout.objects.bulk_create(
            [
                Workout(user=users[0], title='Agility Ladder Blast', difficulty='Intermediate', focus_area='Speed', recommended_minutes=30),
                Workout(user=users[1], title='Core Reactor Burn', difficulty='Advanced', focus_area='Core', recommended_minutes=25),
                Workout(user=users[2], title='Gotham Endurance Builder', difficulty='Advanced', focus_area='Endurance', recommended_minutes=35),
                Workout(user=users[3], title='Amazon Power Flow', difficulty='Intermediate', focus_area='Strength', recommended_minutes=30),
            ]
        )

        self.stdout.write(self.style.SUCCESS('octofit_db populated successfully.'))
