from django.db import models


class CheckType(models.TextChoices):
    KITCHEN = "Kitchen", "kitchen"
    CLIENT = "Client", "client"


class CheckStatus(models.TextChoices):
    CREATED = "Created", "created"
    RENDERED = "Rendered", "rendered"
    PRINTED = "Printed", "printed"


TYPES = (
    ("kitchen", "Kitchen"),
    ("client", "Client"),
)
STATUS = (("new", "New"), ("rendered", "Rendered"), ("printed", "Printed"))


class Printer(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255, unique=True)
    check_type = models.CharField(max_length=10, choices=CheckType.choices)
    point_id = models.IntegerField()

    def __str__(self):
        return self.name


class Check(models.Model):
    printer = models.ForeignKey(
        Printer, on_delete=models.CASCADE, related_name="checks"
    )
    check_type = models.CharField(max_length=10, choices=CheckType.choices)
    order = models.JSONField()
    status = models.CharField(max_length=15, choices=CheckStatus.choices)
    pdf_file = models.FileField()
