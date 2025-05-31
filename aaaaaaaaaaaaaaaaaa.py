import customtkinter as ctk
from PIL import Image
import os

def toggle_senha():
    # Alterna entre mostrar e esconder a senha
    if entry2.cget('show') == '*':
        entry2.configure(show='')
        botao_mostrar_senha.configure(text="Esconder Senha")
    else:
        entry2.configure(show='*')
        botao_mostrar_senha.configure(text="Mostrar Senha")

def vai_la():
    usuario = entry1.get()
    senha = entry2.get()
    if usuario == "admin" and senha == "admin":
        label3.configure(text="Login realizado com sucesso", text_color="green")
    else:
        label3.configure(text="Usuario ou senha invalidos", text_color="red")

ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.title("Aula do dia 27/05/2025")
janela.geometry("800x600")

# Criando o frame principal
frame_principal = ctk.CTkFrame(janela)
frame_principal.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

# Frame para o formulário de login
frame_login = ctk.CTkFrame(frame_principal)
frame_login.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

# Frame para o título e logo do Senac
frame_titulo = ctk.CTkFrame(frame_login, fg_color="transparent")
frame_titulo.grid(row=0, column=0, pady=30)

# Título
titulo = ctk.CTkLabel(frame_titulo, text="Login Senac", text_color="orange", font=("Arial", 24, "bold"))
titulo.grid(row=0, column=0, padx=10)

# Logo do Senac
caminho_imagem_senac = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SenacLogo.png")
imagem_senac = Image.open(caminho_imagem_senac)
imagem_senac_ctk = ctk.CTkImage(light_image=imagem_senac, dark_image=imagem_senac, size=(50, 50))
label_imagem_senac = ctk.CTkLabel(frame_titulo, image=imagem_senac_ctk, text="")
label_imagem_senac.grid(row=0, column=1, padx=5)

# Frame para campo de usuário
frame_usuario = ctk.CTkFrame(frame_login, fg_color="transparent")
frame_usuario.grid(row=1, column=0, pady=(10, 5))

label1 = ctk.CTkLabel(frame_usuario, text="Usuario:", font=("Arial", 20, "bold"))
label1.grid(row=0, column=0)

entry1 = ctk.CTkEntry(frame_login, placeholder_text="Digite seu usuario", width=400)
entry1.grid(row=2, column=0)

# Frame para campo de senha
frame_senha_label = ctk.CTkFrame(frame_login, fg_color="transparent")
frame_senha_label.grid(row=3, column=0, pady=(20, 5))

label2 = ctk.CTkLabel(frame_senha_label, text="Senha:", font=("Arial", 20, "bold"))
label2.grid(row=0, column=0)

# Frame para senha e botão de mostrar
frame_senha = ctk.CTkFrame(frame_login, fg_color="transparent")
frame_senha.grid(row=4, column=0)

entry2 = ctk.CTkEntry(frame_senha, placeholder_text="Digite sua senha", show="*", width=270)
entry2.grid(row=0, column=0, padx=(0, 10))

# Botão para mostrar/ocultar senha
botao_mostrar_senha = ctk.CTkButton(
    frame_senha,
    text="Mostrar Senha",
    width=120,
    height=35,
    command=toggle_senha
)
botao_mostrar_senha.grid(row=0, column=1)

# Botão de login
botao = ctk.CTkButton(frame_login, text="Entrar", font=("Arial", 15, "bold"), command=vai_la, width=200)
botao.grid(row=5, column=0, pady=30)

try:
    # Obtendo o diretório atual do script
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_imagem = os.path.join(diretorio_atual, "Instagram2.png")
    
    imagem = Image.open(caminho_imagem)
    imagem_ctk = ctk.CTkImage(light_image=imagem, dark_image=imagem, size=(30, 30))
    
    # Frame para agrupar imagem do Instagram e texto
    frame_imagem = ctk.CTkFrame(frame_login, fg_color="transparent")
    frame_imagem.grid(row=6, column=0, pady=10)
    frame_imagem.grid_columnconfigure(0, weight=1)  # Espaço à esquerda
    frame_imagem.grid_columnconfigure(2, weight=1)  # Espaço à direita
    
    # Imagem do Instagram
    label_imagem = ctk.CTkLabel(frame_imagem, image=imagem_ctk, text="")
    label_imagem.grid(row=0, column=0, padx=5, sticky="e")
    
    # Texto @Senac.Minas
    label_instagram = ctk.CTkLabel(frame_imagem, text="@Senac.Minas", font=("comic_sans", 14, "bold"))
    label_instagram.grid(row=0, column=1, padx=5, sticky="w")
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

# Label para mensagens
label3 = ctk.CTkLabel(frame_login, text="")
label3.grid(row=7, column=0, pady=10)

# Configurando o grid
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)  # Espaço para a imagem
frame_login.grid_columnconfigure(0, weight=1)

janela.mainloop()
