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
                    ('AUSTIN-HEALEY', 'AUSTIN-HEALEY'),
                    ('BENTLEY', 'BENTLEY'),
                    ('BMW', 'BMW'),
                    ('BUICK', 'BUICK'),
                    ('CADILLAC', 'CADILLAC'),
                    ('CHEVROLET', 'CHEVROLET'),
                    ('CHRYSLER', 'CHRYSLER'),
                    ('DATSUN', 'DATSUN'),
                    ('DODGE', 'DODGE'),
                    ('FERRARI', 'FERRARI'),
                    ('FIAT', 'FIAT'),
                    ('FISKER', 'FISKER'),                    
                    ('FORD', 'FORD'),
                    ('GENESIS', 'GENESIS'),
                    ('GMC', 'GMC'),                    
                    ('HONDA', 'HONDA'),
                    ('HUMMER', 'HUMMER'),
                    ('HYUNDAI', 'HYUNDAI'),
                    ('INEOS', 'INEOS'),
                    ('INFINITI', 'INFINITI'),
                    ('JAGUAR', 'JAGUAR'),
                    ('JEEP', 'JEEP'),
                    ('KARMA', 'KARMA'),
                    ('KIA', 'KIA'),
                    ('LAMBORGHINI', 'LAMBORGHINI'),
                    ('LAND ROVER', 'LAND ROVER'),
                    ('LEXUS', 'LEXUS'),
                    ('LINCOLN', 'LINCOLN'),
                    ('LOTUS', 'LOTUS'),
                    ('LUCID', 'LUCID'),
                    ('MASERATI', 'MASERATI'),
                    ('MAZDA', 'MAZDA'),
                    ('MCLAREN', 'MACLAREN'),
                    ('MERCEDEZ-BENZ', 'MERCEDEZ-BENZ'),
                    ('MERCURY', 'MERCURY'),
                    ('MG', 'MG'),
                    ('MINI', 'MINI'),
                    ('MITSUBISHI', 'MITSUBISHI'),
                    ('NISSAN', 'NISSAN'),
                    ('OLDSMOBILE', 'OLDSMOBILE'),
                    ('PLYMOUTH', 'PLYMOUTH'),
                    ('POLESTAR', 'POLESTAR'),
                    ('PONTIAC', 'PONTIAC'),
                    ('PORSCHE', 'PORSCHE'),
                    ('RAM', 'RAM'),
                    ('RIVIAN', 'RIVIAN'),
                    ('ROLLS-ROYCE', 'ROLLS-ROYCE'),
                    ('SAAB', 'SAAB'),
                    ('SATURN', 'SATURN'),
                    ('SCION', 'SCION'),
                    ('SMART', 'SMART'),
                    ('SUBARU', 'SUBARU'),
                    ('SUZUKI', 'SUZUKI'),
                    ('TESLA', 'TESLA'),
                    ('TOYOTA', 'TOYOTA'),
                    ('TRIUMPH', 'TRIUMPH'),
                    ('VINFAST', 'VINFAST'),
                    ('VOLKSWAGEN', 'VOLSWAGEN'),
                    ('VOLVO', 'VOLVO'),
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
                    ('Sedan', 'Sedan'),
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
            'color': forms.Select(
                attrs={'class': 'form-select col-md-6 mx-auto',
                       'aria-label': 'Default select example'},
                choices=[                    
                    ('aceituna', 'aceituna'),
                    ('amarillo', 'amarillo'),
                    ('azul', 'azul'),
                    ('blanco', 'blanco'),
                    ('carmelita', 'carmelita'),                    
                    ('dorado', 'dorado'),
                    ('gris', 'gris'),
                    ('morado', 'morado'),
                    ('negro', 'negro'),
                    ('plateado', 'plateado'),
                    ('rojo', 'rojo'),
                    ('rosado', 'rosado'),                    
                    ('verde', 'verde'),
                    ('violeta', 'violeta'),
                                        
                ]
            ),
            'descripcion': forms.TextInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'year': forms.NumberInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            'en_stock': forms.NumberInput(attrs={'class': 'form-control col-md-6 mx-auto'}),
            
        }

    def clean_precio(self):
        # Obtener el valor del campo 'precio' del formulario
        precio = self.cleaned_data.get('precio')
        
        # Validar que el precio sea mayor que cero
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        
        # Retornar el precio limpio (validado)
        return precio
