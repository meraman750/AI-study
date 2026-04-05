import os

# Study uploads: PDF / Word / plain text (matches frontend accept list).
ALLOWED_EXTENSIONS = frozenset({".pdf", ".docx", ".txt"})


def _max_upload_bytes():
    raw = os.environ.get("FILE_PROCESS_MAX_UPLOAD_MB", "15")
    try:
        mb = int(raw)
    except ValueError:
        mb = 15
    return max(1, mb) * 1024 * 1024


MAX_UPLOAD_BYTES = _max_upload_bytes()
