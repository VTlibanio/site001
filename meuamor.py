import tkinter as tk

# ----------------- JANELA PRINCIPAL -----------------
root = tk.Tk()
root.title("Para a pessoa que eu mais amo nesse mundo todo...")
root.geometry("820x640")
root.configure(bg="#fce4ec")
root.resizable(False, False)

# ----------------- CONTAINER -----------------
container = tk.Frame(root, bg="#fce4ec")
container.pack(fill="both", expand=True)

pagina1 = tk.Frame(container, bg="#fce4ec")
pagina2 = tk.Frame(container, bg="#fce4ec")

for frame in (pagina1, pagina2):
    frame.place(relwidth=1, relheight=1)

def mostrar_pagina(p):
    p.tkraise()

# ==================================================
# ============= PÁGINA Apresentação ================
# ==================================================

titulo = tk.Label(
    pagina1,
    text="Para: pequena",
    bg="#fce4ec",
    fg="#c2185b",
    font=("Helvetica", 26, "bold")
)
titulo.pack(pady=(30, 10))

caixa1 = tk.Text(
    pagina1,
    height=22,
    width=80,
    font=("Courier New", 12, "bold"),
    bg="#fff5f8",
    fg="#c2185b",
    bd=0,
    highlightthickness=0
)
caixa1.pack(pady=(20, 10))
caixa1.config(state="disabled")

caixa1.tag_configure("centro", justify="center")

# FRASE ALTERADA
frase_coracao = (" Eu te amo com minha alma")
coracao_linhas = [
    "".join(
        [
            (frase_coracao[(x - y) % len(frase_coracao)]
             if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3
                - (x * 0.05) ** 2 * (y * 0.1) ** 3
                <= 0
             else " ")
            for x in range(-30, 30)
        ]
    )
    for y in range(15, -15, -1)
]

def animar_linha(i=0):
    caixa1.config(state="normal")
    if i == 0:
        caixa1.delete("1.0", "end")
    if i < len(coracao_linhas):
        caixa1.insert("end", coracao_linhas[i] + "\n", "centro")
        caixa1.config(state="disabled")
        root.after(35, animar_linha, i + 1)

# ----------------- BOTÕES -----------------
frame_botoes = tk.Frame(pagina1, bg="#fce4ec")
frame_botoes.pack(pady=(10, 20))

tk.Button(
    frame_botoes,
    text=" para o amor da minha vida, clique aqui 💖",
    command=lambda: animar_linha(0),
    font=("Helvetica", 13, "bold"),
    bg="#f8bbd9",
    fg="white",
    activebackground="#f06292",
    padx=20,
    pady=8,
    bd=0,
    cursor="hand2"
).grid(row=0, column=0, padx=10)

tk.Button(
    frame_botoes,
    text="Ir para a página 2 ➜",
    command=lambda: mostrar_pagina(pagina2),
    font=("Helvetica", 12, "bold"),
    bg="#f8bbd9",
    fg="#880e4f",
    activebackground="#f06292",
    padx=16,
    pady=6,
    bd=0,
    cursor="hand2"
).grid(row=0, column=1, padx=10)

# ==================================================
# ==================== PÁGINA 2 ====================
# ==================================================

titulo2 = tk.Label(
    pagina2,
    text=" para minha gata",
    bg="#fce4ec",
    fg="#c2185b",
    font=("Helvetica", 20, "bold")
)
titulo2.pack(pady=(40, 10))

# SEU TEXTO COM PONTUAÇÃO CERTINHA
texto2 = """Garota, quando te conheci o meu mundo mudou completamente.
Sabia que não seria algo de momento, seria algo pra vida.
Tenho orgulho em saber que você é minha e pra sempre será.
Sou louco no seu jeito, no seu rosto, seus detalhes e tudo em você.
Posso garantir que ter te conhecido foi a melhor das coisas que poderiam ter acontecido na minha vida.
Amo ser amado e amo ter você.
Agradeço por todas as memórias que já criamos juntos. Ainda temos a vida pela frente e quero te proporcionar muito mais."""

label_texto2 = tk.Label(
    pagina2,
    text=texto2,
    bg="#fff5f8",
    fg="#880e4f",
    font=("Helvetica", 13),
    justify="left",
    padx=30,
    pady=30,
    wraplength=650
)
label_texto2.pack(padx=60, pady=(0, 30), fill="x")

tk.Button(
    pagina2,
    text="⬅ Voltar a página 1",
    command=lambda: mostrar_pagina(pagina1),
    font=("Helvetica", 12, "bold"),
    bg="#f8bbd9",
    fg="#880e4f",
    activebackground="#f06292",
    padx=16,
    pady=6,
    bd=0,
    cursor="hand2"
).pack()

# ----------------- INÍCIO -----------------
mostrar_pagina(pagina1)
root.mainloop()
