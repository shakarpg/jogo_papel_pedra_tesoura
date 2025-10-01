import random
import tkinter as tk

# Criar a janela principal
tela = tk.Tk()
tela.title("Minha Aplicação")
tela.geometry("500x600")
tela.configure(bg="#2c3e50")

# Título do jogo
titulo = tk.Label(tela, text="Pedra, Papel e Tesoura", font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
titulo.pack(pady=20)

# Label para mostrar a escolha do computador
label_computador = tk.Label(tela, text="Computador: ?", font=("Arial", 14), bg="#2c3e50", fg="white")
label_computador.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(tela, text="Faça sua escolha!", font=("Arial", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
label_resultado.pack(pady=20)

# Frame para os botões
frame_botoes = tk.Frame(tela, bg="#2c3e50")
frame_botoes.pack(pady=20)

# Função do jogo
def jogar(escolha_jogador):
    import random
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_computador = random.choice(opcoes)

    label_computador.config(text=f"Computador: {escolha_computador}")

    if escolha_jogador == escolha_computador:
        resultado = "EMPATE!"
        cor = "#f39c12"
    elif (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_jogador == "Papel" and escolha_computador == "Pedra") or \
         (escolha_jogador == "Tesoura" and escolha_computador == "Papel"):
        resultado = "VOCÊ GANHOU! 🎉"
        cor = "#27ae60"
    else:
        resultado = "VOCÊ PERDEU! 😢"
        cor = "#e74c3c"

    label_resultado.config(text=resultado, fg=cor)

# Botões para as escolhas
btn_pedra = tk.Button(frame_botoes, text="🪨 Pedra", font=("Arial", 14), width=12, height=2,
                      bg="#3498db", fg="white", command=lambda: jogar("Pedra"))
btn_pedra.grid(row=0, column=0, padx=10, pady=10)

btn_papel = tk.Button(frame_botoes, text="📄 Papel", font=("Arial", 14), width=12, height=2,
                      bg="#3498db", fg="white", command=lambda: jogar("Papel"))
btn_papel.grid(row=0, column=1, padx=10, pady=10)

btn_tesoura = tk.Button(frame_botoes, text="✂️ Tesoura", font=("Arial", 14), width=12, height=2,
                        bg="#3498db", fg="white", command=lambda: jogar("Tesoura"))
btn_tesoura.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botão para reiniciar
btn_reiniciar = tk.Button(tela, text="🔄 Jogar Novamente", font=("Arial", 12),
                          bg="#95a5a6", fg="white", command=lambda: [label_computador.config(text="Computador: ?"),
                                                                       label_resultado.config(text="Faça sua escolha!", fg="#ecf0f1")])
btn_reiniciar.pack(pady=20)


# Iniciar o loop da interface
tela.mainloop()
def jogo_ppt():
    opcoes = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opcoes)

    print("Escolha: pedra, papel ou tesoura")
    jogador = input("Sua escolha: ").lower()

    while jogador not in opcoes:
        print("Escolha inválida. Tente novamente: pedra, papel ou tesoura")
        jogador = input("Sua escolha: ").lower()

    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        return "Empate!"
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

# Para jogar, descomente:
print(jogo_ppt())
