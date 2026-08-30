import pytest
from selenium import webdriver
from dataclasses import dataclass

@pytest.fixture()
def text_box_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-guru.github.io/one-page-form/text-box")

    yield driver

    driver.quit()


@dataclass()
class TestData():
    full_name: str
    email: str
    current_address: str
    permanent_address: str