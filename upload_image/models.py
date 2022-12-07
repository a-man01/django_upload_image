from django.db import models

# Create your models here.

class UpImage(models.Model):
    image = models.ImageField(upload_to='up_image_test/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
