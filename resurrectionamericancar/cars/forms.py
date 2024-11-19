from django import forms 
from . import models


class CrearCar(forms.ModelForm):
    
    class Meta:
        model = models.Cars
        fields = ["marca","body_style","fuel_type","nuevo_usado","year","modelo","only_oneowner","imagen","color","descripcion","precio","en_stock"]
        widgets = {
            'marca': forms.Select(
                attrs={'class': 'form-select col-md-6 mx-auto',
                       'aria-label': 'Default select example'},
                choices=[
                    ('ACURA', 'ACURA'),
                    ('ALFA ROMEO', 'ALFA ROMEO'),
                    ('AM GENERAL', 'AM GENERAL'),
                    ('ASTON MARTIN', 'ASTON MARTIN'),
                    ('AUDI', 'AUDI'),
                    ('BENTLEY', 'BENTLEY'),
                    ('BMW', 'BMW'),
                    ('BUICK', 'BUICK'),
                    ('TOYOTA', 'TOYOTA'),
                    ('FORD', 'FORD'),
                    ('KIA', 'KIA'),
                    ('HONDA', 'HONDA'),
                    ('HYUNDAI', 'HYUNDAI'),
                ]
            ),
            'body_style': forms.Select(
                attrs={'class': 'form-select col-md-6 mx-auto',
                       'aria-label': 'Default select example'},
                choices=[
                    ('Truck', 'Truck'),
                    ('Regular cab truck', 'Regular cab truck'),
                    ('Crew cab truck', 'Crew cab truck'),
                    ('Extended cab truck', 'Extended cab truck'),
                    ('Minivan', 'Minivan'),
                    ('Cargo van', 'Cargo van'),
                    ('Passenger van', 'Passenger van'),
                    ('SUV', 'SUV'),
                    ('Wagon', 'Wagon'),
                    ('Hatchback', 'Hatchback'),                    
                ]
            ),
            'fuel_type': forms.Select(
                attrs={'class': 'form-select col-md-6 mx-auto',
                       'aria-label': 'Default select example'},
                choices=[
                    ('Electric', 'Electric'),
                    ('Hybrid', 'Hybrid'),                   
                    ('Gasolina', 'Gasolina'),                   
                    ('Diesel', 'Diesel'),                   
                    ('Híbridos enchufables (PHEV)', 'Híbridos enchufables (PHEV)'),                   
                    ('GNC (Gas Natural Comprimido)', 'GNC (Gas Natural Comprimido)'),                   
                    ('GPL (Gas Licuado de petróleo)', 'GPL (Gas Licuado de petróleo)'),                   
                    ('Biocombustible', 'Biocombustible'),                   
                    ('Etanol', 'Etanol'),                   
                ]
            ),
             'nuevo_usado': forms.Select(
                attrs={'class': 'form-select col-md-6 mx-auto',
                       'aria-label': 'Default select example'},
                choices=[
                    ('nuevo', 'nuevo'),
                    ('usado', 'usado'),                   
                                     
                ]
            ),
            'modelo': forms.TextInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'only_oneowner': forms.CheckboxInput(attrs={'class': 'form-check-input mx-auto'}),
            'color': forms.TextInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'year': forms.NumberInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'en_stock': forms.NumberInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            
        }
