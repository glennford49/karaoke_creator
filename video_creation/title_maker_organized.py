



import cv2
import numpy as np
from moviepy import ImageSequenceClip, ImageClip
import time
from PIL import Image
import imageio
######################################################################
#robotunes   =1   my first youtube account
#karaoke_101 =2   my second youtube account

num_select= 2                               # select account of your choice
title_line1="A Smile"
title_line2 ="In Your"
title_line3 ="Heart"
singer = "Ariel Rivera"
font_adj = 6 # this will subtract the font size
singer_font = 8          # adjust if needed
thickness_adj = 10   # this will subtract the thickness
singer_thickness_adj =4 # this will subtract singer thickess
singer_thickness = int(singer_font*2.5)
title_line = 100             # first line from top range 160 to 260
l2 = 50                       # space between title1 and title2 // unit is pixel
l3 = 110                       # space between title2 and title3 // unit is pixel
duration = 35  # Total GIF duration in seconds max 35
########################################################################
len1 = len(title_line1)
len2 = len(title_line2)
len3 = len(title_line3)
max_char = max(len1,len2,len3)

char_limit = 1
sing_label= -2 # increase in number  means increase in size or fonts
shade = 40#18
bottom_line = 50            # Default offset for bottom lines
singer_line = 100           # Default offset for singer label

txt = ""
txt_size = 2.3

if num_select == 1:
    img="img/robo_bg.png"
    txt ="RoboTunes"
    saved = "C:\\Users\\glenn\\OneDrive\\Documents\\video_creation\\robo_file\\"
elif num_select == 2:
    img="img/karaoke_bg.jpg"
    txt ="Karaoke_101"
    saved = "C:\\Users\\glenn\OneDrive\\Documents\\video_creation\\karaoke101_file\\"
    txt_size = 2.0

frame= cv2.imread(img)

