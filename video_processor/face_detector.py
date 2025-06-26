import face_recognition
from typing import Any

def detect_faces(frame: Any) -> list[tuple[int, int, int, int]]:
    """
    Возвращает координаты лиц (top, right, bottom, left).
    """
    return face_recognition.face_locations(frame)