from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from database import init_db, add_order

TOKEN = os.environ.get("8244327788:AAFm65A4qykA6z_4FzyDlsglsQvxx0yLu4U")

# بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username or update.effective_user.first_name
    await update.message.reply_text(f"أهلاً @{username}! 👋\nاكتب /order لتسجيل طلبك.")

# أمر الطلب
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    add_order(user_id, username)
    await update.message.reply_text("✅ تم تسجيل طلبك! شكراً لك.")

# إنشاء التطبيق
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("order", order))

if __name__ == '__main__':
    init_db()
    app.run_polling()
