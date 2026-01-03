import os
import random
import json

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "l", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "L", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "#", "$", "%", "&", "?", "+", "*", "^", "-", "_", "~"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def clear_console():
    op_system = os.name
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def get_letter():
    number = random.randint(0, 51)
    selection = letters[number]
    return selection
def get_number():
    number = random.randint(0, 9)
    selection = numbers[number]
    return selection
def get_symbol():
    number = random.randint(0, 11)
    selection = symbols[number]
    return selection

def generate_password(chars, syms, nums):
    num_letters = chars - (syms + nums)
    pswd_list = []
    for i in range(num_letters):
        pswd_list.append(get_letter())
    for i in range(syms):
        pswd_list.append(get_symbol())
    for i in range(nums):
        pswd_list.append(get_number())
    random.shuffle(pswd_list)
    password = "".join(pswd_list)
    return password

def menu_guardar(password=""):
    clear_console()
    print("=== GUARDAR CONTRASEÑA ===\n")
    sitio = input("Sitio: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    if not (password):
        password = input("Contraseña: ")
    guardar_contraseña(sitio, password, nombre, correo)
    print("\nDatos guardados correctamente.")

def guardar_contraseña(sitio, contraseña, nombre=None, correo=None):
    element = {
        "Sitio": sitio,
        "Nombre": nombre,
        "Correo": correo,
        "Password": contraseña
    }
    with open("data.json", "r") as json_file:
        datos = json.load(json_file)
    datos.append(element)
    
    with open("data.json", "w") as json_file:
        json.dump(datos, json_file, indent=4)

def menu_ver():
    clear_console()
    print("=== CONTRASEÑAS GUARDADAS ===\n")
    with open("data.json", "r") as json_file:
        datos = json.load(json_file)

    for dato in datos:
        print(f"Sitio: {dato["Sitio"]}")
        print(f"Nombre: {dato["Nombre"]}")
        print(f"Correo: {dato["Correo"]}")
        print(f"Contraseña: {dato["Password"]}\n")

    input("\nPresiona ENTER para volver.")