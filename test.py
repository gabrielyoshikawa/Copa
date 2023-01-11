import random

grupo = ['Brasil', 'Sérvia', 'Suíça', 'Camarões']

#Brasil
pontosBrasil = 0
vitoriasBrasil = 0
empatesBrasil = 0
derrotasBrasil = 0
golMarcadoBrasil = 0
golSofridoBrasil = 0
saldoBrasil = 0

#Servia
pontosServia = 0
vitoriasServia = 0
empatesServia = 0
derrotasServia = 0
golMarcadoServia = 0
golSofridoServia = 0
saldoServia = 0

#Suica
pontosSuica = 0
vitoriasSuica = 0
empatesSuica = 0
derrotasSuica = 0
golMarcadoSuica = 0
golSofridoSuica = 0
saldoSuica = 0

#Camarões
pontosCamaroes = 0
vitoriasCamaroes = 0
empatesCamaroes = 0
derrotasCamaroes = 0
golMarcadoCamaroes = 0
golSofridoCamaroes = 0
saldoCamaroes = 0

resultado = []

#Tabela Jogos e Placares
print("Jogos e Placares:")
for i in grupo:
    for j in grupo:
        if i != j and i != grupo[3] and j != grupo[0]:
            if i == grupo[2] and j == grupo[1]:
                pass
            else:
                placar1 = random.randint(0,10)
                placar2 = random.randint(0,10)
                print(i, placar1, placar2, j)
                resultado.append(i)
                resultado.append(placar1)
                resultado.append(placar2)
                resultado.append(j)

#Pontuação - Vitória / Empate / Derrota
#Brasil x Sérvia
if resultado[1] > resultado[2]:
    vitoriasBrasil += 1
    pontosBrasil += 3
    derrotasServia += 1
elif resultado[1] == resultado[2]:
    empatesBrasil += 1
    pontosBrasil += 1
    empatesServia += 1
    pontosServia +=1
else:
    vitoriasServia += 1
    pontosServia += 3
    derrotasBrasil += 1
    
#Brasil x Suica
if resultado[5] > resultado[6]:
    vitoriasBrasil += 1
    pontosBrasil += 3
    derrotasSuica += 1
elif resultado[5] == resultado[6]:
    empatesBrasil += 1
    pontosBrasil += 1
    empatesSuica += 1
    pontosSuica += 1
else:
    vitoriasSuica += 1
    pontosSuica += 3
    derrotasBrasil += 1

#Brasil x Camarões
if resultado[9] > resultado[10]:
    vitoriasBrasil += 1
    pontosBrasil += 3
    derrotasCamaroes += 1
elif resultado[9] == resultado[10]:
    empatesBrasil += 1
    pontosBrasil += 1
    empatesCamaroes += 1
    pontosCamaroes += 1
else:
    vitoriasCamaroes += 1
    pontosCamaroes += 3
    derrotasBrasil +=1

#Sérvia x Suiça
if resultado[13] > resultado[14]:
    vitoriasServia += 1
    pontosServia += 3
    derrotasSuica += 1
elif resultado[13] == resultado[14]:
    empatesServia += 1
    pontosServia += 1
    empatesSuica += 1
    pontosSuica += 1
else:
    vitoriasSuica += 1
    pontosSuica += 3
    derrotasServia += 1

#Sérvia x Camarões
if resultado[17] > resultado[18]:
    vitoriasServia += 1
    pontosServia += 3
    derrotasCamaroes += 1
elif resultado[17] == resultado[18]:
    empatesServia += 1
    pontosServia += 1
    empatesCamaroes += 1
    pontosCamaroes += 1
else:
    vitoriasCamaroes += 1
    pontosCamaroes += 3
    derrotasServia += 1

#Suiça x Camarões
if resultado[21] > resultado[22]:
    vitoriasSuica += 1
    pontosSuica += 3
    derrotasCamaroes += 1
