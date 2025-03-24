import matplotlib.pyplot as mpl

def collatz_sequence_length(n):
    """Devuelve la cantidad de iteraciones necesarias para que n llegue a 1 siguiendo la conjetura de Collatz."""
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Calcula la cantidad de iteraciones para cada número
numbers = list(range(1, 10001))
iterations = [collatz_sequence_length(n) for n in numbers]

# Grafica resultados
mpl.figure(figsize=(10, 6))
mpl.scatter(iterations, numbers, s=1, color="blue")  
mpl.xlabel("Número de iteraciones hasta converger")
mpl.ylabel("Número inicial n")
mpl.title("Conjetura de Collatz para números entre 1 y 10,000")
mpl.grid(True)

# Guarda en la carpeta "src"
mpl.savefig("src/collatz_plot.png")

# Muestra el gráfico
mpl.show()
