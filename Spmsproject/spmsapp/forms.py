from django import forms

from .models import Category
from .models import Add_vehicle

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id','parking_area_no','vehicle_type','vehicle_limit','parking_charge']
        widgets={
        'parking_area_no':forms.TextInput(attrs={'class':'form-control'}),
        'vehicle_type' :forms.TextInput(attrs={'class':'form-control'}),
        'vehicle_limit' :forms.TextInput(attrs={'class':'form-control'}),
        'parking_charge':forms.TextInput(attrs={'class':'form-control'}),
        }
class VehicleForm(forms.ModelForm):
    class Meta:
        model =Add_vehicle

        fields =['id','vehicle_no','vehicle_type','parking_area_no','parking_charge']
        widgets={
        'vehicle_no':forms.TextInput(attrs={'class':'form-control'}),
        'vehicle_type' :forms.TextInput(attrs={'class':'form-control'}),
        'parking_area_no' :forms.TextInput(attrs={'class':'form-control'}),
        'parking_charge':forms.TextInput(attrs={'class':'form-control'}),
        }
