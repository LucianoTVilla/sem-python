import ahorcado, reverse, tateti
import PySimpleGUI as sg
import json

player_data = []

sg.theme('DarkAmber') 
layout = [  [sg.Text('Bienvenido a Juegos.py')],
            [sg.Text('Ingresa tu nombre'), sg.InputText()],
            [sg.Text('¿Que juego querés jugar?')],
            [sg.Button('Ahorcado'), sg.Button('Reverse'), sg.Button('Tateti')] ]

window = sg.Window('Juegos.py', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  
        break
    if event in('Ahorcado'):
        player_data.append({'Nombre':values[0], 'Juego': 'Ahorcado'})
        window.close()
        ahorcado.game()
    if event in('Reverse'):
        player_data.append({'Nombre':values[0], 'Juego': 'Reverse'})
        window.close()
        reverse.game()
    if event in('Tateti'):
        player_data.append({'Nombre':values[0], 'Juego': 'Tateti'})
        window.close()
        tateti.game()
    archivo = open("Historial.txt", "a")
    json.dump(player_data, archivo)
    archivo.close()
window.close()
