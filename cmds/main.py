import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core import check
import json
import os, random

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

class Main(Cog_Extension):

	'''
	等待使用者回覆檢查 (需要時複製使用)
	async def user_respone():
		def check(m):
			return m.author == ctx.author and m.channel == ctx.channel
		respone = await self.bot.wait_for('message', check=check)
		return respone

	respone_msg = await user_respone
	'''
	

	@commands.command()
	async def ping(self, ctx):
		'''Bot 延遲'''
		await ctx.send(f'{round(self.bot.latency*1000)} ms')


	@commands.command()
	@check.valid_user() #檢查權限, 是否存在於效人員清單中, 否則無法使用指令
	async def test(self, ctx):
		'''有效人員 指令權限測試'''
		await ctx.send('Bee! Bo!')
		

	@commands.command()
	async def sayd(self, ctx, *, content: str):
		'''訊息覆誦'''
		if "@everyone" in content:
			await ctx.send(f"{ctx.author.mention} 請勿標註 `everyone` !")
			return
		else: await ctx.message.delete()
		await ctx.send(content)
	
	@commands.command()
	async def meme(self, msg):
		if msg.channel == jdata['meme_channel']:
			meme_pic = random.choice(jdata['meme_pic'])
			await msg.channel.send(meme_pic)
	
	@commands.group()
	async def info(self, ctx):
		pass
	
	@info.command()		#顏色black #value="內容"
	async def botinfo(self, ctx):
		random_color = random.choice in jdata['color_list']
		embed = discord.Embed(title="機器人的資訊", description="NTUCYCBOT", color=random_color)
		embed.set_thumbnail(url=jdata['club_pic'])
		embed.add_field(name="開發者 Developers", value="儒用#6595", inline=False)
		embed.add_field(name="Powered by", value="discord.py v{}".format(discord.__version__), inline=True)
		embed.add_field(name="Prefix(指令前綴)", value=jdata['Prefix'], inline=False)
		embed.set_footer(text="Made with 儒用❤")
		await ctx.send(embed=embed)
	
	@info.command()		#顏色yellow #value="內容"
	async def clubinfo(self, ctx): 
		embed = discord.Embed(title="單車社的資訊", description="NTUCYCLUB", color=int(jdata['Yellow #FFFF00_color']))
		embed.set_thumbnail(url=jdata['club_pic'])
		embed.add_field(name="社團粉絲專頁", value="[Link](https://www.facebook.com/ntucyc)", inline=False)
		embed.add_field(name="社團", value="[Link](https://www.facebook.com/groups/NTUCYCLUB)" , inline=False)
		embed.add_field(name="Powered by", value="discord.py v{}".format(discord.__version__), inline=True)
		embed.set_footer(text="Made with 儒用❤")
		await ctx.send(embed=embed)

	@info.command()		#顏色White #value="內容"
	async def schedule(self, ctx):
		embed=discord.Embed(title="行事曆", description="台大單車社一學期的活動規劃", color=int(jdata['Medium Violet Red #C20B6A_color']))
		embed.set_thumbnail(url=jdata['club_pic'])
		embed.add_field(name="80王", value="覺得自己夠80就可以領取", inline=False)
		embed.add_field(name="老人", value="覺得自己夠老就可以領取", inline=False)
		embed.set_footer(text="Made with 儒用❤")
		await ctx.send(embed=embed)

	@info.command()		#顏色Blue #value="內容或身分組適用人"
	async def roles(self, ctx):
		embed=discord.Embed(title="身分組獲取", description="尋找適合自己的身分組或信仰(可以複選歐)\n也能讓大家快速了解你喜歡的品牌", color=int(jdata['Blue #0000FF_color']))
		embed.set_thumbnail(url=jdata['club_pic'])
		embed.add_field(name="社員", value="有繳社費可以領取", inline=False)
		embed.add_field(name="老人", value="覺得自己夠老就可以領取", inline=False)
		embed.add_field(name="80王", value="覺得自己夠80就可以領取", inline=False)
		embed.add_field(name="品牌", value="點選自己喜歡的信仰品牌", inline=False)
		embed.set_footer(text="Made with 儒用❤")
		await ctx.send(embed=embed)
	
	@info.command() 	#顏色Red #value="內容或描述"
	async def rules(self, ctx):
		embed=discord.Embed(title="NTUCYCLUB伺服器規則", description="閱讀內文並遵守此伺服器的規則", color=int(jdata['Red #FF0000_color']))
		embed.set_thumbnail(url=jdata['club_pic'])
		embed.add_field(name="規則.", value=jdata['rules'], inline=False)
		embed.set_footer(text="Made with 儒用❤")
		await ctx.send(embed=embed)

	@info.command() 	#顏色green #value="內容或描述"
	async def act(self, ctx):
		embed=discord.Embed(title="NTUCYCLUB--週末活動", description="閱讀內文並遵守此活動的規範", color=int(jdata['Lime #00FF00_color']))
		embed.set_thumbnail(url=jdata['club_pic'])
		embed.add_field(name="概要縣市景點", 
		value="活動敘述", inline=False)
		embed.add_field(name="集合時間", value="110/06/18上午8:00", inline=True)
		embed.add_field(name="集合地點", value="台大正門", inline=True)
		embed.add_field(name="難度", value=" ★☆☆☆☆  ", inline=True)    #一星難度
		embed.add_field(name="路線", value="[路線連結](路線連結)", inline=True)
		embed.add_field(name="里程", value="(km)", inline=True)
		embed.add_field(name="爬升", value="(m)", inline=True)
		embed.add_field(name="主辦", value="[主辦姓名](主辦fb連結)（主辦電話）", inline=True)
		embed.add_field(name="協辦", value="[協辦姓名](協辦fb連結)（協辦電話）", inline=True)
		embed.add_field(name="注意事項", value=jdata['act_rules'], inline=False)
		embed.add_field(name="報名表單", value="[報名表單](表單連結)", inline=False)
		await ctx.send(embed=embed)
	
	@info.command() 	#顏色random #value="內容或描述"
	async def Bact(self, ctx):
		embed=discord.Embed(title="NTUCYCLUB--大 活 動", description="閱讀內文並遵守此活動的規範", color=int(jdata['Chartreuse Yellow #D5EB0D_color']))
		embed.set_thumbnail(url=jdata['club_pic'])
		embed.add_field(name="概要縣市景點", 
		value="活動敘述", inline=False)
		embed.add_field(name="集合時間", value="110/06/18上午8:00", inline=True)
		embed.add_field(name="集合地點", value="台大正門", inline=True)
		embed.add_field(name="難度", value=" ★☆☆☆☆  ", inline=True)    #一星難度
		embed.add_field(name="路線", value="[路線連結](路線連結)", inline=True)
		embed.add_field(name="里程", value="(km)", inline=True)
		embed.add_field(name="爬升", value="(m)", inline=True)
		embed.add_field(name="主辦", value="[主辦姓名](主辦fb連結)（主辦電話）", inline=True)
		embed.add_field(name="協辦", value="[協辦姓名](協辦fb連結)（協辦電話）", inline=True)
		embed.add_field(name="注意事項", value=jdata['act_rules'], inline=False)
		embed.add_field(name="報名表單", value="[報名表單](表單連結)", inline=False)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Main(bot))
