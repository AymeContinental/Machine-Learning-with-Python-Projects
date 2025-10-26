import random

def player(prev_play, opponent_history=[], play_order={}):
    """
    Esta función usa un modelo de cadena de Markov simple para predecir
    la siguiente jugada del oponente basándose en sus 4 jugadas anteriores.
    """
    
    # Paso 1: Reiniciar el historial y el 'playbook' si es un nuevo oponente
    if not prev_play:
        prev_play = 'R' # Jugada inicial por defecto
        opponent_history.clear()
        play_order.clear()

    # Añadir la última jugada del oponente al historial
    opponent_history.append(prev_play)

    # Paso 2: Usar los últimos 4 movimientos como "clave" de predicción
    # Necesitamos al menos 5 movimientos para tener 4 anteriores y 1 actual
    
    prediction = "P" # Predicción por defecto

    if len(opponent_history) > 4:
        # 2a. Crear la clave del 'playbook' (los 4 movimientos anteriores)
        last_four_moves = "".join(opponent_history[-5:-1]) # Clave
        
        # 2b. Registrar el movimiento que siguió a esa clave
        current_move = opponent_history[-1] # Valor
        
        # 2c. Actualizar el 'playbook' (play_order)
        if last_four_moves not in play_order:
            play_order[last_four_moves] = {"R": 0, "P": 0, "S": 0}
        play_order[last_four_moves][current_move] += 1

        # 2d. Usar los 4 movimientos más recientes para predecir
        potential_pattern = "".join(opponent_history[-4:])
        
        if potential_pattern in play_order:
            # Predecir la jugada más probable del oponente
            prediction = max(play_order[potential_pattern], key=play_order[potential_pattern].get)
        else:
            # Si el patrón es nuevo, usa la jugada más frecuente en general
            if opponent_history:
                prediction = max(set(opponent_history), key=opponent_history.count)
            else:
                prediction = random.choice(["R", "P", "S"])

    # Paso 3: Contraatacar la predicción
    # (Elige la jugada que vence a la 'prediction')
    if prediction == "R":
        return "P"
    elif prediction == "P":
        return "S"
    else: # prediction == "S"
        return "R"