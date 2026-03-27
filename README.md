# Portugas Bacalhau

Site institucional da marca **Portugas Bacalhau** — sabores autênticos de Portugal servidos em **Santos, SP**, com a história da família que veio de **Arouca, Portugal**, atravessando o Atlântico.

O projeto inclui linha do tempo interativa (navio animado de Arouca a Santos), catálogo de produtos com cartões 3D e história de cada iguaria, slogan original *“Esta delicia é portuguesa com certeza!”* e API REST para integrações.

---

## Tecnologias

| Camada | Tecnologia |
|--------|------------|
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) (Python 3) |
| **Templates** | [Jinja2](https://jinja.palletsprojects.com/) |
| **Servidor local** | [Uvicorn](https://www.uvicorn.org/) |
| **Validação** | [Pydantic](https://docs.pydantic.dev/) |
| **Frontend** | HTML5, CSS3, JavaScript (vanilla) |
| **UI / animação** | [particles.js](https://vincentgarreau.com/particles.js/), Font Awesome, Google Fonts (Playfair Display, Lato) |
| **Deploy** | [Vercel](https://vercel.com/) (`vercel.json` + runtime Python) |

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

2. **Criar ambiente virtual (opcional, recomendado)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   No Linux/macOS: `source .venv/bin/activate`

3. **Instalar dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Iniciar o servidor**

   ```bash
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Abrir no navegador**

   - Site: [http://localhost:8000](http://localhost:8000)
   - API produtos: [http://localhost:8000/api/produtos](http://localhost:8000/api/produtos)
   - Status da API: [http://localhost:8000/api/status](http://localhost:8000/api/status)

---

## Estrutura principal

```
├── main.py              # App FastAPI, rotas HTML e API
├── requirements.txt
├── vercel.json          # Configuração de deploy na Vercel
├── templates/           # Páginas Jinja2 (base, index, produtos, sobre, contacto)
├── static/              # CSS e JS do site
└── assets/              # Imagens, vídeo (logo, azulejos, cod.mp4, etc.)
```

---

## Demo (produção)

**URL:** [https://project-rcp7k.vercel.app](https://project-rcp7k.vercel.app)

> Se o projeto na Vercel tiver outro nome de domínio, substitua o link acima no `README` ou nas definições do projeto em **Vercel → Settings → Domains**.

Para ligar o repositório GitHub ao projeto na Vercel: **Project → Settings → Git → Connect Git Repository** e escolha `arsgoliveira/Portugas--Bacalhau`.

---

## Licença

Uso privado / projeto da marca Portugas Bacalhau.
