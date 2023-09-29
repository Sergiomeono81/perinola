# Importa las bibliotecas necesarias
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# ... [Tus definiciones de función permanecen sin cambios]

def main():
    st.title("Simulación Montecarlo de Perinola")
    
    # Configura los widgets para la interactividad
    n_jugadores = st.slider("Número de jugadores", 2, 10, 3)
    m_juegos = st.slider("Número de juegos", 10, 100, 50)
    dinero_inicial = st.slider("Dinero inicial", 5, 20, 10)
    
    # Grafica la simulación
    jugadores, pozos, juegos_para_bancarrota = simulacion_montecarlo(n_jugadores, m_juegos, dinero_inicial)
    fig, ax = plt.subplots(figsize=(12, 8))
    
    for i, dinero in enumerate(jugadores):
        ax.plot(range(m_juegos), [dinero_inicial] * m_juegos, label=f'Jugador {i + 1}')
    ax.plot(range(m_juegos), pozos, label='Pozo', linestyle='--')
    ax.axvline(juegos_para_bancarrota, color='red', linestyle='--', label='Jugador en bancarrota')
    ax.set_xlabel('Juegos')
    ax.set_ylabel('Dinero')
    ax.set_title('Ganancia y Pérdida por Jugador en cada Juego')
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)
    
    # Responde a las preguntas
    st.subheader("Análisis:")
    
    # 1. ¿Cuántos juegos son necesarios para que un jugador se quede sin dinero?
    st.write(f"Se necesitan {juegos_bancarrota} juegos para que un jugador se quede sin dinero.")

    # 2. ¿En cuántos juegos en promedio hay un ganador?
    juegos_ganador = juegos_promedio_ganador(n_jugadores, m_juegos, dinero_inicial)
    st.write(f"En promedio, hay un ganador en {juegos_ganador} juegos.")

    # 3. ¿Cómo afecta el número de jugadores al número de juegos para que un jugador se gane todo el dinero?
    juegos_promedio = juegos_promedio_bancarrota_vs_jugadores(10, m_juegos, dinero_inicial)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(range(2, 11), juegos_promedio)
    ax.set_xlabel('Número de Jugadores')
    ax.set_ylabel('Juegos Promedio hasta Bancarrota')
    ax.set_title('Juegos Promedio hasta Bancarrota vs. Número de Jugadores')
    ax.grid(True)
    
    st.pyplot(fig)

if __name__ == "__main__":
    main()
