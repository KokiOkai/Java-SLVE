# 一文字変数の保守性低下要因の検出メソッド
def SingleLetterVariableEvaluation(textFile):
    # ToDo: 自動で出力ファイル名を決めるように変更する
    # output_txt_fileは保存するtxtファイルの場所
    output_txt_file = "./output_SVC.txt"

    try:
        # 読み込むtxtファイルを開く
        with open(textFile) as rf:
            # 書き込むtxtファイルを開く
            with open(output_txt_file, mode="w") as wf:
                # txtファイルを１行ずつ読み込む
                # txtファイルの１行を要素としたlistになる
                readFile = rf.read().splitlines()
                
                # カウント変数
                count = 0

                # txtファイルを１行ずつ処理
                for read_line in readFile:
                    # カウントの更新
                    count += 1

                    # 1行目: 変数の分類
                    if count == 1:
                        # 分類追加
                        line_class = read_line + '\tscope\tAE-Level\tSE-Level\n'
                        # txtファイルに書き込む
                        wf.write(line_class)

                    # 2行目: 分析したdirectory
                    # 3行目: 分析したファイル数
                    elif count <= 3:
                        wf.write(read_line + '\n')

                    # 4行目以降: 変数のデータ
                    else:
                        # listに分割
                        data = read_line.split('\t')

                        # Path: ファイルパスを取得
                        Path = data[0]
                        # Kind: 変数の種類を取得
                        Kind = data[2]
                        # Name: 変数を取得
                        Name = data[3]
                        # Type: 変数の型を取得
                        Type = data[4]
                        # Begin: スコープ開始行を取得
                        Begin = int(data[5])
                        # End: スコープ終了行を取得
                        End = int(data[6])

                        # 変数名の文字数を取得
                        name_length = len(Name)

                        # テスト用とドキュメント用と思われるファイルを除く
                        EX_keyword_1 = 'test'
                        EX_keyword_2 = 'documentation'
                        if EX_keyword_1 not in Path and EX_keyword_2 not in Path:
                            # ローカル（L）かつ一文字変数のデータのみ取得
                            if Kind == 'L' and name_length == 1:
                                # スコープ算出
                                scope_info = str(ScopeCalculation(Begin, End))
                                # スコープ追加
                                line_add_scope = read_line + '\t' + scope_info

                                # アルファベット評価
                                AE_Level_info = AlphabetEvaluation(Name, Type)
                                # アルファベット評価追加
                                line_add_AE_Level = line_add_scope + '\t' + AE_Level_info

                                # スコープ評価
                                SE_Level_info = ScopeEvaluation(Type, float(scope_info))
                                # スコープ評価追加
                                line_add_SE_Level = line_add_AE_Level + '\t' + SE_Level_info

                                # txtファイルに書き込む
                                wf.write(line_add_SE_Level + '\n')

    except FileNotFoundError:
        print(f"Error: '{textFile}' is not found")

    except Exception as e:
        print(f"Error: {e}")


# スコープ計算メソッド
def ScopeCalculation(begin, end):
    scope = end - begin + 1
    return scope


