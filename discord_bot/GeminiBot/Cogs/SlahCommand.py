import discord
from google import genai
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.schema import HumanMessage

# chat_log = str()
# chat_list = list()
load_dotenv()

class SlahCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # discord - 指令 新增對話
    @app_commands.command(name="提問", description="新增一個對話")
    async def add_type(self,interaction: discord.Interaction, string: str):

        await interaction.response.defer()
        await interaction.followup.send("正在處理請稍後...")
        # def api_key():
        #     return os.getenv("APIKEY")
        chat = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
        response = chat([HumanMessage(content=string)])
        # global chat_log, chat_list
        # client = genai.Client(api_key=api_key())

        # if string:
        #     chat1 = chat_log + "\n以上是我們曾經的對話，'user'是我，'gemini'是你，接著是我要繼續跟你的對話\n" + string
        #     response = client.models.generate_content(
        #         model="gemini-2.0-flash",
        #         contents=chat1,
        #         )

        #     user = "user: " + string + "\n"
        #     res = f"gemini: {response.text}"

        #     chat_log += (user + res)
        #     chat_list.append((user.strip(), res))

        await interaction.followup.send(f"{response.content}")


async def setup(bot):
    await bot.add_cog(SlahCommand(bot))