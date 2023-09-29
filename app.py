
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def lanzar_perinola():
    return np.random.choice(['Pon 1', 'Pon 2', 'Toma 1', 'Toma 2', 'Toma todo', 'Todos ponen'])

def jugar_turno(billeteras):
    resultado = lanzar_perinola()
    total_jugadores = len(billeteras)
    if resultado == 'Pon 1':
        billeteras = np.maximum(billeteras - 1, 0)
    elif resultado == 'Pon 2':
        billeteras = np.maximum(billeteras - 2, 0)
    elif resultado == 'Toma 1':
        jugador = np.random.choice(total_jugadores)
        billeteras[jugador] += 1
    elif resultado == 'Toma 2':
        jugador = np.random.choice(total_jugadores)
        billeteras[jugador] += 2
    elif resultado == 'Toma todo':
        jugador = np.random.choice(total_jugadores)
        billeteras[jugador] += np.sum(billeteras)
        billeteras = np.zeros(total_jugadores, dtype=int)
        billeteras[jugador] = np.sum(billeteras)
    elif resultado == 'Todos ponen':
        billeteras = np.maximum(billeteras - 1, 0)
        pot = total_jugadores - np.count_nonzero(billeteras == 0)
        jugador = np.random.choice(total_jugadores)
        billeteras[jugador] += pot
    return billeteras

def analizar_simulacion(N, M, dinero_inicial):
    juegos_hasta_ganador = []
    for _ in range(M):
        billeteras = np.ones(N) * dinero_inicial
        juegos = 0
        while np.max(billeteras) < N * dinero_inicial:
            billeteras = jugar_turno(billeteras)
            juegos += 1
        juegos_hasta_ganador.append(juegos)
    promedio_juegos_hasta_ganador = np.mean(juegos_hasta_ganador)
    return promedio_juegos_hasta_ganador, billeteras

def main():
    st.title("Simulación de Perinola")
    
    N = st.slider("Número de Jugadores", 2, 10, 4)
    M = st.slider("Número de Juegos", 1, 500, 10)
    dinero_inicial = st.slider("Dinero inicial por jugador", 1, 100, 10)

    if st.button("Iniciar Simulación"):
        promedio_ganador, billeteras_finales = analizar_simulacion(N, M, dinero_inicial)
        st.write(f"Promedio de juegos hasta que hay un ganador con {N} jugadores: {promedio_ganador}")

        fig = plt.figure(figsize=(10,6))
        plt.bar(range(1, N+1), billeteras_finales)
        plt.xlabel('Jugador')
        plt.ylabel('Dinero final')
        plt.title('Ganancia y Pérdida por Jugador al final de la Simulación')
        plt.xticks(range(1, N+1))
        plt.grid(True)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
