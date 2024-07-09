# Discord AI 챗봇

이 프로젝트는 OpenAI의 GPT와 DALL-E를 활용한 다기능 Discord 챗봇입니다. 텍스트 대화, 이미지 생성, 음성 메시지 기능을 제공합니다.

## 기능

- **일반 채팅**: ChatGPT를 이용한 대화 응답
- **이미지 생성**: DALL-E를 이용한 이미지 생성 (`!그림` 명령어)
- **음성 메시지**: 텍스트를 음성으로 변환하여 음성 채널에서 재생 (`!말해` 명령어)
- **로깅**: 모든 대화 내용을 파일과 관리자 DM으로 로깅
- **관리자 전용 개인 메시지**: 관리자만 봇과 개인 메시지 가능

## 설치 방법

1. 이 저장소를 클론합니다:
git clone https://github.com/KeonhoChu/discord_bot.git

2. 필요한 라이브러리를 설치합니다:
pip install discord.py python-dotenv openai gTTS

3. FFmpeg를 시스템에 설치합니다. (음성 기능에 필요)

4. `.env` 파일을 생성하고 다음 정보를 입력합니다:
DISCORD_TOKEN=your_discord_bot_token
ADMIN_ID=your_discord_user_id
OPENAI_API_KEY=your_openai_api_key


## 사용 방법

1. 봇을 실행합니다:
python bot.py
Copy
2. Discord 서버에서 다음 명령어를 사용할 수 있습니다:
- 일반 채팅: 봇에게 직접 메시지를 보냅니다.
- 이미지 생성: `!그림 [설명]`
- 음성 메시지: `!말해 [텍스트]`

## 주의사항

- 봇에 필요한 Discord 권한(메시지 읽기/쓰기, 음성 채널 접근 등)을 부여해야 합니다.
- API 사용량과 관련된 비용에 주의하세요.
- 개인정보 보호를 위해 로그에 민감한 정보가 포함되지 않도록 주의하세요.

## 기여 방법

이슈를 제기하거나 풀 리퀘스트를 보내주시면 감사하겠습니다. 모든 기여는 환영합니다!

## 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
