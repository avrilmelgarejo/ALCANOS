import streamlit as st
from sympy import symbols, Eq, solve

# Función para balancear la ecuación de combustión
def balance_combustion(compuesto, tipo):
    # Variables simbólicas para la reacción balanceada
    C, H, O = symbols('C H O')
    
    # Balance de acuerdo al tipo de compuesto
    if tipo == "alcano":
        # Fórmula general para un alcano: CnH2n+2
        n = int(compuesto[1])  # Número de átomos de carbono
        # Reacción: CnH2n+2 + O2 -> CO2 + H2O
        # Balance de átomos de carbono
        c_eq = Eq(n, C)
        # Balance de átomos de hidrógeno
        h_eq = Eq(2 * n + 2, 2 * H)
        # Balance de átomos de oxígeno (deberán ser los productos CO2 y H2O)
        o_eq = Eq(n + n + 1, 2 * O)
        
    elif tipo == "alqueno":
        # Fórmula general para un alqueno: CnH2n
        n = int(compuesto[1])  # Número de átomos de carbono
        # Reacción: CnH2n + O2 -> CO2 + H2O
        # Balance de átomos de carbono
        c_eq = Eq(n, C)
        # Balance de átomos de hidrógeno
        h_eq = Eq(2 * n, 2 * H)
        # Balance de átomos de oxígeno
        o_eq = Eq(n + n, 2 * O)
        
    elif tipo == "alquino":
        # Fórmula general para un alquino: CnH2n-2
        n = int(compuesto[1])  # Número de átomos de carbono
        # Reacción: CnH2n-2 + O2 -> CO2 + H2O
        # Balance de átomos de carbono
        c_eq = Eq(n, C)
        # Balance de átomos de hidrógeno
        h_eq = Eq(2 * n - 2, 2 * H)
        # Balance de átomos de oxígeno
        o_eq = Eq(n + n, 2 * O)
    
    # Resolver las ecuaciones
    soluciones = solve((c_eq, h_eq, o_eq), (C, H, O))
    return soluciones

# Interfaz de usuario en Streamlit
def main():
    st.title('Balanceador de Reacciones de Combustión')
    st.write("""
    Este es un balanceador de reacciones de combustión para **alcanos**, **alquenos** y **alquinos**.
    Introduce la fórmula del compuesto para balancear su reacción de combustión.
    """)

    # Opciones de tipos de compuestos
    tipo = st.selectbox("Selecciona el tipo de compuesto:", ["alcano", "alqueno", "alquino"])
    
    # Ingreso de la fórmula del compuesto
    compuesto = st.text_input(f"Ingrese la fórmula del {tipo} (Ej. C2H6 para alcano, C2H4 para alqueno):", "C2H6")

    if compuesto:
        try:
            # Realizar el balance
            soluciones = balance_combustion(compuesto, tipo)
            
            # Mostrar los resultados
            st.subheader("Reacción balanceada:")
            st.write(f"{soluciones[0]} C + {soluciones[1]} H2 + {soluciones[2]} O2 → {soluciones[0]} CO2 + {soluciones[1]} H2O")
        except Exception as e:
            st.error(f"Hubo un error al balancear la fórmula. Verifica el formato de la fórmula y prueba de nuevo. Error: {str(e)}")

if __name__ == "__main__":
    main()
