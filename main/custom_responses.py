from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import NotFound

class CustomResponseMixin:
    """
    A mixin to standardize custom response formats for list, create, retrieve, and update actions.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "ok": True,
            "data": serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({
                "ok": True,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "ok": False,
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response({
            "ok": True,
            "data": serializer.data
        })

    def update(self, request, *args, **kwargs):
        partial = kwargs.get('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            updated_instance = serializer.save()
            return Response({
                "ok": True,
                "data": serializer.data
            })
        return Response({
            "ok": False,
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            return super().get_object()
        except NotFound:
            return Response({
                "ok": False,
                "message": f"{self.queryset.model.__name__} not found"
            }, status=status.HTTP_404_NOT_FOUND)
