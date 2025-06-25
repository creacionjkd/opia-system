# agente_evaluador.py

"""
Agente Evaluador OPIA
Analiza la calidad del trabajo realizado, detecta errores comunes, propone mejoras
y sugiere prioridades para próximas sesiones. Se conecta con la bitácora.
"""

import json
from datetime import datetime

class AgenteEvaluador:
    def __init__(self, path_bitacora="data/bitacora_opia.json"):
        self.path_bitacora = path_bitacora
        self.bitacora = self.cargar_bitacora()

    def cargar_bitacora(self):
        try:
            with open(self.path_bitacora, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def evaluar_ultima_sesion(self):
        if not self.bitacora:
            return "No hay sesiones registradas para evaluar."

        ultima = self.bitacora[-1]
        reporte = {
            "fecha": ultima.get("fecha", "desconocida"),
            "foco_dia": ultima.get("foco_dia", "no especificado"),
            "evaluacion": [],
        }

        if "acciones_clave" in ultima:
            if any("error" in accion.lower() for accion in ultima["acciones_clave"]):
                reporte["evaluacion"].append("Detectados posibles errores en las acciones clave.")

            if "commit" in ultima.get("acciones_clave", []):
                reporte["evaluacion"].append("Commit realizado correctamente, verificar consistencia con hoja de ruta.")

        if not reporte["evaluacion"]:
            reporte["evaluacion"].append("Sesión sin incidencias críticas. Continuar según hoja de ruta.")

        return reporte

    def guardar_evaluacion(self, resultado, path_salida="data/evaluacion_sesion.json"):
        with open(path_salida, "w", encoding="utf-8") as f:
            json.dump(resultado, f, indent=2, ensure_ascii=False)
        return f"Evaluación guardada en {path_salida}"


# Ejemplo de uso
if __name__ == "__main__":
    evaluador = AgenteEvaluador()
    resultado = evaluador.evaluar_ultima_sesion()
    print(resultado)
    evaluador.guardar_evaluacion(resultado)
