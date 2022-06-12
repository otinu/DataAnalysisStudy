"""
#機会学習の種類

##教師あり学習

◎教師あり学習は、正解となる【ラベルデータ】が存在する場合に用いられる方式。
　このラベルのことを目的変数という。

◎目的変数には、【回帰】と【分類】の2種類がある。

##教師なし学習

・クラスタリング

・次元削減

・DBSCAN法

##強化学習

◎ブラックボックス的な環境の中で行動するエージェントが、得られる報酬を最大化する学習方法


"""

"""
# Python基礎

    ## pyenv と venv の違い

    ・pyenvはPython自体のバージョンを管理してくれる

    ・venvはPythonの中の仮想環境において、モジュールのバージョン管理をしてくれる

    ##正規表現

        [サンプル]
        'py?(th|ers)oni?(a[lmn]|c)?'

        【py?】 pから始まり、その直後のyは?(疑問符)がついていますので0(ゼロ)個もしくは1個という意味になります。つまり、pもしくはpyのどちらかのパターンになります。
        【(th|ers)】thもしくはersのどちらかのパターンになります。
        【oni?】onの直後のiには?がついていますので、onもしくはoniのどちらかのパターンになります。

        【(a[lmn]|c)?】少し複雑ですので1つずつ確認しながら考えます。
        [lmn]はl(エル)またはmまたはnのいずれか1文字のパターンです。つまりa[lmn]は、alまたはamまたはanのいずれかのパターンとなります。
        (a[lmn]|c)は、a[lmn]もしくはcのどちらかのパターンです。つまり、alまたはamまたはanまたはcのいずれかのパターンとなります。
        (a[lmn]|c)?は(a[lmn]|c)に?がついていますので、alまたはamまたはanまたはcのパターンが0個もしくは1個のパターンとなります。
        つまり、この部分のパターンは文字列の中になくても問題はないということです。

    ## モジュール

        ###loggingモジュール
        ・loggingモジュールではバッチ処理などの途中経過を出力することが可能
        　⇒処理後に経過をまとめて出力するだけではない

        ・loggingモジュール5段階あるログレベルのうち、デフォルトは3段階目のWARNING

        ###pickleモジュール
        ◎「データを再利用するために、データの凍結・変換（直列化）と保存（永続化）」一度に行うモジュールです
            通常、プログラムで生成したデータは、プログラムの終了時に消えます。プログラムの終了後もそのデータを利用したい時などにpickleを使います。

        ・読み込み ⇒ 非直列化
        ・書き込み ⇒ 直列化

"""

"""
#JupyterNotebook

・ Jupyter Notebookはオープンソースで開発されているデータ分析、可視化、機械学習などに広く利用されているWebアプリケーションである。
　⇒ブラウザ上でPythonなどのプログラムを実行できる
　⇒テキストエディタやIDEではないため、誤認注意

・JupyterNotebookで保存されるファイルはJSON形式で記述される

・JupyterNotebookで保存されるファイルの拡張子は【.ipynb】
　⇒IPYtnon_NoteBook　の略
　⇒OSSである点もポイント

・先頭に%か%%を付けて特定の文字列を記述することでマジックコマンドが使える
　⇒これはターミナルで叩くことも、コード中に記述することも可能
"""

