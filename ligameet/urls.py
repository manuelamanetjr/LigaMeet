from django.urls import path
from . import views
from .views import SportListView
from users.views import choose_role

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('home/', SportListView.as_view(), name='home'),
    path('about/', views.about, name='ligameet-about'),
    path('choose-role/', choose_role, name='choose_role'),
    path('event_organizer/', views.eventorglandingpage, name='event_org_landingpage'),
    path('player/', views.player_dashboard, name='player-dashboard'),
    path('scout/', views.scout_dashboard, name='scout-dashboard'),
    path('create-event/', views.create_event, name='create-event'),
    path('join_team/<int:team_id>/', views.join_team_request, name='join_team_request'),
    path('approve_join_request/<int:request_id>/', views.approve_join_request, name='approve_join_request'),
    path('leave-team/<int:team_id>/', views.leave_team, name='leave-team'),
    path('event-org-dashboard/', views.event_org_dashboard, name='dashboard'),
    path('poke-player/', views.poke_player, name='poke_player'),
    path('mark_notification/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
]

