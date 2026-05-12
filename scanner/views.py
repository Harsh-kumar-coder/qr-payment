from django.shortcuts import render
import qrcode
from io import BytesIO
from base64 import b64encode


def home(request):

    upi_link = 'upi://pay?pa=kumarharsh09374-1@oksbi&pn=Harsh Kumar'
    # upi_link = 'upi://pay?pa=kumarharsh09374-1@oksbi&pn=Harsh Kumar&am=10'

    qr = qrcode.make(upi_link)

    buffer = BytesIO()
    qr.save(buffer, format='PNG')

    qr_image = b64encode(buffer.getvalue()).decode()

    return render(request, 'scan.html', {
        'qr_image': qr_image
    })