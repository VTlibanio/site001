import os
import webbrowser

# O conteúdo do site (HTML + CSS)
html_content = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Nosso Primeiro Mês</title>
    <style>
        body { background-color: #fff0f5; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; color: #d63384; text-align: center; }
        .container { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); max-width: 500px; }
        h1 { font-size: 2em; margin-bottom: 10px; }
        p { font-size: 1.2em; line-height: 1.6; color: #555; }

        /* O BUQUÊ SIMBÓLICO */
        .bouquet { position: relative; width: 200px; height: 250px; margin: 20px auto; }
        .flower { position: absolute; width: 40px; height: 40px; border-radius: 50%; }

        /* Rosas */
        .rose { background: #ff4d94; border: 3px solid #ff1a75; }
        .rose::after { content: '❤'; color: white; font-size: 15px; display: block; margin-top: 8px; }

        /* Margaridas */
        .daisy { background: white; border: 3px solid #ffd700; }
        .daisy::after { content: ''; display: block; width: 15px; height: 15px; background: #ffd700; border-radius: 50%; margin: 10px auto; }

        /* Posições das flores */
        .f1 { top: 0; left: 80px; } .f2 { top: 30px; left: 40px; }
        .f3 { top: 30px; left: 120px; } .f4 { top: 70px; left: 20px; }
        .f5 { top: 70px; left: 140px; } .f6 { top: 70px; left: 80px; }

        .stems { width: 10px; height: 100px; background: #4caf50; margin: 110px auto 0; border-radius: 5px; position: relative; }
        .stems::before { content: ''; position: absolute; width: 60px; height: 10px; background: #4caf50; top: 20px; left: -25px; transform: rotate(-30deg); border-radius: 5px; }

        .footer { margin-top: 20px; font-weight: bold; font-size: 1.5em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>1 Mês de Nós! ❤️</h1>
        <p>Obrigado por cada momento incrível que passamos juntos. Este é apenas o começo da nossa história!</p>

        <div class="bouquet">
            <div class="flower rose f1"></div>
            <div class="flower daisy f2"></div>
            <div class="flower rose f3"></div>
            <div class="flower daisy f4"></div>
            <div class="flower rose f5"></div>
            <div class="flower daisy f6"></div>
            <div class="stems"></div>
        </div>

        <div class="footer">Eu te amo!</div>
    </div>
</body>
</html>
"""

# Salva o arquivo na pasta atual
filename = "index.html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(html_content)

# Abre o arquivo automaticamente no navegador
path = os.path.abspath(filename)
webbrowser.open(f"file://{path}")

print("Site criado com sucesso! Verifique seu navegador.")