elif resultado[21] == resultado[22]:
    empatesSuica += 1
    pontosSuica += 1
    empatesCamaroes += 1
    pontosCamaroes += 1
else:
    vitoriasCamaroes += 1
    pontosCamaroes += 3
    derrotasSuica += 1

# ----------------------------------------------
#(GM) Gols Marcados / (GC) Sofridos / (SG) Saldo de Gols 

#Brasil
golMarcadoBrasil += resultado[1] + resultado[5] + resultado[9]
golSofridoBrasil += resultado[2] + resultado[6] + resultado[10]
saldoBrasil = golMarcadoBrasil - golSofridoBrasil

#Sérvia
golMarcadoServia += resultado[2] + resultado[13] + resultado[17]
golSofridoServia += resultado[1] + resultado[14] + resultado[18]
saldoServia = golMarcadoServia - golSofridoServia

#Suica
golMarcadoSuica += resultado[6] + resultado[14] + resultado[21]
golSofridoSuica += resultado[5] + resultado[13] + resultado[22]
saldoSuica = golMarcadoSuica - golSofridoSuica

#Camarões
golMarcadoCamaroes += resultado[10] + resultado[18] + resultado[22]
golSofridoCamaroes += resultado[9] + resultado[17] + resultado[21]
saldoCamaroes = golMarcadoCamaroes - golSofridoCamaroes

#Tabela

print('\nSeleção Pontos V E D GM GC SG\nBrasil', pontosBrasil,vitoriasBrasil,empatesBrasil,derrotasBrasil,golMarcadoBrasil, golSofridoBrasil, saldoBrasil,'\nSérvia',pontosServia,vitoriasServia,empatesServia,derrotasServia, golMarcadoServia, golSofridoServia, saldoServia)
print('Suiça', pontosSuica,vitoriasSuica,empatesSuica,derrotasSuica, golMarcadoSuica, golSofridoSuica, saldoSuica,'\nCamarões', pontosCamaroes,vitoriasCamaroes,empatesCamaroes,derrotasCamaroes, golMarcadoCamaroes, golSofridoCamaroes, saldoCamaroes,'\n')

# Sem empate
# Brasil ganha sem empate
if pontosBrasil > pontosServia and pontosBrasil > pontosSuica and pontosBrasil > pontosCamaroes:
    print('1º Brasil')
    if pontosServia > pontosSuica and pontosServia > pontosCamaroes:
        print('2° Sérvia')
    elif pontosSuica > pontosServia and pontosSuica > pontosCamaroes:
        print('2º Suíça')
    elif pontosCamaroes > pontosServia and pontosCamaroes > pontosSuica:
        print('2º Camarões')

# Brasil vencedor e 2º Lugar desempata em saldo de gols
    elif pontosSuica == pontosCamaroes == pontosServia:
        if saldoSuica > saldoCamaroes and saldoSuica > saldoServia:
            print('2º Suíça')
        elif saldoServia > saldoCamaroes and saldoServia > saldoSuica:
            print('2º Sérvia')
        elif saldoCamaroes > saldoSuica and saldoCamaroes > saldoServia:
            print('2º Camarões')

    elif pontosServia == pontosSuica:
        if saldoServia > saldoSuica:
            print('2° Sérvia')
        else:
            print('2° Suíça')
    elif pontosServia == pontosCamaroes:
        if saldoServia > saldoCamaroes:
            print('2° Sérvia')
        else:
            print('2° Camarões')
    elif pontosSuica == pontosCamaroes:
        if saldoSuica > saldoCamaroes:
            print('2° Suíça')
        else:
            print('2° Camarões')

# 3 Seleções disputam 2° lugar
    elif pontosServia == pontosSuica == pontosCamaroes:
        if saldoServia > saldoSuica and saldoServia > saldoCamaroes:
            print('2° Sérvia')
        elif saldoSuica > saldoServia and saldoSuica > saldoCamaroes:
            print('2° Suíça')
        elif saldoCamaroes > saldoServia and saldoCamaroes > saldoSuica:
            print('2° Camarões')

