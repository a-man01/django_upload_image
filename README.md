# django_upload_image

Upload image pada project django dengan menggunakan cloudinary storage

**=========SETUP CLOUDINARY STORAGE=========**

1. Install django-cloudinary-storage dan Pillow
```bash
pip install django-cloudinary-storage
pip install Pillow
```
2. Tambahkan cloudinary pada settings.py
```python
import cloudinary
...
INSTALLED_APPS = [
    ...
    'cloudinary',
    'cloudinary_storage',
]
```
3. Atur media root dan media url pada settings.py
file `settings.py`
```python
import os
...
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
file urls.py
```python
from django.conf import settings
from django.conf.urls.static import static
...
urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
4. Tambahkan config cloudinary pada settings.py
```python
import cloudinary
...
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your_cloud_name',
    'API_KEY': 'your_api_key',
    'API_SECRET': 'your_api_secret'
}
```
> **catatan**: 
> - untuk mendapatkan `CLOUD_NAME`, `API_KEY`, dan `API_SECRET` silahkan buat akun di [cloudinary](https://cloudinary.com/)
> - untuk lebih aman, data-data tersebut bisa disimpan pada file `.env` dan di import menggunakan `python-decouple` atau tambahkan pada environment variable pada sistem operasi atau di repository hosting (github, gitlab, dll)
5. Override default storage pada settings.py
```python
...
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```


