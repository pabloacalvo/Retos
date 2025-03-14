import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo dirigido para el DFM
G = nx.DiGraph()

# Agregar nodos de la tabla de hechos y las dimensiones
G.add_node("Inventario_Almacen", color='lightblue')
G.add_node("Almacen", color='lightgreen')
G.add_node("Articulo", color='lightgreen')
G.add_node("Material", color='lightgreen')
G.add_node("Proveedor", color='lightgreen')
G.add_node("Tiempo", color='lightgreen')

# Agregar conexiones (relaciones)
G.add_edges_from([
    ("Inventario_Almacen", "Almacen"),
    ("Inventario_Almacen", "Articulo"),
    ("Inventario_Almacen", "Tiempo"),
    ("Articulo", "Material"),
    ("Material", "Proveedor")
])

# Dibujar el grafo
pos = nx.spring_layout(G)  # Posición de los nodos
colors = [G.nodes[node]['color'] for node in G.nodes]
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Diagrama DFM: Inventario y Análisis de Almacenes")
plt.show()
