import cv2
import numpy as np
import init_movie_path

class make_frame():
    def __init__(self):
        in_v_path = init_movie_path.init_movie_path
        self.in_movie_path = in_v_path._in_movie_path
    
    def while_frame_maker(self, count, digit,rate):
        for i in range(int(count-2)):
            frame1 = cv2.imread("../out_frame/frame_" + str(i*rate).zfill(digit) + ".jpg")
            frame2 = cv2.imread("../out_frame/frame_" + str((i+1)*rate).zfill(digit) + ".jpg")

            for j in range(1,rate):
                n = round((1/rate)*j,3)
                out = frame1 * (1-n) + frame2 * n
                newframe = out.astype(np.uint8)
                # h, w, c = frame1.shape
                # newframe = np.zeros((h,w,c),uint)
                # for x in range(w):
                #     for y in range(h):
                #         for ch in range(c):
                #             newframe[y][x][ch] = int((frame1[y][x][ch] + frame2[y][x][ch])/2)
                
                cv2.imwrite("../out_frame/frame_" + str(i*rate+j).zfill(digit) + ".jpg", newframe)

        return
    
if __name__ == "__main__":
    count = 2
    digit = 3
    rate = 2

    make_frame().while_frame_maker(count,digit)