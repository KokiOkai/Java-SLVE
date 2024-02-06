import os
import subprocess

# フォルダが存在しない場合、フォルダを作成
if not os.path.exists('Output_JavaVariableExtractor'):
    os.makedirs('Output_JavaVariableExtractor')
if not os.path.exists('Output_Java-SLVE'):
    os.makedirs('Output_Java-SLVE')

# EvaluatedTargetsフォルダのパス
evaluated_targets_path = './EvaluatedTargets'
# フォルダ内のファイル、ディレクトリ一覧を取得
java_file_directory = os.listdir(evaluated_targets_path)
# 評価対象の名称を格納するためのリスト
target_names = []

# フォルダ内の各要素に対して処理
for item in java_file_directory:
    if item != 'JavaVariableExtractor.jar':
        # フルパスを作成
        item_path = os.path.join(evaluated_targets_path, item)
        # ディレクトリの処理
        if os.path.isdir(item_path):
            # リポジトリ名をリストに追加
            target_names.append(item)

        # ファイルの処理
        elif os.path.isfile(item_path):
            # リポジトリ名をリストに追加
            target_names.append(item)


# EvaluatedTargetsを1つずつ実行
for target_name in target_names:
    try:
        # コマンドを実行する場所
        command_path = './EvaluatedTargets'
        # JavaVariableExtractor.jarを実行し結果をresultに保存
        command_1 = ['java', '-jar', 'JavaVariableExtractor.jar', target_name]
        # 結果をresultに保存
        result = subprocess.run(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=command_path, check=True, text=True)

        # JavaVariableExtractor.jarの出力ファイルのパス
        output_path = 'Output_JavaVariableExtractor/' + target_name + '_VariablesData.txt'
        # 結果を新規ファイルに書き込み
        with open(output_path, 'w') as wf:
            # 評価対象がjavaファイルのとき
            if target_name.lower().endswith('.java'):
                wf.write(result.stderr)
                wf.write('\n')
            else:
                wf.write(result.stderr)
            wf.write(result.stdout)

    except subprocess.CalledProcessError:
        print('Error')


# Java-SLVE.pyを実行
try:
    command_2 = ['python3', 'Java-SLVE.py']
    execution = subprocess.run(command_2, stderr=subprocess.PIPE, check=True)

except subprocess.CalledProcessError:
    print('Error')