# 2 Lugar desempata em gols marcados 
    elif pontosServia == pontosCamaroes == pontosSuica:
        if golMarcadoSuica > golMarcadoCamaroes and golMarcadoSuica > golMarcadoServia:
            print('2° Suíça')
        elif golMarcadoServia > golMarcadoSuica and golMarcadoServia > golMarcadoCamaroes:
            print('2° Sérvia')
        elif golMarcadoCamaroes > golMarcadoServia and golMarcadoCamaroes > golMarcadoSuica:
            print('2° Camarões')

# Sérvia ganha sem empate
elif pontosServia > pontosBrasil and pontosServia > pontosSuica and pontosServia > pontosCamaroes:
    print('1º Sérvia')
    if pontosBrasil > pontosSuica and pontosBrasil > pontosCamaroes:
        print('2° Brasil')
    elif pontosSuica > pontosBrasil and pontosSuica > pontosCamaroes:
        print('2º Suíça')
    elif pontosCamaroes > pontosBrasil and pontosCamaroes > pontosSuica:
        print('2º Camarões')

# Sérvia vencedora e 2º Lugar desempata em saldo de gols
    elif pontosBrasil == pontosCamaroes == pontosSuica:
        if saldoBrasil > saldoCamaroes and saldoBrasil > saldoSuica:
            print('2º Brasil')
        elif saldoSuica > saldoCamaroes and saldoSuica > saldoBrasil:
            print('2º Suíça')
        elif saldoCamaroes > saldoBrasil and saldoCamaroes > saldoSuica:
            print('2º Camarões')

    elif pontosBrasil == pontosSuica:
        if saldoBrasil > saldoSuica:
            print('2° Brasil')
        else:
            print('2° Suíça')
    elif pontosBrasil == pontosCamaroes:
        if saldoBrasil > saldoCamaroes:
            print('2° Brasil')
        else:
            print('2° Camarões')
    elif pontosSuica == pontosCamaroes:
        if saldoSuica > saldoCamaroes:
            print('2° Suíça')
        else:
            print('2° Camarões')

# 3 Seleções disputam 2° lugar
    elif pontosBrasil == pontosSuica == pontosCamaroes:
        if saldoBrasil > saldoSuica and saldoBrasil > saldoCamaroes:
            print('2° Brasil')
        elif saldoSuica > saldoBrasil and saldoSuica > saldoCamaroes:
            print('2° Suíça')
        elif saldoCamaroes > saldoBrasil and saldoCamaroes > saldoSuica:
            print('2° Camarões')

# 2 Lugar desempata em gols marcados      
    elif pontosBrasil == pontosCamaroes == pontosSuica:
        if golMarcadoSuica > golMarcadoCamaroes and golMarcadoSuica > golMarcadoBrasil:
            print('2° Suíça')
        elif golMarcadoBrasil > golMarcadoSuica and golMarcadoBrasil > golMarcadoServia:
            print('2° Brasil')
        elif golMarcadoCamaroes > golMarcadoBrasil and golMarcadoCamaroes > golMarcadoSuica:
            print('2° Camarões')

#Suíça ganha sem empate
elif pontosSuica > pontosBrasil and pontosSuica > pontosServia and pontosSuica > pontosCamaroes:
    print('1º Suíça')
    if pontosBrasil > pontosServia and pontosBrasil > pontosCamaroes:
        print('2° Brasil')
    elif pontosServia > pontosBrasil and pontosServia > pontosCamaroes:
        print('2º Sérvia')
    elif pontosCamaroes > pontosBrasil and pontosCamaroes > pontosServia:
        print('2º Camarões')

