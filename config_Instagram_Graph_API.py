# Instagram Graph API の configファイル

# 【要修正】の所は各個人の情報に合わせる事
#  今回、グラフAPIエクスプローラ POST→ v15.0とした

def basic_info():
    # 初期
    config = dict()
    # 【要修正】アクセストークン
    config["access_token"]         = 'XXXXX'
    # 【要修正】アプリID
    config["app_id"]               = 'XXXXX'
    # 【要修正】アプリシークレット
    config["app_secret"]           = 'XXXXX'
    # 【要修正】インスタグラムビジネスアカウントID
    config['instagram_account_id'] = "XXXXX"
    # 【要修正】グラフバージョン
    config["version"]              = 'v15.0'
    # 【修正不要】graphドメイン
    config["graph_domain"]         = 'https://graph.facebook.com/'
    # 【修正不要】エンドポイント
    config["endpoint_base"]        = config["graph_domain"]+config["version"] + '/'
    # 出力
    return config
