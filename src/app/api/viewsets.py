from rest_framework import mixins
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class DefaultCreateModelMixin(CreateModelMixin):
    """Return detail-serialized created instance"""

    def create(self, request, *args, **kwargs):  # type: ignore
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.instance = self.perform_create(serializer)  # No getting created instance in original DRF
        headers = self.get_success_headers(serializer.data)
        return self.response(serializer.instance, status.HTTP_201_CREATED, headers)

    def perform_create(self, serializer):  # type: ignore
        return serializer.save()  # No returning created instance in original DRF


class DefaultUpdateModelMixin(UpdateModelMixin):
    """Return detail-serialized updated instance"""

    def update(self, request, *args, **kwargs):  # type: ignore
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_update(serializer)  # No getting updated instance in original DRF

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return self.response(instance, status.HTTP_200_OK)

    def perform_update(self, serializer):  # type: ignore
        return serializer.save()  # No returning updated instance in original DRF


class ResponseWithRetrieveSerializerMixin:
    """
    Always response with 'retrieve' serializer or fallback to `serializer_class`.
    Usage:

    class MyViewSet(DefaultModelViewSet):
        serializer_class = MyDefaultSerializer
        serializer_action_classes = {
           'list': MyListSerializer,
           'my_action': MyActionSerializer,
        }
        @action
        def my_action:
            ...

    'my_action' request will be validated with MyActionSerializer,
    but response will be serialized with MyDefaultSerializer
    (or 'retrieve' if provided).

    Thanks gonz: http://stackoverflow.com/a/22922156/11440

    """
    def response(self, instance, status, headers=None, refresh=True):  # type: ignore
        if refresh:
            # We do that to apply annotations and stuff from get_queryset()
            instance = self.get_queryset().get(id=instance.id)

        retrieve_serializer_class = self.get_serializer_class(action='retrieve')
        context = self.get_serializer_context()
        retrieve_serializer = retrieve_serializer_class(instance, context=context)
        return Response(retrieve_serializer.data, status=status, headers=headers)


class DefaultModelViewSet(  # type: ignore
    DefaultCreateModelMixin,  # Create response is overriden
    mixins.RetrieveModelMixin,
    DefaultUpdateModelMixin,  # Update response is overriden
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    ResponseWithRetrieveSerializerMixin,  # Response with retrieve or default serializer
    GenericViewSet,
):
    def paginated_serialized_response(self, queryset):  # type: ignore
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
