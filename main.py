import discord
from discord.ext import commands
from commands import dice, quiz, hotpotato, math, rps, leaderboard, settings

# Création de l'instance du bot avec un préfixe '!'
intents = discord.Intents.all()
intents.members = True  # Pour récupérer les événements sur les membres
intents.messages = True  # Pour recevoir les événements sur les messages
bot = commands.Bot(command_prefix='!', intents=intents)

# Commande pour jouer à un jeu spécifique
@bot.command()
async def play(ctx, game: str):
    if game.lower() == "dice":
        await dice.play_dice(ctx)  # Appel de la fonction du jeu de dés
    elif game.lower() == "quiz":
        await quiz.play_quiz(ctx)  # Appel de la fonction du quiz
    elif game.lower() == "hotpotato":
        await hotpotato.play_hotpotato(ctx)  # Appel de la fonction du jeu Hot Potato
    elif game.lower() == "math":
        await math.play_math(ctx)  # Appel de la fonction du jeu mathématique
    elif game.lower() == "rps":
        await rps.play_rps(ctx)  # Appel de la fonction du jeu Pierre-papier-ciseaux
    else:
        await ctx.send("Jeu non reconnu. Choisis parmi: dice, quiz, hotpotato, math, rps.")

# Commande pour afficher le leaderboard
@bot.command()
async def leaderboard(ctx):
    try:
        await leaderboard.show_leaderboard(ctx)  # Affiche le tableau des scores
    except AttributeError:
        await ctx.send("Il y a un problème pour afficher le leaderboard. Vérifie les fichiers du module leaderboard.")

# Commande pour afficher les paramètres du bot
@bot.command()
async def settings(ctx):
    try:
        await settings.show_settings(ctx)  # Affiche les paramètres du bot
    except AttributeError:
        await ctx.send("Il y a un problème pour afficher les paramètres. Vérifie les fichiers du module settings.")

# Démarrage du bot avec ton token (N'oublie pas de remplacer ce token avec le bon)
bot.run('YOUR_BOT_TOKEN')
