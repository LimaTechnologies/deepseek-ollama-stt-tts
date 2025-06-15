import os

def deletar_todos_os_arquivos(pasta='audios'):
    if not os.path.exists(pasta):
        os.makedirs(pasta)  # Cria a pasta se não existir
        return

    arquivos = os.listdir(pasta)
    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_completo):
            try:
                os.remove(caminho_completo)
                print(f"Deletado: {caminho_completo}")
            except Exception as e:
                print(f"Erro ao deletar {caminho_completo}: {e}")
