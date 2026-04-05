import os
from pathlib import Path

from rest_framework import serializers

from .constants import MAX_UPLOAD_BYTES
from .models import StudyMaterial
from .utils import UnsupportedFileFormatError, extract_text_from_file, validate_upload_extension


class StudyMaterialListSerializer(serializers.ModelSerializer):
    """List view: avoid sending full `extracted_text` payloads."""

    class Meta:
        model = StudyMaterial
        fields = [
            "id",
            "user",
            "title",
            "original_filename",
            "file",
            "uploaded_at",
        ]
        read_only_fields = fields


class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = [
            "id",
            "user",
            "title",
            "original_filename",
            "file",
            "extracted_text",
            "uploaded_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "original_filename",
            "extracted_text",
            "uploaded_at",
        ]
        extra_kwargs = {
            "title": {"required": False, "allow_blank": True},
        }

    def validate_file(self, value):
        if value.size > MAX_UPLOAD_BYTES:
            max_mb = MAX_UPLOAD_BYTES // (1024 * 1024)
            raise serializers.ValidationError(
                f"File too large. Maximum size is {max_mb} MB."
            )
        name = getattr(value, "name", "") or ""
        try:
            validate_upload_extension(name)
        except UnsupportedFileFormatError:
            raise serializers.ValidationError(
                "Unsupported format. Use PDF, DOCX, or TXT."
            ) from None
        return value

    def create(self, validated_data):
        upload = validated_data["file"]
        raw_name = getattr(upload, "name", "") or ""
        validated_data["original_filename"] = os.path.basename(raw_name)[:255]

        title = (validated_data.get("title") or "").strip()
        if not title:
            stem = Path(os.path.basename(raw_name)).stem or "Study material"
            title = stem[:255]
        validated_data["title"] = title

        try:
            extracted = extract_text_from_file(upload)
        except UnsupportedFileFormatError:
            raise serializers.ValidationError(
                {"file": "Unsupported format. Use PDF, DOCX, or TXT."}
            )
        except ValueError as exc:
            raise serializers.ValidationError({"file": str(exc)}) from exc

        validated_data["extracted_text"] = extracted
        return super().create(validated_data)
