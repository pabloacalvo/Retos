from Conversor import Conversor
import requests

API_KEY = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Nzk1MDc3NjksInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJwYWJsb2FjYWx2b0BsaXZlLmNvbSJ9.2DKm9OUcOTm4iiIyhv_VfwBXieNQzIonffC9IAGi5V632Ftn17PBodb-HG_PktdSjl9SJytYjiEIHG3LjqBjFg"

class ConversorDolares(Conversor):
    
    def __init__(self):
        self.cotizacion = self.get_cotizacion()

    def convert_valor1_a_valor2(self, valor_1):
        return valor_1 * self.cotizacion
    
    def convert_valor2_a_valor1(self, valor_2):
        return valor_2 / self.cotizacion
    
    def get_tipo(self):
        return "Dolares"

    def get_cotizacion(self):
        headers ={
            'Authorization':f'BEARER {API_KEY}',
        }
        url = 'https://api.estadisticasbcra.com/usd_of'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            value = float(data[-1]['v'])
            return value
        
        raise Exception(f"Error en la consulta a la API: {response.status_code}")