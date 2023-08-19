#Importamos la librería de Json y leer_escribir_archivos.py
import json
from leer_escribir_archivos import *

#Almecenamos la ruta del archivo JSON (clientes.json) en una variable (CLIENTES_JSON)
CLIENTES_JSON = "clientes.json"

#Creamos una variable para cargar el archivo JSON utilizando la función de lectura/carga "eer_archivo_json"
datos_json = leer_archivo_json(CLIENTES_JSON)
#Declaramos la clase

class cajero_Automatico:
    def __init__(self,datos_json):
             
#Creamos un objeto que permita acceder a cada key y value del diccionario Json de los clientes.
        self.datos= datos_json

       

#/FUNCIÓN CLIENTE EXISTE
    def cliente_existe(self, cedula):
        try:
#Recorremos primero la lista de diccionario de JSON con el objeto creado
            for cuenta in self.datos:
#Si el cliente existe retornará un valor True, en caso contrario será False
                if cuenta["cedula"] == cedula:
                    return True
        except Exception as e:
            
            print(f"Error: {e}")
            return False

#FUNCIÓN VALIDACION CLIENTE        
    def validacion_cliente(self,cedula,contrasena):
        try:
#Recorremos primero la lista de diccionario de JSON con el objeto creado
            for cuenta in self.datos:

#Si el cliente existe retornará un valor True, en caso contrario será False
                if cuenta["cedula"] == cedula and cuenta["contrasena"] == contrasena:
                    print("BIENVENIDO AL CLIENTE ",cuenta["nombre"],cuenta["apellido"])
                    return True    
            return False   
        except Exception as e:
            print(f"Error: {e}")

#FUNCIÓN CREAR CUENTA CLIENTE         
    def crear_cuenta_cliente(self,cedula,nombre,apellido,tipo_de_cuenta, saldo,transacciones,contrasena):
          
        try:
#Iniciamos llamando y ejecutamos la función cliente_existe utilizando el objeto self dentro de una condicional IF.
            if self.cliente_existe(cedula):
                raise ValueError("Error: No se puede agregar el cliente, Ya existe")
            
#Recorremos la lista de diccionario de JSON con el objeto creado            
            for cuenta in self.datos:
                        
#Estructuramos el diccionario nuevo                    
                nueva_cuenta_cliente={            
                "cedula": cedula,
                "nombre": nombre,
                "apellido": apellido,
                "tipo_de_cuenta": tipo_de_cuenta,
                "saldo": saldo,
                "transacciones": transacciones,
                "contrasena": contrasena     
            }
#Lo agregamos a la lista de diccionario de JSON
            self.datos.append(nueva_cuenta_cliente)

#Lo guardamos en el archivo JSON                    
            exportar_archivo_json(CLIENTES_JSON, self.datos)
            return print("Cliente agregado exitosamente.")
        except ValueError as e:
            print(e)

#FUNCIÓN DEPOSITAR
    def depositar(self,cedula,contrasena, saldo_depositar):
        try:
            if self.validacion_cliente(cedula, contrasena):              
                for cuenta in self.datos:                                
                    if saldo_depositar >0  and cuenta["cedula"]==cedula: 
                        saldo_actual = int(cuenta["saldo"])              
                        saldo_actual+= saldo_depositar                   
                        cuenta["saldo"] = str(saldo_actual)              
                        exportar_archivo_json(CLIENTES_JSON, self.datos) 
                        return print("Su deposito fue realizado")            
            else:
                return print("Error: Credenciales inválidas. No se pudo realizar el deposito.") 
            if saldo_depositar <0:
                return print("Error: Solo puedes ingresar saldo positivo. No se pudo realizar el deposito.")    
        except Exception as e:
            
            print(f"Error: {e}")

#FUNCIÓN RETIRAR
    def retirar(self,cedula,contrasena, saldo_retirar):
        try:
            if self.validacion_cliente(cedula, contrasena):
                for cuenta in self.datos:                                
                    if saldo_retirar <0  and cuenta["cedula"]==cedula:
                        saldo_actual = int(cuenta["saldo"])              
                        saldo_actual+= saldo_retirar  
                        cuenta["saldo"] = str(saldo_actual)
                        exportar_archivo_json(CLIENTES_JSON, self.datos) 
                        return print("Su retiro fue realizado")        
            
            else:
                return print("Error: Credenciales inválidas. No se pudo realizar el retiro.") 
            if saldo_retirar >0:
                return print("Error: Solo puedes ingresar saldo negativo. No se pudo realizar el retiro.")

        except Exception as e:
            
            print(f"Error: {e}")
            
if datos_json is not None: 
#Almacenamos la información en un objeto de clase llamado cajero y utilizaremos datos_json que vendría siendo donde se encuentra almacenado el diccionario recién creado en cuestión.             
    cajero = cajero_Automatico(datos_json)  
    
#Llamada función crear_cuenta_cliente
#print(cajero.crear_cuenta_cliente("3","Jose", "Alvarez", "Ahorro", "50", "10", "1234"))

 #Llamada función depositar
#print(cajero.depositar("3","1234",1))

#Llamada función retirar
print(cajero.retirar("3","1234", 1))