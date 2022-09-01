from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ticketing.models import Match, Stadium, SeasonTicketHolder, Sector, Seat, Ticket, SeasonTicket


class StadiumSerializer(ModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'


class MatchSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class SectorSerializer(ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class SeatSerializer(ModelSerializer):
    season_ticket_price = serializers.ReadOnlyField()

    class Meta:
        model = Seat
        fields = ('sector', 'number', 'season_ticket_price')


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class SeasonTicketSerializer(ModelSerializer):
    class Meta:
        model = SeasonTicket
        fields = '__all__'


class SeasonTicketHolderSerializer(ModelSerializer):
    class Meta:
        model = SeasonTicketHolder
        fields = '__all__'
