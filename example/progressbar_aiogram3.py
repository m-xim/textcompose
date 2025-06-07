import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from magic_filter import F

from textcompose import Template
from textcompose.elements import Format, ProgressBar

# Initialize the bot with your token
bot = Bot("YOUR_BOT_TOKEN")
dp = Dispatcher()

# Define the message template with a progress bar
template = Template(
    Format("🚀 Task in progress: {task_name}"),
    ProgressBar(current=F["done"], total=100, width=12),
    Format("Completed: {status_emoji} {done}%"),
    sep="\n\n",
)


# Function to determine the status emoji based on progress percentage
def status_emoji(ctx):
    percent = ctx["done"]
    if percent >= 100:
        return "✅"
    elif percent > 70:
        return "🟢"
    elif percent > 40:
        return "🟡"
    else:
        return "🟠"


# Handler for the /progress command
@dp.message(Command("progress"))
async def handle_progress(message: types.Message):
    ctx = {
        "done": 0,
        "task_name": "Data upload",
        "status_emoji": status_emoji({"done": 0}),
    }
    rendered = template.render(ctx)
    sent = await message.answer(rendered)

    # Simulate task progress
    for i in range(1, 101, 9):
        await asyncio.sleep(0.45)
        ctx["done"] = i
        ctx["status_emoji"] = status_emoji(ctx)
        await sent.edit_text(template.render(ctx))


# Start the bot
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
