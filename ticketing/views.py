from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from psycopg2 import IntegrityError
from rest_framework.filters import SearchFilter, OrderingFilter
import json

from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet

from ticketing.exceptions import TransactionException, CreatingException, IncorrectDataException
from ticketing.models import Match, Stadium, SeasonTicketHolder, Sector, Seat, SeasonTicket, Ticket
from ticketing.serializers import MatchSerializer, StadiumSerializer, SeasonTicketHolderSerializer, SectorSerializer, \
    SeatSerializer, TicketSerializer, SeasonTicketSerializer


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['date', 'status', 'type']
    search_fields = ['type', 'status']
    ordering_fields = ['status', 'date', 'type']


class StadiumViewSet(ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer


class SectorViewSet(ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['stadium']


class SeatViewSet(ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['sector']


class SeasonTicketHolderViewSet(ModelViewSet):
    queryset = SeasonTicketHolder.objects.all()
    serializer_class = SeasonTicketHolderSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class SeasonTicketViewSet(ModelViewSet):
    queryset = SeasonTicket.objects.all()
    serializer_class = SeasonTicketSerializer

@csrf_exempt
def buy_season_ticket(request):
    data = json.loads(request.body)
    try:
        ticket = SeasonTicket.buy(data)
    except IncorrectDataException as e:
        return HttpResponse(e.message, status=400)
    except CreatingException as e:
        return HttpResponse(e.message, status=400)
    except TransactionException as e:
        return HttpResponse("Error with paying, try again", status=400)
    return HttpResponse(ticket)


@csrf_exempt
def return_ticket(request):
    data = json.loads(request.body)
    try:
        Ticket.refund(data)
    except IncorrectDataException as e:
        return HttpResponse(e.message, status=400)
    except CreatingException as e:
        return HttpResponse(e.message, status=400)
    except TransactionException as e:
        return HttpResponse("Error with redunding, try again", status=400)
    return HttpResponse("Money will returned in a hour")