# Suíça vencedora e 2º Lugar desempata em saldo de gols
    elif pontosBrasil == pontosCamaroes == pontosServia:
        if saldoBrasil > saldoCamaroes and saldoBrasil > saldoServia:
            print('2º Brasil')
        elif saldoServia > saldoCamaroes and saldoServia > saldoBrasil:
            print('2º Sérvia')
        elif saldoCamaroes > saldoBrasil and saldoCamaroes > saldoServia:
            print('2º Camarões')
    elif pontosServia == pontosBrasil:
        if saldoServia > saldoBrasil:
            print('2° Sérvia')
        else:
            print('2° Brasil')
    elif pontosServia == pontosCamaroes:
        if saldoServia > saldoCamaroes:
            print('2° Sérvia')
        else:
            print('2° Camarões')
    elif pontosBrasil == pontosCamaroes:
        if saldoBrasil > saldoCamaroes:
            print('2° Brasil')
        else:
            print('2° Camarões')
        
# 3 Seleções disputam 2° lugar
    elif pontosBrasil == pontosServia == pontosCamaroes:
        if saldoBrasil > saldoServia and saldoBrasil > saldoCamaroes:
            print('2° Brasil')
        elif saldoServia > saldoBrasil and saldoServia > saldoCamaroes:
            print('2° Sérvia')
        elif saldoCamaroes > saldoBrasil and saldoCamaroes > saldoServia:
            print('2° Camarões')

# 2 Lugar desempata em gols marcados            
    elif pontosBrasil == pontosCamaroes == pontosServia:
        if golMarcadoServia > golMarcadoCamaroes and golMarcadoServia > golMarcadoBrasil:
            print('2° Sérvia')
        elif golMarcadoBrasil > golMarcadoServia and golMarcadoBrasil > golMarcadoCamaroes:
            print('2° Brasil')
        elif golMarcadoCamaroes > golMarcadoBrasil and golMarcadoCamaroes > golMarcadoServia:
            print('2° Camarões')

# Camarões ganha sem empate
elif pontosCamaroes > pontosBrasil and pontosCamaroes > pontosServia and pontosCamaroes > pontosSuica:
    print('1º Camarões')
    if pontosBrasil > pontosServia and pontosBrasil > pontosSuica:
        print('2° Brasil')
    elif pontosServia > pontosBrasil and pontosServia > pontosSuica:
        print('2º Sérvia')
    elif pontosSuica > pontosBrasil and pontosSuica > pontosServia:
        print('2º Suíça')

# Camarões vencedor e 2º Lugar desempata em saldo de gols
    elif pontosBrasil == pontosSuica == pontosServia:
        if saldoBrasil > saldoSuica and saldoBrasil > saldoServia:
            print('2º Brasil')
        elif saldoServia > saldoSuica and saldoServia > saldoBrasil:
            print('2º Sérvia')
        elif saldoSuica > saldoBrasil and saldoSuica > saldoServia:
            print('2º Suíça')

    elif pontosServia == pontosSuica:
        if saldoServia > saldoSuica:
            print('2° Sérvia')
        else:
            print('2° Suíça')
    elif pontosServia == pontosBrasil:
        if saldoServia > saldoBrasil:
            print('2° Sérvia')
        else:
            print('2° Brasil')
    elif pontosSuica == pontosBrasil:
        if saldoSuica > saldoBrasil:
            print('2° Suíça')
        else:
            print('2° Brasil')

# 3 Seleções disputam 2° lugar
    elif pontosBrasil == pontosSuica == pontosServia:
        if saldoBrasil > saldoSuica and saldoBrasil > saldoServia:
            print('2° Brasil')
        elif saldoSuica > saldoBrasil and saldoSuica > saldoServia:
            print('2° Suíça')
        elif saldoServia > saldoBrasil and saldoServia > saldoSuica:
            print('2° Sérvia')

