from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options)
driver.get(base_url)
flag = True
word_count = {}

while flag:
    elements = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[3]/div[5]'
                                                      '/div[2]/div[2]/div[2]/div').find_elements(by=By.TAG_NAME, value='li')
    for elem in elements:
        word = elem.text

        if word[0] == 'a' or word[0] == 'A':
            flag = False
            break

        if word[0] in word_count:
            word_count[word[0]] += 1
        else:
            word_count[word[0]] = 1
    driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[3]/div[5]/div[2]/div[2]/a[2]').click()

with open('word_count.csv', 'w') as file:
    for letter, count in word_count.items():
        file.write(f"{letter.upper()}, {count}\n")



