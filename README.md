# Portugas Bacalhau

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Jinja2](https://img.shields.io/badge/Jinja2-B4171F?style=flat&logo=jinja&logoColor=white)](https://jinja.palletsprojects.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white)](https://vercel.com/)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://pytest.org/)

*Badges de referência rápida; o detalhe do stack está na tabela abaixo.*

Aplicação web institucional da marca **Portugas Bacalhau** — gastronomia portuguesa em **Santos (SP)**, com narrativa da origem familiar em **Arouca (Portugal)** e presença digital alinhada à identidade da marca.

---

## Sobre o projeto

O site combina **páginas HTML** geradas no servidor (templates **Jinja2**) com **API REST** para integrações e futuras extensões. Inclui:

- Páginas institucionais (início, produtos, sobre, contacto)
- Linha do tempo na página **Sobre** (nau na timeline, paragens ao scroll)
- Catálogo de produtos com cartões interativos e conteúdo editorial
- Endpoints JSON: `/api/produtos`, `/api/status`, entre outros
- Slogan de marca: *«Esta delicia é portuguesa com certeza!»*

**Marca (site comercial):** [portugasbacalhau.com.br](https://www.portugasbacalhau.com.br)

---

## Stack tecnológico

| Área | Tecnologia |
|------|------------|
| **Runtime** | Python 3.10+ (recomendado 3.12) |
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Templates** | [Jinja2](https://jinja.palletsprojects.com/) |
| **Validação** | [Pydantic](https://docs.pydantic.dev/) v2 |
| **Servidor de desenvolvimento** | [Uvicorn](https://www.uvicorn.org/) |
| **Frontend** | HTML5, CSS3, JavaScript (vanilla) |
| **UI** | [particles.js](https://vincentgarreau.com/particles.js/), Font Awesome, Google Fonts (Playfair Display, Lato) |
| **Testes / CI** | [pytest](https://pytest.org/), [flake8](https://flake8.pycqa.org/) (GitHub Actions) |
| **Deploy** | [Vercel](https://vercel.com/) — preset FastAPI, `app.py`, `requirements.txt`, `vercel.json` |

---

## Requisitos

- Python **3.10+**
- `pip` (ou ambiente compatível com `requirements.txt`)

---

## Instalação e execução local

Executar os comandos **na raiz do repositório** (onde existem `app.py` e `requirements.txt`).

```bash
git clone https://github.com/arsgoliveira/Portugas-Bacalhau.git
cd Portugas-Bacalhau
```

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

| Recurso | URL local |
|---------|-----------|
| Site | [http://localhost:8000](http://localhost:8000) |
| API produtos | [http://localhost:8000/api/produtos](http://localhost:8000/api/produtos) |
| Estado da API | [http://localhost:8000/api/status](http://localhost:8000/api/status) |

---

## Repositório e ambiente de produção

| | |
| :--- | :--- |
| **Código** | [github.com/arsgoliveira/Portugas-Bacalhau](https://github.com/arsgoliveira/Portugas-Bacalhau) |
| **Produção (Vercel)** | [portugas-bacalhau.vercel.app](https://portugas-bacalhau.vercel.app) |

O deploy em produção é feito pela **integração Git** com a Vercel (push na branch configurada, ex.: `main`). O workflow em `.github/workflows` executa **testes e lint**; não substitui o deploy da Vercel.

**Nome do projeto na Vercel:** apenas minúsculas; não utilizar a sequência `--` no nome (ex.: `portugas-bacalhau`). Se o repositório não aparecer na importação, configurar permissões da [Vercel GitHub App](https://vercel.com/docs/deployments/git/vercel-for-github) para incluir `arsgoliveira/Portugas-Bacalhau`).

---

## Estrutura do repositório

```
├── app.py               # Aplicação FastAPI (rotas e API)
├── requirements.txt
├── vercel.json
├── pyproject.toml
├── .python-version
├── templates/           # Páginas Jinja2
├── static/              # CSS e JavaScript
├── assets/              # Imagens e media
├── tests/               # Testes pytest
├── legacy_static/       # HTML legado (referência)
└── .github/workflows/   # CI
```

---

## Licença

Uso privado — projeto da marca **Portugas Bacalhau**.
