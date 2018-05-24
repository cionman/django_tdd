from django.shortcuts import render
from rest_framework import viewsets

from api.serializer import CodelabSerializer
from codelab.models import Codelab


class CodelabViewSet(viewsets.ModelViewSet):
    queryset = Codelab.objects.all()
    serializer_class = CodelabSerializer