screen_height, screen_width, channels = frame.shape
hd_karaoke = "Crystal Clear KARAOKE"
singer_label = "singer:"
# Define font, scale, and thickness
font = cv2.FONT_HERSHEY_TRIPLEX
color = (0, 255, 255)  # Yellow color for the text
if max_char > char_limit:
    font_scale = 1  # Initial scale
    thickness =1
    img_height, img_width, _ = frame.shape
    # Determine which string has the maximum length
    max_string=""
    if max_char == len1:
        max_string = title_line1
    elif max_char == len2 :
        max_string = title_line2
    elif max_char == len3 :
        max_string = title_line3
    while True:
        text_size, _ = cv2.getTextSize(max_string, font, font_scale, thickness)
        text_width, text_height = text_size

        if text_width >= img_width - 100:  # Keep some padding
            break
        font_scale += 0.1  # Increase font scale gradually
    thickness = int(font_scale*2.5) - thickness_adj
    font_scale = font_scale-font_adj
    adjusty = int(thickness//3)
    print("thickness :",thickness)
    print("font scale:",font_scale)
# Divide the screen height into 6 equal parts
section_height = screen_height // 6
hd_offset = 220
# Get the size of the first line of text
(text_width1, text_height1), baseline1 = cv2.getTextSize(title_line1, font, font_scale, thickness)

# Get the size of the second line of text
(text_width2, text_height2), baseline2 = cv2.getTextSize(title_line2, font, font_scale, thickness)

# Get the size of the 3rd line of text
(text_width3, text_height3), baseline3 = cv2.getTextSize(title_line3, font, font_scale, thickness)

# Get the size of the singer's text
(text_width_singer, text_height_singer), baseline_singer = cv2.getTextSize(singer, font, singer_font,singer_thickness)

# Get the size of the "singer:" label

(text_width_label, text_height_label), baseline_label = cv2.getTextSize(singer_label, font, font_scale+sing_label, thickness)


# Get the size of the "HD KARAOKE" text
kara_thick = 5.9
if len(title_line3) > 1:
    kara_thick = 3
(text_width_hd, text_height_hd), baseline_hd = cv2.getTextSize(hd_karaoke, font, kara_thick, thickness-adjusty)

# Calculate the position for the first line of text (start of the second section)
x_pos_line1 = (screen_width - text_width1) // 2  # Horizontally center the text
y_pos_line1 = (section_height * 1) + title_line  # Start at the second section

# Calculate the position for the second line of text (below line 1)
x_pos_line2 = (screen_width - text_width2) // 2  # Horizontally center the text
y_pos_line2 = y_pos_line1 + text_height1 + 30  # Adjust spacing between the two lines

# Calculate the position for the second line of text (below line 1)
x_pos_line3 = (screen_width - text_width3) // 2  # Horizontally center the text
y_pos_line3 = y_pos_line2 + text_height2 + 30  # Adjust spacing between the two lines

# Calculate the position for "HD KARAOKE" (centered at the very bottom)
x_pos_hd = (screen_width - text_width_hd) // 2  # Horizontally center the text
y_pos_hd = screen_height - bottom_line  # 30 pixels from the bottom edge

# Calculate the position for the singer's text (start of the second-to-last section)
x_pos_singer = (screen_width - text_width_singer) // 2  # Horizontally center the text
y_pos_singer =  y_pos_hd-(text_height_hd+50)# Start at the bottom of the fifth section

# Calculate the position for the "singer:" label (left-aligned, 50 pixels from the left)
x_pos_label = 50  # Fixed position 50 pixels from the left
y_pos_label = y_pos_singer - text_height_label - singer_line  # Adjust spacing above the singer's text
# Place the first line of text
cv2.circle(frame, (screen_width-110,screen_height-100), 50, (0,0,0), -1)
#cv2.putText(frame, title_line1, (x_pos_line1, y_pos_line1), font, font_scale, (255,255,255), thickness+10, cv2.LINE_AA)
cv2.putText(frame, title_line1, (x_pos_line1, y_pos_line1), font, font_scale, (255,255,255), thickness+shade+10, cv2.LINE_AA)
cv2.putText(frame, title_line1, (x_pos_line1, y_pos_line1), font, font_scale, (0,0,0), thickness+shade, cv2.LINE_AA)
cv2.putText(frame, title_line1, (x_pos_line1, y_pos_line1), font, font_scale, (0,255,255), thickness, cv2.LINE_AA)


# Place the second line of text slightly below the first
cv2.putText(frame, title_line2, (x_pos_line2, y_pos_line2+l2), font, font_scale, (255,255,255), thickness+shade+10, cv2.LINE_AA)
cv2.putText(frame, title_line2, (x_pos_line2, y_pos_line2+l2), font, font_scale, (0,0,0), thickness+shade, cv2.LINE_AA)
cv2.putText(frame, title_line2, (x_pos_line2, y_pos_line2+l2), font, font_scale, (0,255,255), thickness, cv2.LINE_AA)

# Place the 3rd line of text slightly below the first
cv2.putText(frame, title_line3, (x_pos_line3, y_pos_line3+l3), font, font_scale, (255,255,255), thickness+shade+10, cv2.LINE_AA)
cv2.putText(frame, title_line3, (x_pos_line3, y_pos_line3+l3), font, font_scale, (0,0,0), thickness+shade, cv2.LINE_AA)
cv2.putText(frame, title_line3, (x_pos_line3, y_pos_line3+l3), font, font_scale, (0,255,255), thickness, cv2.LINE_AA) #screen_height, screen_width
cv2.putText(frame, txt, (screen_width-460,screen_height-80), font, txt_size, (255,255,255), 20, cv2.LINE_AA)
cv2.putText(frame, txt, (screen_width-460,screen_height-80), font, txt_size, (255,0,0), 5, cv2.LINE_AA)

if len(title_line3) > 1:
    # Place the artist text at the calculated position
    #singer = "test"
    cv2.putText(frame, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (0,0, 0), (singer_thickness+36), cv2.LINE_AA)
    cv2.putText(frame, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255, 0, 0), (singer_thickness+16), cv2.LINE_AA)
    cv2.putText(frame, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255, 255, 255), (singer_thickness), cv2.LINE_AA)

    # Place the "HD KARAOKE" text at the bottom of the frame
    cv2.putText(frame, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (255,255,255), 30, cv2.LINE_AA)
    cv2.putText(frame, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (0,0,0), (20), cv2.LINE_AA)
    cv2.putText(frame, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, ((0, 255, 255)), 10, cv2.LINE_AA)
else:
    # Place the artist text at the calculated position
    #cv2.putText(frame, singer, (x_pos_singer, y_pos_singer+10), font, singer_font, (255, 255, 255), (singer_thickness+16), cv2.LINE_AA)
    #cv2.putText(frame, singer, (x_pos_singer, y_pos_singer+10), font, singer_font, (64, 0, 0), (singer_thickness), cv2.LINE_AA)
    #cv2.putText(frame, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255,255,255), (singer_thickness+56), cv2.LINE_AA)
    cv2.putText(frame, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (0,0, 0), (singer_thickness+36), cv2.LINE_AA)
    cv2.putText(frame, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255, 0, 0), (singer_thickness+16), cv2.LINE_AA)
    cv2.putText(frame, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255, 255, 255), (singer_thickness), cv2.LINE_AA)

    # Place the "HD KARAOKE" text at the bottom of the frame
    cv2.putText(frame, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (255,255,255), 40, cv2.LINE_AA)
    cv2.putText(frame, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (0,0,0), (30), cv2.LINE_AA)
    cv2.putText(frame, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, ((0, 255, 255)), 15, cv2.LINE_AA)

