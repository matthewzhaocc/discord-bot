import discord
import time
import datetime
from random import randint
TOKEN = 'NTc5MTU4NjM3OTI3MzMzODk4.XN-How.8Sj4yBuS6JGqLmN0Q6i6txNMyyI'
client = discord.Client()
file = open('nsfw-keywords.txt', 'r')
raw_data = file.read()
str = ''
nsfw=[]
for i in raw_data:
    if i != ',':
        str+=i
    else:
        nsfw.append(str)
        str=''
print(nsfw)

nsfw_filter = True
startTime = time.time()
@client.event
async def on_message(message):
    global nsfw_filter
    guild = message.guild
    if message.author == client.user:
        return

    if message.content.startswith('!construct-url'):
        await message.channel.send('https://'+message.content[15:]+'/')
    if message.content.startswith('!'):
        f = open('log.txt','a')
        f.write('\n'+message.content)
        f.close()
    #nsfw protection
    if message.channel != 'nsfw-chat' or message.channel != 'nsfw-pics':
        if nsfw_filter:
            for i in nsfw:
                if i in message.content.lower():
                    await message.channel.send('mate, dont be naughty')
                    await message.delete()
                    break
    #help
    if message.content.lower() == '!help':
        if '@administator' in [x.name.lower() for x in message.author.roles]:
            await message.channel.send('.!tag all \n !test \n !test \n !reddit \n !warning \n !bot-timeout \n !kick \n !ban \n !scare-em')
            return
        if '@moderator' in [x.name.lower() for x in message.author.roles]:
            await message.channel.send('.!tag all \n !test \n !test \n !reddit \n !warning')
            return
        await message.channel.send('.!tag all \n !test \n !test \n !reddit')
        return

#regular user
    if message.content.startswith('!current-time'):
        await message.channel.send('the current time in pleasanton is '+str(datetime.datetime.now()))

    if message.content.startswith('!urban'):
        await message.channel.send('https://www.urbandictionary.com/define.php?term='+message.content[7:])

    if message.content.lower() == '!tag all':
        await message.channel.send('@everyone')

    if message.content.lower() == '!test':
        await message.channel.send('test success')
        print(message.author)
    if message.content.startswith('!reddit'):
        await message.channel.send('https://www.reddit.com/r/'+message.content[8:])

    if message.content.startswith('!8ball'):
        choice = randint(0,18)
        if choice == 0:
            await message.channel.send('It is certain.')
        if choice == 1:
            await message.channel.send('It is decidedly')
        if choice == 2:
            await message.channel.send('Without a doubt.')
        if choice == 3:
            await message.channel.send(' Yes - definitely.')
        if choice == 4:
            await message.channel.send('You may rely on it.')
        if choice == 5:
            await message.channel.send(' As I see it, yes.')
        if choice == 6:
            await message.channel.send('Most likely.')
        if choice == 7:
            await message.channel.send('Outlook good.')
        if choice == 7:
            await message.channel.send('Yes.')
        if choice == 8:
            await message.channel.send('Signs point to yes.')
        if choice == 9:
            await message.channel.send('Reply hazy, try again.')
        if choice == 10:
            await message.channel.send('Ask again later.')
        if choice == 11:
            await message.channel.send('Better not tell you now.')
        if choice == 12:
            await message.channel.send('Cannot predict now.')
        if choice == 13:
            await message.channel.send('Concentrate and ask again.')
        if choice == 14:
            await message.channel.send('Dont count on it.')
        if choice == 15:
            await message.channel.send('My reply is no.')
        if choice == 16:
            await message.channel.send('My sources say no.')
        if choice == 17:
            await message.channel.send('Outlook not so good.')
        if choice == 18:
            await message.channel.send('Very doubtful.')
    if len(message.content) >= 200:
        await message.channel.send('this message is too long please put it into pastebin')
        await message.delete()
    if message.content.startswith('!hello'):
        await message.channel.send('hello '+str(message.author)+':smile:')







    #if message.content.startswith(!)


#moderator
    if '@moderator' in [x.name.lower() for x in message.author.roles]:
        if message.content.startswith('!warning'):
            await message.channel.send('official warning: '+message.content[9:])
            await message.delete()
    print(message.channel)
    print(guild)

#administrator
    if '@administator' in [x.name.lower() for x in message.author.roles]:
        if message.content.startswith('!bot-timeout'):
            time.sleep(int(message.content[13:]))

        if message.content.startswith('!kick'):
            await guild.kick(message.mentions[0])

            #await message.channel.send('official kick: '+message.content[6:])

        if message.content.startswith('!ban'):
            await guild.ban(message.mentions[0])
            print(int(message.mentions[0].id))
            await message.channel.send('offical ban: '+ message.content[5:])

        if message.content.startswith('!scare-em'):
            await message.delete()
            for i in range(10):
                await message.channel.send('matthew is watching!')
                time.sleep(5)

        if message.content.startswith('!clear-chat'):
            pass

        if message.content.startswith('!send-pic'):
            await message.channel.send(file=discord.File('picture/'+message.content[10:]))

        if message.content.startswith('!bot-kill'):
            for i in range(10):
                #await message.channel.send('bot is killing itself, timer: '+str(i+1))
                time.sleep(1)
            await message.delete()
            raise SystemExit('bot exit by command')

        if message.content.startswith('!override-bot'):
            await message.channel.send('warning, the bot is being overiden by an administrator')
            await message.channel.send('it seems like this override is because of '+str(message.content[14:])+' and is created by '+str(message.author))
            time.sleep(1)
            await message.channel.send('matthew bot signing off for 1min')
            print('matthew bot have been overrided by '+str(message.author))
            for i in range(60):
                time.sleep(1)
                print(60-i)
            await message.channel.send('im back!')

        if message.content.startswith('!nsfw_override'):
            if nsfw_filter:
                nsfw_filter = False
                print('warning: nsfw filter is being overriden by command')
            else:
                nsfw_filter = True
                print('nsfw filter set to on')
            await message.delete()

        if message.content.startswith('!nsfw_status'):
            await message.channel.send('nsfw filter status is '+str(nsfw_filter))

        if message.content.startswith('!uptime'):
            await message.channel.send('the current uptime of matthew bot is '+str((time.time()-startTime)/60)+' minutes')

    return

@client.event
async def on_member_join(member):
    pass

@client.event
async def on_member_remove(member):
    pass


@client.event
async def on_ready():
    print('login success')

client.run(TOKEN)
