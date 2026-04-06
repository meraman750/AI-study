from django.urls import path

from .views import (
    StudyMaterialDetailView,
    StudyMaterialListView,
    StudyMaterialUploadView,
)

urlpatterns = [
    path("materials/upload/", StudyMaterialUploadView.as_view(), name="material-upload"),
    path("materials/", StudyMaterialListView.as_view(), name="material-list"),
    path(
        "materials/<int:pk>/",
        StudyMaterialDetailView.as_view(),
        name="material-detail",
    ),
]
