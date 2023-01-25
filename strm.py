import cv2
import streamlit as st

FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imwrite('test.jpg',frame)
    FRAME_WINDOW.image(frame)
    if cv2.waitKey(1) & 0xff== 27:
        break