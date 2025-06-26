import cv2
from typing import Generator

def extract_frames(video_path: str, frame_interval: int) -> Generator[tuple[int, any], None, None]:
    """
    Извлекает каждый N-ый кадр из видео.

    :param video_path: Путь к видеофайлу
    :param frame_interval: Интервал между кадрами
    :yield: Кортеж (индекс кадра, изображение)
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Не удалось открыть видео: {video_path}")

    index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if index % frame_interval == 0:
            yield index, frame
        index += 1

    cap.release()
