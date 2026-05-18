import pytest
from api_client import api


def test_post_project_without_title_negative():
    """1. Негативный POST: без title"""
    bad_body = {"description": "без названия"}

    result = api.create_project(bad_body)
    assert result.status_code == 400
    assert "error" in result.json()


def test_get_project_with_broken_id_negative():
    """2. Негативный GET: ломаный ID"""
    broken_id = "shashlik-mashlik"

    result = api.get_project(broken_id)
    assert result.status_code in [400, 404]
    assert "error" in result.json()


def test_put_project_with_fake_id_negative():
    """3. Негативный PUT: несуществующий UUID"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    update_body = {"title": "Новое имя"}

    result = api.update_project(fake_id, update_body)
    assert result.status_code == 404
    assert "error" in result.json()
