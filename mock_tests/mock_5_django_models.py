from unittest.mock import patch

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from model_bakery import baker

from api_auth.models import UserAccount
from tahfidzprogram.models import TahfidzPayment
from tahfidzprogram.serializers import TahfidzPaymentSerializer


class TahfidzPaymentSerializerTests(TestCase):
    def setUp(self) -> None:
        self.image = (
            b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04"
            b"\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02"
            b"\x02\x4c\x01\x00\x3b"
        )

    @patch("django.core.files.storage.FileSystemStorage._save")
    def test_serializer_contains_expected_fields(self, mock_save):
        mock_save.return_value = "proof.gif"
        student = baker.make(UserAccount)
        payment_proof = SimpleUploadedFile(
            name="proof.gif", content=self.image
        )
        payment = baker.make(
            TahfidzPayment, student=student, payment_proof=payment_proof
        )
        serializer = TahfidzPaymentSerializer(instance=payment)

        self.assertCountEqual(
            serializer.data.keys(),
            [
                "id",
                "student",
                "referrals",
                "nominal",
                "payment_proof",
                "is_verified",
            ],
        )

    @patch("django.core.files.storage.FileSystemStorage._save")
    def test_serialize_object_properly(self, mock_save):
        mock_save.return_value = "proof.gif"
        students = baker.make(UserAccount, _quantity=3)
        payment_proof = SimpleUploadedFile(
            name="proof.gif", content=self.image
        )
        payment = baker.make(
            TahfidzPayment, student=students[0], payment_proof=payment_proof,
        )
        payment.referrals.add(students[1], students[2])

        serializer = TahfidzPaymentSerializer(instance=payment)
        data = serializer.data

        self.assertEquals(data["id"], payment.id)
        self.assertEquals(
            data["student"],
            {"id": students[0].id, "username": students[0].username},
        )
        self.assertIn(
            {"id": students[1].id, "username": students[1].username},
            data["referrals"],
        )
        self.assertIn(
            {"id": students[2].id, "username": students[2].username},
            data["referrals"],
        )
        self.assertEquals(data["nominal"], payment.nominal)
        self.assertEquals(data["payment_proof"], payment.payment_proof)
        self.assertEquals(data["is_verified"], payment.is_verified)