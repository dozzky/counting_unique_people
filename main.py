from config.settings import VIDEO_PATH, FRAME_INTERVAL
from video_processor.frame_extractor import extract_frames
from video_processor.face_detector import detect_faces
from video_processor.face_encoder import encode_faces
from video_processor.face_database import FaceDatabase
from video_processor.utils import crop_face, save_log, save_metadata

def main():
    db = FaceDatabase()

    print(f"[INFO] Обработка видео: {VIDEO_PATH}")
    i = 0
    for frame_index, frame in extract_frames(VIDEO_PATH, FRAME_INTERVAL):
        #save_log(f"Обработка кадра {frame_index}", "output/logs/run.log") # Нужно было для проверки, по факту бесполезная штука.
        face_locations = detect_faces(frame)
        if face_locations:
            embeddings = encode_faces(frame, face_locations)
            
        else:
            embeddings = []
        for loc, emb in zip(face_locations, embeddings):
            if db.is_unique(emb):
                face_img = crop_face(frame, loc)
                db.add_face(emb, face_img, frame_index)
                print(f"[+] Уникальное лицо найдено на кадре {frame_index}")
                faces_data = [{"id": i, "frame": frame_index, "location": face_locations}]
                save_metadata(faces_data, "output/logs/faces_metadata.log")
                i+=1
        

    print(f"[RESULT] Обнаружено уникальных лиц: {db.count()}")

if __name__ == "__main__":
    main()
