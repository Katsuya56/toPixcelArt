# PixcelArt

画像を読み込んで画素を荒くしてピクセルアートを作成するプログラム

# 環境構築方法

1. 仮想環境を立てる

   ```
   python -m venv .venv
   ```

1. vscode 上の Python の拡張機能が、実行する Python を仮想環境のものにするか聞いてくるので Yes を選択する

1. pip の更新

   ```
   python.exe -m pip install --upgrade pip
   ```

1. ライブラリをインストールする
   ```
   pip install -r requirements.txt
   ```

# 処理順序

1. 画像を開く
1. 画像の元のサイズを取得
1. ピクセル化のための新しいサイズを計算
1. 画像をリサイズ
1. 画像データを書き換え

# 備考

表現できる色の数がすくない方が画像に統一感が出ると思ったので
書き換えるときに各RGBを表現している8bitの下位4bitを0埋めしている

# 使っているライブラリ

requirements.txt

```text
pillow==10.4.0
```

# 自分の環境

- OS
  windows11
- Python
  3.11.1
