import telegram
import subprocess

# replace with your bot token
bot = telegram.Bot(token='your_bot_token_here')
# replace with your chat ID
chat_id = 'your_chat_id_here'

# run the program and get the output file name
output_file = subprocess.check_output(['python', 'program.py']).decode('utf-8').strip()

# send the banner
banner = """
 _____       _ _           _____           _        _ _
|   __|_ _ _|_| |_ ___ ___|   __|___ ___ _| |___   |_| |
|__   | | | | |  _|  _| -_|__   |  _|  _| | | -_|  | | |
|_____|_  |___|_| |_| |___|_____|_| |_| |_  |___|  |_|_|
      |___|                             |___|          
"""
bot.send_message(chat_id=chat_id, text=banner)

# send the output file
with open(output_file, 'rb') as f:
    bot.send_document(chat_id=chat_id, document=f)
