from rest_framework import viewsets

from .serializers import TicketSerializer
from .models import Ticket

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer