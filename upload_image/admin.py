from django.contrib import admin

# Register your models here.
import upload_image.models as upload_image

admin.site.register(upload_image.UpImage)