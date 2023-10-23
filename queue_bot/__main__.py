import os

from telegram.ext import ApplicationBuilder, CommandHandler

from .handlers import start_handler


token = os.environ.get('QUEUE_BOT_TOKEN')
app = ApplicationBuilder().token(token).build()

    
app.add_handler(CommandHandler('start', start_handler))

app.run_polling()