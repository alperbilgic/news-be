from rest_framework import viewsets, pagination
from rest_framework.permissions import AllowAny

from api import models, serializers, mixins


# Create your views here.
class NewsViewSet(mixins.ListDetailSerializerMixin, viewsets.ModelViewSet):
    list_serializer_class = serializers.NewsListSerializer
    detail_serializer_class = serializers.NewsSerializer
    queryset = models.News.objects.all()
    permission_classes_by_action = {
        'create': [AllowAny],
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'partial_update': [AllowAny],
        'destroy': [AllowAny],
    }
    pagination_class = pagination.LimitOffsetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = models.News.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset.order_by("-date")

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]