# アルファベット評価メソッド
def AlphabetEvaluation(AE_name, AE_type):
    ''' アルファベット評価基準
    1.アルファベットの使用割合で上位1位が50%以上の場合は次の6段階に分ける
        AE_Level: 0  →  使用割合40%以上
        AE_Level: 1  →  使用割合30%以上, 40%未満
        AE_Level: 2  →  使用割合15%以上, 30%未満
        AE_Level: 3  →  使用割合 5%以上, 15%未満
        AE_Level: 4  →  使用割合 1%以上,  5%未満
        AE_Level: 5  →  使用割合 0%以上,  1%未満
    
    2.アルファベットの使用割合で上位1位が50%未満の場合は次の6段階に分ける
        AE_Level: 0  →  該当なし
        AE_Level: 1  →  使用割合30%以上, 50%未満
        AE_Level: 2  →  使用割合15%以上, 30%未満
        AE_Level: 3  →  使用割合 5%以上, 15%未満
        AE_Level: 4  →  使用割合 1%以上,  5%未満
        AE_Level: 5  →  使用割合 0%以上,  1%未満
    '''

    # 評価レベル変数
    AE_Level = '-'

    # アルファベット評価 -------------------------------------------------------------------------
    AE_answer = 5
    if AE_type == 'boolean' or AE_type == 'Boolean':
        Level = ['  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,bB,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,dD,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 'aA,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,vV,  ,  ,  ,  ',
                 '  ,  ,cC,  ,eE,  ,gG,  ,iI,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,xX,yY,zZ',
                 '  ,  ,  ,  ,  ,fF,  ,hH,  ,jJ,kK,lL,mM,nN,oO,pP,qQ,rR,sS,tT,uU,  ,wW,  ,  ,  ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'byte' or AE_type == 'Byte':
        Level = ['  ,bB,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 'aA,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,xX,  ,  ',
                 '  ,  ,cC,  ,  ,  ,gG,  ,iI,  ,  ,  ,  ,  ,  ,  ,  ,rR,  ,tT,  ,vV,  ,  ,yY,  ',
                 '  ,  ,  ,dD,eE,fF,  ,hH,  ,jJ,kK,lL,mM,nN,oO,pP,qQ,  ,sS,  ,uU,  ,wW,  ,  ,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'char' or AE_type == 'Character':
        Level = ['  ,  ,cC,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,bB,  ,  ,  ,  ,  ,  ,iI,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 'aA,  ,  ,dD,eE,fF,gG,hH,  ,jJ,kK,lL,mM,nN,oO,pP,qQ,rR,sS,tT,uU,vV,wW,xX,yY,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'short' or AE_type == 'Short':
        Level = ['  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,sS,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,iI,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 'aA,bB,cC,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,vV,  ,xX,  ,  ',
                 '  ,  ,  ,dD,  ,  ,  ,  ,  ,jJ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,yY,  ',
                 '  ,  ,  ,  ,eE,fF,gG,hH,  ,  ,kK,lL,mM,nN,oO,pP,qQ,rR,  ,tT,uU,  ,wW,  ,  ,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'int' or AE_type == 'Integer':
        Level = ['  ,  ,  ,  ,  ,  ,  ,  ,iI,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,jJ,  ,  ,  ,nN,  ,  ,  ,  ,  ,  ,  ,vV,  ,  ,  ,  ',
                 'aA,bB,cC,  ,  ,  ,  ,  ,  ,  ,kK,  ,  ,  ,  ,pP,  ,  ,  ,tT,  ,  ,  ,xX,yY,  ',
                 '  ,  ,  ,dD,eE,fF,gG,hH,  ,  ,  ,lL,mM,  ,oO,  ,qQ,rR,sS,  ,uU,  ,wW,  ,  ,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'float' or AE_type == 'Float':
        Level = ['  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,xX,yY,  ',
                 'aA,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,zZ',
                 '  ,bB,cC,dD,  ,fF,gG,hH,  ,  ,  ,  ,  ,  ,  ,  ,  ,rR,sS,tT,uU,vV,wW,  ,  ,  ',
                 '  ,  ,  ,  ,eE,  ,  ,  ,iI,jJ,kK,lL,mM,nN,oO,pP,qQ,  ,  ,  ,  ,  ,  ,  ,  ,  ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'long' or AE_type == 'Long':
        Level = ['  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,nN,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 'aA,bB,  ,  ,  ,  ,  ,  ,iI,  ,  ,lL,  ,  ,  ,  ,  ,rR,  ,  ,  ,vV,  ,xX,  ,  ',
                 '  ,  ,cC,dD,eE,  ,gG,hH,  ,  ,  ,  ,mM,  ,  ,pP,  ,  ,  ,tT,uU,  ,  ,  ,yY,  ',
                 '  ,  ,  ,  ,  ,fF,  ,  ,  ,jJ,kK,  ,  ,  ,oO,  ,qQ,  ,sS,  ,  ,  ,wW,  ,  ,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'double' or AE_type == 'Double':
        Level = ['  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,xX,yY,  ',
                 '  ,  ,  ,dD,  ,  ,  ,  ,  ,  ,  ,  ,  ,nN,  ,  ,qQ,  ,  ,  ,  ,vV,  ,  ,  ,  ',
                 'aA,bB,cC,  ,  ,  ,  ,  ,  ,  ,kK,  ,  ,  ,  ,pP,  ,  ,sS,tT,  ,  ,wW,  ,  ,zZ',
                 '  ,  ,  ,  ,eE,fF,gG,hH,iI,jJ,  ,lL,mM,  ,oO,  ,  ,rR,  ,  ,uU,  ,  ,  ,  ,  ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'Object':
        Level = ['  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,oO,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,vV,  ,  ,  ,  ',
                 'aA,bB,  ,dD,eE,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,tT,  ,  ,  ,xX,  ,  ',
                 '  ,  ,cC,  ,  ,fF,gG,hH,iI,jJ,kK,lL,mM,nN,  ,pP,qQ,rR,sS,  ,uU,  ,wW,  ,yY,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'String':
        Level = ['  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,sS,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,vV,  ,  ,  ,  ',
                 'aA,bB,cC,  ,eE,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,pP,  ,  ,  ,tT,  ,  ,  ,xX,  ,  ',
                 '  ,  ,  ,dD,  ,fF,gG,hH,iI,jJ,kK,lL,mM,nN,oO,  ,qQ,rR,  ,  ,uU,  ,wW,  ,yY,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'Exception':
        Level = ['  ,  ,  ,  ,eE,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 'aA,bB,cC,dD,  ,fF,gG,hH,iI,jJ,kK,lL,mM,nN,oO,pP,qQ,rR,sS,tT,uU,vV,wW,xX,yY,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    elif AE_type == 'Throwable':
        Level = ['  ,  ,  ,  ,eE,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,tT,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 '  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ',
                 'aA,bB,cC,dD,  ,fF,gG,hH,iI,jJ,kK,lL,mM,nN,oO,pP,qQ,rR,sS,  ,uU,vV,wW,xX,yY,zZ']
        for n in range(6):
            if AE_name in Level[n]:
                AE_answer = n
    else:
        return '-'
    # -------------------------------------------------------------------------------------------

    # レベル付け ---------------
    if AE_answer == 0:
        AE_Level = '0'
    elif AE_answer == 1:
        AE_Level = '1'
    elif AE_answer == 2:
        AE_Level = '2'
    elif AE_answer == 3:
        AE_Level = '3'
    elif AE_answer == 4:
        AE_Level = '4'
    else:
        AE_Level = '5'
    # --------------------------

    return AE_Level


# スコープ評価メソッド
def ScopeEvaluation(SE_type, SE_scope):
    ''' スコープ評価基準
    外れ値 = Q3 + IQR * 1.5

    外れ値から最大値までを5段階に分ける
        stage = (最大値 - 外れ値) / 5
    
    スコープを6段階で評価する
        SE_Level: 0  →  SE_scope < 外れ値 + stage * 0
        SE_Level: 1  →  外れ値 + stage * 0 <= SE_scope < 外れ値 + stage * 1
        SE_Level: 2  →  外れ値 + stage * 1 <= SE_scope < 外れ値 + stage * 2
        SE_Level: 3  →  外れ値 + stage * 2 <= SE_scope < 外れ値 + stage * 3
        SE_Level: 4  →  外れ値 + stage * 3 <= SE_scope < 外れ値 + stage * 4
        SE_Level: 5  →  外れ値 + stage * 4 <= SE_scope
    
    Exceptionにおいては下限の外れ値が存在したため補正する
        SE_Level: 1  →  SE_scope = 1
    '''

    # 評価レベル変数
    SE_Level = ''

    # パラメータ --------------------------------------------
    # boolean
    Q1_boolean = 14.0
    Q3_boolean = 28.75
    IQR_boolean = Q3_boolean - Q1_boolean
    max_boolean = 156.0
    out_boolean = Q3_boolean + IQR_boolean * 1.5
    stage_boolean = (max_boolean - out_boolean) / 5
    # byte
    Q1_byte = 4.0
    Q3_byte = 8.0
    IQR_byte = Q3_byte - Q1_byte
    max_byte = 65.0
    out_byte = Q3_byte + IQR_byte * 1.5
    stage_byte = (max_byte - out_byte) / 5
    # char
    Q1_char = 5.0
    Q3_char = 15.0
    IQR_char = Q3_char - Q1_char
    max_char = 203.0
    out_char = Q3_char + IQR_char * 1.5
    stage_char = (max_char - out_char) / 5
    # short
    Q1_short = 2.5
    Q3_short = 6.0
    IQR_short = Q3_short - Q1_short
    max_short = 19.0
    out_short = Q3_short + IQR_short * 1.5
    stage_short = (max_short - out_short) / 5
    # int
    Q1_int = 3.0
    Q3_int = 11.0
    IQR_int = Q3_int - Q1_int
    max_int = 480.0
    out_int = Q3_int + IQR_int * 1.5
    stage_int = (max_int - out_int) / 5
    # float
    Q1_float = 5.0
    Q3_float = 27.0
    IQR_float = Q3_float - Q1_float
    max_float = 184.0
    out_float = Q3_float + IQR_float * 1.5
    stage_float = (max_float - out_float) / 5
    # long
    Q1_long = 5.0
    Q3_long = 27.0
    IQR_long = Q3_long - Q1_long
    max_long = 161.0
    out_long = Q3_long + IQR_long * 1.5
    stage_long = (max_long - out_long) / 5
    # double
    Q1_double = 4.0
    Q3_double = 12.0
    IQR_double = Q3_double - Q1_double
    max_double = 216.0
    out_double = Q3_double + IQR_double * 1.5
    stage_double = (max_double - out_double) / 5
    # Object
    Q1_Object = 5.0
    Q3_Object = 11.0
    IQR_Object = Q3_Object - Q1_Object
    max_Object = 234.0
    out_Object = Q3_Object + IQR_Object * 1.5
    stage_Object = (max_Object - out_Object) / 5
    # String
    Q1_String = 3.0
    Q3_String = 8.0
    IQR_String = Q3_String - Q1_String
    max_String = 88.0
    out_String = Q3_String + IQR_String * 1.5
    stage_String = (max_String - out_String) / 5
    # Exception
    Q1_Exception = 3.0
    Q3_Exception = 4.0
    IQR_Exception = Q3_Exception - Q1_Exception
    max_Exception = 33.0
    out_Exception = Q3_Exception + IQR_Exception * 1.5
    stage_Exception = (max_Exception - out_Exception) / 5
    # Throwable
    Q1_Throwable = 3.0
    Q3_Throwable = 6.0
    IQR_Throwable = Q3_Throwable - Q1_Throwable
    max_Throwable = 51.0
    out_Throwable = Q3_Throwable + IQR_Throwable * 1.5
    stage_Throwable = (max_Throwable - out_Throwable) / 5
    # -------------------------------------------------------

    # スコープ評価 --------------------------------------------------
    SE_answer = 5
    if SE_type == 'boolean' or SE_type == 'Boolean':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_boolean + stage_boolean * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'byte' or SE_type == 'Byte':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_byte + stage_byte * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'char' or SE_type == 'Character':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_char + stage_char * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'short' or SE_type == 'Short':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_short + stage_short * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'int' or SE_type == 'Integer':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_int + stage_int * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'float' or SE_type == 'Float':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_float + stage_float * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'long' or SE_type == 'Long':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_long + stage_long * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'double' or SE_type == 'Double':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_double + stage_double * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'Object':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_Object + stage_Object * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'String':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_String + stage_String * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'Exception':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_Exception + stage_Exception * n):
                SE_answer = n
                break
        if SE_scope == 1.0:
            SE_answer = 1
        # SE_Level: 5
        # anwer = 5
    elif SE_type == 'Throwable':
        # SE_Level: 0 ~ 4
        for n in range(5):
            if SE_scope < (out_Throwable + stage_Throwable * n):
                SE_answer = n
                break
        # SE_Level: 5
        # anwer = 5
    else:
        return '-'
    # ---------------------------------------------------------------

    # レベル付け ---------------
    if SE_answer == 0:
        SE_Level = '0'
    elif SE_answer == 1:
        SE_Level = '1'
    elif SE_answer == 2:
        SE_Level = '2'
    elif SE_answer == 3:
        SE_Level = '3'
    elif SE_answer == 4:
        SE_Level = '4'
    else:
        SE_Level = '5'
    # --------------------------

    return SE_Level


if __name__ == '__main__':
    # input_txt_fileはtxtファイルの場所
    input_txt_file = "./test_dubbo.txt"
    SingleLetterVariableEvaluation(input_txt_file)
