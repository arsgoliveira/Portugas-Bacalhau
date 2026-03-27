"""Smoke test — garante que a app FastAPI importa (CI + Vercel sanity)."""

def test_app_import():
    from main import app

    assert app.title == "Portugas Bacalhau"
