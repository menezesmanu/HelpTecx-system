# Help Tecx – Sistema de Chamados

O Help Tecx é um sistema simples desenvolvido em Python para criação e gerenciamento de chamados técnicos.  
Os dados são armazenados em um arquivo `.txt`, garantindo que todos os chamados sejam registrados e recuperados automaticamente.

## Funcionalidades
- Criar chamado  
- Listar chamados  
- Cancelar chamado  
- Validações de entrada (somente texto, somente números e produtos permitidos)  
- Geração automática do número do chamado  

## Estrutura
- **main.py** – Controla o menu e o fluxo principal do sistema  
- **funcoes.py** – Contém toda a lógica de criação, listagem, validações, cancelamento e salvamento  
- **chamados.txt** – Arquivo onde os chamados são gravados