from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
import jinja2

# Caminho base absoluto — necessário para Vercel e outros ambientes de deploy
BASE_DIR = Path(__file__).resolve().parent

# redirect_slashes=False: evita redirecionamentos inconsistentes no proxy da Vercel
app = FastAPI(
    title="Portugas Bacalhau",
    version="1.0.0",
    redirect_slashes=False,
)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.mount("/assets", StaticFiles(directory=str(BASE_DIR / "assets")), name="assets")

# Ambiente Jinja2 manual — cache desativado (compatibilidade Python 3.14)
_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(BASE_DIR / "templates")),
    autoescape=jinja2.select_autoescape(["html"]),
    auto_reload=True,
    cache_size=0,
)
_jinja_env.cache = None
templates = Jinja2Templates(env=_jinja_env)

# ─── Dados dos produtos ───────────────────────────────────────────────────────

PRODUTOS = [
    {
        "id": 1,
        "nome": "Bacalhau à Brás",
        "categoria": "prato_principal",
        "preco": "12.50",
        "preco_brl": "68,00",
        "descricao": "O prato mais emblemático de Portugal — bacalhau desfiado envolvido em ovos mexidos, batata palha crocante e azeitonas negras.",
        "historia": (
            "O bacalhau chegou a Portugal no século XV, trazido pelos corajosos pescadores "
            "que navegavam até à Terra Nova em busca do 'fiel amigo'. Tornou-se símbolo da "
            "resistência, da viagem e da alma portuguesa. Dizem os sábios que existem 365 receitas "
            "— uma para cada dia do ano. O Bacalhau à Brás foi criado em Lisboa no século XIX por "
            "um taberneiro do Bairro Alto chamado Brás, que misturou os restos que tinha na cozinha "
            "e criou uma das maiores obras da gastronomia mundial."
        ),
        "ingredientes": ["Bacalhau", "Ovos", "Batata palha", "Cebola", "Azeitonas", "Salsa", "Azeite"],
        "origem": "Lisboa, Portugal",
        "seculo": "XIX",
        "emoji": "🐟",
        "cor": "#006600",
    },
    {
        "id": 2,
        "nome": "Baguete Recheada",
        "categoria": "lanche",
        "preco": "4.50",
        "descricao": "Baguete crocante recheada com fiambre, queijo da Serra, alface fresca e tomate — o lanche favorito de Portugal há gerações.",
        "historia": (
            "A baguete chegou a Portugal no início do século XX, trazida pela influência francesa "
            "através da fronteira e dos marinheiros. Rapidamente foi adotada e reinventada pela "
            "cozinha portuguesa. Recheada com produtos locais como queijo da Serra, presunto alentejano "
            "e atum do Algarve, tornou-se o lanche favorito de gerações de portugueses. Está presente "
            "em cada café, pastelaria e mercado do país, do Minho ao Algarve, das Berlengas aos Açores."
        ),
        "ingredientes": ["Baguete", "Fiambre", "Queijo da Serra", "Alface", "Tomate", "Manteiga"],
        "origem": "França → Portugal",
        "seculo": "XX",
        "emoji": "🥖",
        "cor": "#8B4513",
        "preco_brl": "22,00",
    },
    {
        "id": 3,
        "nome": "Pastel de Belém",
        "categoria": "pastelaria",
        "preco": "1.50",
        "descricao": "O mais famoso doce português — massa folhada crocante e estaladiça com creme de ovos perfumado com canela e açúcar em pó.",
        "historia": (
            "Nasceu em 1837 nos claustros do Mosteiro dos Jerónimos, em Belém, Lisboa. "
            "Os frades do mosteiro usavam as claras dos ovos para engomar as suas vestes religiosas "
            "e com as gemas sobrantes criaram esta maravilha da pastelaria mundial. Quando as ordens "
            "religiosas foram extintas pelo Liberalismo em 1834, a receita foi vendida a uma confeitaria "
            "próxima — a Casa Pastéis de Belém — que existe até hoje, no mesmo lugar, com a mesma "
            "receita secreta. A receita original é segredo guardado a sete chaves, conhecida apenas "
            "por três mestres pasteleiros no mundo inteiro."
        ),
        "ingredientes": ["Massa folhada", "Gemas de ovo", "Açúcar", "Leite", "Canela", "Açúcar em pó"],
        "origem": "Belém, Lisboa",
        "seculo": "XIX",
        "emoji": "🥐",
        "cor": "#FFD700",
        "preco_brl": "9,00",
    },
    {
        "id": 4,
        "nome": "Bola de Berlim",
        "categoria": "pastelaria",
        "preco": "2.00",
        "descricao": "O sonho dourado das praias portuguesas — massa frita macia e fofa com recheio generoso de creme amarelo e açúcar por cima.",
        "historia": (
            "Inspirada no Berliner alemão, a Bola de Berlim chegou a Portugal no século XX "
            "e conquistou definitivamente as praias portuguesas. Conta a lenda que os primeiros "
            "vendedores percorriam as praias com cestos de vime cheios destas delícias, gritando "
            "'Berlim! Berlim!' ao longo da areia. O recheio generoso de creme de pasteleiro amarelo "
            "e a cobertura de açúcar granulado tornaram-na inseparável do verão português. "
            "Hoje é símbolo de férias, praia, alegria e da infância dourada de todos os portugueses. "
            "Também conhecida como 'Sonho' em algumas regiões do país."
        ),
        "ingredientes": ["Farinha", "Ovos", "Açúcar", "Leite", "Fermento", "Creme de pasteleiro", "Óleo"],
        "origem": "Alemanha → Portugal",
        "seculo": "XX",
        "emoji": "🍩",
        "cor": "#FF8C00",
        "preco_brl": "12,00",
    },
]

