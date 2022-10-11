#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Date: 2019/8/2
# spam_dat for content_filter by H.Shirouzu
#
# content_filter.py用設定ファイル
#
# 最初＆データ変更直後は
#   SPAM_ERRCODE = 450
#   DBG = 1
# で動作確認すると良い
#
# なお内容を変更すると、自動的に再ロード。
#

# ポート指定（起動時のみ使われ、spam_dat のリロードでは使われない）
#
SRC_ADDR   = ("localhost", 60025)
DST_ADDR   = ("localhost", 60026)

# マッチ指定の基本書式 (WHITE_DATA / CHECK_DATA)
#
# CHECK_DATA = [
#   [ b'正規表現1_1', b'正規表現1_2,... ],  # ルール1
#   [ b'正規表現2_1', b'正規表現2_2,... ],  # ルール2
#       :
#   [ b'正規表現n_1', b'正規表現2_2,... ],  # ルールn
# ]
#
#  1. 指定は正規表現で行う
#  2. １ルールにつき、１つ以上の正規表現文字列（バイト列）を列挙
#  3. １ルール内の全要素がマッチ（AND条件）＝ そのルールにマッチ
#  4. どれか１つのルールにマッチすると、判定終了
#

# これのどれかにマッチするメールは、無条件でSPAM除外判定
#

# ヘッダのみ検査
WHITE_HEAD = [
]
# ヘッダ＆ボディを検査
WHITE_DATA = [
	[r'(左達|さだち|武蔵野市|吉祥寺|システムメンテナンス|日本酒原価酒蔵)'.encode('utf8')],
]

# （上記を除いて）どれかにマッチするメールはSPAM判定
# （なお、base64/quoted-printable はデコードされるが、文字コードはそのまま）
# （つまり、元メールが JIS であれば、"xxx".encode("iso-2022-jp")等で指定）

# ヘッダのみ検査
CHECK_HEAD = [
]
# ヘッダ＆ボディを検査
CHECK_DATA = [
	# href=, Sunglasses, Deal をすべて含む場合メールを SPAMに
	# [rb'href=', rb'Sunglasses', rb'Deal'],

	# （b64デコード後の）元メール文字コードに合わせる必要あり。
	# encode を使う場合、rb'' ではなくr'' を使う

	# 汎用
	[r'銀行'.encode('utf8'), r'再開'.encode('utf8'), r'認証'.encode('utf8')],
	[r'アカウント'.encode('utf8'), r'24時間以内'.encode('utf8')],
	[r'認証'.encode('utf8'), r'24時間以内'.encode('utf8')],
        [r'銀行'.encode('utf8'), r'一部制限'.encode('utf8')],
        [r'カード'.encode('utf8'), r'一部制限'.encode('utf8')],
        [r'銀行'.encode('utf8'), r'盗もうと'.encode('utf8')],
        [r'カード'.encode('utf8'), r'盗もうと'.encode('utf8')],
	[rb'charset="gb2312"'],
	[r'与信失敗'.encode('utf8')],
	[r'手続き受付時より24時間'.encode('utf8')],
	[r'正当な保有者'.encode('utf8')],
	[r'異常な'.encode('utf8'), r'一時保留'.encode('utf8')],

	# Bitcoin系
	[r'ビットコイン'.encode('utf8'), r'警察'.encode('utf8')],
	[rb'Bitcoin', rb'BTC'],
	#[r'ビットコイン'.encode('iso-2022-jp'), r'警察'.encode('iso-2022-jp')],
	[r'ビットコイン'.encode('utf8'), r'マスターベーション'.encode('utf8')],
	[rb'bitcoin', r'マスターベーション'.encode('utf8')],
	[rb'BTC', r'マスターベーション'.encode('utf8')],

	# ETC系
	[r'ETCサービス'.encode('utf8')],
	[r'ＥＴＣサービス'.encode('utf8')],
	[r'ETC利用照会'.encode('utf8')],
	[r'ＥＴＣ利用照会'.encode('utf8')],

	# えきねっと
	[r'えきねっと'.encode('utf8'), r'退会'.encode('utf8')],

	# Amazon系
	[rb'Amazon', r'機能が制限'.encode('utf8')],
	[rb'Amazon', r'アカウントを維持'.encode('utf8')],
	[rb'Amazon', r'ロック'.encode('utf8')],
	[rb'Amazon', r'解約'.encode('utf8')],
	[rb'Amazon', r'親愛'.encode('utf8')],
	[rb'Amazon', r'直ちに更新'.encode('utf8')],
        [rb'Amazon', r'24時間以内'.encode('utf8')],
	[rb'amazon.co.jp', rb'from: <.+@gmail.com>'],
	[rb'Amazon', r'支払方法を更新'.encode('utf8')],

	# イオン系
	[r'イオン'.encode('utf8'), r'一部制限'.encode('utf8')],
	[rb'AEON', r'一部制限'.encode('utf8')],

	# 中国リンク
	[rb'http[s]?://[^/]+\.cn/'],
]

# SPAM判定されたメールのリターンコード
# （550: パーマネントエラー（再送なし）、450:テンポラリエラー（再送あり））
#
SPAM_ERRCODE = 550

# デバッグオプション（-1でファイル保存せず）
#
#  0: 内部エラー発生時だけ、SMTP通信内容をsmtpファイルとして保存。（TMP_DIR）
#
#  1:（上記に加えて）スパムの場合にも、smtpファイルを保存。
#     さらに、受信デコード内容及びマッチしたルールをspamファイルとして保存。
#
#  2:（上記に加えて）通常メールであっても、smtpファイルを保存。
#     さらに、受信デコード内容をsdecファイルとして保存。
#
DBG = 2

# 上記で、ファイルを作成する場合のディレクトリ
# 
TMP_DIR = "/tmp/content_filter/"


