from django.contrib import admin

from receipt.models import Printer, Check


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_filter = ["check_type"]


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_filter = ["printer_id", "check_type", "status"]
