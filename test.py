from db.models import Hemocentro
from db.database import SessionLocal

def listar_hemocentros():
    db = SessionLocal()
    try:
        hemocentros = db.query(Hemocentro).all()
        for h in hemocentros:
            print(f"ID: {h.id} | Nome: {h.nome} | Data: {h.data} | Cidade: {h.cidade} | Tipo: {h.tipo} | Nível: {h.nivel}")
    finally:
        db.close()


listar_hemocentros()
