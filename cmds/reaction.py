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
      if payload.message_id== jdata['messageID']:                    #使用者新增反映的訊息
        if str(payload.emoji) == jdata['emoji_club']:                #判斷emoji
            guild = self.bot.get_guild(payload.giuild_id)            #取得當前所在伺服器          
            role = guild.get_role(['new role'])                      #取得伺服器內指定身分組
            await payload.member.add_roles(role)                     #給予該成員身分組
            await payload.member.send(f'你取得了 {role} 身分組')
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):                    
        if str(payload.emoji) == jdata['emoji_club']:              
            guild = self.bot.get_guild(payload.giuild_id)            #取得當前所在伺服器
            user = guild.get_member(payload.user_id)                 #設定user變數
            role = guild.get_role(['new role'])                      #取得伺服器內指定身分組
            await user.remove_roles(role)                            #移除該成員身分組
            await payload.user.send(f'你被移除了 {role} 身分組')
           
def setup(bot):
  bot.add_cog(Reaction(bot))

