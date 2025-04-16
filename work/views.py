from rest_framework import generics
from .models import Work
from .serializers import WorkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

class WorkCreateView(generics.CreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class WorkListView(generics.ListAPIView):
    queryset = Work.objects.all().order_by('-uploaded_at')
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]


class WorkDetailView(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uid'


class WorkUpdateView(generics.UpdateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'uid'


class WorkDeleteView(generics.DestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uid'
