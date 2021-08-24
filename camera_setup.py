import cv2 as cv

cap = cv.VideoCapture(1, cv.CAP_DSHOW)

'''
opencv python video and camera parameters reference
source : https://docs.opencv.org/4.5.1/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704dad8b57083fd9bd58e0f94e68a54b42b7e
1. Python: cv.CAP_PROP_POS_MSEC
    Current position of the video file in milliseconds.
2. Python: cv.CAP_PROP_POS_FRAMES
    0-based index of the frame to be decoded/captured next.
3. Python: cv.CAP_PROP_POS_AVI_RATIO
    Relative position of the video file: 0=start of the film, 1=end of the film.
4. Python: cv.CAP_PROP_FRAME_WIDTH [OK]
    Width of the frames in the video stream.
5. Python: cv.CAP_PROP_FRAME_HEIGHT [OK]
    Height of the frames in the video stream.
6 Python: cv.CAP_PROP_FPS [OK]
    Frame rate.
7. Python: cv.CAP_PROP_FOURCC
    4-character code of codec. see VideoWriter::fourcc .
8. Python: cv.CAP_PROP_FRAME_COUNT
    Number of frames in the video file.
9. Python: cv.CAP_PROP_FORMAT
    Format of the Mat objects (see Mat::type()) returned by VideoCapture::retrieve(). Set value -1 to fetch undecoded RAW video streams (as Mat 8UC1).
10. Python: cv.CAP_PROP_MODE
    Backend-specific value indicating the current capture mode.
11. Python: cv.CAP_PROP_BRIGHTNESS [ok]
    Brightness of the image (only for those cameras that support).
12. Python: cv.CAP_PROP_CONTRAST [ok]
    Contrast of the image (only for cameras).
13. Python: cv.CAP_PROP_SATURATION [ok]
    Saturation of the image (only for cameras).
14. Python: cv.CAP_PROP_HUE [ok]
    Hue of the image (only for cameras).
15. Python: cv.CAP_PROP_GAIN [ok]
    Gain of the image (only for those cameras that support).
16. Python: cv.CAP_PROP_EXPOSURE [ok]
    Exposure (only for those cameras that support).
17. cv.CAP_PROP_CONVERT_RGB [ok]
    Boolean flags indicating whether images should be converted to RGB.
    GStreamer note: The flag is ignored in case if custom pipeline is used. It's user responsibility to interpret pipeline output.
18  Python: cv.CAP_PROP_WHITE_BALANCE_BLUE_U
    Currently unsupported. 
19. Python: cv.CAP_PROP_RECTIFICATION
    Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently).
20. Python: cv.CAP_PROP_MONOCHROME
21. Python: cv.CAP_PROP_SHARPNESS [ok]
22. Python: cv.CAP_PROP_AUTO_EXPOSURE [ok]
    DC1394: exposure control done by camera, user can adjust reference level using this feature.
23. Python: cv.CAP_PROP_GAMMA
24. Python: cv.CAP_PROP_TEMPERATURE
25. Python: cv.CAP_PROP_TRIGGER
26. Python: cv.CAP_PROP_TRIGGER_DELAY
27. Python: cv.CAP_PROP_WHITE_BALANCE_RED_V
28. Python: cv.CAP_PROP_ZOOM
29. Python: cv.CAP_PROP_FOCUS
30. Python: cv.CAP_PROP_GUID
31. Python: cv.CAP_PROP_ISO_SPEED
32. Python: cv.CAP_PROP_BACKLIGHT [ok]
33. Python: cv.CAP_PROP_PAN
34. Python: cv.CAP_PROP_TILT
35. Python: cv.CAP_PROP_ROLL 
36. Python: cv.CAP_PROP_IRIS
37. Python: cv.CAP_PROP_SETTINGS
    Pop up video/camera filter dialog (note: only supported by DSHOW backend currently. The property value is ignored)
38. Python: cv.CAP_PROP_BUFFERSIZE
39. Python: cv.CAP_PROP_AUTOFOCUS
40. Python: cv.CAP_PROP_SAR_NUM
    Sample aspect ratio: num/den (num)
41. Python: cv.CAP_PROP_SAR_DEN
    Sample aspect ratio: num/den (den)
42. Python: cv.CAP_PROP_BACKEND
    Current backend (enum VideoCaptureAPIs). Read-only property.
43. Python: cv.CAP_PROP_CHANNEL
    Video input or Channel Number (only for those cameras that support)
44. Python: cv.CAP_PROP_AUTO_WB
    enable/ disable auto white-balance
45. Python: cv.CAP_PROP_WB_TEMPERATURE
    white-balance color temperature
46. Python: cv.CAP_PROP_CODEC_PIXEL_FORMAT
    (read-only) codec's pixel format. 4-character code - see VideoWriter::fourcc . Subset of AV_PIX_FMT_* or -1 if unknown
47. Python: cv.CAP_PROP_BITRATE
    (read-only) Video bitrate in kbits/s
48. Python: cv.CAP_PROP_ORIENTATION_META
    (read-only) Frame rotation defined by stream meta (applicable for FFmpeg back-end only)
49. Python: cv.CAP_PROP_ORIENTATION_AUTO
    if true - rotates output frames of CvCapture considering video file's metadata (applicable for FFmpeg back-end only) (https://github.com/opencv/opencv/issues/15499)
'''
widht =1280
height = 720
fps = 30
cap.set(cv.CAP_PROP_FRAME_WIDTH, widht)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv.CAP_PROP_FPS, fps)
if __name__ == "__main__" :
    try:
        while (1):
            get, frame = cap.read()
            cv.imshow('window', frame)
            
            key = cv.waitKey(1)
            if key == ord('p') or key == ord('P'):
                cap.set(cv.CAP_PROP_SETTINGS, 1)
            if key == ord('q') or key == ord('Q'):
                break

    except KeyboardInterrupt:
        print ("Exiting from user")
    finally:
        cap.release()
        cv.destroyAllWindows()

