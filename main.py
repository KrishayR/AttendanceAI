import face_recognition
import cv2
import numpy as np
import csv
from bs4 import BeautifulSoup 
from datetime import datetime
import pandas as pd
import PIL
import random
import pandas as pd

video_capture = cv2.VideoCapture(0)
row_number = 1

id_list = []
for i in range(6):
    id = "10" + str(random.randint(1000000, 9999999))
    id_list.append(id)

people = {
    "Stephen Curry": "static/images/curry.png",
    "Elon Musk": "static/images/elon.jpg",
    "Jeff Bezos": "static/images/jeff.png",
    "Shah Rukh Khan": "static/images/khan.jpg",
    "LeBron James": "static/images/lebron.jpg",
    "Barack Obama": "static/images/obama.jpg",
}

known_face_encoding = []
known_faces_names = []

for name, path in people.items():
    image = face_recognition.load_image_file(path)
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encoding.append(encoding)
    known_faces_names.append(name)
 
students = known_faces_names.copy()
 
face_locations = []
face_encodings = []
face_names = []
s=True

with open('data.csv','a',newline = '') as f:
    lnwriter = csv.writer(f)
    lnwriter.writerow(["studentid","studentname","date","attendance"])
 
 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
 
 
 
f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)
 
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
 
            face_names.append(name)
            if name in known_faces_names:
                cv2.rectangle(frame, (0, 650), (1280, 720), (255, 255, 255), -1)
                cv2.putText(frame, name.title() + ' marked present.', (100, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (154, 63, 22), 2, cv2.LINE_AA)
 
                if name in students:
                    remove_id = random.choice(id_list)
                    students.remove(name)
                    print(students)
                    current_time = datetime.now().strftime("%A, %I:%M:%S %p")
                    with open('data.csv','a',newline = '') as f:
                        lnwriter = csv.writer(f)
                        lnwriter.writerow([row_number, remove_id, name.title(), current_time, "Present"])
                        row_number += 1 
    cv2.imshow("Attendance AI", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv2.destroyAllWindows()

f.close()
