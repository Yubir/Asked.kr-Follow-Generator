import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()

window_size = "1920,1080"  # 무조건 1920 1080 으로 설정
chrome_options.add_argument(f"--window-size={window_size}")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

while True:
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    driver.get("https://asked.kr/member/join/id")

    time.sleep(2)

    random_string = generate_random_string(20)

    #아이디 입력창
    input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[1]/input')))
    input_element.send_keys(random_string)
    print(random_string+" 의 아이디가 생성중입니다...")

    with open("log.txt", "a") as f:
        f.write(random_string + "\n")

    time.sleep(1)

    button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[2]/div')))
    button_element.click()

    #비밀번호 입력창
    time.sleep(2)

    # 비밀번호 "a123455"
    input_element1 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[1]/input')))
    input_element1.send_keys("a123455")

    time.sleep(1)

    # 확인 비밀번호 "a123455"
    input_element2 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[2]/input')))
    input_element2.send_keys("a123455")

    button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[3]/div')))
    button_element.click()

    #닉네임 설정창
    time.sleep(1)

    #닉네임 설정
    input_element3 = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[1]/input')))
    input_element3.send_keys("Yubi's Asked Bot")

    button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[2]/div')))
    button_element.click()

    button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[5]/div[2]/div[2]')))
    button_element.click()

    #이메일 설정 ( 이메일 설정 안함 / 건너뛰기 )
    time.sleep(1)

    button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[8]/div[2]/div/div[2]/div[2]/div[2]')))
    button_element.click()
    
    print(random_string+" 의 아이디가 생성되었습니다!!")

    time.sleep(1)

    #팔로우 할 아이디 검색
    button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[6]/div/div/div[2]')))
    button_element.click()

    time.sleep(2)

    # 팔로우 할 계정 아이디 입력
    input_element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[6]/div/div[1]/div/input')))
    input_element.send_keys("HERE") # <<< 팔로우 할 계정 아이디 입력하기

    #팔로우 버튼 클릭
    button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[8]/div[3]/div/div[4]/div/div[1]/div/div/div/div/div[3]/div')))
    button_element.click()

    # 비공개 팔로우
    button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/span[1]/div/div/div[3]/div[2]')))
    # 공개 팔로우
    #button_element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/span[1]/div/div/div[3]/div[1]')))
    button_element.click()
    
    print("설정한 아이디로 팔로우를 했습니다!")

    time.sleep(5)

#driver.quit()
