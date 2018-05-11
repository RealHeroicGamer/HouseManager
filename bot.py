import discord
from discord.ext import commands
 
TOKEN = 'Bot token cant be revealed. It is private.'
 
description = '''The bot for the Wii Hacking House, made by @RealHeroicGamer.'''
bot = commands.Bot(command_prefix='wii-', description=description)
 
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
 
@bot.event
async def on_message(message):
    if str(message.author.name).lower() != 'House Manager':
        if message.content.startswith('wii-ping'):
            await bot.send_message(message.channel, "Pong!")
        if message.content.startswith('wii-help'):
            await bot.send_message(message.channel, "Hi there! I'm the House Manager bot for the Wii Hacking House made by RealHeroicGamer. Here's a list of my commands that you can use!\u2424wii-ping: Pong!\u2424wii-help: Displays this message\u2424That's all I can do for right now, but more commands will be added soon!")
        if message.content.startswith('wii-purge'):
            async def clear(self, ctx: commands.Context, number: int, member: discord.Member = None) -> None:
                if number < 1:
                    await command_error(ctx, "You must attempt to purge at least 1 message!")
                    return

                def predicate(msg: discord.Message) -> bool:
                    return msg == ctx.message or member is None or msg.author == member

                if number <= 100:
                    #  Add 1 to limit to include command message, subtract 1 from the return to not count it.
                    msgs = await self.bot.purge_from(ctx.message.channel, limit=number + 1, check=predicate)
                    send(self.bot, '{} message{} cleared.'.format(len(msgs) - 1, "s" if len(msgs) - 1 != 1 else ""),
                         ctx.message.channel, True)
                else:
                    await command_error(ctx, 'Cannot delete more than 100 messages at a time.')
#(iyenal)I particularly dislike Python, but let's say that I do that for the server ;)
        if message.content.startswith('wii-issue'):
            await bot.send_message(message.channel, "Issue manager, please use add to submit a new one or check to check them.")

@bot.command()
async def hello(ctx):
    embed = discord.Embed(title="Hello ! I am the The Wii Hacking House Bot", description="I am hoping to bring a lot of features for this server!", color=0x57ccee)    
    embed.add_field(name="TWHH Members", value="42") #Hardcoded currently, but who cares
    embed.add_field(name="TWHH Invite", value="https://discord.gg/pXdeUqb")
    await ctx.send(embed=embed)

bot.run(TOKEN)
