# leaderboard.py
async def show_leaderboard(ctx):
    leaderboard_message = "🏆 **Leaderboard** 🏆\n"
    leaderboard_message += "1. Player A\n"
    leaderboard_message += "2. Player B\n"
    await ctx.send(leaderboard_message)
