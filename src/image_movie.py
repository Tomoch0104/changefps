import sys
import cv2
import os
import glob
# import moviepy.editor as mp

class make_mp4():
    # 画像群から動画を作成
    def video_maker(self, count,rate,digit,fps):
        # encoder(for mp4)
        img_ = cv2.imread("../out_frame/frame_" + str(0).zfill(digit)+ ".jpg")
        h, w, c = img_.shape
        # 拡張子の指定
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

        # output file name, encoder, fps, size(fit to image size)
        video = cv2.VideoWriter('../out_movie/upmovie.mp4', fourcc, fps*rate, (w,h))

        if not video.isOpened():
            print("can't be opened")
            sys.exit()

        """
        ＊研究用
        """
        # fit_list = os.listdir(path + dirname + "/fit")
        # fit_list = sorted(glob.glob(path + dirname + "/fit"))
        # 1000世代

        for i in range(int((count-2)*rate+1)):
            # フレームの読み込み
            img = cv2.imread("../out_frame/frame_" + str(i).zfill(digit) + ".jpg")
            # リサイズ
            img = cv2.resize(img, (w,h))

            """
            画像表示確認用
            """
            # cv2.imshow("i", img)
            # cv2.waitKey()
            # cv2.destroyAllWindows()

            if img is None:
                print("can't read")
                break
            # add
            video.write(img)
            print(i)

        # 動画の保存
        video.release()
        print('video written')
    

if __name__ == "__main__":
    count = 601
    rate = 4
    digit = 3
    fps = 30.0

    make_mp4().video_maker(count,rate,digit,fps)