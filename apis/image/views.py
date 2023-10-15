import cv2

cap = cv2.VideoCapture('../../static/bombay_traffic.mp4')

model = cv2.CascadeClassifier('cars.xml')

frame_interval = 10 # time interval in ms

traffic_density = []

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) #dtetect cars in grayscale in the frame 'gray'
    # scale factor reduces image scale
    density = len(cars) / (frame.shape[0] * frame.shape[1])
    #minNeighbors specifies
    traffic_density.append(density)

    cv2.imshow('frame', frame)

    if cv2.waitKey(frame_interval) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(traffic_density)

