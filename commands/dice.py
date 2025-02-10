import random

async def play_dice(ctx):
    await ctx.send(f"{ctx.author.name} is rolling the dice... 🎲")
    
    # Player 1 rolls the dice
    player1_roll = random.randint(1, 6)
    await ctx.send(f"{ctx.author.name} rolled a {player1_roll}!")

    # Wait for second player
    def check(m):
        return m.author != ctx.author and m.channel == ctx.channel

    try:
        msg = await ctx.bot.wait_for('message', timeout=30.0, check=check)
    except TimeoutError:
        await ctx.send(f"Time's up! {ctx.author.name} wins by default!")
        return

    player2_roll = random.randint(1, 6)
    await ctx.send(f"{msg.author.name} rolled a {player2_roll}!")

    # Determine the winner
    if player1_roll > player2_roll:
        await ctx.send(f"{ctx.author.name} wins with a {player1_roll}!")
    elif player1_roll < player2_roll:
        await ctx.send(f"{msg.author.name} wins with a {player2_roll}!")
    else:
        await ctx.send(f"It's a tie with both rolling {player1_roll}!")
