#使用者新增反映獲得身分組
#On_raw_reaction_add
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

class Reaction(Cog_Extension):
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        if payload.emoji == jdata['emoji1']:
            guild = self.bot.get_guild(payload.giuild_id)
            role = guild.get_role(['new role'])
            payload.member.add_roles(role)
           
        #2.判斷反應貼圖
        #3.給予身分組
        print(payload.emoji)
        print(payload.user)


def setup(bot):
  bot.add_cog(Reaction(bot))

