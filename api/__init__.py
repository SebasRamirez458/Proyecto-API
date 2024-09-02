from sodapy import Socrata
import pandas as pd

def consultar_api(limite_registros,departamento):
    client = Socrata("www.datos.gov.co", None)
    result = client.get("gt2j-8ykr", limit = limite_registros, departamento_nom = departamento)
    return result

def covertir_a_dataframe(result):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    result_dt = pd.DataFrame.from_records(result)
    df_filtrado = result_dt[["ciudad_municipio_nom","departamento_nom","edad","fuente_tipo_contagio","estado","fecha_diagnostico"]]
    return df_filtrado