# ─── Modelos Pydantic ─────────────────────────────────────────────────────────

class ContactForm(BaseModel):
    nome: str
    email: str
    mensagem: str
    telefone: Optional[str] = None

# ─── Rotas HTML ───────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request, "index.html",
        {"page": "home", "titulo": "Início", "produtos_destaque": PRODUTOS},
    )


@app.get("/produtos", response_class=HTMLResponse)
async def produtos(request: Request, categoria: Optional[str] = None):
    produtos_filtrados = PRODUTOS
    if categoria and categoria != "todos":
        produtos_filtrados = [p for p in PRODUTOS if p["categoria"] == categoria]
    return templates.TemplateResponse(
        request, "produtos.html",
        {"page": "produtos", "titulo": "Os Nossos Produtos",
         "produtos": produtos_filtrados, "categoria_atual": categoria or "todos"},
    )


@app.get("/sobre", response_class=HTMLResponse)
async def sobre(request: Request):
    return templates.TemplateResponse(
        request, "sobre.html",
        {"page": "sobre", "titulo": "A Nossa História"},
    )


@app.get("/contacto", response_class=HTMLResponse)
async def contacto(request: Request):
    return templates.TemplateResponse(
        request, "contacto.html",
        {"page": "contacto", "titulo": "Contacto"},
    )

# ─── API REST ─────────────────────────────────────────────────────────────────

@app.get("/api/produtos")
async def api_produtos(categoria: Optional[str] = None):
    if categoria and categoria != "todos":
        return [p for p in PRODUTOS if p["categoria"] == categoria]
    return PRODUTOS


@app.get("/api/produtos/{produto_id}")
async def api_produto(produto_id: int):
    produto = next((p for p in PRODUTOS if p["id"] == produto_id), None)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.post("/api/contacto")
async def api_contacto(form: ContactForm):
    return {
        "sucesso": True,
        "mensagem": f"Obrigado {form.nome}! Entraremos em contacto brevemente.",
    }


@app.get("/api/status")
async def api_status():
    return {
        "status": "online",
        "app": "Portugas Bacalhau",
        "versao": "1.0.0",
        "total_produtos": len(PRODUTOS),
    }
