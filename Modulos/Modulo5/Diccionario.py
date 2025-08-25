prom = 0
Dic1 = {"Nombre": "Ivan", "Apellido": "Malaver", "Edad": 47, "Nota": (4.5, 3.8, 4.0, 4.6, 4.9) }
Dic2 = {"Nombre": "Nicolas", "Apellido": "Cristiano", "Edad": 17,"Nota":( 4.0, 4.1, 4.3, 4.5, 4.7) }
Dic3 = {"Nombre": "Luis", "Apellido": "Gómez", "Edad": 20, "Nota": (3.5, 4.0, 4.1, 4.3, 4.4) } 
Dic4 = {"Nombre": "Andrés", "Apellido": "Pérez", "Edad": 22, "Nota":( 4.8, 4.9, 4.6, 4.7, 4.5) }
Dic5 = {"Nombre": "Camila", "Apellido": "Ortiz", "Edad": 19, "Nota": (4.2, 4.3, 4.1, 4.0, 4.4) }


Prom1 = (Dic1["Nota"][0] + Dic1["Nota"][1]  + Dic1["Nota"][2]  + Dic1["Nota"][3]  + Dic1["Nota"][4] ) / 5
Prom2 = (Dic2["Nota"][0] + Dic2["Nota"][1]  + Dic2["Nota"][2]  + Dic2["Nota"][3]  + Dic2["Nota"][4] ) / 5
Prom3 = (Dic3["Nota"][0] + Dic3["Nota"][1]  + Dic3["Nota"][2]  + Dic3["Nota"][3]  + Dic3["Nota"][4] ) / 5
Prom4 = (Dic4["Nota"][0] + Dic4["Nota"][1]  + Dic4["Nota"][2]  + Dic4["Nota"][3]  + Dic4["Nota"][4] ) / 5
Prom5 = (Dic5["Nota"][0] + Dic5["Nota"][1]  + Dic5["Nota"][2]  + Dic4["Nota"][3]  + Dic5["Nota"][4] ) / 5

print("Diccionario 1:", Prom1)
print("Diccionario 2:", Prom2)   
print("Diccionario 3:", Prom3)
print("Diccionario 4:", Prom4)   
print("Diccionario 5:", Prom5)
