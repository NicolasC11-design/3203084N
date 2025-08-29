import os
from Inventario import buscar_producto

FACTURAS_FILE = "facturas.txt"
IVA = 0.19

def crear_factura(factura_id, items):
    """
    items = [(producto_id, cantidad, precio_unitario), ...]
    """
    subtotal = sum(cant * precio for _, cant, precio in items)
    iva = subtotal * IVA
    total = subtotal + iva

    with open(FACTURAS_FILE, "a") as f:
        f.write(f"FACTURA:{factura_id}\n")
        for pid, cant, precio in items:
            f.write(f"{pid},{cant},{precio},{cant*precio}\n")
        f.write(f"SUBTOTAL:{subtotal}\nIVA:{iva}\nTOTAL:{total}\n---\n")
    print(f"✅ Factura {factura_id} creada con éxito.")

def listar_facturas():
    if not os.path.exists(FACTURAS_FILE):
        print("⚠️ No hay facturas registradas.")
        return
    with open(FACTURAS_FILE, "r") as f:
        print(f.read())

def eliminar_factura(factura_id):
    if not os.path.exists(FACTURAS_FILE):
        print("⚠️ No hay facturas.")
        return

    lineas = []
    guardar = True
    eliminada = False

    with open(FACTURAS_FILE, "r") as f:
        for line in f:
            if line.startswith(f"FACTURA:{factura_id}"):
                guardar = False
                eliminada = True
            elif line.strip() == "---":
                guardar = True
            elif guardar:
                lineas.append(line)

    with open(FACTURAS_FILE, "w") as f:
        f.writelines(lineas)

    print("🗑️ Factura eliminada." if eliminada else "❌ Factura no encontrada.")