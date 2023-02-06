import cv2
img = cv2.imread("C:/Users/csarm/Downloads/PRO-C116-project-image-main-main/PRO-C116-project-image-main-main/solar-system.jpg")
cv2.putText(img,
"Sun",
(75,40),
cv2.FONT_HERSHEY_COMPLEX,
1,
(0, 0, 255)
)
cv2.putText(img,
"Mercury",
(107,196),
cv2.FONT_HERSHEY_COMPLEX,
0.4,
(255, 255, 255)
)
cv2.putText(img,
"Venus",
(197,250),
cv2.FONT_HERSHEY_COMPLEX,
0.4,
(255, 255, 255)
)
cv2.putText(img,
"Earth",
(287,175),
cv2.FONT_HERSHEY_COMPLEX,
0.4,
(255, 255, 255)
)
cv2.putText(img,
"Mars",
(377,250),
cv2.FONT_HERSHEY_COMPLEX,
0.4,
(255, 255, 255)
)
cv2.putText(img,
"Jupiter",
(497,75),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255, 255, 255)
)
cv2.putText(img,
"Saturn",
(770,297),
cv2.FONT_HERSHEY_COMPLEX,
0.4,
(255, 255, 255)
)
cv2.putText(img,
"Uranus",
(960,137),
cv2.FONT_HERSHEY_COMPLEX,
0.4,
(255, 255, 255)
)
cv2.putText(img,
"Neptune",
(1104,285),
cv2.FONT_HERSHEY_COMPLEX,
0.4,
(255, 255, 255)
)
cv2.imshow("Output",img)
cv2.imwrite("C:/Users/csarm/Downloads/PRO-C116-project-image-main-main/PRO-C116-project-image-main-main/solar-systemwithname.jpg",img)
cv2.waitKey(0)
