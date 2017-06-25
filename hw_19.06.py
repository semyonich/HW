from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import os
from datetime import datetime
import csv
#
# with open("data.csv", "r+") as csvfile:
#     fieldnames = ["title", "subscribers", "published", "answers", "has_correct_answer"]
#     filewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

f = open("data.csv", mode="r+", encoding="UTF-8")
chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
driver = webdriver.Chrome(chromedriver)

driver.set_window_size(414, 736)

driver.get("https://habrahabr.ru/")
driver.find_element_by_xpath("//a[@href='https://habrahabr.ru/auth/register/']").click()
driver.find_element_by_xpath("//input[@name='email']").send_keys("zaurus@bigmir.net")
driver.find_element_by_xpath("//input[@name='login']").send_keys("Semyonich")
driver.find_element_by_xpath("//input[@name='password']").send_keys("123456")
driver.find_element_by_xpath("//input[@name='password2']").send_keys("123456")

driver.maximize_window()



driver.get("http://toster.ru")
search_input = driver.find_element_by_name("q")
search_input.send_keys("python" + Keys.RETURN)


driver.get("https://toster.ru/questions/interesting?page=86")
next_btn = True

while next_btn:
    topics = driver.find_elements_by_class_name("question_short")
    # print("Page {}".format(page))
    # if page == 1:
    for topic in topics:
        title_element = topic.find_element_by_class_name("question__title-link")
        title = title_element.text
        subscribers = topic.find_element_by_class_name("question__views-count").text.split(" ")[0]
        published_string = topic.find_element_by_class_name("question__date_publish").get_attribute("datetime")
        published_datetime = datetime.strptime(published_string, "%Y-%m-%d %H:%M:%S")
        published = published_datetime.strftime("%d-%m-%Y")
        answers = topic.find_element_by_class_name("mini-counter__count_grey").text

        try:
            topic.find_element_by_class_name("icon_check")
            has_correct_answer = True
        except NoSuchElementException:
            has_correct_answer = False
        file_string = "{},{},{},{},{}\n".format(title, subscribers, published, answers, str(has_correct_answer))
        # filewriter.writerow(file_string)
        f.write(file_string)

    try:
        next_btn = driver.find_element_by_partial_link_text("Следующи")
        next_btn.click()
    except NoSuchElementException:
        print("Last page")
        next_btn = False

driver.close()

