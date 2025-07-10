# Verificador de rango de VLAN

def verificar_rango_vlan():
    """
    Script que solicita al usuario un número de VLAN y determina si pertenece al:
    - Rango normal (1-1005)
    - Rango extendido (1006-4094)
    - VLAN nativa (0)
    - VLAN especial (4095)
    """
    print("Verificador de rango de VLAN")
    print("----------------------------")
    
    try:
        # Solicitar al usuario el número de VLAN
        vlan = int(input("Ingrese el número de VLAN: "))
        
        # Verificar el rango de la VLAN
        if 1 <= vlan <= 1001:
            print(f"La VLAN {vlan} pertenece al rango NORMAL (1-1001).")
        elif 1002 <= vlan <= 4094:
            print(f"La VLAN {vlan} pertenece al rango EXTENDIDO (1002-4094).")
        elif vlan == 0:
            print("La VLAN 0 es una VLAN especial (VLAN nativa).")
        elif vlan == 4095:
            print("4095 es reservado y no puede ser usado como VLAN ID.")
        else:
            print(f"El número {vlan} no es un VLAN ID válido (rango válido: 1-4094).")
            
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    verificar_rango_vlan()