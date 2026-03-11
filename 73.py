times = (
    'Flamengo', 'Palmeiras', 'Atlético-MG', 'Grêmio', 'São Paulo',
    'Internacional', 'Fluminense', 'Corinthians', 'Vasco da Gama', 'Botafogo',
    'Cruzeiro', 'Athletico-PR', 'Santos', 'Bahia', 'Fortaleza',
    'Cuiabá', 'Red Bull Bragantino', 'Juventude', 'Vitória', 'Atlético-GO'
)

colocados = times[:5]
rebaixados = times[16:]

# Top 5 em verde
print("\n".join(f"\033[92m{time}\033[0m" for time in colocados))

# Rebaixados em vermelho
print('A seguir os times que estão em zona de rebaixamento nesse exato momento:\n' +
      "\n".join(f"\033[91m{time}\033[0m" for time in rebaixados))

print('o bragantino está em 17º na tabela')