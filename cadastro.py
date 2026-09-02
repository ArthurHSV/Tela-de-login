from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout =[
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')]
]
#Janela
janela= sg.Window('Tela de login', layout)
#Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Arthur' and valores['senha'] == '12345' :
            sg.popup('Bem-vindo ao Dev Mod!')
            break
janela.close()