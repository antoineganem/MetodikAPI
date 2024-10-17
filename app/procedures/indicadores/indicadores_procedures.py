from app.utils.db_helpers import execute_stored_procedure


def ver_Indicadores(data):
    sp_name = "spVerIndicadores"
    params = [
        data.get("Tipo"), 
        data.get("EmpresaID"),
    ]
    return execute_stored_procedure(sp_name, params)





