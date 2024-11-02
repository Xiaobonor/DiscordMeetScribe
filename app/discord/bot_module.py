# app/discord/bot_module.py
import asyncio
import os
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv

from app.discord.application_process.helpers import send_initial_embed
from app.discord.import_existing_members import setup as import_existing_members_setup
from app.discord.application_process import setup as application_process_setup
from app.models.form_response import FormResponse
from app.utils.mail_sender import send_email

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)
load_dotenv()

import_existing_members_setup(bot)
application_process_setup(bot)

@bot.event
async def on_ready():

    from app.discord.application_process.views import (
        AcceptOrCancelView,
        ContactOrFailView,
        ArrangeOrCancelView,
        AttendOrNoShowView,
        InterviewResultView,
        ManagerFillFormView,
        FindMyView,
    )

    bot.add_view(AcceptOrCancelView())
    bot.add_view(ContactOrFailView())
    bot.add_view(ArrangeOrCancelView())
    bot.add_view(AttendOrNoShowView())
    bot.add_view(InterviewResultView())
    bot.add_view(ManagerFillFormView())
    bot.add_view(FindMyView())


def get_bot():
    return bot


# async def import_data():
#     import pandas as pd
#     import hashlib
#     from app.utils.encryption import aes_encrypt as encrypt
#
#     file_path = 'data.csv'
#     df = pd.read_csv(file_path)
#
#     def generate_email_hash(email: str) -> str:
#         return hashlib.sha256(email.encode('utf-8')).hexdigest()
#
#     for index, row in df.iterrows():
#         form_response = FormResponse(
#             name=row['你的名字?'],
#             email=row['電子郵件~'],
#             phone_number=str(row['電話號碼~~']),
#             high_school_stage=row['高中階段~~'],
#             city=row['你住在哪~~~'],
#             interested_fields=row['來找找適合你的領域~'].split(','),
#             preferred_order=str(row['排一排，告訴我們你的優先選擇吧！✨']),
#             reason_for_choice=row['為什麼選擇這些組別？🎯'],
#             related_experience=row['有什麼相關經驗或技能嗎？💡'],
#             email_hash=generate_email_hash(row['電子郵件~']),
#         )
#
#         form_response.save()
#
#         await send_initial_embed(form_response)
#
#         send_email(
#             subject="Counterspell / 已收到您的工作人員報名表！",
#             recipient=row['電子郵件~'],
#             template='emails/notification_email.html',
#             name=row['你的名字?'],
#             uuid=form_response.uuid
#         )
#
#     print("資料匯入完成！")
#
# from app.utils.mail_sender import send_email
# from app.models.staff import Staff
#
# def send_email_to_all_staff():
#     """
#     發送郵件給所有在系統中的員工。
#
#     Args:
#         subject (str): 郵件主題。
#         template (str): 郵件模板路徑。
#         **template_vars: 傳遞給模板的變數。
#     """
#     all_staff = Staff.objects()  # 獲取所有的員工記錄
#     print("正在發送郵件給所有員工...")
#
#     for staff in all_staff:
#         print(f"正在處理員工 {staff.name}...")
#         if staff.email:  # 檢查是否有有效的 email
#             print(f"正在發送郵件給 {staff.name}...")
#             send_email(
#                 subject="Counterspell / 延期通知",
#                 recipient=staff.email,
#                 template='emails/notification_delay.html',
#                 name=staff.name,
#             )
#         time.sleep(2)
#
#     print("所有員工的郵件已發送！")
