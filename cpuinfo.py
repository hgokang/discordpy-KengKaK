from discord.ext import commands
from discord.utils import get
import discord
import psutil
###
# Basic cog for cpu monitoring and static server information
###
class cpu(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name = 'serverinfo',brief="status botserver", help="พิม+serverinfo เพื่อดูram server")
    async def server_info(self, ctx):
        embed = discord.Embed(color=discord.Color.blurple())
        embed.title = 'Server Information'
        data = ""
        data += str(psutil.cpu_count()) + " total threads \n"
        data += f"{psutil.virtual_memory().total / 2**30:.2f}" + " GB Total Memory \n"
        data += f"{psutil.virtual_memory().used / 2**30:.2f}" + "GB Usage \n"
        data += f"{psutil.virtual_memory().available / 2**30:.2f}" + " GB Available Currently \n"
        embed.description = data
        await ctx.channel.send(embed=embed)

    @commands.command(name = 'cpu',brief="ดูการทำงานcpu botserver", help="พิม+cpuเพื่อดูpercentการใช้งานcpuของserver")
    async def cpu_info(self, ctx):
        embed = discord.Embed(color=discord.Color.blurple())
        embed.title = 'CPU Information'
        embed.description = str(psutil.cpu_percent(interval=1)) + "% CPU Usage \n"
        # embed.description += str(psutil.sensors_temperatures(fahrenheit=False)["k10temp"][0][1]) + " C \n" Manjaro version
        embed.description += str(psutil.getloadavg()[1]) + "ค่าเฉลี่ยการใช้งานcpuใน5นาที"
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(cpu(bot))