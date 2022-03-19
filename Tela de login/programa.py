from PySimpleGUI import PySimpleGUI as sg
# layout
sg.theme('Dark')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.InputText(key='senha', size=(20, 1), password_char='*')],
    [sg.Checkbox('Salvaor o loing?')],
    [sg.Button('Entrar')]
]

sg.theme('Dark')
layout2 = [
    [sg.Text('ss'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.InputText(key='senha', size=(20, 1), password_char='*')],
    [sg.Checkbox('Salvaor o loing?')],
    [sg.Button('Entrar')]
]

# janela
janela = sg.Window('Tela de Login',layout)

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos =='Entrar':
        if valores['usuario']=='luiz' and valores['senha'] =='1234':
            print('Bem vindo ao curso de Python!')
        else:
            print ('Credenciais inválidas, verifique!')
