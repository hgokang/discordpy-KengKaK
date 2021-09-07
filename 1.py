from datetime import datetime
from typing import Optional

from discord import Embed, Member
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands.bot import Bot
from discord.utils import get
from discord import activity
import discord

class Info(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command(name="userinfo", aliases=["ui", "mi"] , brief= "แสดงข้อมูลบุคคล", help= "พิม+userinfoเพื่อดูข้อมูลตนเองหรือพิมชื่อคนตามข้างหลังเพื่อดูข้อมูลคนอื่น")
	async def user_info(self, ctx, target: Optional[Member]):
		target = target or ctx.author

		embed = Embed(title="User information",
					  colour=target.colour,
					  timestamp=datetime.utcnow())

		embed.set_thumbnail(url=target.avatar_url)

		fields = [("ชื่อ", str(target), True),
				  ("ID", target.id, True),
				  ("Bot", target.bot, True),
				  ("Role", target.top_role.mention, True),
				  ("Status", str(target.status).title(), True),
				  ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
				  ("สร้างเมื่อ", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("เข้ามา", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
				  ("Boosted", bool(target.premium_since), True)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed=embed)

	@commands.command(name="dev")
	@commands.is_owner()
	async def dev(self, ctx, *,command):
		command = self.bot.get_command(command)
		
		if command is None:
			await ctx.send("ไม่เจอคำสั่ง")

		elif ctx.command == command:
			await ctx.send("ไม่สามารถปิดคำสั่งนี้ได้")

		else:
			command.enable = not command.enabled
			ternary = "เปิด" if command.enabled else "ปิด"
			await ctx.send(f"ได้ {ternary} คำสั่ง {command.qualified_name}")
			
    
def setup(bot):
	    bot.add_cog(Info(bot))