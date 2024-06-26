import cv2
import time
import datetime
import cv2.data
import time


# Teller ned til koden starter
def countdown_timer(seconds):
    for i in range(30, seconds, -10):
        print(f"Starting in {i} seconds...")
        time.sleep(10)

#Sier at koden har startet
def main_code():
    print("Your main code is now running!")

countdown_duration = 0

countdown_timer(countdown_duration)

main_code()

cap = cv2.VideoCapture(0)

# Face library
face_cascade =(cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"))
#body_cascade =cv2.CascadeClassifier(
    #cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int)(cap.get(3)), int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")


# Firkant på face, med farge
while True:
    f, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    #bodies = face_cascade.detectMultiScale(gray, 1.3, 5)


# Lagerer video filer, med navn
    if len(faces) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("started recording")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time > SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print('Stop Recording')
        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break


out.release()
cap.release()
cv2.destroyAllWindows()

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=3000, debug=True)