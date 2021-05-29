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
        if str(payload.emoji) == jdata['emoji_club']:              
            guild = self.bot.get_guild(payload.giuild_id)            #取得當前所在伺服器          
            role = guild.get_role(['new role'])                      #取得伺服器內指定身分組
            await payload.member.add_roles(role)                           #給予該成員身分組
           
        
        

def setup(bot):
  bot.add_cog(Reaction(bot))

