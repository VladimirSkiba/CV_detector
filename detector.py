import cv2


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def set_video_params():
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cam.set(cv2.CAP_PROP_FPS, 15)

def set_image_params(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          # 1. Перевод в градации серого
    blur = cv2.GaussianBlur(gray, (5, 5), 0)                # 2. Размытие для удаления шума
    _, thresh = cv2.threshold(blur, 0, 255, 
                              cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # 3. Бинаризация Оцу
    return thresh






show = True

set_video_params()

while True:
    success, img = cam.read()
    
    if not success:
        break

    img = set_image_params(img)

    if show:
        cv2.imshow("SHOW", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Корректное освобождение ресурсов
cam.release()
cv2.destroyAllWindows()