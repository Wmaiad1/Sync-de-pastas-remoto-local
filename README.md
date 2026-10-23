# sync-pastas

Um script Python que mantém uma pasta de destino como espelho de uma pasta de origem. Ele copia arquivos novos ou modificados, copia pastas e remove do destino os itens que não existem mais na origem. A verificação acontece a cada 10 segundos.

## Como usar

É necessário ter Python 3.11 ou superior e o [uv](https://docs.astral.sh/uv/) instalado.

1. Instale as dependências na pasta do projeto:

   ```powershell
   uv sync
   ```

2. Crie ou edite o arquivo `.env` na pasta do projeto e defina os caminhos:

   ```dotenv
   ORIGEM='C:\caminho\para\pasta-de-origem'
   DESTINO='C:\caminho\para\pasta-de-destino'
   ```

3. Inicie a sincronização:

   ```powershell
   uv run python rsync.py
   ```

Pressione `Ctrl+C` para encerrar. **Atenção:** o destino é mantido como espelho; itens que não existirem na origem serão excluídos do destino. Confira os caminhos antes de iniciar.