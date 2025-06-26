import numpy as np
import os
import cv2
from typing import Any
from config.settings import FACES_OUTPUT_DIR, FACE_DISTANCE_THRESHOLD

class FaceDatabase:
    """
    Класс для хранения уникальных лиц и проверки новых лиц на уникальность.
    """

    def __init__(self) -> None:
        self.known_embeddings: list[np.ndarray] = []
        self.counter = 0

    def is_unique(self, new_embedding: np.ndarray) -> bool:
        """
        Проверяет, является ли лицо уникальным.

        :param new_embedding: Вектор признаков нового лица
        :return: True, если лицо уникально
        """
        if not self.known_embeddings:
            return True

        distances = np.linalg.norm(np.array(self.known_embeddings) - new_embedding, axis=1)
        return np.all(distances > FACE_DISTANCE_THRESHOLD)

    def add_face(self, embedding: np.ndarray, face_image: Any, frame_index: int) -> None:
        """
        Добавляет новое уникальное лицо в базу и сохраняет его изображение.

        :param embedding: Вектор признаков лица
        :param face_image: Изображение лица (BGR)
        :param frame_index: Номер кадра, откуда лицо получено
        """
        self.known_embeddings.append(embedding)
        filename = f"face_{self.counter:04d}_frame_{frame_index}.jpg"
        filepath = os.path.join(FACES_OUTPUT_DIR, filename)
        cv2.imwrite(filepath, face_image)
        self.counter += 1

    def count(self) -> int:
        """
        Возвращает количество уникальных лиц в базе.
        """
        return len(self.known_embeddings)
