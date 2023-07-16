from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from receipt.models import Printer, Check, CheckStatus
from receipt.tasks import generate_check_pdf
from receipt.serializers import PrinterSerializer, CheckSerializer


class PrinterViewSet(viewsets.ModelViewSet):
    serializer_class = PrinterSerializer
    queryset = Printer.objects.all()


class CheckViewSet(viewsets.ModelViewSet):
    serializer_class = CheckSerializer
    queryset = Check.objects.all()


@api_view(["POST"])
def create_order(request):
    order_data = request.data

    printers = Printer.objects.filter(point_id=order_data["point_id"])

    for printer in printers:
        check = Check(
            printer_id=printer,
            check_type=printer.check_type,
            order=order_data["order"],
            status=CheckStatus.CREATED,
        )
        print("CREATED CHECK!")
        check.save()
        generate_check_pdf.delay(check.id)

    return JsonResponse({"success": "The order was successfully processed"})
