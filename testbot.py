import discord
from discord.ext import commands
import random
import sys
import asyncio

description = '''An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='!', description=description)

def random_emoji():
    r = random.randint(1,2384)
    try:
        with open('emojinumcodes') as f:
            for i, line in enumerate(f):
                if i==r:
                    hxcode = list(map(lambda x: chr(int(x, 16)), line.strip().split(',')))
                    hxcode = ''.join(hxcode)
                    print(hxcode, line)
                    break
    except FileNotFoundError:
        print('emojinumcodes file not found')
    return hxcode

@bot.listen()
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.listen()
async def on_message(message):
    #we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!Hello'):
        var = '{0.author.nick}'.format(message) if message.author.nick else '{0.author.name}'.format(message)
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)
"""
@bot.event
async def on_message2(message):
    if message.content.startswith('!editme'):
        msg = await bot.send_message(message.author, '10')
        await asyncio.sleep(3)
        await bot.edit_message(msg, '40')
"""

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together"""
    await bot.say(left + right)

@bot.command()
async def repeat(times : int, content = 'repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def roll(dice : str):
    """Rolls dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command()
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command(pass_context=True)
async def msginfo(ctx):
    m1=bot.messages[-1]
    m2=bot.messages[-2]
    m3=bot.messages[-3]
    print('bot.messages[-1] content: {0}'.format(m1.content))
    print('bot.messages[-2] content: {0}'.format(m2.content))
    print('bot.messages[-3] content: {0}'.format(m3.content))

@bot.command(pass_context=True)
async def echo(ctx, txt:str=''):
    a = chr(0x1F487)
    b = chr(0x0200D)
    c = chr(0x02642)
    d = chr(0x0FE0F)
     
    await bot.say(a)
    await bot.say(''.join((a,b)))
    await bot.say(''.join((a,b,c)))
    await bot.say(''.join((a,b,c,d)))

@bot.command(pass_context=True)
async def rreact(ctx):
    target = bot.messages[-2]
    await bot.delete_message(bot.messages[-1])
    await bot.add_reaction(target, random_emoji())
    await bot.add_reaction(target, random_emoji())

@bot.command(pass_context=True)
async def specreact(ctx, emoj:str):
    target = bot.messages[-2]
    await bot.delete_message(bot.messages[-1])
    await bot.add_reaction(target, emoj)

@bot.command()
async def remoji():
    rem = random_emoji()
    await bot.say(rem)

@bot.command(pass_context=True)
async def polltst(ctx, *polargs : str):
    """Polltst function w/o group"""
    print('polltst')
    await bot.say('polltst')
    asker = '{0.author.nick}'.format(ctx.message) if ctx.message.author.nick else '{0.author.name}'.format(ctx.message)
    #cntntr = '{0.content}'.format(ctx.message)
    #cmd = ctx.command.clean_params
    tmp = ' '.join(polargs)
    arg = list(map(lambda s: s.strip(" "), tmp.split(",")))
    title = arg.pop(0)
    opts = list(arg[0:])
    msg = 'Hey , {0} has made a new poll\n\n{1}'.format(asker, title)
    #msg = 'Hey @everyone, {0} has made a new poll\n\n{1}'.format(asker, title)    
    await bot.say(msg) 

@bot.group(pass_context=True)
async def poll(ctx):
    """Poll function group"""
    global asker
    await bot.say('Poll goes here')
    if ctx.invoked_subcommand is close:
        print('Gonna close')
    elif ctx.invoked_subcommand is check:
        print('Gonna check')
    elif ctx.invoked_subcommand is start:
        print('Gonna open')
        asker = '{0.author.nick}'.format(ctx.message) if ctx.message.author.nick else '{0.author.name}'.format(ctx.message)
    else:
        print('Invalid subcommand')


@poll.command()
async def start(polargs : str):
    global title
    global opts
    print('Poll opened')
    await bot.say('Poll opened')
    #cntntr = '{0.content}'.format(ctx.message)
    #cmd = ctx.command.clean_params
    arg = list(map(lambda s: s.strip(" "), polargs.split(",")))
    title = arg.pop(0)
    opts = {}
    opts = opts.fromkeys(arg[0:],0)
    msg = 'Hey @everyone, {0} has made a new poll\n\n{1}'.format(asker, title)    
    await bot.say(msg)
    
    #await bot.say(list(cmd.values()))

@poll.command()
async def check():
    await bot.say('Checking poll')
    await bot.say(asker)

@poll.command()
async def close():
    await bot.say('Closing poll')
    await bot.say(asker)




#    tst = 'When can people watch a movie?, Mon, Tue, Wed, Thr, Fri, Sat, Sun'

#    for a in range(len(tst)):
#        print("{0} \t{1}".format(a, tst[a]))

#    print(tst[-1])
#    p = {}
#    p=p.fromkeys(tst[1:], 0)
#    p['Question']=tst[0]


    #await bot.say(ctx.message.)
    #asker = '{0.author.nick}'.format(message) if message.author.nick else '{0.author.name}'.format(message)
    #msg = 'Hey {}, {0.author.nick} has made a poll'.format(message)    
bot.run('MzI1NzE0OTQ2OTE2ODc2Mjg4.DCci9A.zZAe3yu8IxiboUtTAnYYq206XSg')
