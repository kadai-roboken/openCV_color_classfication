import cv2
import numpy as np
#from matplotlib import pylot as plt


print(cv2.__version__)

#1.青色を検出する
def main():
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        ret, frame = cap.read()
        # フレームの描画
        cv2.imshow('frame', frame)

        # BGR色空間からHSV色空間への変換
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 青色の色検出しきい値の設定
        lower_blue = np.array([90, 64, 0])
        upper_blue = np.array([150, 255, 255])

        # 赤色の色検出しきい値の設定
        lower_red1 = np.array([0, 64, 0])
        upper_red1 = np.array([30, 255, 255])
        lower_red2 = np.array([150, 64, 0])
        upper_red2 = np.array([179, 255, 255])
        # lower_red = np.array([0, 100, 100])  # 下限値
        # upper_red = np.array([10, 255, 255]) # 上限値


        # 色検出しきい値範囲内の色を抽出するマスクを作成
        blue_frame_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        red_frame_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        red_frame_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        # red_frame_mask = cv2.inRange(hsv, lower_red, upper_red)
        
        red_frame_mask = red_frame_mask1 + red_frame_mask2


        # 色検出のマスクを合成
        mask = blue_frame_mask + red_frame_mask
        #ret, thresh = cv2.threshold(mask,1,255,cv2.THRESH_BINARY)
        #cv2.imshow('threshold',thresh)
        # 論理演算で色検出
        dst = cv2.bitwise_and(frame, frame, mask=mask)

        #2.青色かつ円を検出する
        gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray,1,255,cv2.THRESH_BINARY)
        #gray = cv2.medianBlur(gray, 5)
        #cv2.imshow('gray', gray)
        
        try:
            circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, dp = 1.0, minDist = 100, param1 = 80, param2 = 55, minRadius = 0)
            if circles is not None:
                circles = np.uint16(np.around(circles))
                if len(circles) >0:
                    for circle in circles[0,:]:
                        x, y, radius = circle[0], circle[1], circle[2]
                        print("x:", x, "y:", y, "radius:", radius)
                        cv2.circle(thresh,(circle[0],circle[1]),circle[2],(0,165,255),5)
                        cv2.circle(thresh,(circle[0],circle[1]),2,(0,255,255),3)
                #cv2.imshow("video",frame)
                #k = cv2.waitKey(46) & 0xFF
                #if k == ord('q'):
                    #break
                else:
                    print("No index")
            else:
                print("not circles")
        except Exception as e:
            print(e)
        #3.検出した円の半径から、距離を推定する

        # 画像を表示
        cv2.imshow("Color Detection", thresh)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()




# main関数実行
if __name__ == "__main__":
    main()
