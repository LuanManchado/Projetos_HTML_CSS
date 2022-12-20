import discord
from discord import app_commands

id_do_servidor = 1044326698520424511 #Coloque aqui o ID do seu servidor

class Dropdown(discord.ui.select):
    def __init__(self):
        options = [
         discord.SelectOption(value="ticket",Label="ticket",emoji="🚀"),
         discord.SelectOption(value="denuncia",Lbel="Fazer Denuncia"),
         
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help"
         )
    async def callbanck(self, interaction: discord.Interaction):
        if self.values[0] == "ticket":
            await interaction.response.end_message("o usuario selecionou ticket")
        elif self.values[0] == "denuncia":
            await interaction.response.end_message("o usuario selecionou denuncia")                
                                                        
        class DropdownView(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=None)
            
            self.add_item(Dropdown())            
    
class client(discord.Client):
    def init(self):
        super().init(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez
        
        async def setup_hook(self) -> None:
             self.add_view(Dropdown())            
    

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'youtube', description='Se inscreva no canal!!') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://www.youtube.com/@Luannaarea", ephemeral = True) 


@tree.command(guild = discord.Object(id=id_do_servidor), name = 'instagram', description='Segue meu insta la Tropa !!') #Comando específico para seu servidor
async def slash3(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://www.instagram.com/luanmachadoyt/?next=%2F", ephemeral = True) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'setup', description='Setup!') #Comando específico para seu servidor
async def setup(interaction: discord.Interaction):
    await interaction.response.sendmessage(f"Mensagem do Painel",view=DropdownView())

 
 
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'lives', description='Live todos os dias!!') #Comando específico para seu servidor
async def slash4(interaction: discord.Interaction):
    await interaction.response.sendmessage(f"https://www.twitch.tv/johnwickrp", ephemeral = True)

aclient.run('MTA0NDYwODM5Njg5NDE1ODg0OA.GJXRzX.qn-qDQKJQo5jKGkM3plwoOdKl1i91XoeG-MfU')