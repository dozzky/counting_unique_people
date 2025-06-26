from typing import Any
import json
import os
from datetime import datetime
from typing import Any, List, Dict

def crop_face(frame: Any, location: tuple[int, int, int, int]) -> Any:
    """
    Вырезает лицо из кадра по координатам.

    :param frame: Исходный кадр (BGR)
    :param location: Координаты (top, right, bottom, left)
    :return: Изображение вырезанного лица
    """
    top, right, bottom, left = location
    return frame[top:bottom, left:right]

def save_metadata(data: List[Dict[str, Any]], filepath: str) -> None:
    """
    Сохраняет метаданные лиц в JSON файл.

    :param data: Список словарей с метаданными (например, координаты, ID, timestamp)
    :param filepath: Путь к файлу для сохранения
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {data}\n")

def save_log(message: str, log_path: str) -> None:
    """
    Добавляет сообщение с текущим временем в лог-файл.

    :param message: Текст сообщения
    :param log_path: Путь к лог-файлу
    """
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")
