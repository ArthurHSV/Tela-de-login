from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout =[
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar'), sg.Button('Limpar'), sg.Button('Cadastro')]
]
#Janela
janela= sg.Window('Tela de login', layout)
#Ler eventos

tentativas = 0

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Arthur' and valores['senha'] == '12345' :
            sg.popup('Bem-vindo ao Dev Mod!')
            break
        else:
            tentativas = tentativas + 1
            restantes = 3 - tentativas
            if tentativas >= 3:
                sg.popup('Número màximo de tentativas atingido!')

                break

            sg.popup(f'Senha ou usúario incorretos! Você ainda tem {restantes} tentativa(s)!')
            janela['usuario'].update('')
            janela['senha'].update('')

    if eventos == 'Limpar':
        janela['usuario'].update('')
        janela['senha'].update('')
        sg.popup('Preencha novamente!')

    if eventos == 'Cadastro':
        layout_cadastro =[
        [sg.Text('Nome de Usuário'),sg.Input(key='nome_de_usuario')],
        [sg.Text('E-mail'),sg.Input(key='email_usuario')],
        [sg.Text('Confirmação de E-mail'),sg.Input(key='configrmacao_email_usuario')],
        [sg.Text('Senha'), sg.Input(key='senha',password_char='*')],
        [sg.Text('Confirmação de Senha'), sg.Input(key='confirmacao_senha',password_char='*')]
        ]

        janela_cadastro = sg.Window('Área de Cadastro', layout_cadastro)

        evento_cadastro, valores_cadastro = janela_cadastro.read()

        
janela.close() 