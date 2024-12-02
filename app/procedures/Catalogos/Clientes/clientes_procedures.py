from app.utils.db_helpers import execute_stored_procedure


def ver_Clientes(data):
    sp_name = "spverClientes"
    params = [
        data.get("EmpresaID"),
        data.get("EstatusID"),
    ]
    return execute_stored_procedure(sp_name, params)


def ver_ClienteID(ID):
    sp_name = "spVerClienteID"
    params = [ ID ]
    return execute_stored_procedure(sp_name, params)

def act_Cliente(data):
    sp_name = "spActCliente"
    params = [
        data.get("ID"), data.get("EstatusID"), data.get("Cliente"), data.get("Nombre"),
        data.get("NombreCorto"), data.get("Observaciones"), data.get("CodigoPostal"), data.get("Direccion"),
        data.get("DireccionNumero"), data.get("DireccionNumeroInt"), data.get("Delegacion"), data.get("Colonia"),
        data.get("Poblacion"), data.get("Estado"), data.get("Pais"), data.get("RFC"),
        data.get("CURP"), data.get("Telefonos"), data.get("Sexo"), data.get("Email"),
        data.get("FechaNacimiento"), data.get("usoCFDI"), data.get("FormaPago"), data.get("MetodoPago"),
        data.get("RegimenFiscal"), data.get("CreditoLimite"), data.get("CreditoCondiciones"), data.get("BloquearMorosos"),
        data.get("Descuento"), data.get("SucursalEmpresa"),
        #nuevos
        data.get("PedirTono"), data.get("PedidosParciales"), data.get("VtasConsignacion"), data.get("Conciliar"),
        data.get("CreditoEspecial"), data.get("CreditoConLimite"), data.get("CreditoConDias"), data.get("CreditoConCondiciones"),
        data.get("EmpresaID")
    ]
    return execute_stored_procedure(sp_name, params)