def create_frame(color):
    frame_copy = cv2.imread(img)
    if frame_copy is None:
        print("Error: Could not read image. Please make sure 'images/sunset2.jpg' exists.")
        return None
    # Place the first line of text
    cv2.putText(frame_copy, title_line1, (x_pos_line1, y_pos_line1), font, font_scale, (0,0,0), thickness+shade, cv2.LINE_AA)
    cv2.putText(frame_copy, title_line1, (x_pos_line1, y_pos_line1), font, font_scale, (color), thickness, cv2.LINE_AA)


    # Place the second line of text slightly below the first
    cv2.putText(frame_copy, title_line2, (x_pos_line2, y_pos_line2+l2), font, font_scale, (0,0,0), thickness+shade, cv2.LINE_AA)
    cv2.putText(frame_copy, title_line2, (x_pos_line2, y_pos_line2+l2), font, font_scale, (color), thickness, cv2.LINE_AA)

    # Place the 3rd line of text slightly below the first
    cv2.putText(frame_copy, title_line3, (x_pos_line3, y_pos_line3+l3), font, font_scale, (0,0,0), thickness+shade, cv2.LINE_AA)
    cv2.putText(frame_copy, title_line3, (x_pos_line3, y_pos_line3+l3), font, font_scale, (color), thickness, cv2.LINE_AA)

    ##################
    if len(title_line3) > 1:
        # Place the artist text at the calculated position
        #singer = "test"
        cv2.putText(frame_copy, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255, 0, 0), (singer_thickness+16), cv2.LINE_AA)
        cv2.putText(frame_copy, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255, 255, 255), (singer_thickness), cv2.LINE_AA)

        # Place the "HD KARAOKE" text at the bottom of the frame
        cv2.putText(frame_copy, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (255,255,255), 20+shade, cv2.LINE_AA)
        cv2.putText(frame_copy, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (0,0,0), (10+shade), cv2.LINE_AA)
        cv2.putText(frame_copy, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (color), 10, cv2.LINE_AA)
    else:
        # Place the artist text at the calculated position
        #cv2.putText(frame_copy, singer, (x_pos_singer, y_pos_singer+10), font, singer_font, (255, 255, 255), (singer_thickness+16), cv2.LINE_AA)
        #cv2.putText(frame_copy, singer, (x_pos_singer, y_pos_singer+10), font, singer_font, (64, 0, 0), (singer_thickness), cv2.LINE_AA)
        cv2.putText(frame_copy, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255, 0, 0), (singer_thickness+16), cv2.LINE_AA)
        cv2.putText(frame_copy, singer, (x_pos_singer, (y_pos_hd)-text_height_hd), font, singer_font, (255, 255, 255), (singer_thickness), cv2.LINE_AA)

        # Place the "HD KARAOKE" text at the bottom of the frame
        cv2.putText(frame_copy, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (255,255,255), 35+shade, cv2.LINE_AA)
        cv2.putText(frame_copy, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (0,0,0), (25+shade), cv2.LINE_AA)
        cv2.putText(frame_copy, hd_karaoke, (x_pos_hd-hd_offset, y_pos_hd+30), font, kara_thick, (color), 25, cv2.LINE_AA)
    ############3####
    return frame_copy
def gif_create():
    # Generate frames with different colors
    frame1 = create_frame((0, 255, 255))  # Yellow
    frame2 = create_frame((0, 0, 255))    # Blue
    frame3 = create_frame((255, 204, 0))  # Light Blue

    # Check if frame creation was successful
    if not all(frame is not None for frame in [frame1, frame2, frame3]):
        print("Error: Could not create all frames. Please check image path.")
    else:
        frames = [cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB), cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB), cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)]

        
        fps = 1  # Frames per second (1 frame per second)

        total_frames = duration * fps
        looped_frames = []
        for i in range(total_frames):
            looped_frames.append(frames[i % 3]) #looping frames

        clip = ImageSequenceClip(looped_frames, fps=fps)
        clip.write_gif('universal.gif', fps=fps)

        print("GIF saved")

        gif_path = "universal.gif"
        try:
            gif = imageio.mimread(gif_path)  # Read all frames
            scale_percent = 90  # Resize to 90% of original size (adjust as needed)
            # You can add resizing logic here if needed, but the error suggests memory issues with reading.
            print(f"GIF read successfully with {len(gif)} frames.")
        except RuntimeError as e:
            print(f"Error reading GIF: {e}")
            print("Consider reducing the GIF duration or the number of frames to avoid memory issues.")
    time.sleep(3)
while True:
    res= cv2.resize(frame,(1024,700))
    cv2.imshow("Movie Title", res)
    key = cv2.waitKey(1) & 0xFF  # Only call it once
    
    if key == ord('q'):
        cv2.imwrite(saved + txt + "_title.jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
        #cv2.imwrite(saved+txt+"_title.jpg", frame)
        cv2.destroyAllWindows()
        break
    elif key == ord('w'):
        cv2.imwrite(saved + txt + "_title.jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
        #cv2.imwrite(txt+"_title.jpg", frame)
        cv2.destroyAllWindows()
        gif_create()
        time.sleep(4)
        break



