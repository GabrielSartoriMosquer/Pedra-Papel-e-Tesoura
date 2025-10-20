# Jogo Pedra, Papel e Tesoura contra o Computador

# Bibliotecas necessárias
import random
import os
import time
from datetime import datetime

# Definição das variáveis principais
jogadas = ['Pedra', 'Papel', 'Tesoura'] # Opções de jogadas disponíveis

regras = {
    'Pedra': 'Tesoura', # Pedra ganha de Tesoura
    'Papel': 'Pedra', # Papel ganha de Pedra
    'Tesoura': 'Papel' # Tesoura ganha de Papel
}

# Funções do jogo

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal, independente do sistema operacional

def numero_de_jogos(): # Conta o número de jogos registrados no arquivo de histórico
    if not os.path.exists('historico_jogos.txt'):
        return 0
    with open('historico_jogos.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        jogos = conteudo.count('-----------------------')
    return jogos

def hora_atual(): # Retorna a hora atual formatada
    agora = datetime.now()
    return agora.strftime('%d/%m/%Y %H:%M:%S')

def menu_inicial(): # Exibe o menu inicial e retorna a escolha do usuário
    limpar_tela()
    print(f'Vamos jogar {jogadas[0]}, {jogadas[1]}, {jogadas[2]}!')
    print('1. Iniciar novo jogo')
    print('2. Verificar jogos anteriores')
    print('3. Sair')
    escolha = input('Por favor, selecione uma opção (1-3): ')
    return escolha

def jogada_do_computador(): # Gera a jogada do computador aleatoriamente
    jogada_computador = random.choice(jogadas)
    print(f'Jogada do Computador: {jogada_computador.upper()}\n')
    return jogada_computador

def jogada_do_usuario(): # Solicita a jogada do usuário e valida a entrada
    while True:
        print('Escolha sua jogada:')
        print(f'1. {jogadas[0]} | 2. {jogadas[1]} | 3. {jogadas[2]}')
        jogada_usuario = input('Por favor, selecione uma opção (1-3): ')

        match jogada_usuario:
            case '1':
                print(f'\nSua Jogada: {jogadas[0].upper()}')
                return jogadas[0]
            case '2':
                print(f'\nSua Jogada: {jogadas[1].upper()}')
                return jogadas[1]
            case '3':
                print(f'\nSua Jogada: {jogadas[2].upper()}')
                return jogadas[2]
            case _:
                print('Opção inválida. Tente novamente.\n')

def relatorio_jogo(jogada_pc, jogada_user, vencedor): # Registra o resultado do jogo no arquivo de histórico
    with open('historico_jogos.txt', 'a') as arquivo:
        arquivo.write(f'Jogo Número: {numero_de_jogos() + 1}\n')
        arquivo.write(f'Horário do jogo: {hora_atual()}\n')
        arquivo.write(f'Jogada do Computador: {jogada_pc}\n')
        arquivo.write(f'Jogada do Usuário: {jogada_user}\n')
        arquivo.write(f'Vencedor: {vencedor}\n')
        arquivo.write('-----------------------\n')

# Loop principal do jogo

if __name__ == '__main__': 
    while True:
        escolha = menu_inicial()
        match escolha:
            case '1':
                print('Iniciando novo jogo...')
                time.sleep(1)
                limpar_tela()

                print(f'{jogadas[0].upper()}, {jogadas[1].upper()}, {jogadas[2].upper()} - JOGO INICIADO!') 
                print(f'As regras são simples: {jogadas[0]} ganha de {jogadas[2]}, {jogadas[2]} ganha de {jogadas[1]}, {jogadas[1]} ganha de {jogadas[0]}.\n')
                print('É VOCÊ CONTRA O COMPUTADOR.\nMELHOR DE TRÊS\nQUE VENÇA O MELHOR!\n')

                jogada_usuario = jogada_do_usuario()
                jogada_computador = jogada_do_computador()

                if jogada_usuario == jogada_computador:
                        vencedor = 'empate'
                else:
                    if regras[jogada_usuario] == jogada_computador:
                        vencedor = 'jogador'
                    else:
                        vencedor = 'computador'

                match vencedor:
                    case 'jogador':
                        print('Parabéns! Você venceu!\n')
                    case 'computador':
                        print('O computador venceu. Tente novamente!\n')                        
                    case 'empate':
                        print('Ambos fizeram a mesma jogada. Empate!\n')

                input("Pressione Enter para continuar...")
                limpar_tela()

                relatorio_jogo(jogada_computador, jogada_usuario, vencedor)

            case '2':
                limpar_tela()
                print('Consultando jogos anteriores...\n')
                if os.path.exists('historico_jogos.txt'):
                    with open('historico_jogos.txt', 'r') as arquivo:
                        conteudo = arquivo.read()
                        print('Histórico de Jogos Anteriores:\n')
                        print(conteudo)

                else:
                    print('Nenhum jogo anterior encontrado.\n')
   
            case '3':
                print('Saindo do jogo. Até a próxima!')
                break
            
            case _:
                print('Opção inválida. Tente novamente.\n')