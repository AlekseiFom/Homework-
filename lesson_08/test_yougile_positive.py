from api_client import api


def test_project_flow():
    """Полный позитивный сценарий: создание → получение → обновление"""
    # 1. Создаём проект
    create_body = {"title": "Новый автотест проект"}
    create_result = api.create_project(create_body)
    assert create_result.status_code == 201
    project_id = create_result.json()["id"]

    get_result = api.get_project(project_id)
    assert get_result.status_code == 200
    assert get_result.json()["title"] == "Новый автотест проект"

    update_body = {"title": "Измененное имя автотеста"}
    update_result = api.update_project(project_id, update_body)
    assert update_result.status_code == 200

    get_after_update = api.get_project(project_id)
    assert get_after_update.status_code == 200
    assert get_after_update.json()["title"] == "Измененное имя автотеста"
