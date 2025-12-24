import cv2
frame= cv2.imread("img/karaoke_bg.jpg")
screen_height, screen_width, channels = frame.shape
font = cv2.FONT_HERSHEY_TRIPLEX

# Thanks for Watching,
# Subscribe for more 
# Karaoke sessions
# Enjoy Singing !
s1="Thanks for Watching ,"
s2 = "   Dont Forget"
s3 = "   To Subscribe !"
s4 = "Enjoy Singing !"
cv2.circle(frame, (screen_width-110,screen_height-110), 45, (0,0,0), -1)
#"""
cv2.putText(frame, "Interlude !", (700,300), font, 8.3, (255,255,255), 70, cv2.LINE_AA)
cv2.putText(frame, "Interlude !", (700,300), font, 8.3, (0,0,0),       60, cv2.LINE_AA)
cv2.putText(frame, "Interlude !", (700,300), font, 8.3, (0,0,255),   25, cv2.LINE_AA)

cv2.putText(frame, s1, (600,600), font, 4.5, (255,255,255),     45, cv2.LINE_AA)
cv2.putText(frame, s1, (600,600), font, 4.5, (0,0,0),           35, cv2.LINE_AA)
cv2.putText(frame, s1, (600,600), font, 4.5, (180, 230, 255),   15, cv2.LINE_AA)

cv2.putText(frame, s2, (700,800), font, 4.5, (255,255,255),     45, cv2.LINE_AA)
cv2.putText(frame, s2, (700,800), font, 4.5, (0,0,0),           35, cv2.LINE_AA)
cv2.putText(frame, s2, (700,800), font, 4.5, (180, 230, 255),   15, cv2.LINE_AA)

cv2.putText(frame, s3, (600,1000), font, 4.4, (255,255,255),     45, cv2.LINE_AA)
cv2.putText(frame, s3, (600,1000), font, 4.4, (0,0,0),           35, cv2.LINE_AA)
cv2.putText(frame, s3, (600,1000), font, 4.4, (180, 230, 255),   15, cv2.LINE_AA)

cv2.putText(frame, s4, (600,1300), font, 7.3, (255,255,255), 70, cv2.LINE_AA)
cv2.putText(frame, s4, (600,1300), font, 7.3, (0,0,0),       60, cv2.LINE_AA)
cv2.putText(frame, s4, (600,1300), font, 7.3, (0,0,255),   25, cv2.LINE_AA)

cv2.putText(frame, "by : Singalong", (screen_width-960,screen_height-50), font, 3.0, (255,255,255), 20, cv2.LINE_AA)
cv2.putText(frame, "by : Singalong", (screen_width-960,screen_height-50), font, 3.0, (255,0,0), 5, cv2.LINE_AA)
#"""


while True:
    res = cv2.resize(frame,(1100,700))
    cv2.imshow("Movie Title", res)
    key = cv2.waitKey(1) & 0xFF  # Only call it once
    if key == ord('q'):
        cv2.imwrite("interlude_img.jpg", frame)
        cv2.destroyAllWindows()
        break
    



