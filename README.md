# python_question_instagram
pythonでInstagram投稿

参考サイト
https://di-acc2.com/system/rpa/19288/
https://di-acc2.com/system/rpa/19280/
https://di-acc2.com/marketing/sns-tech/18499/
https://developers.facebook.com/docs/instagram-basic-display-api/reference/media?locale=ja_JP


ハッシュタグ入力の省力化の為、PC/スマホのpythonからの投稿が出来るようにしたい

【現在出来ている事】
[1] IMAGE　設定時の写真一枚投稿
[2] VIDEO　設定時の動画一個投稿


【今後出来るようにしたいこと】

[1] 複数のファイルを一括投稿 [CAROUSEL_ALBUM] でも可能にしたい
※ここまではなるべく早めに解決したい

※以下、可能であれば実装したい
[2]ローカル (Windows / pydroid3 )の画像も対象にしたい

【別途注意】
facebookやInstagramの開発者用の設定等が必要。
当方は問題なく出来ている。


トークン発行時、グラフAPIエクスプローラ　にて POST v15.0にすること
me?fields=accounts{name,instagram_business_account,access_token} で検索
