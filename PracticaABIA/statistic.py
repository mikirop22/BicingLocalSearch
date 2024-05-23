"""import statistics
import numpy as np

# Datos
tiempos = [57, 64, 65, 71, 76]

# Calcular la media
media = statistics.mean(tiempos)

# Calcular la desviación estándar
desviacion_estandar = np.std(tiempos)

# Mostrar resultados
print(f"Media: {media:.2f} segundos")
print(f"Desviación estándar: {desviacion_estandar:.2f} segundos")"""

#------------------------------------------------------------------------------

"""import networkx as nx
import matplotlib.pyplot as plt

# Lista de predicados
predicados = ["paralelos l2 l1", "paralelos l3 l2", "paralelos l4 l3", "paralelos l3 l6", "paralelos l8 l9"]

# Crear un grafo dirigido
G = nx.DiGraph()

# Procesar los predicados y construir el grafo
for predicado in predicados:
    _, linea1, linea2 = predicado.split()
    G.add_edge(linea2, linea1)  # Agregar arista dirigida de linea2 a linea1

# Visualizar el grafo
pos = nx.spring_layout(G)  # Elegir el diseño del grafo
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', arrowsize=20)
plt.title("Grafo de relaciones paralelas")
plt.show()
"""
import random
libros_catalogo = ['libro1', 'libro2', 'libro3', 'libro4', 'libro5', 'libro6', 'libro7', 'libro8']


libros_quiere_leer = ['libro1']
paralels = [('libro3', 'libro2'), ('libro4', 'libro3'), ('libro3', 'libro6'), ('libro2', 'libro1')]

primeros = []
restantes = []

for libros in paralels:
    if libros[0] in libros_quiere_leer or libros[1] in libros_quiere_leer:
        primeros.append(libros)
    else:
        restantes.append(libros)

# Concatenar las listas de primeros y restantes
paralels_ordenados = primeros + restantes

predecessors = [('libro1', 'libro2'), ('libro2', 'libro3')]

visited = set()
def cadena_predecessor(librox):
    for predecesor in predecessors:
        if predecesor in visited:
            continue
        
        if librox == predecesor[0]:
            visited.add(predecesor)
            if predecesor[1] in libros_quiere_leer:
                return True
            else:
                return cadena_predecessor(predecesor[1])
        
        visited.add(predecesor) 

for i, libros in enumerate(paralels_ordenados):
    if (libros[1] in libros_quiere_leer or cadena_predecessor(libros[1])) and libros[0] not in libros_quiere_leer:
        libros_quiere_leer.append(libros[0])
    elif (libros[1] in libros_quiere_leer or cadena_predecessor(libros[1])) and libros[0] in libros_quiere_leer:
        continue
    elif libros[0] in libros_quiere_leer:
        paralels_ordenados[i] = (libros[1], libros[0])  


visited = set()
def trobar_predecessor(librox, libroy):

    for predecesor in predecessors:
        if predecesor in visited:
            continue

        if (librox == predecesor[1] and libroy == predecesor[0]) or (librox == predecesor[0] and libroy == predecesor[1]):
            return True
        
        elif librox == predecesor[0]:
            visited.add(predecesor)
            return trobar_predecessor(predecesor[1], libroy)
            
        elif librox == predecesor[1]:
            visited.add(predecesor)
            return trobar_predecessor(predecesor[0], libroy)
                
    return False



if trobar_predecessor('libro1', 'libro3'):
    print('va be, no es produex paralelos')
else:
    print('va malament')