import base64
import json
import os

from django.conf import settings
import requests


def generate_pdf(html):
    b = base64.b64encode(bytes(html, "utf-8"))
    data = {
        "contents": b.decode("utf-8"),
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(
        settings.WKHTMLTOPDF_URL, data=json.dumps(data), headers=headers
    )
    print(response)
    return response


def save_pdf_to_media(pdf_file, order_id, check_type):
    target_path = os.path.join(settings.MEDIA_ROOT, "pdf")
    os.makedirs(target_path, exist_ok=True)

    file_name = f"{order_id}_{check_type}.pdf"
    file_path = os.path.join(target_path, file_name)
    with open(file_path, "wb") as file:
        file.write(pdf_file.content)

    return file_path
