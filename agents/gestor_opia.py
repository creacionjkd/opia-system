import json
from datetime import datetime

# Ruta simplificada (se puede adaptar con os.path)
BITACORA_PATH = "data/bitacora_opia.json"

def cargar_bitacora():
    with open(BITACORA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_bitacora(data):
    with open(BITACORA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def registrar_foco_dia(foco, intencion, proyectos, energia, emocional, mental):
    data = cargar_bitacora()
    entrada = {
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "foco_dia": foco,
        "intención_usuario": intencion,
        "proyectos_asociados": proyectos,
        "estado_inicial": {
            "energía": energia,
            "emocional": emocional,
            "mental": mental
        },
        "acciones_clave": [],
        "resultados_obtenidos": [],
        "notas_finales": "",
        "evaluación_auto": {
            "logros": "",
            "retos": "",
            "aprendizajes": ""
        }
    }
    data["bitacora"].append(entrada)
    data["última_actualización"] = entrada["fecha"]
    guardar_bitacora(data)
    print(f"✅ Foco del día registrado: {foco}")

# Ejemplo de uso
if __name__ == "__main__":
    registrar_foco_dia(
        foco="Finalizar módulo de agente Foco",
        intencion="Avanzar el sistema OPIA un 10%",
        proyectos=["opia-system", "curso IA avanzada"],
        energia="Alta",
        emocional="Motivado",
        mental="Enfocado"
    )
