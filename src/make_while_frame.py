import cv2
import numpy as np
import init_movie_path

class make_frame():
    # イニシャライザでパスを取得
    def __init__(self):
        in_v_path = init_movie_path.init_movie_path
        self.in_movie_path = in_v_path._in_movie_path
    
    # 補間フレームの作成
    def while_frame_maker(self, count, digit,rate):
        # フレーム数分回す
        for i in range(int(count-2)):
            # 前フレームと後フレームの取得
            frame1 = cv2.imread("../out_frame/frame_" + str(i*rate).zfill(digit) + ".jpg")
            frame2 = cv2.imread("../out_frame/frame_" + str((i+1)*rate).zfill(digit) + ".jpg")

            # 補間フレームを作成
            for j in range(1,rate):
                # フレーム2（後フレーム）の割合を計算
                n = round((1/rate)*j,3)
                # 前フレームを割合(1-n)で，後フレームを割合(n)で補間フレームを作成
                out = frame1 * (1-n) + frame2 * n
                # 画素値を整数化
                newframe = out.astype(np.uint8)
                
                # 補間フレームを保存
                cv2.imwrite("../out_frame/frame_" + str(i*rate+j).zfill(digit) + ".jpg", newframe)
        return
    
if __name__ == "__main__":
    count = 2
    digit = 3
    rate = 2

    make_frame().while_frame_maker(count,digit)