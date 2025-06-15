import edge_tts
import asyncio
import pygame
import uuid
import os
import re

VOICE = "pt-BR-AntonioNeural"

async def play_text(text: str):
    print("Preparando o áudio para rodar...")
    output_file = f"audios/{uuid.uuid4().hex}.mp3"
    
    text = re.sub(r'[^a-zA-Z0-9áéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ .,;:!?\'"-]', '', text)
    
    if "</think>" in text:
        text = text.split("</think>", 1)[1]
    
    communicate = edge_tts.Communicate(text, VOICE)

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.stop()

    await communicate.save(output_file)

    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()
