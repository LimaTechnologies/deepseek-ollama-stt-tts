import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

inital_prompt = "Embody Jarvis from Iron Man: be direct, concise, and intelligent. Engage in natural conversations, using context from previous interactions. Handle a wide range of tasks effectively. Provide short responses when appropriate, and add personality only when it fits."


def perguntar_ollama(prompt: str, model="deepseek-r1:8b"):
    print(f"Enviando requisição para Ollama com o prompt: {prompt}")
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "deepseek-r1:8b",
            "messages": [
                {"role": "system", "content": inital_prompt},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
        },
    )

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data.get("message", {}).get("content", "").strip()
    else:
        print(f"Ollama erro: {response.status_code}")
        return "Desculpe, ocorreu um erro ao obter a resposta da IA."
