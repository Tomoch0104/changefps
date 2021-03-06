# 動画のフレームレートを上げるツールを作ってみた
自分でぬるぬるした動画を作って楽しみたい！と思い簡単なフレーム補間でfpsを上げるツールを作成

## フォルダ構成

### \src
    プログラムフォルダ
        - ツールのソースコードが含まれる
### \in_movie
    入力動画フォルダ
        - 1つの動画を入れる
### \out_movie
    出力動画フォルダ
        - fps変更後の動画が出力される
### \out_frame
    出力動画のフレーム画像が出力される
        - プログラムを実行すると作成される

## 使い方
### \src\make_fpsupmovie.pyを実行
    #26 動画のフレームレートの倍率を入力
    (例) rate = 2
        30fps → 60fps
    - 入力動画と指定倍率を中間フレーム生成関数に送る
    - 動画の読み込みに失敗した場合にはエラーをはく

## その他のファイル
### \src\up_fps.py
    フレーム補間関数
    make_fpsupmovie.pyから入力動画と指定倍率を受け取る
    - 入力動画の補間フレームの前後フレームを.\make_while_frameに送り，補間フレーム画像を生成し，全フレームを../out_frame/に出力
### \src\make_while_frame.py
    補間フレーム生成関数
    - 引数で受け取った2枚の画像の中間の輝度値を持つ画像を生成
### \src\image_movie.py
    複数枚の画像を動画に変換する関数

## フレームの補間について
初めての制作物ということもあり，簡単に前後フレームの間の輝度値をとるように中間フレームを生成


|前フレーム|補間フレーム|後フレーム|
|---|---|---|
|　<img src="https://user-images.githubusercontent.com/80777762/114273657-e9c79180-9a55-11eb-9ec5-b3b97b2c7e9d.jpg" width="250">　|　<img src="https://user-images.githubusercontent.com/80777762/114273745-4dea5580-9a56-11eb-9cb8-2ae11c164b38.jpg" width="250">　|　<img src="https://user-images.githubusercontent.com/80777762/114273715-327f4a80-9a56-11eb-9df1-2e4a9fc243c0.jpg" width="250">　|

# 処理
./src/～.pyの処理の説明を以下に示します．

## make_fpsupmovie.py
実行するファイル
- 使用ライブラリ
    - Open-CV

"rate"にfpsの倍率を代入（整数のみ対応可）
```python
if __name__ ==  "__main__":
    rate = 1

    videomaker().upfps(rate)
```
イニシャライザではパスを取得
```python
    def __init__(self):
        in_v_path = init_movie_path.init_movie_path
        self.in_movie_path = in_v_path._in_movie_path
```

## image_movie.py

## init_movie_path.py

## make_while_frame.py

## up_fps.py