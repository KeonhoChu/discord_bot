import os
import discord
from dotenv import load_dotenv
from chatgpt import send_to_chatGpt
import datetime
from openai import OpenAI
from discord import FFmpegPCMAudio
from gtts import gTTS
import asyncio

# 환경 변수 로드
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Discord 클라이언트 설정
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# 로그 파일 설정
log_file = "bot_logs.txt"

# OpenAI 클라이언트 설정
openai_client = OpenAI(api_key=OPENAI_API_KEY)

async def log_and_send(message, response, admin):
    # (이전 코드와 동일)

async def generate_image(prompt):
    try:
        response = openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        print(f"Image generation error: {str(e)}")
        return None

async def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 개인 메시지 처리
    if isinstance(message.channel, discord.DMChannel):
        if str(message.author.id) != ADMIN_ID:
            await message.channel.send("죄송합니다. 개인 메시지는 서버 관리자만 사용할 수 있습니다.")
            return

    # 이미지 생성 명령어
    if message.content.startswith('!그림'):
        prompt = message.content[4:].strip()
        image_url = await generate_image(prompt)
        if image_url:
            await message.channel.send(image_url)
        else:
            await message.channel.send("이미지 생성 중 오류가 발생했습니다.")
        return

    # 음성 메시지 명령어
    if message.content.startswith('!말해'):
        # (이전 코드와 동일)

    # 일반 채팅 처리
    messages = [{"role": "user", "content": message.content}]
    try:
        response = send_to_chatGpt(messages)
        await message.channel.send(response)

        admin = await client.fetch_user(int(ADMIN_ID))
        await log_and_send(message, response, admin)
    except Exception as e:
        print(f"오류 발생: {e}")
        await message.channel.send("죄송합니다. 요청을 처리하는 동안 오류가 발생했습니다.")

# 봇 실행
client.run(DISCORD_TOKEN)
