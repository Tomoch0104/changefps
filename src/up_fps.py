import cv2
import init_movie_path
import make_while_frame

class fpsupper():
    # イニシャライザでパスを取得
    def __init__(self):
        v_path = init_movie_path.init_movie_path
        self.out_frame_path = v_path._out_movie_path

    # フレームを補完した画像群を作成
    def up_fps(self, movie, rate):
        # フレーム数の桁数
        digit = len(str(int(movie.get(cv2.CAP_PROP_FRAME_COUNT))))
        print("digit：",digit)

        # 画像を生成する際の作成中フレーム数（カウンター）
        n = 0

        # 総フレーム数を取得
        count = movie.get(cv2.CAP_PROP_FRAME_COUNT)
        print("総フレーム数：",count)
        # 元の動画のfpsを取得
        fps = movie.get(cv2.CAP_PROP_FPS)
        print("fps：",fps)

        # 動画のフレーム画像を書き出し
        while True:
            # 1フレームずつ取得
            ret, frame = movie.read()
            if ret:
                # 動画フレームの保存
                cv2.imwrite('{}_{}.{}'.format("../out_frame/frame", str(n).zfill(digit), "jpg"), frame)
                # フレーム数間隔はrate（間に補間フレームが入るため）
                n += rate
            # 最後まで行ったらbreak
            else:
                break
        
        # インスタンス化
        make_frame = make_while_frame.make_frame()
        # 補間フレームの作成
        make_frame.while_frame_maker(count, digit,rate)

        return fps, digit, count