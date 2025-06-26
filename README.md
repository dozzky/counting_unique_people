## Пояснения

| Файл / Директория    | Назначение                                                           |
| -------------------- | -------------------------------------------------------------------- |
| `main.py`            | Основной скрипт запуска, связывает все модули.                       |
| `frame_extractor.py` | Извлекает кадры из видео на основе заданной частоты.                 |
| `face_detector.py`   | Использует `face_recognition` для детекции лиц.                      |
| `face_encoder.py`    | Генерирует эмбеддинги лиц.                                           |
| `face_database.py`   | Хранит эмбеддинги и изображения уникальных лиц, сравнивает новых.    |
| `utils.py`           | Универсальные утилиты: сохранение изображений, логирование, метрики. |
| `settings.py`        | Настройки: путь к видео, FPS, пороги, логика сохранения.             |
| `output/faces/`      | Кадры с уникальными лицами сохраняются сюда.                         |
| `output/logs/`       | Лог-файлы.                                                           |
| `requirements.txt`   | Всё, что нужно установить.                                           |
| `README.md`          | Документация, инструкция по установке и использованию.               |


При желании можно заменить `face_recognition` на другую библиотеку.

## Инструкция

### Установка системных зависимостей

1. sudo apt update && sudo apt upgrade -y

2. sudo apt install -y build-essential cmake libboost-all-dev libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev python3-dev python3-pip

### Запуск виртуалки

3.  pip install --upgrade virtualenv

4. python3 -m venv env_count

5. source env_count/bin/activate

### Установка зависимостей

6. pip install --upgrade pip

7. pip install -r requirements.txt

### Запуск скрипта

8. Настраиваем под себя `config/settings.py` - указываем путь к файлу, частоту и пороговое значения для лиц (0.65 в моем случае работало лучше всего).

9. python3 main.py
