from celery import shared_task
from django.template.loader import render_to_string

from receipt.models import Printer, CheckStatus, Check
from receipt.utils import generate_pdf, save_pdf_to_media


@shared_task
def generate_check_pdf(check_id):
    check = Check.objects.get(id=check_id)
    template_name = "check_template.html"
    context = {"check": check}
    html = render_to_string(template_name, context)
    pdf_file = generate_pdf(html)
    saved_pdf_path = save_pdf_to_media(
        pdf_file, check.order["order_id"], check.check_type
    )
    check.status = CheckStatus.RENDERED
    check.pdf_file = saved_pdf_path
    check.save()
    print_checks.delay()


@shared_task
def print_checks() -> None:
    printers = Printer.objects.all()

    for printer in printers:
        checks = printer.checks.filter(status=CheckStatus.RENDERED)

        for check in checks:
            check.status = CheckStatus.PRINTED
            check.save()
