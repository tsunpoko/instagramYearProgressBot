from PIL import Image, ImageDraw, ImageFont
import calendar
import time

def splitImage(num, filename, percent):
    height = 1080
    width = 1080
    img = Image.open(filename)

    for i in range(num):
        img_crop = img.crop((width * i, 0, width * i + width, height))
        img_crop.save("data_" + str(i) + ".jpg")

def main():
    img = Image.new('RGB', (3240, 1080), color=(255, 255, 255, 0))
    img_percent = Image.open('percent.png')

    back_img = img.copy()
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())

    all_days = 0
    past_days = 0

    for i in range(1, 12 + 1):
        current_days = calendar.monthrange(year, i)[1]
        all_days += current_days

        if i <= month:
            if month == i:
                past_days += day
            else:
                past_days += current_days


    #past_days = 16
    percent = past_days / all_days
    percent_str = '{:.1f}'.format( percent * 100)

    print('past_days: {}'.format(past_days))
    print('all_days: {}'.format(all_days))
    print('percent: {}'.format(percent))

    height = 1080
    width = 1080 * 3

    msg = percent_str + ' %'


    draw = ImageDraw.Draw(back_img)
    draw.rectangle((0, 0, 1080 * 3 * percent , 1080), fill=(143,86,255))
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Impact.ttf", 100)
    w, h = draw.textsize(msg, font=font)
    back_img.paste(img_percent, (1080, 0), img_percent)
    draw.text(((width - w) / 2, (height - h) / 2 - 10), msg, fill=(255, 255, 255), font=font)

    filename = 'pil_white.jpg'

    back_img.save(filename)
    splitImage(3, filename, 98.1)


if __name__ == '__main__':
    main()
