import discord
from discord import utils
from discord.ext import commands

import config

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_message(message):
    if message.content.startswith('роль'):
        channel = message.channel # Получаем канал
        member = message.author # Получаем автора сообщения
        role = utils.get(message.guild.roles, id=config.ROOKIE_ROLE) # Получаем роль по id

        await member.add_roles(role) # Бот выдает роль, человеку написавшему сообщение
        await channel.send('{.author} получает роль "Новичок"'.format(message)) # Выводим в чат сооб-е, о получении роли


bot.run(config.TOKEN)