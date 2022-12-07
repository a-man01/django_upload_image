from django import forms
from .models import UpImage

class UpImageForm(forms.ModelForm):
    class Meta:
        model = UpImage
        fields = ['image', 'name', 'description']
        
        labels = {
            
            "image" : "Gambar",
            "name" : "Nama",
            "description" : "Deskripsi",
        }
        
        widgets = {
            'name' : forms.TextInput(
                attrs={
                'type' : 'text',
                'placeholder' : 'Masukan Nama Gambar',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
            'description' : forms.Textarea(
                attrs={
                'placeholder' : 'Masukan Deskripsi Gambar',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
            'image' : forms.FileInput(
                attrs={
                "accept":"image/*",
                'placeholder' : 'Masukan Gambar',
                'class':'form-control',
                'aria-describedby':'inputGroupPrepend',
                }
            ),
        }
 