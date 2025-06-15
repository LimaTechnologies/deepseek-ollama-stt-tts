import asyncio
from audio.recorder import record_text
from audio.tts import play_text
from utils.cleaner import deletar_todos_os_arquivos
from ai.ollama_client import perguntar_ollama
import pygame

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

AGENT_NAME = "ok"
IS_RUNNING = False
END_WORD = "finalizo"
FULL_TEXT = "Em até 300 palavras resposta a pergunta ou afirmação do usuário, de modo direto e descontraído, sem formalidades. Se a resposta for uma pergunta, responda com uma afirmação direta. Se a resposta for uma afirmação, responda com uma pergunta direta. Sempre use o nome do usuário no início da resposta, usuario joão, e resposda em portugues brasileiro. Se o usuário disser 'cancelar', pare de falar e aguarde a próxima entrada de voz."

deletar_todos_os_arquivos()

def run_bot():
    global IS_RUNNING, FULL_TEXT, AGENT_NAME, END_WORD
    while True:
        texto_entrada = record_text()
        
        print("🎤 Entrada de voz:", texto_entrada)
        
        if not texto_entrada:
            continue

        palavras = texto_entrada.lower().split()
        
        if "cancelar" in palavras and not AGENT_NAME in palavras:
            pygame.mixer.music.stop()
            asyncio.run(play_text("Ok, cancelando."))
            continue
        
        if(not IS_RUNNING):
            if AGENT_NAME in palavras:
                IS_RUNNING = True
                asyncio.run(play_text("Estou ouvindo"))
            else:
                continue
        
        FULL_TEXT += " " + texto_entrada
        
        SPLITTED_TEXT = FULL_TEXT.lower().split()
        
        if END_WORD in SPLITTED_TEXT:
            SPLITTED_TEXT.remove(AGENT_NAME)
            SPLITTED_TEXT.remove(END_WORD)
           
            prompt = " ".join(SPLITTED_TEXT)
            
            IS_RUNNING = False
            SPLITTED_TEXT = ""

            if prompt:
                asyncio.run(play_text("Gerando resposta..."))
                resposta = perguntar_ollama(prompt)
                print("🧠 Resposta do Ollama:", resposta)
                asyncio.run(play_text(resposta))

if __name__ == "__main__":
    run_bot()
