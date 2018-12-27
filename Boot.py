import discord 
from discord.ext.commands import Bot
from discord.ext import commands 
import asyncio
import time
import urlgetter
Client = discord.Client()

client=commands.Bot(command_prefix="!")
Token="Put your Bot Token"
         
@client.event
async def on_ready():
    print("Op is ready")

    

@client.event
async def on_message(message):
        Url="https://9gag.com/gag/"
        r1=urlgetter.getUrl()
        r2=urlgetter.getUrl_Funny()
        r3=urlgetter.Top_9gag()
        r4=urlgetter.Hot_9gag()
       
        if message.content.startswith('Help_9gag'):
         
          await client.send_message(message.channel,"This Bot share with you links from 9gag web_site \n "+
          "commands are ( All commands start with capital letters ) : \n 1)  Hot+numbers from 1 to 10 example : Hot3 \n"+
          " 2)Top+numbers from 1 to 10 example : Top3 \n"+
          "3)  Funny+numbers from 1 to 10 example : Funny3 \n"+ 
          "if any issue feedback me at zaidasouhil@gmail.com")
     
 
      
        if message.content.startswith('Funny1'):
          F=Url+r2[0][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Funny2'):
          F=Url+r2[1][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Funny3'):
          F=Url+r2[2][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Funny4'):
          F=Url+r2[3][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Funny5'):
          F=Url+r2[4][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Funny6'):
          F=Url+r2[5][31:38]
          await client.send_message(message.channel, F)
        if message.content.startswith('Funny7'):
          F=Url+r2[6][31:38]
          await client.send_message(message.channel, F)  
        if message.content.startswith('Funny8'):
          F=Url+r2[7][31:38]
          await client.send_message(message.channel, F)
        if message.content.startswith('Funny9'):
         var=Url+r2[8][31:38]
         await client.send_message(message.channel,var)
        if message.content.startswith('Funny10'):
          F=Url+r2[9][31:38]
          await client.send_message(message.channel, F) 





        if message.content.startswith('Top1'):
          F=Url+r3[0][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Top2'):
          F=Url+r3[1][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Top3'):
          F=Url+r3[2][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Top4'):
          F=Url+r3[3][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Top5'):
          F=Url+r3[4][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Top6'):
          F=Url+r3[5][31:38]
          await client.send_message(message.channel, F)
        if message.content.startswith('Top7'):
          F=Url+r3[6][31:38]
          await client.send_message(message.channel, F)  
        if message.content.startswith('Top8'):
          F=Url+r3[7][31:38]
          await client.send_message(message.channel, F)
        if message.content.startswith('Top9'):
         var=Url+r3[8][31:38]
         await client.send_message(message.channel,var)
        if message.content.startswith('Top10'):
          F=Url+r3[9][31:38]
          await client.send_message(message.channel, F) 



        if message.content.startswith('Hot1'):
          F=Url+r4[0][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Hot2'):
          F=Url+r4[1][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Hot3'):
          F=Url+r4[2][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Hot4'):
          F=Url+r4[3][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Hot5'):
          F=Url+r4[4][31:38]
          await client.send_message(message.channel, F) 
        if message.content.startswith('Hot6'):
          F=Url+r4[5][31:38]
          await client.send_message(message.channel, F)
        if message.content.startswith('Hot7'):
          F=Url+r4[6][31:38]
          await client.send_message(message.channel, F)  
        if message.content.startswith('Hot8'):
          F=Url+r4[7][31:38]
          await client.send_message(message.channel, F)
        if message.content.startswith('Hot9'):
         var=Url+r4[8][31:38]
         await client.send_message(message.channel,var)
        if message.content.startswith('Hot10'):
          F=Url+r4[9][31:38]
          await client.send_message(message.channel, F) 

client.run(Token)

