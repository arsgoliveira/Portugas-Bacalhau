"""Smoke test — garante que a app FastAPI importa (CI + Vercel sanity)."""

def test_app_import():
    from app import app

    assert app.title == "Portugas Bacalhau"
