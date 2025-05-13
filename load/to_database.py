from db.models import Hemocentro
from db.database import SessionLocal
import json

def load_hemocentro_data(dados_transformados, db):
        with open(dados_transformados, "r", encoding="utf-8") as f:
                dados = json.load(f)
        
        for dado in dados:
                hemocentro = Hemocentro(
                        nome= dado["nome"],
                        data= dado["data"],
                        cidade= dado["cidade"],
                        tipo= dado["tipo"],
                        nivel= dado["nivel"]
                )
                db.add(hemocentro)
                db.commit()