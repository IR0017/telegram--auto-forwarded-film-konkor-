# 🎬 Telegram Konkur Auto Forward Bot

این پروژه شامل دو اسکریپت پایتون است که با استفاده از تلگرام، ویدیوهای ربات‌های آموزشی کنکور را به صورت خودکار فوروارد می‌کند و ذخیره می‌کند.

---

## 🚀 ویژگی‌ها

* ⏱️ فوروارد خودکار و سریع ویدیوها (کمتر از ۳۰ ثانیه)
* 🔗 استخراج لینک‌ها از پیام‌های ذخیره شده تلگرام
* 🗄️ جلوگیری از فوروارد دوباره پیام‌ها
* 📂 مرتب‌سازی ویدیوها به ترتیب انتشار

---

## ⚙️ نصب و راه‌اندازی

### پیش‌نیازها

* Python 3.10+
* pip
* [Telethon](https://docs.telethon.dev/en/latest/)
* حساب تلگرام برای گرفتن **API\_ID** و **API\_HASH**
* Bot Token از @BotFather (در صورت نیاز به استفاده از ربات)

### مراحل نصب

```bash
# کلون کردن مخزن
git clone https://github.com/IR0017/telegram-konkur-bot.git
cd telegram-konkur-bot

# ساخت محیط مجازی (اختیاری)
python -m venv venv
source venv/bin/activate   # لینوکس
venv\Scripts\activate      # ویندوز

# نصب وابستگی‌ها
pip install -r requirements.txt
```

---

## 🔑 پیکربندی

### 1️⃣ استخراج لینک‌ها

در `extract_links.py` مقادیر زیر را تنظیم کنید:

```python
api_id = "API ID تلگرام"
api_hash = "API HASH تلگرام"
phone = "+98********"
output_file = "saved_links.txt"
```

### 2️⃣ فوروارد خودکار

در `forward_bot.py` مقادیر زیر را تنظیم کنید:

```python
api_id = "API ID تلگرام"
api_hash = "API HASH تلگرام"
phone = "+98********"

bot_links = [
    "لینک ربات‌ها یا لینک‌هایی که extract_links.py ایجاد کرده"
]

target_channel = "@your_channel_username یا ID کانال"

forwarded_ids_file = "forwarded_ids.txt"
```

---

## ▶️ اجرای پروژه

1. **استخراج لینک‌ها**

```bash
python extract_links.py
```

این اسکریپت لینک‌ها را از پیام‌های ذخیره شده تلگرام استخراج و در `saved_links.txt` ذخیره می‌کند.

2. **فوروارد خودکار فایل‌ها**

```bash
python forward_bot.py
```

این اسکریپت لینک‌ها را پردازش کرده و فایل‌ها را به کانال مشخص شده فوروارد می‌کند.

---

## 📂 ساختار پوشه‌ها

```
project/
│── extract_links.py
│── forward_bot.py
│── requirements.txt
│── forwarded_ids.txt   # ایجاد می‌شود هنگام فوروارد
│── saved_links.txt     # ایجاد می‌شود هنگام استخراج لینک‌ها
│── README.md
```

---

## 🤝 مشارکت

پیشنهادها و Pull Request ها خوش‌آمدند 🙌

---

## 📜 لایسنس

[MIT](LICENSE)
