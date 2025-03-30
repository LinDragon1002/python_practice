import io
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import discord
import requests
from discord.ext import commands
from discord import app_commands
import datetime
import Cogs.Select
import os

API_URL = os.getenv("API_URL")
font_path = "C:/WINDOWS/FONTS/MSJHL.TTC"

class SlahCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # discord - 指令 新增類型
    @app_commands.command(name="add_type", description="新增一個消費類型")
    async def add_type(self,interaction: discord.Interaction, items: str):
        response = requests.post(f"{API_URL}/add_type", json={"items": items})
        if response.status_code == 200:
            await interaction.response.send_message(f"類型 `{items}` 已新增！")
        else:
            await interaction.response.send_message("新增類型時發生錯誤！")

    # discord - 指令 新增消費項目
    @app_commands.command(name="新增消費項目", description="新增一筆消費紀錄")
    @app_commands.choices(
        enorin=[
            app_commands.Choice(name="支出", value=1),
            app_commands.Choice(name="收入", value=2),
        ]
    )
    async def newitmes(
        self,
        interaction: discord.Interaction,
        name: str,
        amount: int,
        enorin: app_commands.Choice[int],
    ):
        """ 使用者輸入 name、amount，並選擇收入/支出 """
        date = datetime.date.today()
        transaction_data = {
            "name": name,
            "amount": amount,
            "date": str(date),  # 存成字串，避免 JSON 格式錯誤
            "enorin_id": enorin.value,
        }

        # 📌 顯示類型選擇下拉式選單
        view = Cogs.Select.TypeDropdownView(transaction_data)
        await interaction.response.send_message("📌 **請選擇一個類型**：", view=view)

    # discord - 指令 查看月份花費金額
    @app_commands.command(name="查看月份花費金額",description="可以查看某月份所花費金額")
    async def monthtot(self,
                       interaction: discord.Interaction,
                       year: int,
                       month: int,
                       ):
        response = requests.get(f"{API_URL}/find_month/{year}/{month}")
        data = response.json()
        if data and response.status_code == 200:
            total = 0
            for i in range(len(data)):
                total += data[i]['amount']

            embed = discord.Embed(title=f"查詢範圍：{year}{month}")
            embed.add_field(name="金額：", value=f"**{total}**", inline=False)
            await interaction.response.send_message(embed=embed)

    # discord - 指令 查看當天花費金額
    @app_commands.command(name="查看今日花費",description="可以查看某月份所花費金額")
    async def todaytot(self, interaction: discord.Interaction):
        date = datetime.date.today()
        response = requests.get(f"{API_URL}/today/{str(date)}")
        data = response.json()
        if data and response.status_code == 200:
            total = 0
            for i in range(len(data)):
                name = data[i]['name']
                total += data[i]['amount']
                amount = data[i]['amount']
                type_name = data[i]['type_name']

            embed = discord.Embed(title=f"查詢範圍：{str(date)}")
            embed.add_field(name="名稱：", value=f"**{name}**",inline=False)
            embed.add_field(name="金額：", value=f"**{amount}**", inline=False)
            embed.add_field(name="類型：",value=f"**{type_name}**",inline=False)
            await interaction.response.send_message(embed=embed)
        await interaction.response.send_message(f"今日總金額：{total}")

    # discord - 指令 text chart
    @app_commands.command(name="圖表",description="測試圖表")
    async def charttext(self, interaction: discord.Interaction):
        my_font = fm.FontProperties(fname=font_path)
        """繪製一個簡單的長條圖並發送"""
        # 📌 1. 準備數據
        labels = ["A", "B", "C", "D"]
        values = [10, 20, 15, 25]

        # 📌 2. 繪製圖表
        plt.figure(figsize=(6, 4))
        plt.bar(labels, values, color=['blue', 'green', 'red', 'purple'])
        plt.xlabel("分類", fontproperties=my_font, fontsize=14)
        plt.ylabel("數值", fontproperties=my_font, fontsize=14)
        plt.title("測試圖表", fontproperties=my_font, fontsize=14)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # 📌 3. 儲存到 BytesIO
        img_stream = io.BytesIO()
        plt.savefig(img_stream, format="png")
        plt.close()
        img_stream.seek(0)

        # 📌 4. 發送到 Discord
        await interaction.response.send_message(file=discord.File(img_stream, filename="plotly_chart.png"))

async def setup(bot):
    await bot.add_cog(SlahCommand(bot))