# 2 Lugar desempata em gols marcados        
    elif pontosBrasil == pontosCamaroes == pontosSuica:
        if golMarcadoSuica > golMarcadoServia and golMarcadoSuica > golMarcadoBrasil:
            print('2° Suíça')
        elif golMarcadoBrasil > golMarcadoSuica and golMarcadoBrasil > golMarcadoServia:
            print('2° Brasil')
        elif golMarcadoServia > golMarcadoBrasil and golMarcadoServia > golMarcadoSuica:
            print('2° Sérvia')

# 2 Seleções empatando em primeiro
elif pontosBrasil == pontosServia and pontosBrasil > pontosCamaroes and pontosBrasil > pontosSuica:
    if saldoBrasil > saldoServia:
        print('1º Brasil\n2° Sérvia')
    else:
        print('1° Sérvia\n2° Brasil')

elif pontosBrasil == pontosSuica and pontosBrasil > pontosServia and pontosBrasil > pontosCamaroes:
        if saldoBrasil > saldoSuica:
            print('1º Brasil\n2° Suíça')
        else:
            print('1° Suíça\n2° Brasil')

elif pontosBrasil == pontosCamaroes and pontosBrasil > pontosServia and pontosBrasil > pontosSuica:
        if saldoBrasil > saldoCamaroes:
            print('1º Brasil\n2° Camarões')
        else:
            print('1° Camarões\n2° Brasil')

elif pontosServia == pontosSuica and pontosServia > pontosCamaroes and pontosServia > pontosBrasil:
        if saldoServia > saldoSuica:
            print('1º Sérvia\n2° Suíça')
        else:
            print('1° Suíça\n2° Sérvia')

elif pontosServia == pontosCamaroes and pontosServia > pontosSuica and pontosServia > pontosBrasil:
        if saldoServia > saldoCamaroes:
            print('1º Sérvia\n2° Camarões')
        elif saldoCamaroes > saldoServia:
            print('1° Camarões\n2° Sérvia')

elif pontosSuica == pontosCamaroes and pontosSuica > pontosServia and pontosSuica > pontosBrasil:
        if saldoSuica > saldoCamaroes:
            print('1º Suíça\n2° Camarões')
        else:
            print('1° Camarões\n2° Suíça')

# 3 Seleções empatando em primeiro

elif pontosBrasil == pontosSuica and pontosBrasil == pontosServia:
    if saldoBrasil > saldoSuica and saldoBrasil > saldoServia:
        print('1° Brasil')
        if saldoServia > saldoSuica:
            print('2º Sérvia')
        elif saldoSuica > saldoServia:
            print('2º Suíça')
        elif saldoServia == saldoSuica:
            if golMarcadoServia > golMarcadoSuica:
                print('2º Sérvia')
            else:
                print('2º Suíça')

    elif saldoSuica > saldoBrasil and saldoSuica > saldoServia:
        print('1° Suíça')
        if saldoServia > saldoBrasil:
            print('2º Sérvia')
        elif saldoBrasil > saldoServia:
            print('2º Brasil')
        elif saldoBrasil == saldoServia:
            if golMarcadoBrasil > golMarcadoServia:
                print('2º Brasil')
            else:
                print('2º Sérvia')

    elif saldoServia > saldoBrasil and saldoServia > saldoSuica:
        print('1° Sérvia')
        if saldoBrasil > saldoSuica:
            print('2º Brasil')
        elif saldoSuica > saldoBrasil:
            print('2º Suíça')
        elif saldoSuica == saldoBrasil:
            if golMarcadoSuica > golMarcadoBrasil:
                print('2º Suíça')
            else:
                print('2º Brasil')

