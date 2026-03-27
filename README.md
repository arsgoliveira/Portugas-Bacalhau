# Portugas Bacalhau

Site institucional da marca **Portugas Bacalhau** — sabores de Portugal em **Santos (SP)**, com a história da família que veio de **Arouca (Portugal)** através do Atlântico.

Inclui linha do tempo interativa (navio animado de Arouca a Santos), catálogo de produtos com cartões 3D e história de cada iguaria, slogan *«Esta delicia é portuguesa com certeza!»* e **API REST** para integrações (`/api/produtos`, `/api/status`).

---

## Repositório e demo

| | |
| :--- | :--- |
| **Código no GitHub** | [github.com/arsgoliveira/Portugas--Bacalhau](https://github.com/arsgoliveira/Portugas--Bacalhau/) |
| **Site em produção (Vercel)** | **[portugas-bacalhau.vercel.app](https://portugas-bacalhau.vercel.app)** — nome do projeto na Vercel: **portugas-bacalhau** ([dashboard](https://vercel.com/dashboard)) |

> **`DEPLOYMENT_NOT_FOUND`** significa que **não há deployment de produção válido** (nunca concluiu com sucesso ou o domínio não está ligado ao último deploy). No dashboard: **Deployments** → abre o último → se estiver **Error**, lê os **Build Logs**. Confirma **Settings → Git** (repo `Portugas--Bacalhau`, branch `main`) e **Settings → General → Framework Preset** em **FastAPI** (ou redeploy após `git push`). O URL **`https://portugas-bacalhau.vercel.app`** só responde depois de existir pelo menos um deploy **Ready** em **Production**.

---

## Tecnologias

| Camada | Stack |
|--------|--------|
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) (Python 3) |
| **Templates** | [Jinja2](https://jinja.palletsprojects.com/) |
| **Servidor local** | [Uvicorn](https://www.uvicorn.org/) |
| **Validação** | [Pydantic](https://docs.pydantic.dev/) |
| **Frontend** | HTML5, CSS3, JavaScript (vanilla) |
| **UI / animação** | [particles.js](https://vincentgarreau.com/particles.js/), Font Awesome, Google Fonts (Playfair Display, Lato) |
| **Deploy** | [Vercel](https://vercel.com/) — deteção nativa de [FastAPI](https://vercel.com/docs/frameworks/backend/fastapi) (`main.py` + `requirements.txt`) |

---

## Pré-requisitos

- Python **3.10+** (recomendado 3.11 ou 3.12)
- `pip`

---

## Como rodar localmente

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/arsgoliveira/Portugas--Bacalhau.git
   cd Portugas--Bacalhau
   ```

2. **Ambiente virtual (recomendado)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   Linux/macOS: `source .venv/bin/activate`

3. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Subir o servidor**

   ```bash
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Abrir no navegador**

   | Recurso | URL |
   |---------|-----|
   | Site | [http://localhost:8000](http://localhost:8000) |
   | API produtos | [http://localhost:8000/api/produtos](http://localhost:8000/api/produtos) |
   | Status da API | [http://localhost:8000/api/status](http://localhost:8000/api/status) |

---

## Deploy na Vercel

O workflow do GitHub (`.github/workflows`) **só corre testes e lint** — **não** faz deploy. O deploy é feito pela **integração Vercel ↔ GitHub**:

1. [Vercel Dashboard](https://vercel.com/dashboard) → **Add New…** → **Project** → importa **`arsgoliveira/Portugas--Bacalhau`**.
2. **Root Directory:** raiz do repo (`.`). Em **Build & Deployment → Framework Preset**, escolhe **FastAPI** se não detetar sozinho.
3. Confirma **Deploy**. Depois, cada `git push` na branch ligada (ex.: `main`) gera um novo deployment.

**Importante:** HTML estático antigo (`index.html`, etc.) foi movido para **`legacy_static/`** para não competir com o **FastAPI** na raiz (a Vercel pode priorizar site estático se existir `index.html` no topo do repo).

Se o projeto **portugas-bacalhau** estiver ligado a **outro** repositório ou pasta errada, em **Settings → Git** reconecta a **`arsgoliveira/Portugas--Bacalhau`**.

**Nota:** Foi removido o `vercel.json` antigo com `builds` + `@vercel/python` só em `main.py`. Nesse modo a Vercel **não incluía** `templates/`, `static/` e `assets/` no pacote — o deploy falhava ou o site quebrava. Com a configuração atual, a função Python inclui o projeto completo, como na [documentação](https://vercel.com/docs/functions/runtimes/python).

**CLI (opcional):** na pasta do projeto, `npx vercel login` e depois `npx vercel --prod`.

---

## Estrutura do repositório

```
├── main.py              # App FastAPI, rotas HTML e API
├── requirements.txt
├── pyproject.toml       # Metadados do projeto (Vercel / Python)
├── .python-version      # Versão sugerida (ex.: 3.12)
├── templates/           # Páginas Jinja2 (base, index, produtos, sobre, contacto)
├── static/              # CSS e JS
├── assets/              # Imagens, vídeo, etc.
└── legacy_static/       # HTML estático antigo (não usado em produção)
```

---

## Licença

Uso privado / projeto da marca Portugas Bacalhau.
