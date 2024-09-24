from django.shortcuts import render, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Sport, Team, Match, TeamParticipant
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch


def home(request):
    context = {
        'sports': Sport.objects.all()
    }
    return render(request, 'ligameet/home.html', context)

# class SportListView(LoginRequiredMixin,ListView):
class SportListView(ListView):
    model = Sport
    template_name = 'ligameet/home.html'
    context_object_name = 'sports'
    ordering = ['-EDITED_AT'] # - so that it displays the newest 

def about(request):
    return render(request, 'ligameet/about.html', {'title':'About'})

def landingpage(request):
    return render (request, 'ligameet/landingpage.html', {'title': 'Landing Page'})

def eventorglandingpage(request):
    return render (request, 'ligameet/eventorglandingpage.html', {'title': 'Event Organizer Landing Page'})

def player_dashboard(request):
    if request.user.profile.role == 'Player':
        query = request.GET.get('q', '')
        match_type = request.GET.get('type', '')
        match_category = request.GET.get('category', '')

        # Fetch Basketball and Volleyball Sport IDs
        basketball_sport = Sport.objects.filter(SPORT_NAME__iexact='Basketball').first()
        volleyball_sport = Sport.objects.filter(SPORT_NAME__iexact='Volleyball').first()

        # Fetch teams based on their SPORT_ID (basketball or volleyball)
        basketball_teams = Team.objects.filter(SPORT_ID=basketball_sport).prefetch_related(
            Prefetch('teamparticipant_set', queryset=TeamParticipant.objects.select_related('PART_ID'))
        )
        volleyball_teams = Team.objects.filter(SPORT_ID=volleyball_sport).prefetch_related(
            Prefetch('teamparticipant_set', queryset=TeamParticipant.objects.select_related('PART_ID'))
        )

        # Apply search query to team names if provided
        if query:
            basketball_teams = basketball_teams.filter(TEAM_NAME__icontains=query)
            volleyball_teams = volleyball_teams.filter(TEAM_NAME__icontains=query)

        # Fetch and filter matches (you already have the logic for this)
        matches = Match.objects.all()
        if match_type:
            matches = matches.filter(MATCH_TYPE__icontains=match_type)
        if match_category:
            matches = matches.filter(MATCH_CATEGORY__icontains(match_category))
        if query:
            matches = matches.filter(TEAM_ID__TEAM_NAME__icontains(query))

        # Pass filtered teams and matches to the context
        context = {
            'basketball_teams': basketball_teams,
            'volleyball_teams': volleyball_teams,
            'matches': matches,
        }

        return render(request, 'ligameet/player_dashboard.html', context)
    else:
        return redirect('home')
    
@login_required
def player_landing(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.role == 'Player':
        return render(request, 'ligameet/player_landing.html')
    else:
        return redirect('home')  # Redirect to home or another page if not a player