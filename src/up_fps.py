import cv2
import os
import init_movie_path
import make_while_frame

class fpsupper():
    def __init__(self):
        v_path = init_movie_path.init_movie_path
        self.out_frame_path = v_path._out_movie_path

    def up_fps(self, movie, rate):
        digit = len(str(int(movie.get(cv2.CAP_PROP_FRAME_COUNT))))
        print("digit：",digit)

        n = 0
        movie_frame = []

        #  総フレーム数
        count = movie.get(cv2.CAP_PROP_FRAME_COUNT)
        print("総フレーム数：",count)
        fps = movie.get(cv2.CAP_PROP_FPS)
        print("fps：",fps)

        while True:
            ret, frame = movie.read()
            if ret:
                cv2.imwrite('{}_{}.{}'.format("../out_frame/frame", str(n).zfill(digit), "jpg"), frame)
                n += rate
            else:
                break
        
        make_frame = make_while_frame.make_frame()
        make_frame.while_frame_maker(count, digit,rate)

        return fps, digit, count