elif pontosBrasil == pontosServia and pontosBrasil == pontosCamaroes:
    if saldoBrasil > saldoServia and saldoBrasil > saldoCamaroes:
        print('1° Brasil')
        if saldoServia > saldoCamaroes:
            print('2º Sérvia')
        elif saldoCamaroes > saldoServia:
            print('2º Camarões')
        elif saldoCamaroes == saldoServia:
            if golMarcadoCamaroes > golMarcadoServia:
                print('2º Camarões')
            else:
                print('2º Sérvia')
            
    elif saldoServia > saldoBrasil and saldoServia > saldoCamaroes:
        print('1° Sérvia')
        if saldoBrasil > saldoSuica:
            print('2° Brasil')
        elif saldoSuica > saldoBrasil:
            print('2° Camarões')
        elif saldoSuica == saldoBrasil:
            if golMarcadoSuica > golMarcadoBrasil:
                print('2º Suíça')
            else:
                print('2º Brasil')
        
    elif saldoCamaroes > saldoBrasil and saldoCamaroes > saldoServia:
        print('1° Camarões')
        if saldoBrasil > saldoServia:
            print('2° Brasil')
        elif saldoServia > saldoBrasil:
            print('2° Sérvia')
        elif saldoServia == saldoBrasil:
            if golMarcadoServia > golMarcadoBrasil:
                print('2º Sérvia')
            else:
                print('2º Brasil')

elif pontosBrasil == pontosSuica and pontosBrasil == pontosCamaroes:
    if saldoBrasil > saldoSuica and saldoBrasil > saldoCamaroes:
        print('1° Brasil')
        if saldoSuica > saldoCamaroes:
            print('2º Suíça')
        elif saldoCamaroes > saldoSuica:
            print('2º Camarões')
        elif saldoCamaroes == saldoSuica:
            if golMarcadoCamaroes > golMarcadoSuica:
                print('2º Camarões')
            else:
                print('2º Suíça')

    elif saldoSuica > saldoBrasil and saldoSuica > saldoCamaroes:
        print('1° Suíça')
        if saldoBrasil > saldoCamaroes:
            print('2º Brasil')
        elif saldoBrasil < saldoCamaroes:
            print('2º Camarões')
        elif saldoBrasil == saldoCamaroes:
            if golMarcadoCamaroes > golMarcadoBrasil:
                print('2º Camarões')
            else:
                print('2º Brasil')

    elif saldoCamaroes > saldoBrasil and saldoCamaroes > saldoSuica:
        print('1° Camarões')
        if saldoBrasil > saldoSuica:
            print('2º Brasil')
        elif saldoSuica > saldoBrasil:
            print('2º Suíça')
        elif saldoSuica == saldoBrasil:
            if golMarcadoSuica > golMarcadoBrasil:
                print('2º Suíça')
            else:
                print('2º Brasil')

elif pontosServia == pontosSuica and pontosServia == pontosCamaroes:
    if saldoServia > saldoSuica and saldoServia> saldoCamaroes:
        print('1° Sérvia')
        if saldoSuica > saldoCamaroes:
            print('2º Suíça')
        elif saldoCamaroes > saldoSuica:
            print('2º Camarões')
        elif saldoCamaroes == saldoSuica:
            if golMarcadoCamaroes > golMarcadoSuica:
                print('2º Suíça')
            elif golMarcadoSuica > golMarcadoCamaroes:
                print('2º Camarões')

    elif saldoSuica > saldoServia and saldoSuica > saldoCamaroes:
        print('1° Suíça')
        if saldoServia > saldoCamaroes:
            print('2º Sérvia')
        elif saldoCamaroes > saldoServia:
            print('2º Camarões')
        elif saldoCamaroes == saldoServia:
            if golMarcadoCamaroes > golMarcadoServia:
                print('2º Camarões')
            else:
                print('2º Sérvia')

    elif saldoCamaroes > saldoServia and saldoCamaroes > saldoSuica:
        print('1° Camarões')
        if saldoServia > saldoSuica:
            print('2º Sérvia')
        elif saldoSuica > saldoServia:
            print('2º Suíça')
        elif saldoServia == saldoSuica:
            if golMarcadoServia > golMarcadoSuica:
                print('2º Sérvia')
            else:
                print('2º Suíça')
    