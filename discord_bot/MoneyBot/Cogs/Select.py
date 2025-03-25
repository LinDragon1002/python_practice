import discord
import requests
from typing import cast, Dict, Any
import os

API_URL = os.getenv("API_URL")

# --- 📌 類型選擇下拉選單 ---
class TypeDropdown(discord.ui.Select):
    def __init__(self, transaction_data: Dict[str, Any]):
        self.transaction_data = transaction_data  # 儲存 Slash Command 提供的交易資料

        # 📌 從 Flask API 獲取所有類型
        response = requests.get(f"{API_URL}/get_types")
        if response.status_code != 200:
            options = [discord.SelectOption(label="⚠️ 無法獲取類型，請稍後再試", value="0")]
        else:
            types = response.json()
            options = [
                discord.SelectOption(label=t["items"], value=str(t["id"])) for t in types
            ]

        # 📌 初始化下拉選單
        super().__init__(placeholder="選擇一個類型", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        """ 當使用者選擇類型時執行 """
        if self.values[0] == "0":
            await interaction.response.send_message("⚠️ 無法獲取類型，請稍後再試！")
            return

        type_id = int(self.values[0])  # 取得選擇的類型 ID
        type_name = [option.label for option in self.options if option.value == self.values[0]][0]

        # 📌 發送資料到 Flask API
        response = requests.post(f"{API_URL}/add_expense", json={
            "name": self.transaction_data["name"],
            "amount": self.transaction_data["amount"],
            "enorin_id": self.transaction_data["enorin_id"],
            "type_id": type_id,
            "date": self.transaction_data["date"]
        })

        if response.status_code == 200:
            await interaction.response.send_message(
                f"✅ **{self.transaction_data['name']}** 已新增！💰 金額：{self.transaction_data['amount']}，類型：`{type_name}`"
            )
        else:
            await interaction.response.send_message("❌ 儲存消費項目時發生錯誤！")


# --- 📌 類型選擇視圖 ---
class TypeDropdownView(discord.ui.View):
    def __init__(self, transaction_data):
        super().__init__()
        self.add_item(TypeDropdown(transaction_data))
