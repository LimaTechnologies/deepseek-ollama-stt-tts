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
    
    text = re.sub(r'^.*?</think>', '', text, flags=re.DOTALL)
    
    # text = re.sub(r'[^a-zA-Z0-9áéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ .,;:!?\'"-]', '', text)
    # Pega apenas o texto após a primeira ocorrência de "</think>"
    # Extrai apenas o texto após a primeira ocorrência de "</think>", se existir
    communicate = edge_tts.Communicate(text, VOICE)

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.stop()

    await communicate.save(output_file)

    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()
