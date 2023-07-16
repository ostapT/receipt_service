# Generated by Django 4.2.3 on 2023-07-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipt", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="check",
            name="check_type",
            field=models.CharField(
                choices=[("Kitchen", "kitchen"), ("Client", "client")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="check",
            name="status",
            field=models.CharField(
                choices=[
                    ("Created", "created"),
                    ("Rendered", "rendered"),
                    ("Printed", "printed"),
                ],
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="printer",
            name="check_type",
            field=models.CharField(
                choices=[("Kitchen", "kitchen"), ("Client", "client")], max_length=10
            ),
        ),
    ]