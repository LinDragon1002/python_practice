import discord
from discord import app_commands
from discord.ext import commands
import random
import requests
import os

API_URL = os.getenv("API_URL")

class DictionaryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_games = {}

    # Discord 指令 - 新增單字
    @app_commands.command(name="新增單字", description="新增資料庫的單字")
    async def newvoc(self,
        interaction: discord.Interaction,
        word: str,
        translation: str,
        abbreviation: str,
        definition: str,
        example: str):
        """ 解析格式並新增單字到資料庫 """
        data = {
            "word":word,
            "translation":translation,
            "abbreviation":abbreviation,
            "definition":definition,
            "example":example
        }
        response = requests.post(f"{API_URL}/add_voc",json=data)

        if response.status_code == 200:
            await interaction.response.send_message(f"✅ 單字 `{word}` 已成功新增到資料庫！")
        else:
            await interaction.response.send_message(f"⚠️ 單字 `{word}` 已經存在於資料庫中！")

    # Discord 指令 - 查單字
    @app_commands.command(name="單字查詢", description="查詢資料庫中的單字")
    async def checkvoc(self, interaction: discord.Interaction, word: str):
        """ 查詢資料庫中的單字 """

        response = requests.get(f"{API_URL}/check_voc/{word}")
        data = response.json()

        if data and response.status_code == 200:
            translation = data['translation']
            abbreviation = data['abbreviation']
            definition = data['definition']
            example = data['example'] if data['example'] else "沒有例句"

            embed = discord.Embed(title=f"📖單字查詢：{word}", color=0x00aaff)
            embed.add_field(name="🌏 中文翻譯：", value=f'**{translation}**', inline=False)
            embed.add_field(name="🔤 詞性：", value=f'**{abbreviation}**', inline=False)
            embed.add_field(name="📌 定義：", value=f'**{definition}**', inline=False)
            embed.add_field(name="💬 例句：", value=f'**{example}**', inline=False)

            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(f"❌ 沒有找到 `{word}` 這個單字，請先使用 `!新增單字` 指令來新增！")

    # Discord 指令 - 列出所有單字
    @app_commands.command(name="所有單字",description="列出資料庫全部的單字")
    async def allvoc(self, interaction: discord.Interaction):
        """ 列出資料庫中的所有單字 """
        response = requests.get(f"{API_URL}/allvoc")
        words = response.json()

        if words and response.status_code == 200:
            await interaction.response.send_message(f"📚 資料庫中的單字：總共{len(words)}個\n{','.join(words)}")
        else:
            await interaction.response.send_message("❌ 資料庫中沒有任何單字！")


    # Discord 指令 - 刪除單字
    @app_commands.command(name="刪除單字",description="刪除資料庫的單字")
    async def delvoc(self, interaction: discord.Interaction, word: str):
        """ 刪除資料庫中的單字 """
        response = requests.delete(f"{API_URL}/del_voc/{word}")
        if response.status_code == 200:
            await interaction.response.send_message(f"✅ 單字 `{word}` 已成功刪除！")
        else:
            await interaction.response.send_message("刪除單字時發生錯誤！")


    # Discord 指令 - 更新單字
    @app_commands.command(name="更新單字", description="修改單字的某個欄位")
    @discord.app_commands.choices(
        correct_type=[
            app_commands.Choice(name="單字", value="word"),
            app_commands.Choice(name="詞性", value="abbreviation"),
            app_commands.Choice(name="定義", value="definition"),
            app_commands.Choice(name="例句", value="example"),
            app_commands.Choice(name="翻譯", value="translation")
        ]
    )
    async def update_word(
        self,
        interaction: discord.Interaction,
        word: str,
        correct_type: app_commands.Choice[str],
        correct_content: str):
        """ 允許修改單字的 某一個欄位 (詞性、定義、例句、翻譯) """
        response = requests.post(f'{API_URL}/update_voc/{word}')
        if response.status_code == 200:
            await interaction.response.send_message(f"✅ **已更新 `{word}` 的 {correct_type}**：\n🔹 {correct_content}")
        else:
            await interaction.response.send_message(f"❌ 有問題請再試一次！")

    # # Discord 指令 - 單字測驗
    @app_commands.command(name="單字測驗", description="測驗自己的熟練度")
    async def voctest(self, interaction: discord.Interaction):
        response = requests.get(f"{API_URL}/random_word")
        data = response.json()
        engorchi = random.randint(1,2)

        if data and response.status_code == 200:
            correct_word = data["word"]
            chinese_word = data["translation"]

            if engorchi == 1:
                self.active_games[interaction.user.id] = correct_word.lower()
                await interaction.response.send_message(f"📝 **請輸入 `{chinese_word}` 的英文單字！**\n（輸入 `/回答 <你的答案>` 來作答）")
            else:
                self.active_games[interaction.user.id] = chinese_word
                await interaction.response.send_message(f"📝 **請輸入 `{correct_word}` 的英文單字！**\n（輸入 `/回答 <你的答案>` 來作答）")
        else:
            await interaction.response.send_message("❌ 資料庫中沒有任何單字！")

    @app_commands.command(name="回答",description="回答測驗問題")
    async def ansvoc(self, interaction: discord.Interaction, user_answer: str):
        user_id = interaction.user.id

        if user_id not in self.active_games:
            await interaction.response.send_message("❌ 你沒有進行中的測驗，請使用 `/單字測驗` 開始測驗！")
            return

        correct_answer = self.active_games[user_id]

        # 📌 判斷是否正確（忽略大小寫）
        if user_answer.lower() == correct_answer:
            await interaction.response.send_message(f"✅ **正確！答案是 `{correct_answer}`！🎉**")
        else:
            await interaction.response.send_message(f"❌ **錯誤！正確答案是 `{correct_answer}`！😢**")

        # 📌 刪除使用者的測驗紀錄
        del self.active_games[user_id]

async def setup(bot):
    await bot.add_cog(DictionaryCog(bot))