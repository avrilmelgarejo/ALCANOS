import streamlit as st
from sympy import symbols, Eq, solve

# Función para balancear la ecuación de combustión
def balance_combusion(compuesto, tipo):
    # Variables simbólicas para la reacción balanceada
    C, H, O = symbols('C H O')
    
    if tipo == "alcano":
        # Fórmula general para un alcano: CnH2n+2
        n = int(compuesto[0])  # número de átomos de carbono
        # Reacción: CnH2n+2 + O2 -> CO2 + H2O
        # Balance de átomos de carbono
        c_eq = Eq(n, C)
        # Balance de átomos de hidrógeno
        h_eq = Eq(2 * n + 2, 2 * H)
        # Balance de átomos de oxígeno (deberán ser los productos CO2 y H2O)
        o_eq = Eq(n + n + 1, 2 * O)
        
    elif tipo == "alqueno":
        # Fórmula general para un alqueno: CnH2n
        n = int(compuesto[0])  # número de átomos de carbono
        # Reacción: CnH2n + O2 -> CO2 + H2O
        # Balance de átomos de carbono
        c_eq = Eq(n, C)
        # Balance de átomos de hidrógeno
        h_eq = Eq(2 * n, 2 * H)
        # Balance de átomos de oxígeno
        o_eq = Eq(n + n, 2 * O)
        
    elif tipo == "alquino":
        # Fórmula general para un alquino: CnH2n-2
        n = int(compuesto[0])  # número de átomos de carbono
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

# Interfaz de Streamlit
def main():
    st.title('Balanceador de Combustión')
    st.write("Este es un balanceador de reacciones de combustión para alcanos, alquenos y alquinos.")
    
    # Selección de tipo de compuesto
    tipo = st.selectbox("Selecciona el tipo de compuesto:", ["alcano", "alqueno", "alquino"])
    
    # Ingreso de fórmula
    compuesto = st.text_input(f"Ingrese la fórmula del {tipo} (Ej. CnH2n+2):", "C2H6")  # ejemplo de alcano

    # Realizar el balance
    if st.button('Balancear'):
        soluciones = balance_combusion(compuesto, tipo)
        st.write(f"La reacción balanceada es: {soluciones[C]}C + {soluciones[H]}H2 + {soluciones[O]}O2 -> {soluciones[C]}CO2 + {soluciones[H]}H2O")

if __name__ == "__main__":
    main()
