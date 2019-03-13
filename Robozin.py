import discord
import asyncio
import random
import os

cliente_discord = discord.Client()


palavroes = ["viado", "puta", "filho da puta","boi", "gay", "caralho", "corno", "sapatão", "bobo",
             "bocó", "inútil","babaca","otário","otario","besta","idiota","filho da egua","imundo",
             "imundiça","viadinho","viadão","tosco","babão","bundinha","bundão","tralha","bolsominion","priranha",]#array de palavões

digitos = ["1","2","3","4","5","6","7","8","9","0","#"]

@cliente_discord.event
async def on_ready():
    print('LIGOU')

@cliente_discord.event
async def on_message(texto):
    texto.content.startswith("")
    frase = texto.content
    
    if(texto.author.id == '550749213709828096'): return
    if texto.content.startswith('Robozin'):#se uma frase começar com 'Robozin'
        frase = texto.content[7:].strip()#remove 'Robozin'
        if frase.lower().startswith('dado'):#se uma frase começar com 'dado'
            num = random.randint(1,6)#sorteia um número de 1 até 6
            await cliente_discord.send_message(texto.channel, str(num))#escreve o número na tela do discord
            return
        if frase.endswith('?'):# se uma fraze começar com 'Robozin' e terminar com '?', ele vai responder uma frase aleatória no arrei a baixo
            resposta = random.choice(['Não respondo a isso','Sim','As vezes','Não','Claro','NUNCA!','Um dia talvez','A resposta está dentro de ti','Mais ou menos','Uma Bosta','Podia ser pior'])
            await cliente_discord.send_message(texto.channel,resposta)
            return

    for i in palavroes:
        if i in frase:
            if "leo" in frase:
                resposta = "RESPEITE MEU CRIADOR!!!"
                await cliente_discord.send_message(texto.channel,resposta)
                return

    for i in palavroes:#Este bloco irá tratar palavrões
        if i in frase:
            autorTotal = str(texto.author)#captura o nome de quem digitou
            autor = ""
            for j in autorTotal:#este bloco 'for' é para tirar os dígitos do nome de quem digitou
                if j not in digitos:
                    autor += j            
            resposta = autor+", olha a boca, não permitimos esse linguajar aqui!\n"  
            await cliente_discord.send_message(texto.channel,resposta)
            
    


cliente_discord.run('NTUwNzQ5MjEzNzA5ODI4MDk2.D1rGfw.-jCJSPTVubEsybhLIdLlUEFTQkw')
