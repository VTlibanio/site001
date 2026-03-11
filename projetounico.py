from flask import Flask, request, session, redirect, render_template_string, url_for
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'vml_top_tier_curator_2026'

# --- DATABASE DE ELITE COMPLETO ---
CATALOGO = {
    'carnes': {
        'Wagyu A5 Kobe Beef': {'p': 920.0, 'tag': '🔥 TOP 1 RELEVANTE'},
        'Picanha Wagyu A5': {'p': 890.0, 'tag': '🔥 TOP 2 RELEVANTE'},
        'Picanha Black Angus': {'p': 175.0, 'tag': '🔥 TOP 3 RELEVANTE'},
        'Tomahawk Gold Leaf': {'p': 310.0, 'tag': '🔥 TOP 4 RELEVANTE'},
        'Dry Aged 60 Days': {'p': 350.0, 'tag': '🔥 TOP 5 RELEVANTE'},
        'Bife de Tira (Picanha)': {'p': 165.0}, 'Prime Rib Angus': {'p': 185.0},
        'Short Rib Wagyu': {'p': 240.0}, 'Assado de Tira': {'p': 145.0},
        'Carré de Cordeiro': {'p': 280.0}, 'Filé Mignon c/ Trufas': {'p': 210.0},
        'Linguiça de Trufa Negra': {'p': 85.0}, 'Chorizo Wagyu': {'p': 320.0}
    },
    'bebidas': {
        'Royal Salute 21y': {'p': 1180.0, 'tag': '🔥 TOP 1 RELEVANTE'},
        'Dom Pérignon': {'p': 2850.0, 'tag': '🔥 TOP 2 RELEVANTE'},
        'Whisky Blue Label': {'p': 1280.0, 'tag': '🔥 TOP 3 RELEVANTE'},
        'Heineken (Long Neck)': {'p': 16.0, 'tag': '🍺 FAVORITA'},
        'Corona Extra (Long)': {'p': 15.5, 'tag': '🍺 FAVORITA'},
        'Stella Artois Gold': {'p': 14.0}, 'Gin Monkey 47': {'p': 360.0},
        'Tequila Don Julio 1942': {'p': 1800.0}, 'Vinho Almaviva': {'p': 2200.0},
        'Vinho Pêra-Manca': {'p': 4500.0}, 'Champagne Krug': {'p': 2900.0}
    }
}

REGIOES = {
    'SP': {'nome': 'São Paulo', 'fator': 1.15},
    'RJ': {'nome': 'Rio de Janeiro', 'fator': 1.18},
    'MS': {'nome': 'Mato Grosso do Sul', 'fator': 1.10},
    'SC': {'nome': 'Santa Catarina', 'fator': 1.12}
}

