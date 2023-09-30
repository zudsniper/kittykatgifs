# `kittykatgifs`
_A Simple Python 3 Discord Bot_

## Overview

`kittykatgifs` is a Discord bot built using Python 3. Unlike other projects, this bot focuses on providing various functionalities for Discord servers, including the ability to fetch and display cat GIFs.

<div align="center">

![A rainbow cat on a stripper pole or something silly](/cat_gif.gif)

</div>

### 🧰 Tech Stack

- Python 3.x
- Disnake library
- GIPHY API
- Loguru for logging

### 🌟 Features

- Fetches cat GIFs based on user input
- Utilizes slash commands for easy interaction
- Provides colorful debug output via Loguru

### 📦 Prerequisites

- Python 3.x
- pip (Python package installer)
- Discord account
- GIPHY account

### 🚀 Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/zudsniper/kittykatgifs.git
    cd kittykatgifs
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables**

    Create a `.env` file in the root directory and add your Discord and GIPHY API tokens like so:

    ```env
    DISCORD_BOT_TOKEN=your_discord_bot_token_here
    GIPHY_API_KEY=your_giphy_api_key_here
    ```
   
    > 📌 _or you can clone the `.env.example` file and rename it to `.env` and add your tokens there._  

## 🎮 Usage

0. Add the bot to your Discord server by visiting the following link:

    ```bash
    https://discord.com/api/oauth2/authorize?client_id=your_discord_bot_client_id_here&permissions=0&scope=bot%20applications.commands
    ```

1. **Run the Bot**

    ```bash
    python main.py
    ```

2. **Bot Commands**

    Use `/prrr <words>` in any channel the bot has access to fetch a cat GIF based on the words provided.

## 🧪 Testing

This project includes basic unit tests. To run the tests, execute the following command:

```bash
python -m unittest discover tests
```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### 🙏 Acknowledgements

Inspired by various Discord bot projects and cat lovers everywhere.

---

Feel free to contribute to this project. For any issues, please open an issue or submit a pull request.

[![Discord](https://img.shields.io/discord/your_discord_server_id?label=discord)](https://discord.gg/your_discord_invite_link)