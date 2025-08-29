import os

INVENTARIO_FILE = "inventario.txt"

def add_producto(producto_id, nombre, precio, stock):
    with open(INVENTARIO_FILE, "a") as f:
        f.write(f"{producto_id},{nombre},{precio},{stock}\n")
    print("✅ Producto agregado correctamente.")

def listar_productos():
    if not os.path.exists(INVENTARIO_FILE):
        print("⚠️ No hay productos registrados.")
        return
    with open(INVENTARIO_FILE, "r") as f:
        for line in f:
            pid, nombre, precio, stock = line.strip().split(",")
            print(f"ID:{pid} | {nombre} | Precio: {precio} | Stock: {stock}")

def buscar_producto(busqueda):
    if not os.path.exists(INVENTARIO_FILE):
        print("⚠️ Inventario vacío.")
        return
    with open(INVENTARIO_FILE, "r") as f:
        for line in f:
            pid, nombre, precio, stock = line.strip().split(",")
            if busqueda == pid or busqueda.lower() in nombre.lower():
                print(f"Encontrado: ID:{pid} | {nombre} | Precio:{precio} | Stock:{stock}")
                return
    print("❌ Producto no encontrado.")

def actualizar_producto(producto_id, nuevo_precio=None, nuevo_stock=None):
    if not os.path.exists(INVENTARIO_FILE):
        print("⚠️ Inventario vacío.")
        return

    actualizado = False
    lineas = []
    with open(INVENTARIO_FILE, "r") as f:
        for line in f:
            pid, nombre, precio, stock = line.strip().split(",")
            if pid == producto_id:
                if nuevo_precio: precio = nuevo_precio
                if nuevo_stock: stock = nuevo_stock
                lineas.append(f"{pid},{nombre},{precio},{stock}\n")
                actualizado = True
            else:
                lineas.append(line)
    with open(INVENTARIO_FILE, "w") as f:
        f.writelines(lineas)
    print("✅ Producto actualizado." if actualizado else "❌ Producto no encontrado.")

def eliminar_producto(producto_id):
    if not os.path.exists(INVENTARIO_FILE):
        print("⚠️ Inventario vacío.")
        return

    eliminado = False
    lineas = []
    with open(INVENTARIO_FILE, "r") as f:
        for line in f:
            pid, nombre, precio, stock = line.strip().split(",")
            if pid != producto_id:
                lineas.append(line)
            else:
                eliminado = True
    with open(INVENTARIO_FILE, "w") as f:
        f.writelines(lineas)
    print("🗑️ Producto eliminado." if eliminado else "❌ Producto no encontrado.")