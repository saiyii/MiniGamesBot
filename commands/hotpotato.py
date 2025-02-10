import random
import asyncio

async def play_hotpotato(ctx):
    players = [ctx.author.name]
    await ctx.send(f"Hot Potato! {ctx.author.name}, you start the game. Pass the bomb before it explodes!")
    
    def check(m):
        return m.author != ctx.author and m.channel == ctx.channel

    for i in range(5):  # Let's keep it short
        try:
            msg = await ctx.bot.wait_for('message', timeout=5.0, check=check)
            players.append(msg.author.name)
        except TimeoutError:
            await ctx.send(f"Time's up! {random.choice(players)} lost!")
            return

    winner = random.choice(players)
    await ctx.send(f"{winner} is the last one standing! 🎉")
