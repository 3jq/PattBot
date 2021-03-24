import discord
import time
import asyncio
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix="$")
current_time = int(0)
time_limit = int(30)
check_for_roles_time = int(30)
roles = ['allperms', 'banperms', 'kickperms']

client.remove_command('help')


@client.event
async def on_ready():
    print('BOT connected in as {0.user}. Good luck with using it.'.format(client))


# Kick command (Anti-nuke)
@client.command(pass_context=True)
@commands.has_any_role('kickperms', 'allperms')
async def kick(ctx, member: discord.Member, *, reason=None):
    new_time = time.time()
    if kick.current_time == 0:
        time_diff = time_limit + 1
    else:
        time_diff = new_time - kick.current_time

    kick.current_time = new_time
    if time_diff < time_limit:
        await ctx.send('Do not try to nuke server. The delay reloaded.')
        return
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)

    kick.current_time = 0


# Ban command (Anti-Nuke)
@client.command(pass_context=True)
@commands.has_any_role('banperms', 'allperms')
async def ban(ctx, member: discord.Member, *, reason=None):
    new_time = time.time()
    if ban.current_time == 0:
        time_diff = time_limit + 1
    else:
        time_diff = new_time - ban.current_time

    ban.current_time = new_time
    if time_diff < time_limit:
        await ctx.send('Do not try to nuke server. The delay reloaded.')
        return
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    await ctx.send(f'Successfully banned user {member.mention}.')


ban.current_time = 0


# Info command
@client.command(pass_context=True)
async def info(ctx):
    await ctx.send(f'Hi! I am a bot "Patt", my developer created me for safe moderation in discord servers.')
    time.sleep(3)
    await client.change_presence(status=discord.Status.online, activity=discord.Game('$help'))



# Auto-Creating Roles
@client.event
async def on_guild_join(guild):
    for role in roles:
        if not get(guild.roles, name=role):
            await guild.create_role(name=role)
        print(f'Role created: {role}')

"""
    client.loop.create_task(check_for_roles(guild))


async def check_for_roles(guild):
    while True:
        for role in roles:
            if not get(guild.roles, name=role):
                await guild.create_role(name=role)
        await asyncio.sleep(check_for_roles_time)
"""



# Join message
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hey, owners! I hope you see that message. Please, do not delete roles "allperms", '
                               '"banperms" and "kickperms". I hope you will enjoy using me! If you find any bug or '
                               'wanna add any feature: https://github.com/depression2k/PattBot')
        break


# Help message
@client.command(pass_context=True)
async def help(ctx, *args):
    embStr = ("""```\n\nHey! There are my commands: \n\n$ban (Only for admins); \n\n$kick (Only for admins); 
    \n\n$info; \n\n$help; \n\nMy github page: 
    github.com/depression2k/PattBot \n\nMy developer: 
    discord.bio/p/urdepression```""")
    embed = discord.Embed(title="Some info.", colour=discord.Colour.green())
    embed.add_field(name="Do you want to be able to write the same messages? Buy Premium!", value=embStr)
    await ctx.send(embed=embed)

    time.sleep(3)


client.run('ur token there')
