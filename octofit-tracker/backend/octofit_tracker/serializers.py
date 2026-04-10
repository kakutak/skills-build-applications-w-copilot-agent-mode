from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'universe']


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    team_id = serializers.CharField(source='team.id', read_only=True)
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'hero_alias', 'email', 'team', 'team_id', 'team_name']


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField(source='user.id', read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'activity_type', 'duration_minutes', 'calories_burned']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField(source='user.id', read_only=True)
    hero_alias = serializers.CharField(source='user.hero_alias', read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'user_id', 'hero_alias', 'points', 'rank']


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField(source='user.id', read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'user_id', 'title', 'difficulty', 'focus_area', 'recommended_minutes']
