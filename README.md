
# Discord AI Chatbot

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/Discord.py-1.7.3-blue)](https://github.com/Rapptz/discord.py)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-brightgreen)](https://openai.com/)
[![gTTS](https://img.shields.io/badge/gTTS-2.2.3-green)](https://pypi.org/project/gTTS/)
[![GNU GPLv3](https://img.shields.io/badge/license-GNU%20GPLv3-blue)](https://www.gnu.org/licenses/gpl-3.0)

[한국어](#한국어) | [English](#english) | [日本語](#日本語)

## 한국어

이 프로젝트는 OpenAI의 GPT와 DALL-E를 활용한 다기능 Discord 챗봇입니다. 텍스트 대화, 이미지 생성, 음성 메시지 기능을 제공합니다.

### 기능

- **일반 채팅**: ChatGPT를 이용한 대화 응답
- **이미지 생성**: DALL-E를 이용한 이미지 생성 (`!그림` 명령어)
- **음성 메시지**: 텍스트를 음성으로 변환하여 음성 채널에서 재생 (`!말해` 명령어)
- **로깅**: 모든 대화 내용을 파일과 관리자 DM으로 로깅
- **관리자 전용 개인 메시지**: 관리자만 봇과 개인 메시지 가능

### 설치 방법

1. 이 저장소를 클론합니다:
   ```sh
   git clone https://github.com/KeonhoChu/discord_bot.git
   ```

2. 필요한 라이브러리를 설치합니다:
   ```sh
   pip install discord.py python-dotenv openai gTTS
   ```

3. FFmpeg를 시스템에 설치합니다. (음성 기능에 필요)

4. `.env` 파일을 생성하고 다음 정보를 입력합니다:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   ADMIN_ID=your_discord_user_id
   OPENAI_API_KEY=your_openai_api_key
   ```

### 사용 방법

1. 봇을 실행합니다:
   ```sh
   python bot.py
   ```

2. Discord 서버에서 다음 명령어를 사용할 수 있습니다:
   - 일반 채팅: 봇에게 직접 메시지를 보냅니다.
   - 이미지 생성: `!그림 [설명]`
   - 음성 메시지: `!말해 [텍스트]`

### 주의사항

- 봇에 필요한 Discord 권한(메시지 읽기/쓰기, 음성 채널 접근 등)을 부여해야 합니다.
- API 사용량과 관련된 비용에 주의하세요.
- 개인정보 보호를 위해 로그에 민감한 정보가 포함되지 않도록 주의하세요.

### 기여 방법

이슈를 제기하거나 풀 리퀘스트를 보내주시면 감사하겠습니다. 모든 기여는 환영합니다!

### 라이선스

이 프로젝트는 GNU 라이선스 하에 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

## English

This project is a multifunctional Discord chatbot utilizing OpenAI's GPT and DALL-E, offering text conversation, image generation, and voice message functionalities.

### Features

- **General Chat**: Responds to conversations using ChatGPT
- **Image Generation**: Generates images using DALL-E (`!image` command)
- **Voice Messages**: Converts text to speech and plays it in a voice channel (`!speak` command)
- **Logging**: Logs all conversations to a file and DM to admin
- **Admin-Only DMs**: Only admins can DM the bot

### Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/KeonhoChu/discord_bot.git
   ```

2. Install the required libraries:
   ```sh
   pip install discord.py python-dotenv openai gTTS
   ```

3. Install FFmpeg on your system (required for voice functionality).

4. Create a `.env` file and add the following information:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   ADMIN_ID=your_discord_user_id
   OPENAI_API_KEY=your_openai_api_key
   ```

### Usage

1. Run the bot:
   ```sh
   python bot.py
   ```

2. Use the following commands on your Discord server:
   - General chat: Send a direct message to the bot.
   - Image generation: `!image [description]`
   - Voice message: `!speak [text]`

### Notes

- Ensure the bot has the necessary Discord permissions (read/send messages, access voice channels, etc.).
- Be mindful of API usage costs.
- Ensure sensitive information is not included in logs to protect privacy.

### Contribution

Feel free to open issues or submit pull requests. All contributions are welcome!

### License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.

---

## 日本語

このプロジェクトは、OpenAIのGPTとDALL-Eを活用した多機能なDiscordチャットボットです。テキスト対話、画像生成、音声メッセージ機能を提供します。

### 機能

- **一般チャット**: ChatGPTを利用した対話応答
- **画像生成**: DALL-Eを利用した画像生成（`!画像`コマンド）
- **音声メッセージ**: テキストを音声に変換し、ボイスチャネルで再生（`!話して`コマンド）
- **ログ記録**: すべての対話内容をファイルと管理者DMに記録
- **管理者専用DM**: 管理者のみボットとDM可能

### インストール方法

1. このリポジトリをクローンします:
   ```sh
   git clone https://github.com/KeonhoChu/discord_bot.git
   ```

2. 必要なライブラリをインストールします:
   ```sh
   pip install discord.py python-dotenv openai gTTS
   ```

3. システムにFFmpegをインストールします（音声機能に必要）。

4. `.env`ファイルを作成し、以下の情報を追加します:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   ADMIN_ID=your_discord_user_id
   OPENAI_API_KEY=your_openai_api_key
   ```

### 使用方法

1. ボットを実行します:
   ```sh
   python bot.py
   ```

2. Discordサーバーで以下のコマンドを使用できます:
   - 一般チャット: ボットに直接メッセージを送信します。
   - 画像生成: `!画像 [説明]`
   - 音声メッセージ: `!話して [テキスト]`

### 注意事項

- ボットに必要なDiscord権限（メッセージの読み取り/書き込み、音声チャネルへのアクセスなど）を付与してください。
- API使用量に関連する費用に注意してください。
- プライバシー保護のため、ログに機密情報が含まれないように注意してください。

### 貢献方法

問題を提起したり、プルリクエストを送信したりしてください。すべての貢献を歓迎します！

### ライセンス

このプロジェクトはGNUライセンスの下でライセンスされています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。

