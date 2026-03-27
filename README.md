# Portugas Bacalhau

Site institucional da marca **Portugas Bacalhau** — sabores de Portugal em **Santos (SP)**, com a história da família que veio de **Arouca (Portugal)** através do Atlântico.

Inclui linha do tempo interativa (navio animado de Arouca a Santos), catálogo de produtos com cartões 3D e história de cada iguaria, slogan *«Esta delicia é portuguesa com certeza!»* e **API REST** para integrações (`/api/produtos`, `/api/status`).

**Site comercial (marca):** [portugasbacalhau.com.br](https://www.portugasbacalhau.com.br)

---

## Repositório e demo

| | |
| :--- | :--- |
| **Código no GitHub** | [github.com/arsgoliveira/Portugas-Bacalhau](https://github.com/arsgoliveira/Portugas-Bacalhau) |
| **Site em produção (Vercel)** | **[portugas-bacalhau.vercel.app](https://portugas-bacalhau.vercel.app)** — nome do projeto na Vercel: **portugas-bacalhau** ([dashboard](https://vercel.com/dashboard)) |

> **`DEPLOYMENT_NOT_FOUND`:** não há deployment de produção válido ou o build falhou — em **Deployments** abre o último e lê os **Build Logs**. Na Vercel, importa **`arsgoliveira/Portugas-Bacalhau`**. **Nome do projeto na Vercel:** só **minúsculas**; **não pode** conter a sequência **`--`**. Exemplo válido: `portugas-bacalhau`. Confirma **Settings → Git** (branch `main`) e **Framework Preset → FastAPI** quando aplicável.

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
| **Deploy** | [Vercel](https://vercel.com/) — [FastAPI](https://vercel.com/docs/frameworks/backend/fastapi) (`app.py` + `requirements.txt` + `vercel.json`) |

---

## Pré-requisitos

- Python **3.10+** (recomendado 3.11 ou 3.12)
- `pip`

---

## Como rodar localmente

1. **Clonar o repositório**

   ```bash
   git clone https://github.com/arsgoliveira/Portugas-Bacalhau.git
   cd Portugas-Bacalhau
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
   python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
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

1. [Vercel Dashboard](https://vercel.com/dashboard) → **Add New…** → **Project** → importa **`arsgoliveira/Portugas-Bacalhau`** (confirma o repositório na lista — não uses outro projeto por engano, ex.: `winbakk-solution`).
2. **Root Directory:** raiz do repo (`.`). Em **Build & Deployment → Framework Preset**, escolhe **FastAPI** se não detetar sozinho.
3. Confirma **Deploy**. Depois, cada `git push` na branch ligada (ex.: `main`) gera um novo deployment.

**Importante:** HTML estático antigo (`index.html`, etc.) foi movido para **`legacy_static/`** para não competir com o **FastAPI** na raiz (a Vercel pode priorizar site estático se existir `index.html` no topo do repo).

Se o projeto na Vercel estiver ligado a **outro** repositório, em **Settings → Git** reconecta a **`arsgoliveira/Portugas-Bacalhau`**.

**Nota:** O `vercel.json` **não** usa o modo antigo `builds` (que excluía `templates/`, etc.). Entrada da app: **`app.py`** (preferido pela Vercel em relação a `main.py`). **`redirect_slashes=False`** na app evita conflitos com o proxy da Vercel.

**URLs:** Usa sempre o domínio em **Settings → Domains** (ex.: `portugas-bacalhau.vercel.app`) ou o botão **Visit** no deployment. URLs longos do tipo `*-xxxx-*.vercel.app` são **por deployment** e podem deixar de funcionar quando há um deploy novo.

**CLI (opcional):** `npx vercel deploy --prod --yes --name portugas-bacalhau` (o nome do projeto tem de ser minúsculo e **sem** `--`).

---

## Estrutura do repositório

```
├── app.py               # App FastAPI, rotas HTML e API
├── requirements.txt
├── vercel.json          # installCommand (sem builds legacy)
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
