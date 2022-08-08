import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLk:

    def test_registration(self): #Успешная регистрация
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()  #кнопка Зарегистрироваться
        elements = driver.find_elements(By.XPATH, './/input')
        elements[0].send_keys('zxcv')
        elements = driver.find_elements(By.XPATH, './/input')
        elements[1].send_keys('vbnm@ya.ru')
        elements = driver.find_elements(By.XPATH, './/input')
        elements[2].send_keys('wwwwwy1wwww')
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()  #кнопка Зарегистрироваться
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))


        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()

    def test_registration_error_password(self, get_random_name=None):  # Ошибка для некорректного пароля
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()  #кнопка Зарегистрироваться
        elements = driver.find_elements(By.XPATH, './/input')
        elements[0].send_keys('kdsf')
        elements = driver.find_elements(By.XPATH, './/input')
        elements[1].send_keys('gg1g1tкfрg1@ya.ru')
        elements = driver.find_elements(By.XPATH, './/input')
        elements[2].send_keys('1')
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()  #кнопка Зарегистрироваться
        assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']")

        driver.quit()

    def test_click_on_Log_on(self):  # вход по кнопке «Войти в аккаунт» на главной
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  #кнопка Войти в аккаунт
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
        driver.find_element(By.NAME, 'name').send_keys('nina_pechurkina_1_555@yandex.ru')  #поле ввода имени
        driver.find_element(By.NAME, 'Пароль').send_keys('qwerty')  #поле ввода почты
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  #поле ввода пароля
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")  #кнопка Оформить заказ

        driver.quit()

    def test_click_on_LK(self):  # вход через кнопку «Личный кабинет»
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
        driver.find_element(By.NAME, 'name').send_keys('nina_pechurkina_1_555@yandex.ru')  #поле ввода имени
        driver.find_element(By.NAME, 'Пароль').send_keys('qwerty')  #поле ввода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  #кнопка Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")  #кнопка Оформить заказ

        driver.quit()

    def test_click_on_registration_form(self):  #вход через кнопку в форме регистрации
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  #кнопка Войти
        driver.find_element(By.NAME, 'name').send_keys('nina_pechurkina_1_555@yandex.ru')  #поле ввода имени
        driver.find_element(By.NAME, 'Пароль').send_keys('qwerty')  #поле ввода пароля
        time.sleep(3)
        driver.find_element(By.XPATH, './/html/body/div/div/main/div/form/button').click()  #кнопка Войти
        time.sleep(5)

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")  #кнопка Оформить заказ
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_click_on_password_recovery_form(self): #вход через кнопку в форме восстановления пароля
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')

        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click()  #кнопка Восстановить пароль
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()  #кнопка Войти
        driver.find_element(By.NAME, 'name').send_keys('nina_pechurkina_1_555@yandex.ru')  #поле ввода имени
        driver.find_element(By.NAME, 'Пароль').send_keys('qwerty')  #поле ввода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  #кнопка Войти
        WebDriverWait(driver, 3).until(
             expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_click_through_lk(self): #Проверь переход по клику на «Личный кабинет»
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  #кнопка Войти в аккаунт
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
        driver.find_element(By.NAME, 'name').send_keys('nina_pechurkina_1_555@yandex.ru')  #поле ввода имени
        driver.find_element(By.NAME, 'Пароль').send_keys('qwerty')  #поле ввода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  #кнопка Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")  #кнопка Оформить заказ
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_click_on_the_constructor(self): #переход по клику на «Конструктор»
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  #кнопка Войти в аккаунт
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
        driver.find_element(By.NAME, 'name').send_keys('nina_pechurkina_1_555@yandex.ru')  #поле ввода имени
        driver.find_element(By.NAME, 'Пароль').send_keys('qwerty')  #поле ввода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  #кнопка Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")  #кнопка Оформить заказ
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()  #кнопка Конструктор
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_click_on_the_Stellar_Burgers(self): #переход по клику на «Stellar Burgers»
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  #кнопка Войти в аккаунт
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
        driver.find_element(By.NAME, 'name').send_keys('nina_pechurkina_1_555@yandex.ru')  #поле ввода имени
        driver.find_element(By.NAME, 'Пароль').send_keys('qwerty')  #поле ввода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  #кнопка Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")  #кнопка Оформить заказ
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))

        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/div/a').click()  #кнопка «Stellar Burgers»

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_logout(self): #выход по кнопке «Выйти» в личном кабинете
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()  #кнопка Войти в аккаунт
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//a[text()='Зарегистрироваться']")))
        driver.find_element(By.NAME, 'name').send_keys('nina_pechurkina_1_555@yandex.ru')  #поле ввода имени
        driver.find_element(By.NAME, 'Пароль').send_keys('qwerty')  #поле ввода пароля
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()  #кнопка Войти
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()  #кнопка Личный кабинет
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Выход']")))
        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()  #кнопка
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text()='Войти']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_moving_on_to_buns(self): #Переход к булкам
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click() #соусы
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]').click() #булочки

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')  #подзаголовок булок


    def test_moving_on_to_sauces(self): #Переход к соусам
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click() #соусы

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]')  #подзаголовок соусов


    def test_moving_on_to_stuffing(self): #Переход к начинкам
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()  # начинки

        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')  #подзаголовок начинок












