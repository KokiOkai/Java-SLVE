import csv
import os

# txtファイルを開いてcsvファイルに書き込む
def txt_csv_converter(txt_file):
    # 保存するcsvファイルのパス
    csv_file = os.path.join('Output_csv', os.path.basename(txt_file).replace("txt", "csv"))

    # 読み込むtxtファイルを開く
    with open(txt_file) as rf:
        # 書き込むcsvファイルを開く
        with open(csv_file, mode="w") as wf:
            # テキストを１行ずつ読み込む
            # テキストの１行を要素としたlistになる
            readfile = rf.read().splitlines()
           
            # テキスト１行ずつ処理
            for read_text in readfile:
                # listに分割
                read_text = read_text.split('\t')
                # csvファイルに書き込む
                writer = csv.writer(wf, delimiter=',')
                writer.writerow(read_text)


if __name__ == '__main__':
    # フォルダが存在しない場合、フォルダを作成
    if not os.path.exists('Output_csv'):
        os.makedirs('Output_csv')

    # filenameはcsv変換したいtxtファイルのパス
    file_path = "./Output_Java-SLVE/SampleProject_SingleLetterVariablesData.txt"
    txt_csv_converter(file_path)