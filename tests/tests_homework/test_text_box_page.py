import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

def test_fill_all_fields_in_russian(text_box_page):
    print("Тест 1: Заполнить все поля валидными данными на русском языке")

    full_name = 'Василий алибабаев'
    user_email = 'vasiliy-a@mail.com'
    current_address = 'Улица Строителей, дом 25, квартира 13, г. Лениград, РСФСР, 127000'
    permanent_address = 'Улица Строителей, дом 25, квартира 13, г. Москва-Столица, РСФСР, 125000'

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    current_address_field = text_box_page.find_element(By.ID, "currentAddress")
    permanent_address_field = text_box_page.find_element(By.ID, "permanentAddress")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)
    submit_button.click()

    print(output_field.text, '\n')

    assert output_field is not None
    assert full_name in output_field.text
    assert user_email in output_field.text
    assert current_address in output_field.text
    assert permanent_address in output_field.text


def test_fill_all_fields_in_inglish(text_box_page):
    print("Тест 2: Заполнить все поля валидными данными на английском языке")

    full_name = 'Dean Potter'
    user_email = 'dean.p@mail.com'
    current_address = '12-34 Red Dot str, 14320 LA'
    permanent_address = '13 McAvery Drive, 14321 LA'

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    current_address_field = text_box_page.find_element(By.ID, "currentAddress")
    permanent_address_field = text_box_page.find_element(By.ID, "permanentAddress")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)
    submit_button.click()

    print(output_field.text, '\n')

    assert output_field is not None
    assert full_name in output_field.text
    assert user_email in output_field.text
    assert current_address in output_field.text
    assert permanent_address in output_field.text


def test_fill_name_and_email(text_box_page):
    print("Тест 3: Заполнить только поля \"Full name\" и \"Email\"")

    full_name = 'Dean Potter'
    user_email = 'dean.p@mail.com'

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")
    output_cur_addr_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Current Address :')]"))
    output_per_addr_field = (text_box_page.find_element(By.XPATH,"//*[contains(text(), 'Permananet Address :')]"))

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    submit_button.click()

    print(output_field.text, '\n')

    assert output_field is not None
    assert f'Name:{full_name}' in output_field.text
    assert f'Email:{user_email}' in output_field.text
    assert output_cur_addr_field.text == ''
    assert output_per_addr_field.text == ''


def test_submit_empty_form(text_box_page):
    print("Тест 4: Подтвердить форму с незаполненными полями")

    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")
    output_name_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Name:')]"))
    output_email_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Email:')]"))
    output_cur_addr_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Current Address :')]"))
    output_per_addr_field = (text_box_page.find_element(By.XPATH,"//*[contains(text(), 'Permananet Address :')]"))

    submit_button.click()

    print(output_field.text, '\n')

    assert output_field is not None
    assert output_name_field.text == ''
    assert output_email_field.text == ''
    assert output_cur_addr_field.text == ''
    assert output_per_addr_field.text == ''


def test_submit_email_without_full_domain_name(text_box_page):
    print("Тест 5: Заполнить поле \"Email\" без домена и подтвердить форму")

    full_name = 'Dean Potter'
    user_email = 'dean.p@'
    current_address = '12-34 Red Dot str, 14320 LA'
    permanent_address = '13 McAvery Drive, 14321 LA'

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    current_address_field = text_box_page.find_element(By.ID, "currentAddress")
    permanent_address_field = text_box_page.find_element(By.ID, "permanentAddress")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")
    output_name_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Name:')]"))
    output_email_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Email:')]"))
    output_cur_addr_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Current Address :')]"))
    output_per_addr_field = (text_box_page.find_element(By.XPATH,"//*[contains(text(), 'Permananet Address :')]"))

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)
    submit_button.click()

    tooltip_text = text_box_page.execute_script("return arguments[0].validationMessage;", mail_field)
    print(f"Текст предупреждения: {tooltip_text}")

    print(output_field.text, '\n')

    assert user_email in tooltip_text
    assert tooltip_text == f'Введите часть адреса после символа "@". Адрес "{user_email}" неполный.'
    assert output_field is not None
    assert output_name_field.text == ''
    assert output_email_field.text == ''
    assert output_cur_addr_field.text == ''
    assert output_per_addr_field.text == ''


def test_submit_email_without_domain(text_box_page):
    print("Тест 6: Заполнить поле \"Email\" без указания неймспейса домена и подтвердить форму")

    full_name = 'Dean Potter'
    user_email = 'dean.p@.ru'
    current_address = '12-34 Red Dot str, 14320 LA'
    permanent_address = '13 McAvery Drive, 14321 LA'
    user_email_domain = user_email.split('.')[2]
    print(user_email_domain)

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    current_address_field = text_box_page.find_element(By.ID, "currentAddress")
    permanent_address_field = text_box_page.find_element(By.ID, "permanentAddress")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")
    output_name_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Name:')]"))
    output_email_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Email:')]"))
    output_cur_addr_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Current Address :')]"))
    output_per_addr_field = (text_box_page.find_element(By.XPATH,"//*[contains(text(), 'Permananet Address :')]"))

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)
    submit_button.click()

    tooltip_text = text_box_page.execute_script("return arguments[0].validationMessage;", mail_field)
    print(f"Текст предупреждения: {tooltip_text}")

    print(output_field.text, '\n')

    assert user_email_domain in tooltip_text
    assert tooltip_text == f'Недопустимое положение символа "." в адресе ".{user_email_domain}".'
    assert output_field is not None
    assert output_name_field.text == ''
    assert output_email_field.text == ''
    assert output_cur_addr_field.text == ''
    assert output_per_addr_field.text == ''


