from django.contrib import admin

from ticketing.models import *

admin.site.register(Match)
admin.site.register(Stadium)
admin.site.register(Sector)
admin.site.register(Seat)
admin.site.register(SeasonTicketHolder)
admin.site.register(SeasonTicket)
admin.site.register(Ticket)
admin.site.register(RefundingPayment)
