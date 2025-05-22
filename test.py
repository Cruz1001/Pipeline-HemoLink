from db.models import Hemocentro, Hospital
from db.database import SessionLocal


def listar_hemocentros():
    db = SessionLocal()
    try:
        hemocentros = db.query(Hemocentro).all()
        for h in hemocentros:
            print(f"ID: {h.id} | Nome: {h.nome} | Data: {h.data} | Cidade: {h.cidade} | Tipo: {h.tipo} | Nível: {h.nivel}")
    finally:
        db.close()

def adicionar_hospitais():
    db = SessionLocal()
    with open("hospitais.txt", "r", encoding="utf-8") as f:
        conteudo = f.readlines()
    for linha in conteudo:
        nome = linha.strip()
        db.add(Hospital(nome=nome, hemocentro="Fundanção Pró Sangue"))
        db.commit()

def listar_hospitais():
    db = SessionLocal()
    try:
        hospitais = db.query(Hospital).all()
        for h in hospitais:
            print(f"ID: {h.id} | Nome: {h.nome} | Hemocentro: {h.hemocentro}")
    finally:
        db.close()

listar_hospitais()