def test_submit_email_without_at_symbol(text_box_page):
    print("Тест 7: Заполнить поле \"Email\" без символа \"@\" и подтвердить форму")

    full_name = 'Dean Potter'
    user_email = 'dean.p dfddf.com'
    current_address = '12-34 Red Dot str, 14320 LA'
    permanent_address = '13 McAvery Drive, 14321 LA'

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    current_address_field = text_box_page.find_element(By.ID, "currentAddress")
    permanent_address_field = text_box_page.find_element(By.ID, "permanentAddress")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")
    output_name_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Name:')]"))
    output_email_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Email:')]"))
    output_cur_addr_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Current Address :')]"))
    output_per_addr_field = (text_box_page.find_element(By.XPATH,"//*[contains(text(), 'Permananet Address :')]"))

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)
    submit_button.click()

    tooltip_text = text_box_page.execute_script("return arguments[0].validationMessage;", mail_field)
    print(f"Текст предупреждения: {tooltip_text}")

    print(output_field.text, '\n')

    assert user_email in tooltip_text
    assert tooltip_text == (f'Адрес электронной почты должен содержать символ "@". '
                            f'В адресе "{user_email}" отсутствует символ "@".')
    assert output_field is not None
    assert output_name_field.text == ''
    assert output_email_field.text == ''
    assert output_cur_addr_field.text == ''
    assert output_per_addr_field.text == ''


def test_submit_email_with_with_parenthesis_symbol(text_box_page):
    print("Тест 8: Заполнить поле \"Email\" c символом \"(\" и подтвердить форму")

    full_name = 'Dean Potter'
    user_email = 'dean.p@df(ddf.com'
    current_address = '12-34 Red Dot str, 14320 LA'
    permanent_address = '13 McAvery Drive, 14321 LA'

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    current_address_field = text_box_page.find_element(By.ID, "currentAddress")
    permanent_address_field = text_box_page.find_element(By.ID, "permanentAddress")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")
    output_name_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Name:')]"))
    output_email_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Email:')]"))
    output_cur_addr_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Current Address :')]"))
    output_per_addr_field = (text_box_page.find_element(By.XPATH,"//*[contains(text(), 'Permananet Address :')]"))

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)
    submit_button.click()

    tooltip_text = text_box_page.execute_script("return arguments[0].validationMessage;", mail_field)
    print(f"Текст предупреждения: {tooltip_text}")

    print(output_field.text, '\n')

    assert "(" in tooltip_text
    assert tooltip_text == (f'Часть адреса после символа "@" не должна содержать символ "(".')
    assert output_field is not None
    assert output_name_field.text == ''
    assert output_email_field.text == ''
    assert output_cur_addr_field.text == ''
    assert output_per_addr_field.text == ''


def test_submit_email_with_duplicated_at_symbol(text_box_page):
    print("Тест 9: Заполнить поле \"Email\" c задублированным символом \"@\" и подтвердить форму")

    full_name = 'Dean Potter'
    user_email = 'dean@.p@dfddf.com'
    current_address = '12-34 Red Dot str, 14320 LA'
    permanent_address = '13 McAvery Drive, 14321 LA'

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    current_address_field = text_box_page.find_element(By.ID, "currentAddress")
    permanent_address_field = text_box_page.find_element(By.ID, "permanentAddress")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")
    output_name_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Name:')]"))
    output_email_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Email:')]"))
    output_cur_addr_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Current Address :')]"))
    output_per_addr_field = (text_box_page.find_element(By.XPATH,"//*[contains(text(), 'Permananet Address :')]"))

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)
    submit_button.click()

    tooltip_text = text_box_page.execute_script("return arguments[0].validationMessage;", mail_field)
    print(f"Текст предупреждения: {tooltip_text}")

    print(output_field.text, '\n')

    assert '@' in tooltip_text
    assert tooltip_text == (f'Часть адреса после символа "@" не должна содержать символ "@".')
    assert output_field is not None
    assert output_name_field.text == ''
    assert output_email_field.text == ''
    assert output_cur_addr_field.text == ''
    assert output_per_addr_field.text == ''


def test_submit_email_without_host_name(text_box_page):
    print("Тест 10: Заполнить поле \"Email\" без имени хоста и подтвердить форму")

    full_name = 'Dean Potter'
    user_email = '@dfddf.com'
    current_address = '12-34 Red Dot str, 14320 LA'
    permanent_address = '13 McAvery Drive, 14321 LA'

    full_name_field = text_box_page.find_element(By.ID, "userName")
    mail_field = text_box_page.find_element(By.ID, "userEmail")
    current_address_field = text_box_page.find_element(By.ID, "currentAddress")
    permanent_address_field = text_box_page.find_element(By.ID, "permanentAddress")
    submit_button = text_box_page.find_element(By.ID, "submit")
    output_field = text_box_page.find_element(By.ID, "output")
    output_name_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Name:')]"))
    output_email_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Email:')]"))
    output_cur_addr_field = (text_box_page.find_element(By.XPATH, "//*[contains(text(), 'Current Address :')]"))
    output_per_addr_field = (text_box_page.find_element(By.XPATH,"//*[contains(text(), 'Permananet Address :')]"))

    full_name_field.send_keys(full_name)
    mail_field.send_keys(user_email)
    current_address_field.send_keys(current_address)
    permanent_address_field.send_keys(permanent_address)
    submit_button.click()

    tooltip_text = text_box_page.execute_script("return arguments[0].validationMessage;", mail_field)
    print(f"Текст предупреждения: {tooltip_text}")

    print(output_field.text, '\n')

    assert user_email in tooltip_text
    assert tooltip_text == (f'Введите часть адреса до символа "@". Адрес "{user_email}" неполный.')
    assert output_field is not None
    assert output_name_field.text == ''
    assert output_email_field.text == ''
    assert output_cur_addr_field.text == ''
    assert output_per_addr_field.text == ''