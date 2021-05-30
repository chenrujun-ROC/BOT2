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
      if payload.message_id == jdata['messageID']:                   #使用者新增反映的限定訊息
        if str(payload.emoji) == jdata['trek_emoji']:                #判斷emoji
            guild = self.bot.get_guild(payload.guild_id)             #取得當前事件所在伺服器          
            role = guild.get_role(jdata['test_role'])                #取得伺服器內指定身分組
            await payload.member.add_roles(role)                     #給予該成員身分組
            await payload.member.send(f'你取得了 {role} 身分組')      #pm成員已被加入'test_role'身分組
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):                    
        if str(payload.emoji) == jdata['trek_emoji']:                #判斷emoji
            guild = self.bot.get_guild(payload.guild_id)             #取得當前事件所在伺服器
            user = await guild.fetch_member(payload.user_id)         #設定user變數
            role = guild.get_role(jdata['test_role'])                #取得伺服器內指定身分組
            await user.remove_roles(role)                            #移除該成員身分組                        
            await user.send(f'你被移除了 {role} 身分組')              #pm成員已被從'test_role'身分組移除
           
def setup(bot):
  bot.add_cog(Reaction(bot))

