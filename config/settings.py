import os

# Путь к видеофайлу для обработки
VIDEO_PATH = "input_video.mp4"

# Частота извлечения кадров (каждый N-ый кадр)
FRAME_INTERVAL = 5

# Пороговое значение расстояния для определения уникальности лиц
FACE_DISTANCE_THRESHOLD = 0.65

# Директория для сохранения найденных уникальных лиц
FACES_OUTPUT_DIR = "output/faces"
os.makedirs(FACES_OUTPUT_DIR, exist_ok=True)
