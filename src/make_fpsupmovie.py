import cv2
import init_movie_path
import up_fps
import image_movie

class videomaker():
    # イニシャライザ：入力パスを取得
    def __init__(self):
        in_v_path = init_movie_path.init_movie_path
        self.in_movie_path = in_v_path._in_movie_path

    # プレームレート変換
    def upfps(self, rate):
        # 動画を取得
        movie = cv2.VideoCapture(self.in_movie_path)

        # 読み込みが失敗だと"False"を返す
        if not movie.isOpened():
            print("ビデオの読み込みに失敗しました")
            return

        # インスタンス化
        up_fps_path = up_fps.fpsupper()
        # フレームレートを増加し画像の保存
        fps, digit, count = up_fps_path.up_fps(movie, rate)

        # インスタンス化
        make_m = image_movie.make_mp4()
        # フレーム補間した画像群を動画に変換
        make_m.video_maker(count,rate,digit,fps)


if __name__ ==  "__main__":
    print("FPSの倍率を入力：")
    rate = int(input())

    videomaker().upfps(rate)
