import random

async def play_math(ctx):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2
    await ctx.send(f"What is {num1} + {num2}?")
    
    def check(m):
        return m.channel == ctx.channel

    try:
        msg = await ctx.bot.wait_for('message', timeout=10.0, check=check)
    except TimeoutError:
        await ctx.send(f"Time's up! The correct answer was {answer}.")
        return

    if int(msg.content) == answer:
        await ctx.send(f"Correct! {msg.author.name} wins!")
    else:
        await ctx.send(f"Wrong! The correct answer was {answer}.")
