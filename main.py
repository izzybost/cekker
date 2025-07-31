import telebot
import os

# Ambil token dari environment variable BOT_TOKEN
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Daftar lengkap prefix provider Indonesia
prefix_provider = {
    # Telkomsel
    '0811': 'Telkomsel', '0812': 'Telkomsel', '0813': 'Telkomsel',
    '0821': 'Telkomsel', '0822': 'Telkomsel', '0823': 'Telkomsel',
    '0852': 'Telkomsel', '0853': 'Telkomsel', '0851': 'by.U (Telkomsel)',

    # Indosat Ooredoo Hutchison
    '0814': 'Indosat', '0815': 'Indosat', '0816': 'Indosat',
    '0855': 'Indosat Matrix', '0856': 'Indosat IM3', '0857': 'Indosat IM3', '0858': 'Indosat IM3',

    # XL Axiata
    '0817': 'XL', '0818': 'XL', '0819': 'XL',
    '0859': 'XL', '0877': 'XL', '0878': 'XL',

    # Axis (anak perusahaan XL)
    '0831': 'Axis', '0832': 'Axis', '0833': 'Axis', '0838': 'Axis',

    # Tri (3)
    '0895': 'Tri (3)', '0896': 'Tri (3)', '0897': 'Tri (3)', '0898': 'Tri (3)', '0899': 'Tri (3)',

    # Smartfren
    '0881': 'Smartfren', '0882': 'Smartfren', '0883': 'Smartfren',
    '0884': 'Smartfren', '0885': 'Smartfren', '0886': 'Smartfren',
    '0887': 'Smartfren', '0888': 'Smartfren', '0889': 'Smartfren',
}

# Fungsi cek provider berdasarkan 4 digit prefix
def cek_provider(nomor):
    nomor = nomor.strip().replace('+62', '0')
    prefix = nomor[:4]
    return prefix_provider.get(prefix, 'Provider tidak dikenal')

# Handler untuk semua pesan masuk
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    nomor = message.text.strip()
    if nomor.startswith('08') or nomor.startswith('+62'):
        provider = cek_provider(nomor)
        bot.reply_to(message, f"✅ Nomor {nomor} adalah dari: *{provider}*", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Kirim nomor HP yang valid (08xxx atau +62xxx)")

# Menjalankan bot
print("Bot jalan...")
bot.polling()
