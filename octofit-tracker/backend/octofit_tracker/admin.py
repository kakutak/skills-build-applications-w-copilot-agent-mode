from django.contrib import admin
from .models import Team, UserProfile, Activity, LeaderboardEntry, Workout

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'universe')
    search_fields = ('name', 'universe')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('hero_alias', 'name', 'email', 'team')
    search_fields = ('hero_alias', 'name', 'email')
    list_filter = ('team',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'calories_burned')
    search_fields = ('user__hero_alias', 'activity_type')
    list_filter = ('activity_type',)

@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'rank')
    search_fields = ('user__hero_alias',)
    list_filter = ('rank',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'difficulty', 'focus_area', 'recommended_minutes')
    search_fields = ('user__hero_alias', 'title', 'focus_area')
    list_filter = ('difficulty', 'focus_area')
