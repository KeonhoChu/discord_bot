async def log_and_send(message, response, admin):
    log_entry = f"[{datetime.datetime.now()}]\n"
    log_entry += f"사용자: {message.author.name} (ID: {message.author.id})\n"
    
    if isinstance(message.channel, discord.TextChannel):
        log_entry += f"채널: {message.channel.name} (ID: {message.channel.id})\n"
        log_entry += f"서버: {message.guild.name} (ID: {message.guild.id})\n"
    else:
        log_entry += f"채널: 개인 메시지 (ID: {message.channel.id})\n"
    
    log_entry += f"입력: {message.content}\n"
    log_entry += f"출력: {response}\n\n"
    
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(log_entry)
    
    await admin.send(f"새로운 대화 로그:\n```\n{log_entry}```")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 개인 메시지 처리
    if isinstance(message.channel, discord.DMChannel):
        if str(message.author.id) != ADMIN_ID:
            await message.channel.send("죄송합니다. 개인 메시지는 서버 관리자만 사용할 수 있습니다.")
            return
    
    messages = [{"role": "user", "content": message.content}]
    try:
        response = send_to_chatGpt(messages)
        await message.channel.send(response)

        admin = await client.fetch_user(int(ADMIN_ID))
        await log_and_send(message, response, admin)
    except Exception as e:
        print(f"오류 발생: {e}")
        await message.channel.send("죄송합니다. 요청을 처리하는 동안 오류가 발생했습니다.")