UI_BASE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root { --gold: linear-gradient(135deg, #8A6E2F, #FFECB3, #8A6E2F); --pure-gold: #D4AF37; --dark: #000; }
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background: var(--dark); color: #FFF; font-family: 'Inter', sans-serif; }
        .shutter-transition { position: fixed; top: 0; left: 0; width: 100%; height: 100%; display: flex; z-index: 9999; pointer-events: none; }
        .shutter-part { flex: 1; background: #000; transition: transform 0.8s ease-in-out; border: 1px solid #111; }
        body.loaded .shutter-part.left { transform: translateX(-100%); }
        body.loaded .shutter-part.right { transform: translateX(100%); }
        .vlm-nav { text-align: center; padding: 40px 0; font-size: 2rem; background: var(--gold); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: 15px; font-weight: bold; }
        .container { max-width: 500px; margin: 0 auto; padding: 20px; }
        .card { background: #080808; border: 1px solid #151515; border-radius: 35px; padding: 30px; margin-bottom: 20px; }
        label { font-size: 9px; text-transform: uppercase; color: #444; letter-spacing: 2px; display: block; margin: 20px 0 8px; }
        input, select { width: 100%; background: #000; border: 1px solid #1a1a1a; padding: 15px; border-radius: 15px; color: white; }
        .quick-select { display: flex; gap: 10px; margin-top: 10px; }
        .quick-btn { flex: 1; padding: 15px; background: transparent; border: 1px solid #222; color: #666; border-radius: 15px; cursor: pointer; transition: 0.3s; font-size: 11px; }
        .quick-btn.active { border-color: var(--pure-gold); color: var(--pure-gold); background: rgba(212, 175, 55, 0.05); }
        .item-row { display: flex; justify-content: space-between; align-items: center; padding: 15px 0; border-bottom: 1px solid #111; }
        .btn-gold { width: 100%; padding: 20px; background: var(--gold); border: none; border-radius: 18px; color: #000; font-weight: bold; cursor: pointer; margin-top: 30px; letter-spacing: 2px; }
        .qty-input { width: 60px !important; text-align: center; color: var(--pure-gold) !important; font-weight: bold; }
    </style>
</head>
<body onload="setTimeout(() => document.body.classList.add('loaded'), 100)">
    <div class="shutter-transition"><div class="shutter-part left"></div><div class="shutter-part right"></div></div>
    <div class="vlm-nav">V L M</div>
    <div class="container">{% block content %}{% endblock %}</div>
    <script>
        function setVal(id, val, el) {
            document.getElementById(id).value = val;
            let btns = el.parentElement.querySelectorAll('.quick-btn');
            btns.forEach(b => b.classList.remove('active'));
            el.classList.add('active');
        }
    </script>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def step_setup():
    if request.method == 'POST':
        session['setup'] = request.form.to_dict()
        session['carrinho'] = {}
        return redirect(url_for('step_items', categoria='carnes'))

    hoje = datetime.now().strftime('%d/%m')
    amanha = (datetime.now() + timedelta(days=1)).strftime('%d/%m')
    return render_template_string(UI_BASE + """
    {% block content %}
    <div class="card">
        <form method="POST">
            <label>Título do Evento</label>
            <input type="text" name="titulo" placeholder="Ex: Diamond Gala" required>
            <label>Agendamento (Data)</label>
            <input type="hidden" name="data" id="d_in" value="{{hoje}}">
            <div class="quick-select">
                <button type="button" class="quick-btn active" onclick="setVal('d_in','{{hoje}}',this)">HOJE ({{hoje}})</button>
                <button type="button" class="quick-btn" onclick="setVal('d_in','{{amanha}}',this)">AMANHÃ ({{amanha}})</button>
                <button type="button" class="quick-btn" onclick="setVal('d_in','FDS',this)">PRÓX. FDS</button>
            </div>
            <label>Horário</label>
            <input type="hidden" name="hora" id="h_in" value="20:00">
            <div class="quick-select">
                <button type="button" class="quick-btn" onclick="setVal('h_in','13:00',this)">13:00</button>
                <button type="button" class="quick-btn" onclick="setVal('h_in','18:00',this)">18:00</button>
                <button type="button" class="quick-btn active" onclick="setVal('h_in','20:00',this)">20:00</button>
            </div>
            <label>Região</label>
            <select name="regiao">{% for k,v in regioes.items() %}<option value="{{k}}">{{v.nome}}</option>{% endfor %}</select>
            <button type="submit" class="btn-gold">CONFIGURAR CARNES</button>
        </form>
    </div>
    {% endblock %}
    """, hoje=hoje, amanha=amanha, regioes=REGIOES)


@app.route('/items/<categoria>', methods=['GET', 'POST'])
def step_items(categoria):
    if request.method == 'POST':
        for item, qtd in request.form.items():
            if int(qtd) > 0: session['carrinho'][item] = int(qtd)
        proxima = 'bebidas' if categoria == 'carnes' else 'resumo'
        return redirect(url_for('step_items', categoria=proxima) if proxima != 'resumo' else url_for('resumo'))

    itens = CATALOGO.get(categoria, {})
    return render_template_string(UI_BASE + """
    {% block content %}
    <div class="card">
        <h3 style="color:var(--pure-gold); text-align:center; text-transform:uppercase;">Selecionar {{categoria}}</h3>
        <form method="POST">
            {% for nome, info in itens.items() %}
            <div class="item-row">
                <div>
                    {% if info.tag %}<span style="font-size:8px; color:var(--pure-gold)">{{info.tag}}</span><br>{% endif %}
                    <span style="font-size:14px">{{nome}}</span>
                </div>
                <input type="number" name="{{nome}}" value="0" min="0" class="qty-input">
            </div>
            {% endfor %}
            <button type="submit" class="btn-gold">PRÓXIMO</button>
        </form>
    </div>
    {% endblock %}
    """, categoria=categoria, itens=itens)


@app.route('/resumo')
def resumo():
    setup = session.get('setup', {})
    carrinho = session.get('carrinho', {})
    fator = REGIOES[setup['regiao']]['fator']

    total = 0
    detalhes = []
    for item, qtd in carrinho.items():
        # Busca o preço original no catálogo (procura em carnes e bebidas)
        p_orig = (CATALOGO['carnes'].get(item) or CATALOGO['bebidas'].get(item))['p']
        preco_final = p_orig * fator * qtd
        total += preco_final
        detalhes.append({'nome': item, 'qtd': qtd, 'sub': preco_final})

    return render_template_string(UI_BASE + """
    {% block content %}
    <div class="card" style="text-align:left">
        <h2 style="color:var(--pure-gold)">{{setup.titulo}}</h2>
        <p style="font-size:12px; color:#666">{{setup.data}} às {{setup.hora}} | {{setup.regiao}}</p>
        <hr style="margin:20px 0; border:0; border-top:1px solid #222">
        {% for d in detalhes %}
        <div style="display:flex; justify-content:space-between; margin-bottom:10px">
            <span>{{d.qtd}}x {{d.nome}}</span>
            <span style="color:var(--pure-gold)">R$ {{ "{:,.2f}".format(d.sub) }}</span>
        </div>
        {% endfor %}
        <div style="margin-top:30px; border-top:1px solid var(--pure-gold); padding-top:20px; display:flex; justify-content:space-between">
            <span style="font-weight:bold">TOTAL ESTIMADO</span>
            <span style="font-weight:bold; color:var(--pure-gold); font-size:1.4rem">R$ {{ "{:,.2f}".format(total) }}</span>
        </div>
        <button onclick="window.print()" class="btn-gold">GERAR PDF DE ELITE</button>
    </div>
    {% endblock %}
    """, setup=setup, detalhes=detalhes, total=total)


if __name__ == '__main__':
    app.run(debug=True)