"""
#数学

##基礎
・数式で、足し算の繰り返しを表す際にはギリシャ文字のシグマ(Σ)の大文字を用い、
　掛け算の繰り返しを表す際には、ギリシャ文字のパイ(Π)の大文字を用いる。
　⇒小文字はそれぞれ σ、π

・直径が1のときの円周の長さを円周率と呼ぶ。 約3.1415
・自然対数の底をネイピア数と呼ぶ。 約2.7182

・ 関数の入力が別の数字の肩に乗って使われる関数を指数関数と呼ぶ。 2の3乗の「3」
・入力された値が底の何乗に相当するかという出力を行う関数を対数関数と呼ぶ。 log のこと

・深層学習(ディープラーニング)におけるニューラルネットワークで用いられる関数は【シグモイド関数】
　⇒シグモイド関数はS字形を描く
　⇒シグモイド関数は生物の神経細胞が持つ性質をモデル化したもの

・sin ⇒ 正弦
・cos ⇒ 余弦
・tan ⇒ 正接
https://gist.github.com/otinu/e8c2c3b0d10c5a99dd6ea18abdde802c?permalink_comment_id=4196976#gistcomment-4196976

##ベクトル
    [サンプル]
    A. (3,4)、 B. (4,7)、 C. (2,4,5)

・A + C や B + C のように、次元数の異なるベクトルの計算は不可

###ユークリッド距離

◎原点から終点までの直線距離
⇒2次元であれば、どの方向でも直角三角形
　⇒三平方の定理(c**2 = a**2 + b**2)が使える

Aの場合、 c*2 = 3**2 + 4**2
            c = 5

###マンハッタン距離

◎原点から座標軸に沿って終点に至るまでの距離
　⇒タンジェント(tan)のルートの長さ

Bの場合、 4 + 7 = 11(Bのマンハッタン距離)

###内積

AとBの内積
(3・4) + (4・7) = 12 + 28 = 40(AとBの内積)

###行列

・行列どうしの和や差を計算するには二つの行列の構造が同じである必要がある。
　⇒行や列の数が一つでも違うと計算できない
　⇔行列同士の掛け算は、行列Aの列数と行列Bの行数が同じであれば、可能。
https://gist.github.com/otinu/e8c2c3b0d10c5a99dd6ea18abdde802c?permalink_comment_id=4196917#gistcomment-4196917

・行列の列の数とベクトルのサイズが同じ場合は、これらの掛け算を定義することができ、
　結果は、元の行列の行数と同じサイズのベクトルになる。
https://gist.github.com/otinu/e8c2c3b0d10c5a99dd6ea18abdde802c?permalink_comment_id=4196909#gistcomment-4196909

・行列どうしの掛け算ではA*BとB*Aで積が異なる
　⇔ただし、正方行列を含む場合は積が同じになる
https://gist.github.com/otinu/e8c2c3b0d10c5a99dd6ea18abdde802c?permalink_comment_id=4196911#gistcomment-4196911

###次元削減
①行列4×10000 と 行列100000×3 の積を求めることができる
②最終的な積の構造は4×3になる  (1万個以上の要素を計算するにも関わらず)

③ならば、最初から【行列4×1 と 行列1×3 の積を求める計算をすればいい】という考え
　⇒【説明変数の次元数を削減すればいい】 と表現される

###  @演算子 / dot()

Pythonでは@演算子 または dot() によってドット積(行列どうしの積)を求めることができる
a = np.array([1, 3])    # [1 3]
b = np.array([-1, 5])   # [-1 5]

d = a @ b
d = np.dot(a, b)
print(d)
"""
# [1 3] @ [-1 5] = [(1 * -1) + (3 * 5) = 14
# https://study.prime-strategy.co.jp/wp-content/uploads/2021/01/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC19%E5%95%8Fd-2.png
"""


###積分
[サンプル]
　6x^2（6掛けるxの二乗）

◎サンプルを積分する とは、「Xの微分」 = サンプル + C(定数)　ということ
　⇒ (2(指数)+ 1)x = 6　をイメージすると求められる
　　⇒ サンプルの積分は、 2x^3 + C となる
https://gist.github.com/otinu/e8c2c3b0d10c5a99dd6ea18abdde802c?permalink_comment_id=4196940#gistcomment-4196940

・サンプルについて、2x^3, 2x^3 + 1, 2x^3 + 2, 2x^3 - 1 はいずれもサンプルの【不定積分】
https://goukaku-suppli.com/archives/38126

・「サンプルを1～2まで積分」した場合などを【定積分】という
　⇒サンプルを積分した後にx=1の場合とx=2の場合の和を求める
https://gist.github.com/otinu/e8c2c3b0d10c5a99dd6ea18abdde802c?permalink_comment_id=4196947#gistcomment-4196947
https://goukaku-suppli.com/archives/38253


◎微分は傾き、積分は面積と捉えることができる。

・データ分析や機会学習において、
　予測と測定値の接点 = 関数の傾きがゼロの点 ⇒ 有益な情報　となる
https://study.prime-strategy.co.jp/wp-content/uploads/2021/01/%E5%8B%BE%E9%85%8D%E9%99%8D%E4%B8%8B%E6%B3%95-1536x398.png

・x^3 + 2y^2 + 4z^4　のように、変数が複数存在する場合の微分を【偏微分】という。
　⇒偏微分ではどの変数で微分したのか示す必要がある
https://study.prime-strategy.co.jp/wp-content/uploads/2021/01/%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%898-6-1536x864.png
"""

"""
#確立と統計

・統計における中央値は全てのサンプル(データ)を順に並べた際の真ん中の値
　⇔平均値はサンプル総量の真ん中の値のイメージ。混同に注意
https://study.prime-strategy.co.jp/wp-content/uploads/2021/01/%E3%82%B9%E3%83%A9%E3%82%A4%E3%83%893-9-1536x864.png

・分散とは「すべてのデータの平均値からの差分を、2乗して、データの個数で割った値」

・6面体のサイコロを1回振った場合、その出目の数自体は不明なものの、奇数がでていることを教えられたとする。
　この場合の確率を条件付き確率と呼び、これはベイズの定理の基本となっている。

・確率変数が離散的な場合は確率質量関数、連続的な場合が確率密度関数
　⇒標準正規分布などの確率分布は、確率密度関数から得られます。
"""