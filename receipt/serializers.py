from rest_framework import serializers

from receipt.models import Printer, Check


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = ("id", "name", "api_key", "check_type", "point_id")


class CheckSerializer(serializers.ModelSerializer):
    printer_id = PrinterSerializer()

    class Meta:
        model = Check
        fields = (
            "id",
            "printer_id",
            "check_type",
            "order",
            "status",
            "pdf_file"
        )

    def create(self, validated_data):
        point_id = validated_data["printer_id"]["point_id"]
        if not Printer.objects.filter(point_id=point_id).exists():
            raise serializers.ValidationError(
                "Error: The point does not have any printer"
            )

        order = validated_data["order"]
        if Check.objects.filter(order=order).exists():
            raise serializers.ValidationError(
                f"Error: Receipts for the order {order['order_id']} "
                f"has already been created"
            )

        check = Check.objects.create(**validated_data)
        return check
