from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from .models import StudyMaterial
from .serializers import StudyMaterialListSerializer, StudyMaterialSerializer


class StudyMaterialPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50


class StudyMaterialListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StudyMaterialPagination

    def get_serializer_class(self):
        return StudyMaterialListSerializer

    def get_queryset(self):
        return StudyMaterial.objects.filter(user=self.request.user)


class StudyMaterialUploadView(generics.CreateAPIView):
    serializer_class = StudyMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StudyMaterialDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = StudyMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyMaterial.objects.filter(user=self.request.user)
