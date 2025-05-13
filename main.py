from sqlalchemy.orm import Session
from db.database import SessionLocal
from extract.scraping import scraping_estoque_sp
from transform.clean_data import limpar_dados
from load.to_database import load_hemocentro_data
from datetime import datetime
import json
import os
from db.database import Base
from db.database import engine

def main():
        Base.metadata.create_all(bind=engine)
        print("Iniciando o processo de scraping...")
        dados_brutos = scraping_estoque_sp()
        
        print("Scraping concluído. Iniciando a transformação dos dados...")
        dados_transformados = limpar_dados(dados_brutos)
        print("Transformação concluída. Iniciando o salvamento dos dados...")
        db = SessionLocal()
        load_hemocentro_data(dados_transformados, db)
        db.close()

main()