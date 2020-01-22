from selenium import webdriver
import time
import os

class Color:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    END       = '\033[0m'
    BOLD      = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'

url_home = "https://instagram.com"
url_login = "https://www.instagram.com/accounts/login/?source=auth_switcher"
url_search = "https://www.instagram.com/explore/search/"
url_hashtag = "https://www.instagram.com/explore/tags/"

driver_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(driver_path)
username = os.environ["INSTA_USERNAME"]
password = os.environ["INSTA_PASSWORD"]

def transPage(driver, url):
    driver.get(url)

    # waiting for loading all elements completely
    time.sleep(3)

def login():
    transPage(driver, url_login)
    print("[ " + Color.YELLOW + "+" + Color.END + " ] login() is started")
    print("[ " + Color.BLUE + "-" + Color.END + " ] username: {}".format(username))
    print("[ " + Color.BLUE + "-" + Color.END + " ] password: {}".format(password))

    element_username = driver.find_element_by_name("username")
    element_password = driver.find_element_by_name("password")
    element_username.send_keys(username)
    element_password.send_keys(password)

    element_button_login = driver.find_element_by_xpath("//button[@type='submit']")
    element_button_login.click()

    print("[ " + Color.YELLOW + "+" + Color.END + " ] login() is finished\n")
    time.sleep(3)

def deletePopup():
    element_button_later = driver.find_elements_by_xpath("//button")[-1]
    element_button_later.click()

def likeWithHashtag(hashtag="fuck"):
    print("[ " + Color.YELLOW + "+" + Color.END + " ] likeWithHashtag() is started")
    transPage(driver, url_search)
    element_search = driver.find_element_by_xpath("//input[@type='text']")
    element_search.send_keys("#" + hashtag)

    transPage(driver, url_hashtag + hashtag + "/")

    time.sleep(5)

    print("[ " + Color.BLUE + "-" + Color.END + " ] search with #{}".format(hashtag))

    element_latest_post_top = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]")
    element_popular_post_top = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]")
    element_latest_post_top.click()
    time.sleep(2)

    element_button_like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
    element_button_like.click()

    print("[ " + Color.BLUE + "-" + Color.END + " ] liked to https://instagram.com")

    time.sleep(3)
    element_button_next = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
    element_button_next.click()

    time.sleep(3)
    element_button_like = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
    element_button_like.click()

    time.sleep(3)
    element_button_next = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]")
    element_button_next.click()

    print("[ " + Color.BLUE + "-" + Color.END + " ] liked to https://instagram.com")
    print("[ " + Color.YELLOW + "+" + Color.END + " ] likeWithHashtag() is finished\n")
    time.sleep(3)

    element_button_close = driver.find_element_by_xpath("/html/body/div[4]/button[1]")
    element_button_close.click()

    time.sleep(3)
    element_button_follow = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
    t = element_button_follow.text
    print(t)
    
def followWIthHashtag(hashtag="fuck"):
    pass

def main():
    login()
    deletePopup()
    likeWithHashtag("ヤクブーツはやめろ")

if __name__ == '__main__':
    driver.get(url_home)
    main()
    time.sleep(10)
    #driver.close()
