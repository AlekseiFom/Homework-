import random
from sqlalchemy import Engine, text


class SubjectTable:
    def __init__(self, db_engine: Engine):
        self.db = db_engine

    def create(self, title: str) -> int:
        """Добавляет предмет с вручную сгенерированным ID и возвращает его"""
        with self.db.begin() as connection:
            # 1. Генерируем случайное число для ID (например, от 1000 до 99999)
            generated_id = random.randint(1000, 99999)

            # 2. Передаем этот ID в INSERT принудительно
            sql = text('INSERT INTO subject(subject_id, '
                       'subject_title) VALUES (:id, :title)')
            connection.execute(sql, {"id": generated_id, "title": title})

            # 3. Возвращаем этот ID обратно в тест
            return generated_id

    def get_by_id(self, subject_id: int) -> dict | None:
        """Получает предмет по subject_id в виде словаря"""
        with (self.db.begin() as connection):
            sql = text("SELECT * FROM subject WHERE subject_id = :id")
            result = connection.execute(sql, {"id": subject_id
                                              }).mappings().first()
            return dict(result) if result else None

    def update(self, subject_id: int, new_title: str) -> None:
        """Обновляет название предмета по его subject_id"""
        with self.db.begin() as connection:
            sql = text("UPDATE subject SET "
                       "subject_title = :new_title WHERE subject_id = :id")
            connection.execute(sql, {"new_title": new_title, "id": subject_id})

    def delete(self, subject_id: int) -> None:
        """Удаляет предмет по subject_id"""
        with self.db.begin() as connection:
            sql = text("DELETE FROM subject WHERE subject_id = :id")
            connection.execute(sql, {"id": subject_id})
