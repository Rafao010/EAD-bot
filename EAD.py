import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

frases = ['Lute como nunca, perca como sempre', 'É só um dia ruim, amanhã vai ser pior',
          'Se alguem te ofendeu sem você merecer, volte lá, e mereça', 'Sem lutas não há derrotas',
          'O não você ja tem, agora vá buscar a decepção', 'A maior derrota é achar que é capaz,',
          'Você não pode mudar o seu passado, mas pode arruinar o seu futuro', 'Nunca é tarde pra desistir',
          'O caminho é longo, mas a derrota é certa', 'Não sabendo que era impossivel, fui lá e soube',
          'A melhor parte do sonho é quando percebemos que é impossivel realiza-lo',
          'Seja o protagonista do seu fracasso', 'A vida é um conto de falhas', 'Só dará errado se você tentar',
          'Não deixe ninguem estragar o seu dia, estrague você mesmo']

autores = ['Jade Picon', 'Jair Bolsonaro', 'Cabo Daciolo', 'Juliette', 'Mao Tse Tung', 'Donald Trump', 'Dilma Rousef',
           'Monkey D. Luffy', 'Mark Zukenberg', 'Albert Einstein', 'Getúlio Vargas', 'Lukinhas', 'Vitor Kim',
           'Papai Noel']

ja_tem_sala = list()


@bot.event
async def on_ready():
    print('estou pronto')


@bot.event
async def on_member_join(member):
    canal_boas_vindas = bot.get_channel(889567326184304722)
    canal_de_regras = bot.get_channel(935254519221194793)

    mensagens = [f'Opaa!! Eai {member.mention}! Dá uma olhado no {canal_de_regras.mention} pra conferir as regras do '
                 f'nosso magnifico servidor!!', f'Eai meu querido {member.mention}!!! Seja bem vindo, e não esqueça de '
                                                f'olhar o {canal_de_regras.mention}'
                 f' para entender as regras do servidor!',
                 f'Bem vindo {member.mention}!! Confira as regras em {canal_de_regras.mention}',
                 f'Olha só quem apareceu aqui, se não é o {member.mention}!!! Dá uma conferida no '
                 f'{canal_de_regras.mention} pra ver as regras servidor', f'Salve {member.mention}!!! Dá uma passada'
                                                                          f' no {canal_de_regras.mention} pra ver as '
                                                                          f'regras do nosso lindo servidor']

    await canal_boas_vindas.send(random.choice(mensagens))


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    if 'lukinhas' in message.content:
        await message.channel.send(f'Lukinhas é uma lenda, use esse nome com cuidado {message.author.name}')

    if 'cavalo' in message.content:
        await message.channel.send('CAVALOOOO')

    with open('RA.txt', 'r') as ra_arquivo:

        RA = ra_arquivo.readlines()

        for linha in RA:
            if message.content == linha:
                canal_pessoas_liberadas = bot.get_channel(949829444229558282)
                await canal_pessoas_liberadas.send(f'O {message.author} está liberado!')

    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):

    if user not in ja_tem_sala:
        if reaction.emoji == '🇦':
            role = user.guild.get_role(935351766382432286)
            await user.add_roles(role)
            ja_tem_sala.append(user)

        elif reaction.emoji == '🇧':
            role = user.guild.get_role(935352237021093898)
            await user.add_roles(role)
            ja_tem_sala.append(user)

        elif reaction.emoji == '🇨':
            role = user.guild.get_role(935352385470103602)
            await user.add_roles(role)
            ja_tem_sala.append(user)

        elif reaction.emoji == '🇩':
            role = user.guild.get_role(935352449567424553)
            await user.add_roles(role)
            ja_tem_sala.append(user)

        elif reaction.emoji == '🇪':
            role = user.guild.get_role(935352502218547252)
            await user.add_roles(role)
            ja_tem_sala.append(user)

        elif reaction.emoji == '🇫':
            role = user.guild.get_role(935352554714460160)
            await user.add_roles(role)
            ja_tem_sala.append(user)

        elif reaction.emoji == '🇬':
            role = user.guild.get_role(935352710507671582)
            await user.add_roles(role)
            ja_tem_sala.append(user)

        elif reaction.emoji == '🇭':
            role = user.guild.get_role(935352775309676544)
            await user.add_roles(role)
            ja_tem_sala.append(user)

    else:
        if reaction.emoji == '❌':

            role = user.guild.get_role(935351766382432286)
            await user.remove_roles(role)

            role = user.guild.get_role(935352237021093898)
            await user.remove_roles(role)

            role = user.guild.get_role(935352385470103602)
            await user.remove_roles(role)

            role = user.guild.get_role(935352449567424553)
            await user.remove_roles(role)

            role = user.guild.get_role(935352502218547252)
            await user.remove_roles(role)

            role = user.guild.get_role(935352554714460160)
            await user.remove_roles(role)

            role = user.guild.get_role(935352710507671582)
            await user.remove_roles(role)

            role = user.guild.get_role(935352775309676544)
            await user.remove_roles(role)

            ja_tem_sala.remove(user)


