from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Snack
from .serializer import SnackSerializer
from .permissions import isOwnerOrReadOnly


class SnackList(ListAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
