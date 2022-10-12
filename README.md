# python_question_instagram
pythonでInstagram投稿

【事前準備】
https://di-acc2.com/system/rpa/19280/
     Instagram Graph APIの利用手順｜InstagramとFacebookの連携
       1.インスタグラムプロアカウントの開設
       2.Meta Business Suiteにアカウントを登録する
       3.FacebookとInstagramをリンク
     (上記がわかりにくいようであれば https://www.asobou.co.jp/blog/web/facebookgraphapi )  

【参考サイト】
https://di-acc2.com/system/rpa/19288/

https://di-acc2.com/marketing/sns-tech/18499/
  → Meta for Developersにアクセスし開発者登録
https://developers.facebook.com/docs/instagram-basic-display-api/reference/media?locale=ja_JP
  → 開発者ドキュメント

Meta for Developers
https://developers.facebook.com/
Meta for Developers_グラフAPI
https://developers.facebook.com/docs/graph-api

メディアの読み取り
メソッドについて
https://developers.facebook.com/docs/instagram-basic-display-api/reference/media?locale=ja_JP

[脱線？]CAROUSEL_ALBUM の ダウンロードの場合
https://shintaro-lab.hatenablog.com/entry/2022/08/28/221900

【目的】
ハッシュタグ入力の省力化の為、PC/スマホのpythonからの投稿が出来るようにしたい

【現在出来ている事】
※Windows、pydroid3(Androidでpythonを動かすアプリ)で確認
[1] IMAGE　設定時の写真一枚投稿 (投稿できるのはWebサーバに上がっているファイルのみ？)
[2] VIDEO　設定時の動画一個投稿 (投稿できるのはWebサーバに上がっているファイルのみ？)


【今後出来るようにしたいこと】

[1] 複数のファイルを一括投稿 [CAROUSEL_ALBUM] でも可能にしたい
※ここまではなるべく早めに解決したい

※以下、可能であれば実装したい
[2]ローカル (Windows / pydroid3 )の画像も対象にしたい

【別途注意】
facebookやInstagramの開発者用の設定等が必要。

Instagramはビジネスアカウント（プロアカウント）に切り換える
（Instagramクリエイターアカウントでは不可）
facebookはMeta for DevelopersウェブサイトにてFacebook開発者として登録する必要がある。

当方は問題なく出来ている。


トークン発行時、グラフAPIエクスプローラ　にて POST v15.0にすること
me?fields=accounts{name,instagram_business_account,access_token} で検索
