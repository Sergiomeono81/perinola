# Importa las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Definiendo la función que simula la perinola
def perinola():
    opciones = ['Pon 1', 'Pon 2', 'Toma 1', 'Toma 2', 'Toma todo', 'Todos ponen']
    return np.random.choice(opciones)

# Definiendo la función que realiza la simulación Montecarlo
def simulacion_montecarlo(n_jugadores, m_juegos, dinero_inicial):
    jugadores = np.full(n_jugadores, dinero_inicial)
    pozos = []
    juegos_para_bancarrota = 0
    
    for juego in range(m_juegos):
        pozo = 0
        jugada = perinola()
        if jugada == 'Pon 1':
            jugadores = np.maximum(0, jugadores - 1)
            pozo += n_jugadores
        elif jugada == 'Pon 2':
            jugadores = np.maximum(0, jugadores - 2)
            pozo += 2 * n_jugadores
        elif jugada == 'Toma 1':
            jugador_elegido = np.random.randint(n_jugadores)
            jugadores[jugador_elegido] += 1
            pozo -= 1
        elif jugada == 'Toma 2':
            jugador_elegido = np.random.randint(n_jugadores)
            jugadores[jugador_elegido] += 2
            pozo -= 2
        elif jugada == 'Toma todo':
            jugador_elegido = np.random.randint(n_jugadores)
            jugadores[jugador_elegido] += pozo
            pozo = 0
        elif jugada == 'Todos ponen':
            jugadores = np.maximum(0, jugadores - 1)
            pozo += n_jugadores
            
        pozos.append(pozo)
        if juegos_para_bancarrota == 0 and np.min(jugadores) == 0:
            juegos_para_bancarrota = juego + 1
            
    return jugadores, pozos, juegos_para_bancarrota

def main():
    # Configura los widgets para la interactividad
    n_jugadores = st.slider("Número de jugadores", 2, 10, 3)
    m_juegos = st.slider("Número de juegos", 10, 100, 50)
    dinero_inicial = st.slider("Dinero inicial", 5, 20, 10)
    
    # Grafica la simulación
    jugadores, pozos, juegos_para_bancarrota = simulacion_montecarlo(n_jugadores, m_juegos, dinero_inicial)
    plt.figure(figsize=(12, 8))
    
    for i, dinero in enumerate(jugadores):
        plt.plot(np.full(m_juegos, dinero), label=f'Jugador {i + 1}')
        
    plt.plot(pozos, label='Pozo', linestyle='--')
    
    plt.axvline(juegos_para_bancarrota, color='red', linestyle='--', label='Jugador en bancarrota')
    plt.xlabel('Juegos')
    plt.ylabel('Dinero')
    plt.title('Ganancia y Pérdida por Jugador en cada Juego')
    plt.legend()
    plt.grid(True)
    
    st.pyplot(plt)

# Ejecutar la función main() si se ejecuta el script
if __name__ == "__main__":
    main()
