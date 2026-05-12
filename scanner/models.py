from django.db import models

class QRCode(models.Model):
    image = models.ImageField(upload_to='qr/')
    data = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data