import os
import datetime
mensagens = []
while True:
    os.system('cls')
    print("Chat de mensagens:")
    for mensagem in mensagens:
        print(mensagem)
    print("\n______________________________________________________________")
    nova_mensagem = input("Digite sua mensagem (ou 'sair' para encerrar): ")
    horario_atual = datetime.datetime.now().strftime("%H:%M")
    if nova_mensagem.lower() == 'sair':
        break
    if nova_mensagem.strip() != "":
        mensagens.append(f"[{horario_atual}] {nova_mensagem}")