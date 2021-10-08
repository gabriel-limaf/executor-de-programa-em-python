import PySimpleGUI as sg
import os


def escolher_arquivo():
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layout = [[sg.Text('Caminho do arquivo')],
              [sg.Input(), sg.FileBrowse(key='-FOLDER-')],
              [sg.Button('OK')],
              [sg.Button('Cancelar')]
              ]
    return sg.Window('Executor de programa em Python', layout=layout, finalize=True)


def erro():
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layout = [[sg.Text('Favor escolha um arquivo ou programa!')],
              [sg.Button('Voltar'), sg.Button('Cancelar')]]
    return sg.Window('ATENÇÃO', layout=layout, size=(300, 100), finalize=True)


janela1, janela2 = escolher_arquivo(), None
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Cancelar':
        break
    if window == janela1 and event == 'OK' and values['-FOLDER-'] == '':
        janela2 = erro()
    if window == janela1 and event == 'OK' and values['-FOLDER-'] != '':
        folder = values['-FOLDER-']
        os.startfile(folder)
        break
    if window == janela2 and event == 'Voltar':
        janela1 = escolher_arquivo()
    if window == janela2 and event == 'Cancelar':
        break
