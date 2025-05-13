import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scraping_estoque_sp():
        url = "https://www.prosangue.sp.gov.br/home/"
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html.parser")

        estoque = soup.find("ul", class_="estoque")
        linhas = estoque.find_all("li")

        sangue_data = []

        #Legenda níveis: critico: baixo, emergencia: medio, estavel: alto
        for linha in linhas:
                tag_span = linha.find("span")
                nivel = tag_span.get("class", [])[0] if tag_span else "desconhecido"
                tipo = linha.text.strip()
                print(f"Tipo: {tipo} Nivel: {nivel} ")
                
                sangue_data_dict = {
                        "tipo": tipo,
                        "nivel": nivel
                }

                sangue_data.append(sangue_data_dict)
        
        timestamp = datetime.now().strftime("%Y-%m-%d")
        info = {
                "horario": timestamp,
                "cidade": "São Paulo - SP",
                "estoque": "Fundação_Pró_Sangue",
        }
        sangue_data.append(info)
        with open(f"data/raw/nivel_estoque_sp&{timestamp}.json", "w", encoding="utf-8") as f:
                json.dump(sangue_data, f, indent=4)
        
        return f"data/raw/nivel_estoque_sp&{timestamp}.json"

def main():
        scraping_estoque_sp()

main()
        
