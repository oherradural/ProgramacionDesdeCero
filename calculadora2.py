# -*- coding: utf-8 -*-
# calculadora en python mas avanzada


operadores = ("+", "-", "*", "**", "/")


def valida_operador(operadores):
    operacion = input("Ingresa la operacion a realizar: ")

    for operador in operadores:
        if operador == operacion:
            return True

def realizar_operacion():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")

    resultado = float(num1) *  float(num2)

    print(f"El resultado de la operacion es {resultado}")

    ##################################################################################################

ver = valida_operador(operadores)

if ver:
    print("Operacion permitida")
    realizar_operacion()

else:
    print("Error!!! Operacion no permitida")
