# Java-SLVE
**Java-SLVE**は，Javaプロジェクトにおけるソースコード内の一文字変数を評価するツールです．<br>


## 目次
- [概要](#概要)
- [使用方法](#使用方法)
- [出力結果の確認方法](#出力結果の確認方法)
- [出力フォーマット](#出力フォーマット)
- [出力ファイルのcsv変換](#出力ファイルのcsv変換)


## 概要
**Java-SLVE**は，Java プロジェクトにおけるソースコード内の一文字変数を評価するツールです．<br>
本ツールは [JavaVariableExtractor](https://github.com/amanhirohisa/JavaVariableExtractor) を内蔵しています．<br>
Java プロジェクトであるディレクトリまたはファイルを入力として，ソースコードに含まれる変数のデータを収集し，<br>
一文字変数を変数の型・アルファベット・スコープをもとに評価したデータを出力します．


## 使用方法
1. `Java-SLVE/src`にある **EvaluatedTargets** フォルダに，本ツールを適用したいディレクトリまたは java ファイルをコピーします．<br>
   注意点として，**JavaVariableExtractor.jar** は消さないようにしてください．
2. cd コマンドで`Java-SLVE/src`に移動する．
```
$ cd Java-SLVE/src
```
3. **Main.py** を実行する．例では **python3** のバージョンを使用していますが，必要に応じて変更してください．<br>
   バージョンを変更する場合は，**Main.py** 内のコード`command_2 = ['python3', 'Java-SLVE.py']`も変更してください．
```
$ python3 Main.py
```
`Java-SLVE/src`にある **EvaluatedTargets** フォルダにサンプルのディレクトリと java ファイルがあります．<br>
本ツールのテスト実行用として用意したものなので，削除しても問題ありません．


## 出力結果の確認方法
- `Java-SLVE/src`にある **Output_JavaVariableExtractor** フォルダに，txt ファイルとしてすべての変数のデータが出力されます．
- `Java-SLVE/src`にある **Output_Java-SLVE** フォルダに，txt ファイルとして一文字変数を評価したデータが出力されます．<br>
これらのフォルダには，サンプルのディレクトリと java ファイルに対して本ツールを実行した出力結果があります．<br>
本ツールのテスト実行例として用意したものなので，削除しても問題ありません．


## 出力フォーマット
| データ | 説明 |
| :--- | :--- |
| path | 変数のデータを抽出した java ファイルのパス |
| line | 変数が宣言された行番号 |
| kind | 変数の種類（F: フィールド変数，M: メソッドの引数，L: ローカル変数） |
| name | 変数名 |
| type | 変数の型 |
| begin | 変数のスコープの開始行番号 |
| end | 変数のスコープの終了行番号 |
| scope | 変数のスコープ |
| AE-Level | 一文字変数のアルファベット評価値 |
| SE-Level | 一文字変数のスコープ評価値 |


## 出力ファイルのcsv変換
1. cd コマンドで`Java-SLVE/src`に移動する．
```
$ cd Java-SLVE/src
```
2. **txt_csv_Converter.py** を実行する．例では **python3** のバージョンを使用していますが，必要に応じて変更してください．
```
$ python3 txt_csv_Converter.py
```
本ツールによって出力された結果は txt ファイルとして保存されます．<br>
csv ファイルに変換することによって，詳細な変数のデータを確認することが容易となります．<br>
例えば，**[データ]** タブの **[フィルター]** 機能を使うと，必要な情報のみを確認できます．<br>

<img src="https://github.com/KokiOkai/GitHub_Note/assets/105481222/775e3d8f-1641-4ae2-b6f6-ca98d9876f2a.jpg" width="80%">
<img src="https://github.com/KokiOkai/GitHub_Note/assets/105481222/355b9db9-66d3-40e6-84fd-ef81842b8892.jpg" width="80%">