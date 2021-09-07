from discord.ext import commands
import requests
from discord import Embed
from requests.sessions import SessionRedirectMixin




#source = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
#stat = source.json()[0]
#print(stat["new_case"])

class covidstat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="covid")
    async def covid(self, ctx):
        
        source = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
        stat = source.json()[0]
        
        Today = stat["txn_date"]
        New = stat["new_case"]
        All = stat["total_case"]
        excludeabroad = stat["new_case_excludeabroad"]
        Allexcludeabroad = stat["total_case_excludeabroad"]
        update = stat["update_date"]
        
        if New > 10000:
            X = 0x801b01
        elif 5000 < New < 8000:
            X = 0xff9900
        else:
            X = 0x9cffcf
            
        embed = Embed(title=f"สถานการณ์ Covid 19 วันที่{Today}", colour= (X) )
        
        embed.set_thumbnail(url="https://images.squarespace-cdn.com/content/v1/54f58e94e4b08c831d4161f4/1584392475798-RE3O586Q17VIHDV7G939/image-asset.png")
        
        embed.add_field(name="ติดเชื้อใหม่", value=New)
        embed.add_field(name="ติดเชื้อสะสม", value=All)
        embed.add_field(name="ติดเชื้อในประเทศ", value=excludeabroad)
        embed.add_field(name="ติดเชื้อในประเทศสะสม", value=Allexcludeabroad)
        embed.add_field(name="ผลของวันที่", value=update)
        await ctx.channel.send(embed=embed)





def setup(bot):
	    bot.add_cog(covidstat(bot))