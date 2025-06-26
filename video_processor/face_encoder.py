import face_recognition
import cv2

def encode_faces(frame, face_locations):
    """
    Возвращает список эмбеддингов для переданных координат лиц.
    """
    try:
        # OpenCV -> RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Проверка на пустые координаты
        if not face_locations:
            return []

        # Получаем эмбеддинги
        encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        return encodings

    except Exception as e:
        print(f"[WARN] Ошибка при извлечении эмбеддингов: {e}")
        return []

