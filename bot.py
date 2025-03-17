
import discord
from discord.ext import commands
from database import TaskDatabase

bot = commands.Bot(command_prefix='!')

# Veritabanı bağlantısını başlat
db = TaskDatabase()

@bot.command()
async def add_task(ctx, description: str):
    """Görev ekler"""
    task_id = db.add_task(description)
    await ctx.send(f'Görev eklendi: {description} (ID: {task_id})')

@bot.command()
async def delete_task(ctx, task_id: int):
    """Görev siler"""
    if db.delete_task(task_id):
        await ctx.send(f'Görev silindi: {task_id}')
    else:
        await ctx.send(f'Görev bulunamadı: {task_id}')

@bot.command()
async def show_tasks(ctx):
    """Tüm görevleri gösterir"""
    tasks = db.get_all_tasks()
    if tasks:
        response = "\n".join([f"ID: {task[0]} - {task[1]} - {'Tamamlandı' if task[2] else 'Tamamlanmadı'}" for task in tasks])
        await ctx.send(response)
    else:
        await ctx.send("Hiç görev bulunmamaktadır.")

@bot.command()
async def complete_task(ctx, task_id: int):
    """Görevi tamamlanmış olarak işaretler"""
    if db.complete_task(task_id):
        await ctx.send(f'Görev tamamlandı: {task_id}')
    else:
        await ctx.send(f'Görev bulunamadı: {task_id}')

bot.run('YOUR_DISCORD_TOKEN')
