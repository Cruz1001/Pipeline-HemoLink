import json
from datetime import datetime

def limpar_dados(caminho_json):
        with open(caminho_json, "r", encoding="utf-8") as f:
                dados = json.load(f)
        metadados = dados[-1]
        dados_sangue = dados[:-1]
        dados_limpos = []
        
        timestamp = metadados["horario"]
        estoque = metadados["estoque"]
        
        
        for item in dados_sangue:
                match item["nivel"]:
                        case "critico":
                                item["nivel"] = "3"
                        case "emergencia":
                                item["nivel"] = "2"
                        case "estavel":
                                item["nivel"] = "1"
                        case _:
                                item["nivel"] = "Desconhecido"        
                                
                novo_item = {
                "tipo": item["tipo"],
                "nivel": item["nivel"],
                "nome": estoque,
                "data": timestamp,
                "cidade": metadados["cidade"]
                }
                dados_limpos.append(novo_item)
        
        
        
        
        with open(f"data/processed/{estoque}&{timestamp}.json", "w", encoding="utf-8") as f:
                json.dump(dados_limpos, f, indent=4)
        
        return f"data/processed/{estoque}&{timestamp}.json"
        
        