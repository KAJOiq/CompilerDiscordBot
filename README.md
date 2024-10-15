
# Discord Language Translator Bot

This repository contains a Discord bot that serves as a language translator for programming languages like Python, Java, and C++. It enables users to write code in these languages, execute it, and receive results directly through Discord commands.

## Features

- **Code Execution**: Run Python, Java, and C++ code snippets.
- **Multi-language Support**: Supports three major programming languages.
- **Real-time Feedback**: Get instant results for the code executed in the Discord chat.
- **Error Handling**: Provides error messages and debugging help if the code fails to compile or execute.

## Supported Languages

- **Python**
- **Java**
- **C++**

## Technologies Used

- **Discord API**: To manage interactions between users and the bot.
- **Python**: Used for building the bot's core logic and executing Python code.
- **Java and C++**: Executed in a secure environment from the bot.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KAJOiq/Discord-tasks.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Discord-tasks
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment by creating a `.env` file and adding your Discord bot token:
   ```
   DISCORD_TOKEN=your-bot-token-here
   ```

5. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

- **Run Python Code**: Use the `/runpython [code]` command to execute Python code.
- **Run Java Code**: Use the `/runjava [code]` command to execute Java code.
- **Run C++ Code**: Use the `/runcpp [code]` command to execute C++ code.
- **Error Handling**: The bot will return any compilation or runtime errors along with suggestions.

## Contributing

If you'd like to contribute, feel free to fork the repository and submit pull requests with new features or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, you can reach out through GitHub.
