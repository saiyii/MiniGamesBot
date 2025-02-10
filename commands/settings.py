# commands/settings.py

async def show_settings(ctx):
    settings_message = "🔧 **Bot Settings** 🔧\n"
    settings_message += "1. Enable/Disable games\n"
    settings_message += "2. Customize rewards\n"
    await ctx.send(settings_message)
