import pytest
from api_client import api
#проект
created_project_id = ""


def test_post_project_positive():
    """1. Позитивный POST: Создаем проект"""
    global created_project_id
    good_body = {"title": "Новый автотест проект"}

    result = api.create_project(good_body)
    assert result.status_code == 201

    created_project_id = result.json()["id"]


def test_get_project_positive():
    """2. Позитивный GET: Получаем проект"""
    global created_project_id

    result = api.get_project(created_project_id)
    assert result.status_code == 200
    assert result.json()["title"] == "Новый автотест проект"


def test_put_project_positive():
    global created_project_id
    update_body = {"title": "Измененное имя автотеста"}

    api.update_project(created_project_id, update_body)

    get_result = api.get_project(created_project_id)

    assert get_result.status_code == 200
    assert get_result.json()["title"] == "Измененное имя автотеста"