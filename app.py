import streamlit as st

# ホームページのタイトル
st.title('山田バイクショップ')

# ショップの画像
st.image('image/shop.webp', caption='山田バイクショップの外観')

# ショップについての説明
st.header('ショップについて')
st.write('山田バイクショップへようこそ！私たちは、最高のバイクとサービスを提供することに情熱を注いでいます。')

# 提供サービスの一覧
st.header('提供サービス')
st.write('''
- 新車・中古車の販売
- 修理・メンテナンス
- カスタマイズ
- レンタルサービス
''')

# バイクの画像
st.image(['image/bike.webp', 'image/bike.webp'], caption=['バイク1', 'バイク2'])

# 連絡先情報
st.header('連絡先')
st.write('住所: 東京都新宿区...')
st.write('電話番号: 03-1234-5678')
st.write('メールアドレス: contact@yamadabike.com')
