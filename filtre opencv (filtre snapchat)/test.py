import cv2 as cv

cascade_visage = cv.CascadeClassifier('visage.xml')
lunettes_img = cv.imread("lunettes.png",-1)
moustache_img = cv.imread("moustache.png",-1)

def objet(R_Color, mon_objet):
    h, w, _ = mon_objet.shape
    y, x = 0,0

    for i in range(h):
        for j in range(w):
            if mon_objet[i][j][3] != 0:
                R_Color[y + i, x + j] = mon_objet[i, j][:3]

cap = cv.VideoCapture(0)

while cap.isOpened():
    test, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    visage_detecter = cascade_visage.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in visage_detecter:
        l_min = int(y + 1.5 * h / 5)
        l_max = int(y + 2.5 * h / 5)
        l_hauteur = l_max - l_min


        m_min = int(y + 3.2 * h / 5)
        m_max = int(y + 4.1 * h / 5)
        m_hauteur = m_max - m_min

        l_clr = img[l_min:l_max, x:x + w]
        m_clr = img[m_min:m_max, x:x + w]

        lunette = cv.resize(lunettes_img, (w, l_hauteur), interpolation=cv.INTER_CUBIC)
        moustache = cv.resize(moustache_img, (w, m_hauteur), interpolation=cv.INTER_CUBIC)

        objet(l_clr, lunette)
        objet(m_clr, moustache)

    cv.imshow("SnapChat", img)
    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()
