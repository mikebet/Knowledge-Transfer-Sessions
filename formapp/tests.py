import json
from pathlib import Path

from django.test import TestCase, override_settings


class FormSubmissionTests(TestCase):
    @override_settings(SUBMISSIONS_FILE=Path("test_submissions.json"))
    def test_successful_submission_is_saved(self) -> None:
        target_path = Path("test_submissions.json")
        if target_path.exists():
            target_path.unlink()

        response = self.client.post(
            "/",
            {
                "name": "Jane Doe",
                "email": "jane@example.com",
                "id": "ABC123",
                "phone": "1234567890",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(target_path.exists())

        with target_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Jane Doe")

        target_path.unlink()

    @override_settings(SUBMISSIONS_FILE=Path("test_submissions_invalid.json"))
    def test_missing_fields_return_errors(self) -> None:
        response = self.client.post(
            "/",
            {
                "name": "",
                "email": "",
                "id": "",
                "phone": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertTrue(form.errors)
