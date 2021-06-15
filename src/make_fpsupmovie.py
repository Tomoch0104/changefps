import cv2
import init_movie_path
import up_fps
import image_movie

class videomaker():
    def __init__(self):
        in_v_path = init_movie_path.init_movie_path
        self.in_movie_path = in_v_path._in_movie_path

    def upfps(self, rate):
        movie = cv2.VideoCapture(self.in_movie_path)

        if not movie.isOpened():
            print("ビデオの読み込みに失敗しました")
            return

        up_fps_path = up_fps.fpsupper()
        fps, digit, count = up_fps_path.up_fps(movie, rate)

        make_m = image_movie.make_mp4()
        make_m.video_maker(count-5,rate,digit,fps)


if __name__ ==  "__main__":
    rate = 1

    videomaker().upfps(rate)
