"""
# Matplotlib

##拡張子ごとの読み込み・書き込み 関数一覧

・style属性 ⇒ 装飾(文字の色など)の追加
    https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC27%E5%95%8F%E9%81%B8%E6%8A%9E%E8%82%A2%E2%91%A0%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E3%82%B3%E3%83%BC%E3%83%892-1536x793.png
・plot() ⇒ 線の太さ・種類・色 などを追加(linewidth=10 や linestyle="--" 、color="red"など)

・suptitle() ⇒ 描画オブジェクトのタイトルを指定
・set_title() ⇒ サブプロットのタイトルを指定
    set_titleでは、フォントの種類・文字の大きさ・太さ などの変更が可能(family='monospace', size=25, weight='heavy' など)

・legend() ⇒ サブプロットでの凡例を表示
　また、 loc=”best” を指定するとデータとの重なりが最小な位置に出力できる。

・savefig() ⇒ ファイルに出力。ファイル形式としては、png、pdf、svgなどが選択可能。

・text() ⇒　グラフ上の好きな座標に好きな文字列を出力できる
    https://gist.github.com/otinu/e8c2c3b0d10c5a99dd6ea18abdde802c?permalink_comment_id=4197299#gistcomment-4197299

・様々な種類のグラフを描画できる
    https://study.prime-strategy.co.jp/wp-content/uploads/2021/02/%E7%AC%AC1%E5%9B%9E_Python3%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E6%A8%A1%E8%A9%A6_%E7%AC%AC27%E5%95%8F%E9%81%B8%E6%8A%9E%E8%82%A2%E2%91%A42-1024x260.png


・2種類の棒グラフを一つにまとめたマーブル状の棒グラフを作ることもできる
    https://study.prime-strategy.co.jp/coverage/py3an1-30/
    　⇒マーブルにするための肝は一つのサブプロットに2つめ以降のグラフを追加するとき、片方の座標は同じにする(上記URLではX座標がどちらもx)

・Numpy.randomモジュールを活用し、横向きのヒストグラムを作成することもできる
　また、それぞれのbin(棒グラフ)の範囲や境界値を取得することもできる
    https://study.prime-strategy.co.jp/coverage/py3an1-31/

・円グラフの作成
    [サンプル]
    ax.pie(x, labels=labels, startangle=90, counterclock=False, shadow=True, autopct=’%1.2f%%’)
    ・xでグラフの中身を指定
    ・startangle=90 で12時を始点に指定(デフォルトは3時)
    ・counterclock=False で時計回りを指定
    ・autopct=’%1.2f%%’で整数部は最低1桁・小数部は2桁を指定(末尾の%は純粋に'%'として出力される)
https://study.prime-strategy.co.jp/coverage/py3an1-32/
"""