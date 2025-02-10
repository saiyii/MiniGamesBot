import random

async def play_rps(ctx):
    options = ["rock", "paper", "scissors"]
    await ctx.send("Choose rock, paper, or scissors!")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in options

    try:
        msg = await ctx.bot.wait_for('message', timeout=15.0, check=check)
    except TimeoutError:
        await ctx.send(f"Time's up! {ctx.author.name} loses!")
        return

    player_choice = msg.content.lower()
    bot_choice = random.choice(options)
    
    await ctx.send(f"{ctx.author.name} chose {player_choice}, Bot chose {bot_choice}.")
    
    if player_choice == bot_choice:
        await ctx.send("It's a tie!")
    elif (player_choice == "rock" and bot_choice == "scissors") or (player_choice == "scissors" and bot_choice == "paper") or (player_choice == "paper" and bot_choice == "rock"):
        await ctx.send(f"{ctx.author.name} wins!")
    else:
        await ctx.send(f"Bot wins!")
