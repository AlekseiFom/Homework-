from api_client import api


created_project_id = ""


def test_post_project_positive():
    global created_project_id
    result = api.create_project({"title": "Новый автотест проект"})
    assert result.status_code == 201
    created_project_id = result.json()["id"]


def test_get_project_positive():
    result = api.get_project(created_project_id)
    assert result.status_code == 200
    assert result.json()["title"] == "Новый автотест проект"


def test_put_project_positive():
    api.update_project(created_project_id,
                       {"title": "Измененное имя автотеста"})
    get_result = api.get_project(created_project_id)
    assert get_result.status_code == 200
    assert get_result.json()["title"] == "Измененное имя автотеста"
