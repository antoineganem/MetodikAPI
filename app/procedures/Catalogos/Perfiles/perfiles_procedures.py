from app.utils.db_helpers import execute_stored_procedure

def ver_Perfiles(EstatusID, EmpresaID, Buscar):
    sp_name = "spVerPerfiles"
    params = [ EstatusID, EmpresaID, Buscar ]
    return execute_stored_procedure(sp_name, params)
            
def ver_PerfilID(ID):
    sp_name = "spVerPerfilID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def act_Perfil(data):
    sp_name = "spActPerfiles"
    params = [
        data.get("ID"), 
        data.get("nombre"), 
        data.get("notas"), 
        data.get("estatus"), 
        data.get("EmpresaID"),
    ]
    return execute_stored_procedure(sp_name, params)

def ver_ModulosAcceso(PerfilID, PersonaID):
    sp_name = "spVerModulosAcceso"
    params = [ PerfilID, PersonaID ]
    return execute_stored_procedure(sp_name, params)

def act_accesosPerfil(data):
    sp_name = "spActAccesosPerfil"
    params = [
        data.get("ChecksCatalogos"), 
        data.get("ChecksConfiguracion"), 
        data.get("CheckMenu"), 
        data.get("CheckSubModulo"), 
        data.get("PerfilID"),
    ]
    return execute_stored_procedure(sp_name, params)

def crear_menus(PersonaID):
    # Llamada al procedimiento almacenado
    sp_name = "spCrearMenus"
    params = [PersonaID]
    menu_data, status_code = execute_stored_procedure(sp_name, params)

    # Verificación de que menu_data es una lista y contiene elementos válidos
    if not isinstance(menu_data, list):
        return [{"label": "Dashboard", "labelDisable": False, "children": []},
                {"label": "Modulos", "children": []}]

    # Estructura de salida
    dashboard_menu = {"label": "Dashboard", "labelDisable": True, "children": []}
    modulos_menu = {"label": "Modulos", "children": []}

    # Mapa de menús principales para agregar submenús
    menu_map = {}

    # Paso 1: Crear todos los menús principales y clasificarlos en Dashboard y Modulos
    for item in menu_data:
        if item["Tipo"] == "Menu":
            # Verificación para no agregar children a "Inicio"
            menu_entry = {
                "name": item["Nombre"],
                "labelDisable": False,
                "active": True,
                "children": None if item["Nombre"] in ["Inicio", "Soporte"] else [],
                "to": item["NombreArchivo"] if item["NombreArchivo"] else f"/{item['Menu'].lower()}/{item['Nombre'].lower().replace(' ', '_')}",
                "icon": item["Icono"] 
            }
            menu_map[item["Nombre"]] = menu_entry
            # Clasificación en Dashboard o Modulos según el TipoMenu
            if item["TipoMenu"] == "Dashboard":
                dashboard_menu["children"].append(menu_entry)
            elif item["TipoMenu"] == "Modulo":
                modulos_menu["children"].append(menu_entry)

    # Paso 2: Agregar submenús y módulos a los menús principales en cada sección
    for item in menu_data:
        if item["Tipo"] in ["Modulo", "Catalogo"]:
            parent_menu = menu_map.get(item["Menu"])
            if parent_menu and parent_menu["children"] is not None:
                submenu_entry = {
                    "name": item["Nombre"],
                    "to": item["NombreArchivo"] if item["NombreArchivo"] else f"/{item['Menu'].lower()}/{item['Nombre'].lower().replace(' ', '_')}",
                    "active": True,
                    "icon": item["Icono"] 
                }
                # Agrega el submenú al menú principal correspondiente
                parent_menu["children"].append(submenu_entry)

    # Resultado final con "Dashboard" y "Modulos" como objetos principales
    final_menu = [dashboard_menu, modulos_menu]

    return final_menu
