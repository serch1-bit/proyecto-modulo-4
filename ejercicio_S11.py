# main.py

from m_retosemanal import crear_varias_listas, eliminar_valores_repetidos

# Crear las listas
listas = crear_varias_listas()

# Mostrar listas originales
print("\nListas originales:")
for idx, lista in enumerate(listas, start=1):
    print(f"Lista {idx}: {lista}")


print("\n=============================\n")

# Eliminar elementos repetidos
listas_modificadas = eliminar_valores_repetidos(listas)

# Mostrar listas modificadas
print("\nListas despues de eliminar elementos repetidos en listas posteriores:")
for idx, lista in enumerate(listas_modificadas, start=1):
    print(f"Lista {idx}: {lista}")