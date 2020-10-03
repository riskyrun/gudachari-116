#to import modules
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
import json


#client for bot
client=discord.Client()

######## TORN API DATA #########


apikey='insert_key_here'


@client.event
async def on_message(message):

   if message.content.startswith('!stats'):
      async def torn_script(player_ID):
         apiurl='https://api.torn.com/user/'+str(player_ID)+'?selections=personalstats&key='+apikey
         r=requests.get(apiurl)
         astext=r.text
         asdict=json.loads(astext)
         data=json.loads(requests.get(apiurl).text)['personalstats']
         #print('attacks won: ',data['attackswon'])
         async def discord_display(end_data):
            #await message.channel.send(end_data )
            embed_var=discord.Embed(
               
               
               title='Stats',
               description=str(end_data),
               colour=discord.Colour.green()
               )
            
            
            
            
            embed_var.set_footer(text='Riskyrun did this shiz')
            embed_var.add_field(name='name',value='value',inline=True)
            
            await message.channel.send(embed=embed_var)
         
         
         
         await discord_display(
            f"Attacks won: {data['attackswon']}\n"  
            f"Attacks lost: {data['attackslost']}\n"
            f"Defends won: {data['defendswon']}\n"
            f"Defends lost: {data['defendslost']}\n"
            #f"Total defends: {data(int['defendswon'])+(['defendslost'])}\n"
            f"Networth: {data['networth']}\n"
            f"Money mugged: {data['moneymugged']}\n"
            f"Largest mug: {data['largestmug']}\n"
            f"Max level beaten: {data['highestbeaten']}\n"
            f"Boosters used: {data['boostersused']}\n"
            f"Xanax used: {data['xantaken']}\n"
            f"Ecstacy used: {data['exttaken']}\n"
            f"Time played: {data['boostersused']}\n"
            f"Energy refills: {data['refills']}\n")
             
   await torn_script(message.content[6:])
   
#gen_channel=client.get_channel(742694272662503447)


#running client on server
client.run('insert_bot_token_here')


