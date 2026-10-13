# Professional Research MCP

[English](README.md) | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)


Conector MCP local para pesquisar profissionais, empresas e possíveis stakeholders a partir de **informações públicas indexadas na web**, por meio de um cliente MCP compatível.

**Gratuito para instalar:** não exige chave de API, cartão de crédito ou login no LinkedIn. A pesquisa depende de provedores públicos, que podem limitar ou bloquear consultas.

> **Importante:** não é a API oficial do LinkedIn. Não acessa mensagens, conexões, perfis privados ou dados da conta do usuário.

## Requisitos

- Windows com PowerShell **ou** macOS com Terminal
- Python **3.11 ou superior**
- Git instalado
- cliente MCP com suporte a conexões MCP locais
- Conexão com a internet para pesquisar páginas públicas

Verifique as ferramentas:

**Windows (PowerShell):**
```powershell
py --version
git --version
```

**macOS (Terminal):**
```bash
python3 --version
git --version
```

Se algum comando não funcionar, instale Python 3.11+ e Git antes de continuar. No Windows, se `py` não estiver disponível, use `python` nos comandos equivalentes.

## Instalação no Windows (PowerShell)

1. Abra o PowerShell.
2. Copie e execute, **uma linha por vez**:

```powershell
git clone https://github.com/caiqueescaler86/jouleandlinkedin.git
cd jouleandlinkedin
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

3. Mantenha essa janela aberta. O resultado esperado é semelhante a:

```text
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
```

**Para executar novamente em outro dia**, abra o PowerShell dentro da pasta do projeto e rode:

```powershell
.\.venv\Scripts\python.exe server.py
```

## Instalação no macOS (Terminal)

```bash
git clone https://github.com/caiqueescaler86/jouleandlinkedin.git
cd jouleandlinkedin
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

Mantenha o Terminal aberto enquanto utilizar o conector.

**Para executar novamente:**

```bash
./.venv/bin/python server.py
```

## Configuração no cliente MCP

Com o servidor Python em execução:

1. Abra o cliente MCP.
2. Vá à área de **conectores/extensões MCP** (o nome da opção pode variar conforme a versão).
3. Escolha a opção para **adicionar um servidor MCP**.
4. Preencha os campos:

| Campo | Valor |
| --- | --- |
| Nome | Professional Research |
| URL | `http://127.0.0.1:8000/sse` |
| Protocolo | SSE |
| Autenticação | Nenhuma |
| ID do cliente | Automático (se aparecer) |
| Chave secreta do cliente | Automático (se aparecer) |

5. Salve e habilite o conector.
6. Confirme que as ferramentas do conector aparecem no cliente MCP.

**Use `127.0.0.1`, não `localhost`:**

```text
http://127.0.0.1:8000/sse
```

O cliente MCP precisa executar **na mesma máquina** do servidor ou ter acesso explícito ao serviço local. A conexão local não funcionará automaticamente a partir de uma instância somente na nuvem.

## Primeiro teste

No chat do cliente MCP, experimente:

```text
Use a ferramenta research_professional para pesquisar o perfil
público de "Pessoa Exemplo". Mostre os links das fontes e não invente dados.
```

Outro exemplo:

```text
Use map_stakeholders para pesquisar possíveis stakeholders
de Marketing e CRM da empresa X no Brasil. Retorne nomes, cargos,
fontes e sinalize informações não verificadas.
```

## Ferramentas disponíveis

| Ferramenta | Para que serve |
| --- | --- |
| `search_professionals(company, role, country, limit)` | Buscar profissionais por empresa, função e país |
| `research_professional(name, company)` | Pesquisar referências públicas sobre uma pessoa |
| `research_company(company, country)` | Pesquisar informações públicas de uma empresa |
| `map_stakeholders(company, country, function)` | Identificar possíveis stakeholders e decisores |

Os resultados são **indícios de pesquisa**, não confirmação de identidade, vínculo empregatício ou poder de decisão.

## Diagnóstico e problemas comuns

### O cliente MCP não consegue conectar

- Confirme que o servidor Python está rodando.
- Confirme a URL exata: `http://127.0.0.1:8000/sse`.
- Se a conexão foi criada anteriormente com `localhost`, edite ou recrie usando `127.0.0.1`.
- Se o cliente MCP apresentar falha ao reconectar, remova e adicione novamente o conector.

**Teste SSE no Windows** (em um segundo PowerShell, sem parar o servidor):

```powershell
curl.exe -N --max-time 5 http://127.0.0.1:8000/sse
```

A resposta esperada começa com:

```text
event: endpoint
data: /messages/?session_id=...
```

O timeout após cinco segundos é esperado porque SSE mantém a conexão aberta. Esse teste confirma o endpoint SSE, **não** a execução completa de uma ferramenta MCP.

### Muitas linhas `GET /sse 200 OK`

O cliente pode estar abrindo novas conexões repetidamente. Verifique se o cliente MCP está tentando reconectar. `200 OK` isoladamente não garante que o handshake MCP tenha sido concluído.

### `MCP error -32602: Invalid request parameters`

Pode haver incompatibilidade ou parâmetros inválidos na comunicação MCP. Tente reconectar o conector; se persistir, capture a mensagem de erro e os logs para diagnóstico.

### `Error: name 'clean' is not defined`

Atualize o projeto para a versão mais recente (o problema foi corrigido):

```powershell
git pull
```

Reinicie o servidor depois da atualização.

### A pesquisa não encontra resultados

O mecanismo público de pesquisa pode limitar consultas, estar indisponível ou não encontrar perfis indexados. Isso não significa necessariamente que o MCP esteja desconectado.

## Atualização

Pare o servidor com `Ctrl+C`. Na pasta do projeto:

**Windows:**
```powershell
git pull
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

**macOS:**
```bash
git pull
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

## Segurança e limitações

- O servidor escuta somente em `127.0.0.1` por padrão.
- **Não exponha esse servidor sem autenticação na internet ou em redes compartilhadas.**
- O projeto faz consultas públicas por meio da biblioteca `ddgs`, sem autenticação no LinkedIn.
- Fontes e trechos podem estar incompletos ou desatualizados; valide antes de tomar decisões comerciais.
- Respeite termos de serviço, políticas corporativas e legislação de proteção de dados.
