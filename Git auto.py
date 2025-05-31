import pyautogui as pa
import time
import pyperclip
import os

# Configuração de segurança do PyAutoGUI
pa.FAILSAFE = True
pa.PAUSE = 1.0  # Pausa entre comandos

def atualizar_versao():
    try:
        # Verifica se o arquivo existe
        if not os.path.exists('versao.txt'):
            with open('versao.txt', 'w') as f:
                f.write('1.0')
            return '1.0'

        # Lê a versão atual
        with open('versao.txt', 'r') as f:
            versao = f.read().strip()

        # Atualiza a versão
        try:
            major, minor = map(int, versao.split('.'))
            minor += 1
            nova_versao = f"{major}.{minor}"
        except ValueError:
            print("Erro no formato da versão. Resetando para 1.0")
            nova_versao = '1.0'

        # Salva a nova versão
        with open('versao.txt', 'w') as f:
            f.write(nova_versao)

        return nova_versao

    except Exception as e:
        print(f"Erro ao atualizar versão: {e}")
        return None

def executar_comandos_git(nova_versao):
    try:
        # Abre o terminal
        for tecla in ['`', "'"]:
            pa.hotkey('ctrl', 'shift', tecla)
            time.sleep(1)  # Espera o terminal abrir

        # Comandos Git
        comandos = [
            "git add .",
            f"git commit -m '{nova_versao}'",
            "git push"
        ]

        for comando in comandos:
            pa.write(comando)
            pa.press('enter')
            time.sleep(2)  # Espera entre comandos

        print("Comandos Git executados com sucesso!")
        return True

    except Exception as e:
        print(f"Erro ao executar comandos Git: {e}")
        return False

def main():
    # Atualiza a versão
    nova_versao = atualizar_versao()
    if not nova_versao:
        print("Falha ao atualizar versão. Programa encerrado.")
        return

    # Executa comandos Git
    print(f"Iniciando commit da versão {nova_versao}")
    if not executar_comandos_git(nova_versao):
        print("Falha ao executar comandos Git.")

if __name__ == "__main__":
    main()