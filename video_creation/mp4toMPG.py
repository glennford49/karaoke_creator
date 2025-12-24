import cv2
import subprocess

# === SETTINGS ===
fps = 30
duration_seconds = 75
total_frames = int(fps * duration_seconds)

# === LOAD BACKGROUND IMAGE ===
bg_image = cv2.imread("img/karaoke_bg.jpg")
if bg_image is None:
    print("Error: Cannot load background images")
    exit()

frame_height, frame_width = bg_image.shape[:2]

# === LOAD OVERLAY IMAGE ===
image = cv2.imread("img/k101.jpg", cv2.IMREAD_UNCHANGED)
if image is None:
    print("Error: Cannot load overlay images")
    exit()

# === TEXT SETTINGS ===
text_h = "Karaoke_101"
text_v = "Subscribe !"
font = cv2.FONT_HERSHEY_TRIPLEX
font_scale = 1.5
color = (203, 192, 255)
thickness = 2

(text_width_h, text_height_h), _ = cv2.getTextSize(text_h, font, font_scale, thickness)
(text_width_v, text_height_v), _ = cv2.getTextSize(text_v, font, font_scale, thickness)

desired_img_height = text_height_h + 30
scale = desired_img_height / image.shape[0]
new_img_width = int(image.shape[1] * scale)
image_resized = cv2.resize(image, (new_img_width, desired_img_height), interpolation=cv2.INTER_AREA)

# watermark
cv2.circle(bg_image, (2705, 1420), 50, (0, 0, 0), -1)
cv2.putText(bg_image, text_h, (2250,1400), font, 2.3, (255,255,255), 30, cv2.LINE_AA)
cv2.putText(bg_image, text_h, (2250,1400), font, 2.3, (0,0,0), 18, cv2.LINE_AA)
cv2.putText(bg_image, text_h, (2250,1400), font, 2.3, (0,255,255), 8, cv2.LINE_AA)

# === SLIDER POSITIONS ===
x_pos_h = 0.0
direction_h = 1
y_pos_h = 60

y_pos_v = 60.0
direction_v = 1
x_pos_v = 10

step_h = image.shape[1] * 0.0038
step_v = image.shape[0] * 0.00227

# === VIDEO WRITER (SAFE AVI) ===
fourcc = cv2.VideoWriter_fourcc(*'X','V','I','D')
out = cv2.VideoWriter("temp.avi", fourcc, fps, (frame_width, frame_height))

# === FRAME GENERATION LOOP ===
for _ in range(total_frames):
    frame = bg_image.copy()

    x_pos_h += step_h * direction_h
    ix_pos_h = int(x_pos_h)
    total_width = new_img_width + 5 + text_width_h
    if ix_pos_h + total_width >= frame_width or ix_pos_h <= 0:
        direction_h *= -1
        x_pos_h = max(0, min(frame_width - total_width - 1, x_pos_h))

    y_pos_v += step_v * direction_v
    iy_pos_v = int(y_pos_v)
    if iy_pos_v >= frame_height - text_height_v or iy_pos_v <= text_height_v:
        direction_v *= -1
        y_pos_v = max(text_height_v + 1, min(frame_height - text_height_v - 1, y_pos_v))

    y_img = int(y_pos_h - image_resized.shape[0] // 1.5)
    if image_resized.shape[2] == 4:
        roi = frame[y_img:y_img + image_resized.shape[0], ix_pos_h:ix_pos_h + new_img_width]
        alpha_s = image_resized[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        for c in range(3):
            roi[:, :, c] = (alpha_s * image_resized[:, :, c] + alpha_l * roi[:, :, c])
    else:
        frame[y_img:y_img + image_resized.shape[0], ix_pos_h:ix_pos_h + new_img_width] = image_resized

    gap = 10
    text_x = ix_pos_h + new_img_width + gap
    cv2.putText(frame, text_h, (text_x, y_pos_h), font, font_scale, (255, 255, 255), thickness + 20, cv2.LINE_AA)
    cv2.putText(frame, text_h, (text_x, y_pos_h), font, font_scale, (0,0,0), thickness + 12, cv2.LINE_AA)
    cv2.putText(frame, text_h, (text_x, y_pos_h), font, font_scale, (0,225,225), thickness, cv2.LINE_AA)

    cv2.putText(frame, text_v, (x_pos_v, iy_pos_v), font, font_scale, (255,255,255), thickness + 20, cv2.LINE_AA)
    cv2.putText(frame, text_v, (x_pos_v, iy_pos_v), font, font_scale, (0, 0, 0), thickness + 12, cv2.LINE_AA)
    cv2.putText(frame, text_v, (x_pos_v, iy_pos_v), font, font_scale, (0,255,255), thickness, cv2.LINE_AA)

    out.write(frame)

    cv2.imshow("Preview", cv2.resize(frame, (1100, 700)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
#"""
print("AVI video saved as temp.avi")

# === Convert to MPEG with ffmpeg ===
subprocess.run([
    "C:/ffmpeg/bin/ffmpeg.exe", "-y", "-i", "temp.avi",
    "-target", "ntsc-dvd", "-aspect", "16:9",
    "outputkara.mpg"
])

print("MPEG video saved as output.mpg")
#"""