"""TicketingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from ticketing.views import MatchViewSet, StadiumViewSet, SeasonTicketHolderViewSet, SectorViewSet, SeatViewSet, \
    buy_season_ticket, return_ticket, SeasonTicketViewSet, TicketViewSet

router = SimpleRouter()
router.register(r'match', MatchViewSet)
router.register(r'stadium', StadiumViewSet)
router.register(r'sector', SectorViewSet)
router.register(r'seat', SeatViewSet)
router.register(r'season-ticket-holder', SeasonTicketHolderViewSet)
router.register(r'ticket', TicketViewSet)
router.register(r'season-ticket', SeasonTicketViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('buy-season-ticket/', buy_season_ticket, name='buy'),
    path('return-ticket/', return_ticket, name='refund')
]

urlpatterns += router.urls
