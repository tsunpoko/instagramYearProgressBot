import instabot
from PIL import Image, ImageDraw
from io import BytesIO
import os
import requests
import time

try:
    username = os.environ["INSTA_USERNAME"]
    password = os.environ["INSTA_PASSWORD"]

except:
    print("username or password don't setting. Please check it.")
    os.exit(1)


bot = instabot.Bot()
bot.login(username=username, password=password, proxy=None)

def downloadImage(url, output_filename):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(output_filename, 'wb') as f:
            f.write(r.content)

def main():
    for i in reversed(range(3)):
        filename = 'data_' + str(i) + '.jpg'
        #filename = 'test' + str(i) + '.jpg'
        bot.upload_photo(filename)

if __name__ == '__main__':
    print("[+] initialized.")
    main()
