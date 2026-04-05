from django.contrib.auth.models import User
from django.db import models


class StudyMaterial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    original_filename = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to="materials/")
    extracted_text = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(
                fields=["user", "uploaded_at"],
                name="fp_mat_user_uploaded",
            ),
        ]
        ordering = ["-uploaded_at"]

    def __str__(self):
        if self.title:
            return self.title
        if self.original_filename:
            return self.original_filename
        return self.file.name

    @property
    def content(self):
        """Alias used by study AI views (`material.content`)."""
        return self.extracted_text or ""
