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
	[r'左達'.encode('utf8')],
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

	# Bitcoin系
	[rb'Bitcoin', rb'BTC'],
	[r'ビットコイン'.encode('utf8'), r'警察'.encode('utf8')],
	[r'ビットコイン'.encode('iso-2022-jp'), r'警察'.encode('iso-2022-jp')],
	#[rb'&#12499;&#12483;&#12488;&#12467;&#12452;&#12531;', rb'&#35686;&#23519;'],
	[r'(copy and paste|Ƿorn|Ƿayment|camera|video)'.encode('utf8')],

	# ETC系
	[r'(ETCサービス|ＥＴＣサービス|ETC利用照会|ＥＴＣ利用照会)'.encode('utf8')],

	# えきねっと
	[r'えきねっと'.encode('utf8'), r'退会'.encode('utf8')],

	# Amazon系
	[
	  rb'Amazon',
	  r'(エラー|維持|プライム|ロック|解約)'.encode('utf8'),
	],
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

