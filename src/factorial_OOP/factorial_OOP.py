import sys

class Factorial:
    def __init__(self):
        pass
    
    def calcular(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact
    
    def run(self, min_val, max_val):
        if min_val > max_val:
            print("El límite inferior no puede ser mayor que el superior")
            return
        
        for i in range(min_val, max_val + 1):
            print(f"Factorial {i}! es {self.calcular(i)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        entrada = input("Ingrese un número o un rango (ejemplo: 5, 4-8, -10, 5-): ")
    else:
        entrada = sys.argv[1]
    
    if "-" in entrada:
        partes = entrada.split("-")
        if partes[0] == "":  # Caso '-10' -> de 1 a 10
            min_val, max_val = 1, int(partes[1])
        elif partes[1] == "":  # Caso '5-' -> de 5 a 60
            min_val, max_val = int(partes[0]), 60
        else:  # Caso '4-8'
            min_val, max_val = int(partes[0]), int(partes[1])
    else:
        min_val = max_val = int(entrada)
    
    factorial = Factorial()
    factorial.run(min_val, max_val)
