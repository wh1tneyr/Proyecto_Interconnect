import pandas as pd
import os, sys
sys.path.append(os.getcwd())

from funciones.funcion import read_csv


#leer los datasets ----------------------------------------------
user_contract = read_csv('/Users/whitneyrios/PYTHON/My projects py/Proyecto Final 17 Telecom/Proyecto_Final_Telecom/files/datasets/final_provider/contract.csv')
user_personal_info = read_csv('/Users/whitneyrios/PYTHON/My projects py/Proyecto Final 17 Telecom/Proyecto_Final_Telecom/files/datasets/final_provider/personal.csv')
phone_ser = read_csv('/Users/whitneyrios/PYTHON/My projects py/Proyecto Final 17 Telecom/Proyecto_Final_Telecom/files/datasets/final_provider/phone.csv')
internet_ser = read_csv('/Users/whitneyrios/PYTHON/My projects py/Proyecto Final 17 Telecom/Proyecto_Final_Telecom/files/datasets/final_provider/internet.csv')

#visualizar datos (contratos) ------------------------------------------------
user_contract.head(20)
user_contract.info()

#ver valores ausentes y duplicados
user_contract.isna().sum()
user_contract.duplicated().sum()
user_contract['customerID'].duplicated().sum()
#no hay ausentes ni duplicados 

# TODO : convertir 'BeginDate' a formato fecha
# TODO: convetir 'TotalCharges' a formato float

user_contract['BeginDate'] = pd.to_datetime(user_contract['BeginDate'], format='%Y-%m-%d')
