import tweepy
import requests

# === Konfigurasi Twitter API ===
BEARER_TOKEN = "ISI_DENGAN_BEARER_TOKEN_TWITTER"

# === Konfigurasi Telegram ===
TELEGRAM_BOT_TOKEN = "ISI_DENGAN_TOKEN_BOT_TELEGRAM"
TELEGRAM_CHAT_ID = "ISI_DENGAN_CHAT_ID"

# === Fungsi Kirim Notifikasi ke Telegram ===
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

# === Streaming Listener ===
class TwitterStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        tweet_text = tweet.text  # Ambil isi tweet
        tweet_url = f"https://twitter.com/{tweet.author_id}/status/{tweet.id}"  # Buat URL tweet
        message = f"🚀 **Tweet Baru!**\n\n📌 *{tweet_text}*\n🔗 [Lihat Tweet]({tweet_url})"
        send_telegram_message(message)

# === Jalankan Stream ===
stream = TwitterStream(BEARER_TOKEN)
USER_ID = "ISI_DENGAN_USER_ID_TWITTER"  # ID akun Twitter target
stream.add_rules(tweepy.StreamRule(f"from:{USER_ID}"))
stream.filter()
