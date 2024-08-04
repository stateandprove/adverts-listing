from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import F

from .models import Advert
from .serializers import AdvertSerializer


class GenericAdvertViewSet(GenericViewSet):
    serializer_class = AdvertSerializer
    http_method_names = ["get"]
    queryset = Advert.objects.select_related(
        "city", "category"
    ).order_by(
        "-id"
    ).all()


class AdvertListViewSet(ListModelMixin, GenericAdvertViewSet):
    ...


class AdvertRetrieveViewSet(RetrieveModelMixin, GenericAdvertViewSet):
    
    def retrieve(self, request, pk=None):
        if not pk.isnumeric():
            raise Http404

        queryset = self.get_queryset().filter(pk=pk)

        # increments views by one avoiding race condition
        queryset.update(views=F('views')+1)

        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
