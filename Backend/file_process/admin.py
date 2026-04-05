from django.contrib import admin

from .models import StudyMaterial


@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "user", "original_filename", "uploaded_at"]
    list_filter = ["uploaded_at"]
    search_fields = ["title", "original_filename", "extracted_text"]
    readonly_fields = ["extracted_text", "uploaded_at"]
