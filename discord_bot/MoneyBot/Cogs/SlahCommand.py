from urllib import response
import discord
import requests
from discord.ext import commands
from discord import app_commands
import datetime
import Cogs.Select
import os
from typing import Optional

API_URL = os.getenv("API_URL")

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
    @app_commands.command(name="total_month",description="可以查看某月份所花費金額")
    async def monthtot(self,
                       interaction: discord.Interaction,
                       year: int,
                       month: int,
                       day: Optional[int] = None):
        # response = requests.post(f"{API_URL}/add_type", json={"items": items})
        await interaction.response.send_message("")

async def setup(bot):
    await bot.add_cog(SlahCommand(bot))