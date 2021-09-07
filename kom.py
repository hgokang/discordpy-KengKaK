import json
from discord.ext import commands
import random



class KOM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name = 'คำคมadd',brief="เพิ่มคำคม", help="พิม+คำคม add [คำคม]")
    async def คำคมadd(self, ctx, *,kom):
        with open('.\\database\\kom.json', 'r') as file:
                    data = json.load(file)
                    new_kom = kom
                    await ctx.send(f"เพิ่ม{kom}ในlistแล้ว")
                    
        if new_kom in data:
            
            await ctx.send("มีคำคมนั้นแล้ว")
            
        else:
            data[new_kom] = new_kom
            with open('.\\database\\kom.json', 'w') as new_kom_data:
                json.dump(data, new_kom_data, indent=4)
                
    @commands.command(name = 'คำคม',brief="สุ่มคำคม", help="พิม+คำคม เพื่อสุ่มคำคม")
    async def คำคม(self, ctx):
        with open('.\\database\\kom.json', 'r') as file:
                    data = json.load(file)
                    
        word = random.choice(list(data.values()))
                    
                    
        await ctx.send(f"{word}")
        


def setup(bot):
    bot.add_cog(KOM(bot))
                


