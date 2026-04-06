from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .utils import (
    UnsupportedFileFormatError,
    extract_text_from_file,
    file_extension,
    validate_upload_extension,
)


class FileExtensionTests(TestCase):
    def test_file_extension(self):
        self.assertEqual(file_extension("Notes.PDF"), ".pdf")
        self.assertEqual(file_extension("noext"), "")

    def test_validate_upload_extension(self):
        validate_upload_extension("doc.docx")
        with self.assertRaises(UnsupportedFileFormatError):
            validate_upload_extension("x.exe")


class ExtractTextTests(TestCase):
    def test_txt_extract(self):
        f = SimpleUploadedFile("note.txt", b"Hello \xc3\xbc", content_type="text/plain")
        self.assertEqual(extract_text_from_file(f), "Hello ü")

    def test_bad_extension(self):
        f = SimpleUploadedFile("x.bin", b"abc", content_type="application/octet-stream")
        with self.assertRaises(UnsupportedFileFormatError):
            extract_text_from_file(f)
