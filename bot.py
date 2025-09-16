from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 Tumhara Bot Token
TOKEN = "8171331380:AAEOxdrZANqNYWxd84xwZ7N088FVvNBkCJ8"

# 🖼 Image URLs
THUMBNAIL_URL = "https://i.postimg.cc/D0v3QFq2/thumbnail.png"
CLASS9_URL = "https://i.postimg.cc/4yPZjnJ7/class9th.jpg"
CLASS10_URL = "https://i.postimg.cc/6pLVgXRs/class10th.jpg"
CLASS11_URL = "https://i.postimg.cc/7ZxJCTCc/class11th.jpg"


# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Class 9", callback_data="class9")],
        [InlineKeyboardButton("📗 Class 10", callback_data="class10")],
        [InlineKeyboardButton("📕 Class 11", callback_data="class11")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=THUMBNAIL_URL,
        caption="👋 Dear student,\nWelcome to *TheMadXpawan Bot*.\n\nChoose your class to start your Free learning Journey!",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


# Button click handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "class9":
        await query.message.reply_photo(
            photo=CLASS9_URL,
            caption="✅ Thank you for using our bot!\nHere is your destination link for *Class 9*: [Join Class 9 Channel](https://t.me/nexttoper9thAarambh)",
            parse_mode="Markdown"
        )

    elif query.data == "class10":
        await query.message.reply_photo(
            photo=CLASS10_URL,
            caption="✅ Thank you for using our bot!\nHere is your destination link for *Class 10*: [Join Class 10 Channel](https://t.me/nexttoper10thAarambh)",
            parse_mode="Markdown"
        )

    elif query.data == "class11":
        await query.message.reply_photo(
            photo=CLASS11_URL,
            caption="✅ Thank you for using our bot!\nHere is your destination link for *Class 11*: [Join Class 11 Channel](https://t.me/nexttoperclass11th)",
            parse_mode="Markdown"
        )

    # Final message
    await query.message.reply_text("🔥 Is baar system faad denge!! 🔥")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🤖 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()