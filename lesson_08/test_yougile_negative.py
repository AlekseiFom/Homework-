from api_client import api


def test_post_project_without_title_negative():
    bad_body = {"description": "без названия"}
    result = api.create_project(bad_body)
    assert result.status_code == 400
    # Проверяем, что ответ — JSON, прежде чем вызывать .json()
    if result.headers.get('Content-Type', '').startswith('application/json'):
        assert "error" in result.json()
    else:
        # Если не JSON, проверяем, что текст ошибки не пустой
        assert result.text


def test_get_project_with_broken_id_negative():
    broken_id = "shashlik-mashlik"
    result = api.get_project(broken_id)
    assert result.status_code in [400, 404]
    # Аналогичная защита
    if result.headers.get('Content-Type', '').startswith('application/json'):
        assert "error" in result.json()
    else:
        assert result.text


def test_put_project_with_fake_id_negative():
    # Используем заведомо несуществующий, но валидный UUID
    fake_id = "123e4567-e89b-12d3-a456-426614174000"
    update_body = {"title": "Новое имя"}
    result = api.update_project(fake_id, update_body)
    assert result.status_code == 404
    if result.headers.get('Content-Type', '').startswith('application/json'):
        assert "error" in result.json()
    else:
        assert result.text
