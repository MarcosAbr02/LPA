# ---------------------------------------------------------------------------------------------------------------------
# # 1.1 Evento de Teclado
# import keyboard
#
#
# def on_key_event(event):
#     if event.event_type == keyboard.KEY_DOWN:  # Verifica se a tecla foi pressionada
#         print(f'Tecla pressionada: {event.name}')
#         if event.name == 'a':
#             print('a em especial')
#
#
# #  main
# keyboard.on_press(on_key_event)  # Registra o hook para o evento de tecla pressionada
#
# # Mantém o programa em execução para capturar os eventos de tecla indefinidamente
# try:
#     while True:
#         pass  # aqui eu poderia colocar o resto do meu código
# except KeyboardInterrupt:
#     print("Programa interrompido pelo usuário.")
# # ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# 1.2 Evento de Tempo
import sched
import time


def exibir_mensagem(mensagem):
    print(mensagem)


def agendar_evento(scheduler, intervalo, mensagem):
    # Agendando o próximo evento
    scheduler.enter(intervalo, 1, agendar_evento, (scheduler, intervalo, mensagem))

    # Exibindo a mensagem
    exibir_mensagem(mensagem)


# Cria uma instância do objeto scheduler
new_scheduler = sched.scheduler(time.time, time.sleep)

# Agendando o primeiro evento
agendar_evento(new_scheduler, 1, "Esta é a mensagem agendada a cada 1 segundo!")

print("Esperando para exibir as mensagens agendadas...")

# Executando o scheduler em loop (Ctrl + F2 para interromper manualmente)
new_scheduler.run()
# ---------------------------------------------------------------------------------------------------------------------
