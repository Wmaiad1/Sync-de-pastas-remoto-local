# %%

import os
import shutil
import time

# Configuração dos caminhos (Origem e Destino)
ORIGEM = r"C:\Users\WalaceFranciscoMaia\OneDrive - NIAD SHOPPING CENTERS\Downloads"
DESTINO = r"C:\Users\WalaceFranciscoMaia\OneDrive - NIAD SHOPPING CENTERS\Desktop\Rsync"

def sincronizar_pastas():
    # Cria a pasta de destino se ela não existir
    if not os.path.exists(DESTINO):
        os.makedirs(DESTINO)
        print(f"Pasta de destino criada: {DESTINO}")

    # 1. Copiar arquivos novos ou modificados da Origem para o Destino
    for item in os.listdir(ORIGEM):
        caminho_origem = os.path.join(ORIGEM, item)
        caminho_destino = os.path.join(DESTINO, item)
        
        # Pula o próprio arquivo do script se ele estiver na mesma pasta
        if "__file__" in locals() and caminho_origem == os.path.abspath(__file__):
            continue

        try:
            if os.path.isdir(caminho_origem):
                # Se for uma pasta, copia a árvore de diretórios
                if os.path.exists(caminho_destino):
                    shutil.rmtree(caminho_destino)
                shutil.copytree(caminho_origem, caminho_destino)
                print(f"Pasta copiada: {item}")
            else:
                # Se for um arquivo, verifica se mudou antes de copiar
                if not os.path.exists(caminho_destino) or os.path.getmtime(caminho_origem) > os.path.getmtime(caminho_destino):
                    shutil.copy2(caminho_origem, caminho_destino)
                    print(f"Arquivo copiado/atualizado: {item}")
        except Exception as e:
            print(f"Erro ao copiar {item}: {e}")

    # 2. Efeito Espelho (/MIR): Deleta no Destino o que não existe mais na Origem
    for item in os.listdir(DESTINO):
        caminho_origem = os.path.join(ORIGEM, item)
        caminho_destino = os.path.join(DESTINO, item)
        
        if not os.path.exists(caminho_origem):
            try:
                if os.path.isdir(caminho_destino):
                    shutil.rmtree(caminho_destino)
                else:
                    os.remove(caminho_destino)
                print(f"Item excluído no destino (não existe na origem): {item}")
            except Exception as e:
                print(f"Erro ao excluir {item}: {e}")

print("Monitoramento iniciado... Pressione CTRL+C para fechar.")
while True:
    try:
        sincronizar_pastas()
        time.sleep(10)  # Verifica se há alterações a cada 10 segundos
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo usuário.")
        break
    except Exception as e:
        print(f"Erro no loop de monitoramento: {e}")
        time.sleep(10)

# %%
