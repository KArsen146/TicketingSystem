import decimal

from django.db import models

from ticketing.exceptions import TransactionException, CreatingException, IncorrectDataException


class Stadium(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'Stadium {self.name}'


class Sector(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f'Sector on the {self.stadium.name} with number: {self.number}'

    class Meta:
        unique_together = ['stadium', 'number']


class Seat(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    number = models.IntegerField()

    def season_ticket_price(self):
        price = 0
        for match in Match.objects.all():
            if match.stadium == self.sector.stadium:
                price += match.ticket_price
        return price * decimal.Decimal(0.8)

    def __str__(self):
        return f'Seat on the sector {self.sector.number} with number {self.number}'

    class Meta:
        unique_together = ['sector', 'number']


class Match(models.Model):
    STATUS_CHOICES = (
        ('played', 'Played'),
        ('planned', 'Planned')
    )

    TYPE_CHOICES = (
        ('league', 'League'),
        ('cup', 'Cup'),
        ('international', 'International'),
        ('friendly', 'Friendly')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='planned')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='friendly')
    opponent = models.CharField(max_length=50)
    ticket_price = models.DecimalField(max_digits=7, decimal_places=2, default=500)
    date = models.DateTimeField(unique=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

    def __str__(self):
        return f'Match on the stadium {self.stadium} with id: {self.id} on {self.date}'


class SeasonTicketHolder(models.Model):
    surname = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    passport_id = models.IntegerField(unique=True)

    def __str__(self):
        return f'Season ticket holder with with id: {self.id}'


class SeasonTicket(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    holder = models.OneToOneField(SeasonTicketHolder, on_delete=models.CASCADE, unique=True)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f'SeasonTicket  with id: {self.id} and holder {self.holder.id}'


    @classmethod
    def buy(cls, data):
        try:
            stadium_id = data["stadium_id"]
            stadium = Stadium.objects.get(pk=stadium_id)
            holder_id = data["holder_id"]
            holder = SeasonTicketHolder.objects.get(pk=holder_id)
            seat_id = data["seat_id"]
            seat = Seat.objects.get(pk=seat_id)
        except Exception as e:
            raise IncorrectDataException(e.args[0])
        try:
            st = SeasonTicket(
                stadium=stadium,
                holder=holder,
                seat=seat
            )

            st.save()
        except Exception as e:
            raise CreatingException(e.args[0])
        card_number = data["card_number"]
        price = data["price"]
        payment = Payment(
            ticket=st,
            value=price,
            pay_from=card_number,
            pay_to='1234567812345678'
        )
        try:
            payment.process()
        except TransactionException as e:
            payment.status = 'canceled'
            st.delete()
            st.save()
            raise e
        st.save()
        payment.save()
        return st

    class Meta:
        unique_together = ['stadium', 'seat']


class Ticket(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f'Ticket to the match {self.match} with id: {self.id}'

    @classmethod
    def refund(cls, data):
        try:
            ticket_id = data['ticket_id']
            t = Ticket.objects.get(pk=ticket_id)
            transaction = RefundingPayment.objects.get(ticket=t)
        except Exception as e:
            raise IncorrectDataException(e.args[0])
        r = Refund(
            transaction
        )
        try:
            r.process()
        except TransactionException as e:
            r.status = 'canceled'
            raise e
        t.delete()

    class Meta:
        unique_together = ['stadium', 'match', 'seat']


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('inprogress', 'In progress'),
        ('complited', 'Complited'),
        ('canceled', 'Canceled')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inprogress')

    def __str__(self):
        return f'Transaction {self.id}'

    def process(self):
        pass


class AbstractPayment(Transaction):
    value = models.DecimalField(max_digits=7, decimal_places=2)
    pay_from = models.CharField(max_length=16)
    pay_to = models.CharField(max_length=16)

    def __str__(self):
        return f'Payment {self.id}'

    class Meta:
        abstract = True


class Payment(AbstractPayment):
    ticket = models.OneToOneField(SeasonTicket, on_delete=models.CASCADE)


class RefundingPayment(AbstractPayment):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)


class Refund(Transaction):
    transaction = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return f'Refund {self.id}'
