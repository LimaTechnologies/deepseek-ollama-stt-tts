# deepseek-ollama-tts-speech

Um app simples para interação por voz usando reconhecimento de fala, integração com Ollama e síntese de voz (TTS).

## Funcionalidades

- **Ativação por voz:** Diga "ok" para iniciar a gravação.
- **Feedback sonoro:** O app avisa quando está pronto para ouvir.
- **Reconhecimento de fala:** Grave sua mensagem normalmente.
- **Finalização por voz:** Diga "finalizo" para encerrar a gravação.
- **Processamento automático:** O app envia sua fala para o Ollama, recebe a resposta e converte em áudio (TTS).

## Como usar

1. Instale as dependências necessárias (veja `requirements.txt`).
2. Certifique-se de que o modelo `deepseek-r1:8b` está instalado e rodando no Ollama ([veja aqui](https://ollama.com/library/deepseek-r1)).  
    - Caso queira usar outro modelo, altere o parâmetro correspondente em `ollama_client.py` ou em `main.py`.
3. Execute o app:
     ```bash
     python main.py
     ```
5. Diga "ok" para começar a gravar.
6. Fale normalmente.
7. Diga "finalizo" para encerrar e ouvir a resposta.

## Requisitos

- Python 3.8+
- Microfone configurado
- Dependências do projeto (`pip install -r requirements.txt`)
- Ollama instalado e rodando com o modelo `deepseek-r1:8b`

## Observações

- O app utiliza o Ollama para processar as mensagens.
- A resposta é convertida em áudio usando TTS.