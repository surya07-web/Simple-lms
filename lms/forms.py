from django import forms
from .models import Mahasiswa

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['foto', 'nama', 'prodi', 'angkatan', 'alamat']
        widgets = {
            'nama': forms.TextInput(attrs={'readonly': 'readonly'}),
            'prodi': forms.TextInput(attrs={'readonly': 'readonly'}),
            'angkatan': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'alamat': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Masukkan alamat Anda di sini...'}),
        }
