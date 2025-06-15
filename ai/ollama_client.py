import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def perguntar_ollama(prompt: str, model="deepseek-r1:8b"):
    print(f"Enviando requisição para Ollama com o prompt: {prompt}")
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        data = response.json()
        return data.get("response", "").strip()
    else:
        print(f"Ollama erro: {response.status_code}")
        return "Desculpe, ocorreu um erro ao obter a resposta da IA."
