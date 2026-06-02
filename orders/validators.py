"""
Validation helpers for security and data quality.
"""
from django.core.exceptions import ValidationError

ALLOWED_UPLOAD_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".zip"}
MAX_UPLOAD_SIZE_BYTES = 10 * 1024 * 1024


def validate_upload(file_obj):
    name = (file_obj.name or "").lower()
    size = getattr(file_obj, "size", 0)

    if size > MAX_UPLOAD_SIZE_BYTES:
        raise ValidationError("File too large (max 10MB).")

    ext = "." + name.split(".")[-1]
    if ext not in ALLOWED_UPLOAD_EXTENSIONS:
        raise ValidationError("Unsupported file type.")
