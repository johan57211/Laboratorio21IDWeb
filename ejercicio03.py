class OperadorInvalidoError(Exception):
    pass


def calcular(operacion):
    try:
        partes = operacion.split()

        if len(partes) != 3:
            raise ValueError("La operación debe tener el formato: numero operador numero")

        num1_str, operador, num2_str = partes

        num1 = float(num1_str)
        num2 = float(num2_str)

        if operador not in ["+", "-", "*", "/"]:
            raise OperadorInvalidoError(f"Operador inválido: {operador}")

        if operador == "+":
            return num1 + num2
        elif operador == "-":
            return num1 - num2
        elif operador == "*":
            return num1 * num2
        elif operador == "/":
            if num2 == 0:
                raise ZeroDivisionError
            return num1 / num2

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError as e:
        print(f"Error de valor: {e}")
    except OperadorInvalidoError as e:
        print(f"Error de operador: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

operacion = input("Ingresa la operación (ej: 10 / 2): ")
resultado = calcular(operacion)

if resultado is not None:
    print("Resultado:", resultado)
