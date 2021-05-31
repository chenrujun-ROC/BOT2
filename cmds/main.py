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
	async def info(self, ctx):
		embed = discord.Embed(title="奴工的個人資訊", description="NTUCYCBOT!", color=0x00ffff)
		# embed.set_thumbnail(url="#")
		embed.add_field(name="開發者 Developers", value="儒用#6595 (<@![Owner_id]>)", inline=False)
		embed.add_field(name="社團粉絲專頁", value="[Link](https://www.facebook.com/ntucyc)", inline=False)
		embed.add_field(name="社團", value="[Link](https://www.facebook.com/groups/NTUCYCLUB)" , inline=False)
		embed.add_field(name="版本 Version", value="0.1.0 a", inline=False)
		embed.add_field(name="Powered by", value="discord.py v{}".format(discord.__version__), inline=True)
		embed.add_field(name="Prefix", value=jdata['Prefix'], inline=False)
		embed.set_footer(text="Made with 儒用❤")
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Main(bot))
