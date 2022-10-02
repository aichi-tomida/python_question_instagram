# -*- coding: utf-8 -*-

import datetime
import json
import time
from pprint import pprint

import requests

import config_Instagram_Graph_API

# pydroid3でも動作確認済

# APIリクエスト用の関数
def InstaApiCall(url, params, request_type):

    # リクエスト
    if request_type == 'POST' :
        # POST
        req = requests.post(url,params)
    else :
        # GET
        req = requests.get(url,params)

    # レスポンス
    res = dict()
    res["url"] = url
    res["endpoint_params"]        = params
    res["endpoint_params_pretty"] = json.dumps(params, indent=4)
    res["json_data"]              = json.loads(req.content)
    res["json_data_pretty"]       = json.dumps(res["json_data"], indent=4)

    # 出力
    return res

# メディア作成
def createMedia(params) :
    """
    ******************************************************************************************************
    【画像・動画コンテンツ作成】
    https://graph.facebook.com/v5.0/{ig-user-id}/media?image_url={image-url}&caption={caption}&access_token={access-token}
    https://graph.facebook.com/v5.0/{ig-user-id}/media?video_url={video-url}&caption={caption}&access_token={access-token}
    ******************************************************************************************************
    """
    # エンドポイントURL
    url = params['endpoint_base'] + params['instagram_account_id'] + '/media'
    # エンドポイント用パラメータ
    Params = dict()
    Params['caption'] = params['caption']           # 投稿文
    Params['access_token'] = params['access_token'] # アクセストークン
    # メディアの区分け
    if 'IMAGE' == params['media_type'] :
        # 画像：メディアURLを画像URLに指定
        Params['image_url'] = params['media_url']    # 画像URL
    else :
        # 動画：メディアURLを動画URLに指定
        Params['media_type'] = params['media_type']  # メディアタイプ
        Params['video_url']  = params['media_url']   # ビデオURL

    print(' ------------------------------------------------------', url, Params ,sep='\t')
    # 出力
    return InstaApiCall(url, Params, 'POST')


# メディアID別ステータス管理
def getMediaStatus(mediaObjectId, params) :
    """
    ******************************************************************************************************
    【APIエンドポイント】
    https://graph.facebook.com/v5.0/{ig-container-id}?fields=status_code
    ******************************************************************************************************
    """
    # エンドポイントURL
    url = params['endpoint_base'] + '/' + mediaObjectId
    # パラメータ
    Params = dict()
    Params['fields']       = 'status_code'          # フィールド
    Params['access_token'] = params['access_token'] # アクセストークン
    # 出力
    return InstaApiCall(url, Params, 'GET')

# メディア投稿
def publishMedia(mediaObjectId, params):
    """
    ******************************************************************************************************
    【APIエンドポイント】
    https://graph.facebook.com/v5.0/{ig-user-id}/media_publish?creation_id={creation-id}&access_token={access-token}
    ******************************************************************************************************
    """
    # エンドポイントURL
    url = params['endpoint_base'] + params['instagram_account_id'] + '/media_publish'
    # エンドポイント送付用パラメータ
    Params = dict()
    Params['creation_id'] = mediaObjectId           # メディアID
    Params['access_token'] = params['access_token'] # アクセストークン
    # 出力
    return InstaApiCall(url, Params, 'POST')

# ユーザの公開レート制限・使用率を取得
def getContentPublishingLimit( params ) :
    """
    ******************************************************************************************************
    https://graph.facebook.com/v5.0/{ig-user-id}/content_publishing_limit?fields=config,quota_usage
    ******************************************************************************************************
    """
    # エンドポイントURL
    url = params['endpoint_base'] + params['instagram_account_id'] + '/content_publishing_limit' # endpoint url
    # エンドポイント送付用のパラメータ
    Params = dict()
    Params['fields'] = 'config,quota_usage'         # フィールド
    Params['access_token'] = params['access_token'] # アクセストークン

    return InstaApiCall(url, Params, 'GET')


# 画像投稿
def instagram_upload_image(media_url, media_caption):
    # パラメータ
    # params = basic_info()
    params = config_Instagram_Graph_API.basic_info()
    # ★★★★★★ 'IMAGE' 並びに 'VIDEO'の動作確認は取れた CAROUSEL_ALBUM は悩み中
    params['media_type'] = 'IMAGE'         # メディアType 'IMAGE' or 'VIDEO' もしくは以下
    # params['media_type'] = 'VIDEO'         # メディアType 'IMAGE' or 'VIDEO' もしくは以下
    # params['media_type'] = 'CAROUSEL_ALBUM' # 画像のみ2枚以上、動画のみ2つ以上、画像＋動画、動画＋画像はいずれもCAROUSEL_ALBUMになる
    params['media_url']  =  media_url      # メディアURL
    params['caption']    = media_caption

    # APIでメディア作成＆ID発行
    imageMediaId = createMedia(params)['json_data']['id']

    # メディアアップロード
    StatusCode = 'IN_PROGRESS';
    while StatusCode != 'FINISHED' :
        # メディアステータス取得
        StatusCode = getMediaStatus(imageMediaId,params)['json_data']['status_code']
        # 待ち時間
        time.sleep(2)

    # Instagramにメディア公開
    publishImageResponse = publishMedia(imageMediaId,params)
    # 出力
    print("Instagram投稿完了")
    return publishImageResponse['json_data_pretty']

if __name__ == "__main__":
   # 投稿内容 ※ローカル不可、複数不可

   # media_url      = 'C:/picture/2022-10-01/IMG20221001123005.jpg'  # 画像
   # media_url      = ['https://example.com/img/DSCN7564.JPG','https://example.com/img/IMG20210724153545_kai.jpg']
   media_url      = 'https://example.com/img/DSCN7564.JPG'           # 画像
   # media_url      = 'https://example.com/img/20220909150022.mp4'   # 動画
   media_caption  = '本日○○に来ています #公園 #park # 写真好きな人とつながりたい'               # 投稿文

   # 関数実行
   instagram_upload_image(media_url, media_caption)
