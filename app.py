import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# [No hay cambios en las funciones perinola, simulacion_montecarlo, tiene_ganador, juegos_promedio_ganador, juegos_promedio_bancarrota_vs_jugadores]

def main():
    st.title("Simulación de Perinola con Montecarlo")

    n_jugadores = st.slider("Número de jugadores", 2, 10, 3)
    m_juegos = st.slider("Número de juegos", 10, 100, 50)
    dinero_inicial = st.slider("Dinero inicial", 5, 20, 10)

    if st.button("Graficar"):
        graficar(n_jugadores, m_juegos, dinero_inicial)
        
        _, _, juegos_bancarrota = simulacion_montecarlo(n_jugadores, m_juegos, dinero_inicial)
        st.write(f"Se necesitan {juegos_bancarrota} juegos para que un jugador se quede sin dinero.")

        juegos_ganador = juegos_promedio_ganador(n_jugadores, m_juegos, dinero_inicial)
        st.write(f"En promedio, hay un ganador en {juegos_ganador} juegos.")

        juegos_promedio = juegos_promedio_bancarrota_vs_jugadores(10, m_juegos, dinero_inicial)
        plt.figure(figsize=(12, 8))
        plt.plot(range(2, 11), juegos_promedio)
        plt.xlabel('Número de Jugadores')
        plt.ylabel('Juegos Promedio hasta Bancarrota')
        plt.title('Juegos Promedio hasta Bancarrota vs. Número de Jugadores')
        plt.grid(True)
        st.pyplot()


def graficar(n_jugadores, m_juegos, dinero_inicial):
    jugadores, pozos, juegos_para_bancarrota = simulacion_montecarlo(n_jugadores, m_juegos, dinero_inicial)
    plt.figure(figsize=(12, 8))

    for i, dinero in enumerate(jugadores):
        plt.plot(range(m_juegos), [dinero_inicial] * m_juegos, label=f'Jugador {i + 1}')

    plt.plot(range(m_juegos), pozos, label='Pozo', linestyle='--')

    plt.axvline(juegos_para_bancarrota, color='red', linestyle='--', label='Jugador en bancarrota')
    plt.xlabel('Juegos')
    plt.ylabel('Dinero')
    plt.title('Ganancia y Pérdida por Jugador en cada Juego')
    plt.legend()
    plt.grid(True)
    st.pyplot()


if __name__ == "__main__":
    main()

  
