import pytest
from sqlalchemy import create_engine
from subject_table import SubjectTable

DB_URL = "postgresql://postgres@localhost:5432/QA"
db = create_engine(DB_URL, echo=True)


@pytest.fixture
def subject_db():
    return SubjectTable(db)


# ТЕСТ 1: ДОБАВЛЕНИЕ
def test_add_subject(subject_db):
    sub_id = None
    try:
        sub_id = subject_db.create("Высшая математика")
        # Проверяем, что ID вернулся и это не None
        assert sub_id is not None

        subject = subject_db.get_by_id(sub_id)
        # Проверяем, что запись нашлась и её имя совпадает
        assert subject is not None
        assert subject["subject_title"] == "Высшая математика"
    finally:
        if sub_id:
            subject_db.delete(sub_id)


# ТЕСТ 2: ИЗМЕНЕНИЕ
def test_edit_subject(subject_db):
    sub_id = None
    try:
        sub_id = subject_db.create("Старая Физика")
        assert sub_id is not None

        subject_db.update(sub_id, "Квантовая Физика")

        subject = subject_db.get_by_id(sub_id)
        assert subject is not None
        assert subject["subject_title"] == "Квантовая Физика"
    finally:
        if sub_id:
            subject_db.delete(sub_id)


# ТЕСТ 3: УДАЛЕНИЕ
def test_delete_subject(subject_db):
    sub_id = subject_db.create("Предмет на удаление")
    assert sub_id is not None

    subject_db.delete(sub_id)

    # Проверяем, что предмета больше нет в базе (get_by_id должен вернуть None)
    subject = subject_db.get_by_id(sub_id)
    assert subject is None