@bot.command(name='728365787127087127')
async def send_reaction_embed(ctx):

    embed = discord.Embed(title='Salas', description='Reaja essa mensagem com a sua sala! Caso você tenha miopia, e '
                                                     'acabe clicando na letra errada, clique no ❌ para ressetar sua '
                                                     'sala',
                          colour=discord.Colour.dark_orange())
    await ctx.send(embed=embed)


@bot.command(name='salve')
async def send_hello(ctx):
    name = ctx.author.name
    responce = f'Salve {name}'
    await ctx.send(responce)


@bot.command(name='calendario')
async def send_calendario(ctx):
    '''responce = f'Ainda não estamos em semana de provas, agradeça {ctx.author.name}!!!'
    await ctx.send(responce)'''

    embed = discord.Embed(title='Calendário de provas', description='Dia 1 - Mat, Geo, Socio\nDia 2 - Bio, Hist, Filo'
                                                                    '\nDia 3 - Quim, LP\nDia 4 - Física, Inglês',
                          colour=discord.Colour.dark_gold())
    await ctx.send(embed=embed)


@bot.command(name='motivação')
async def send_motivation(ctx):
    await ctx.send(f'{frases[random.randint(0, len(frases))]}\n     -{autores[random.randint(0, len(autores))]}')


@bot.command(name='intro')
async def send_intro(ctx):
    await ctx.send('Salve, eu sou o Bot EAD, um bot programado pelo @Rafão#6162 exclusivo desse servidor!!!'
                   'Eu tenho vários comandos, para ve-los, digite !comandos. Se você tiver alguma ideia de comando'
                   'para ser adicionado no meu código, mande uma mensagem para o rafão, explicando a sua ideia,'
                   ' para que '
                   'seja adicionada no codigo! ')


@bot.command(name='codigo')
async def send_code(ctx):
    embed = discord.Embed(title='Código versão 2.0', description='https://drive.google.com/file/d/1VvJKY7podEJ2xYc3akt'
                                                                 'xIIRjnFRhLoBD/view?usp=sharing',
                          colour=discord.Colour.blue())
    await ctx.send(embed=embed)


@bot.command(name='ajuda')
async def send_help(ctx):

    regras = bot.get_channel(935254519221194793)
    geral = bot.get_channel(855108335770533961)
    comandos = bot.get_channel(894012397260529705)
    comunicados = bot.get_channel(934980328207036477)

    embed = discord.Embed(
        title='Ajuda',
        description=f'Eai {ctx.author.name}, aqui vou te passar algumas dicas basicas sobre o servidor,'
                    f' caso depois de ler tudo você ainda tiver duvida, manda sua duvida para um ADM :) \n\n'
                    f'Cargos - Aqui temos cargos para definir a sala na qual cada um está na escola.'
                    f'Fora isso temos 3 cargos principais, sendo eles: Hashiras, Caçadores, Novatos. Cada um tem um'
                    f' nível de acesso ao servidor diferente. Caso queira uma promoção, explique o motivo para um '
                    f'ADM\n\n'
                    f'Canais - Nos temos o canal de {regras.mention},'
                    f' onde você pode conferir todas as regras do servidor\n'
                    f'Obviamente temos o canal para conversas, que é o {geral.mention}, ali você pode conversar sobre '
                    f'assuntos da escola, e que não são da escola\n'
                    f'Tambem temos um canal para usar {comandos.mention}, que pode ser os comandos da Loritta'
                    f', do Carlinhos, do Tiket, ou é claro, meus comandos\n'
                    f'E para facilitar a nossa vida, temos um chat de {comunicados.mention}, para que agente não perca '
                    f'os comunicados importantes da escola\n\n Fora tudo isso, temos uma pasta onde colocamos os '
                    f'MELHORES videos que existem de cada materia!! Sério, isso ajuda muito! (Principalmente em '
                    f'matematica ksksksk)\nE só pra fechar com chave de ouro, temos uma outra pasta, onde tem vários '
                    f'prints de anotações, pdfs, e dos momentos mais importantes dos videos!\n'
                    f'\n {ctx.author.name}, espero que eu tenha esclarecido suas duvidas, se não, use o canal do meu '
                    f'amigo tiket.mention, duvidas.mention para que suas duvidas sejam totalmente esclarecidas '
                    f'(só não vale perguntar coisa de matéria, se não me complica kkkkkkkk',

        colour=discord.Colour.green()
    )
    await ctx.send(embed=embed)


@bot.command(name='comandos')
async def send_commands(ctx):
    embed = discord.Embed(title='Código versão 1.0', description='Essa é a lista de comandos\n\n!salve\n!calendario'
                                                                 '\n!motivação\n!intro\n!codigo\n!ajuda\n!comandos',
                          colour=discord.Colour.red())
    await ctx.send(embed=embed)

TOKEN = os.getenv('TOKEN_SECRETO')
bot.run(TOKEN)
