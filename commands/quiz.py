import random

questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    # Add more questions
]

async def play_quiz(ctx):
    question = random.choice(questions)
    await ctx.send(f"Quiz time! {question['question']}")
    
    def check(m):
        return m.channel == ctx.channel

    try:
        msg = await ctx.bot.wait_for('message', timeout=15.0, check=check)
    except TimeoutError:
        await ctx.send(f"Time's up! The correct answer was {question['answer']}.")
        return

    if msg.content.lower() == question['answer']:
        await ctx.send(f"Correct! {msg.author.name} wins!")
    else:
        await ctx.send(f"Wrong! The correct answer was {question['answer']}.")
