import requests

bot_token = 'your_bot_token'
bot_chatID = 'your_chat_id'

file_path = 'path_to_file'
file_name = 'file_name.ext'

url = 'https://api.telegram.org/bot' + bot_token + '/sendDocument'
files = {'document': open(file_path, 'rb')}
data = {'chat_id': bot_chatID}
response = requests.post(url, files=files, data=data)

if response.status_code == 200:
    print(f'File {file_name} has been sent successfully to Telegram!')
else:
    print(f'Failed to send file {file_name} to Telegram.')
