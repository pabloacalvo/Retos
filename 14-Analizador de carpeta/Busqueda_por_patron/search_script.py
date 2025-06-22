from pathlib import Path
import shutil
import json
import pandas as pd



search_root = Path('C:/procesarRtlog/Xcash reprocesos/')
main_root = Path(__file__).parent

def clshift_filter(search_root):
    store_list = []
    try:
        for file in search_root.rglob('*ClShift*'):
            with open(file,'r') as close_file:
                data = json.load(close_file)
                # Obtenemos los shiftPayment del shiftPayments, sino hay info se genera un dict vacio y lista vacia
                shift_payment_list = data.get('shiftPayments', {}).get('shiftPayment', [])
                cashier_data = data.get('cashier',{})
                movement_data = data.get('movement',{})
                store = movement_data['storeCode']
                cashier = cashier_data['code']
                date = data.get('dateHour')
                codes = [item.get('code') for item in shift_payment_list if isinstance(item, dict)] # Valida que sea dict para evitar fallos
                # Validamos la existencia de t.online y qri
                if 10 in codes and 18 in codes:
                    print(f"{date} Tienda:{store} Cajero:{cashier}: {file.name}")
                    move_to = main_root / Path('result') / file.name
                    shutil.copy2(file, move_to)
                    store_list.append(store)
                return store_list
    except Exception as e:
        print(e)


def files_filter(search_root, cashier_number):
    try:
        for file in search_root.glob("*"):
            if not file.is_file():
                continue
            with open(file,"r") as f:
                data = json.load(f)
                cashier_data = data.get('cashier',{})
                cashier = cashier_data.get("code") if isinstance(cashier_data, dict) else None
                if cashier_number == cashier:
                    move_to = main_root / Path('result') / file.name
                    shutil.copy2(file, move_to)
                    print(f'Archivo {file.name}, corresponde a cashier: {cashier}')
                
    except Exception as e:
        print(e)

def clshift_calculate_amount(search_root):
    data_list = []
    try:
        for file in search_root.rglob('*ClShift*'):
            with open(file,'r') as close_file:
                data = json.load(close_file)
                # Obtenemos los shiftPayment del shiftPayments, sino hay info se genera un dict vacio y lista vacia
                shift_payment_list = data.get('shiftPayments', {}).get('shiftPayment', [])
                cashier_data = data.get('cashier',{})
                movement_data = data.get('movement',{})
                store = movement_data['storeCode']
                cashier = cashier_data['code']
                date = data.get('dateHour')
                shift_number_data = data.get('shiftNumber')
                process_data = {item.get('code'):item.get('totalAmount') for item in shift_payment_list if isinstance(item, dict)} # Valida que sea dict para evitar fallos
                process_data['Turno'] = shift_number_data
                process_data['cashier'] = cashier
                process_data['Archivo'] = file.name
                data_list.append(process_data)
        df_clshift = pd.DataFrame(data_list)
        print(df_clshift.dropna())
    except Exception as e:
        print(e)

#files_filter(search_root,30)
clshift_calculate_amount(search_root)