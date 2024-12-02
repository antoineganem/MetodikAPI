from app.procedures.Catalogos.Clientes.clientes_procedures import ver_ClienteID, ver_Clientes, act_Cliente


def verClientes(data):
    return ver_Clientes(data)


def verClienteID(ID):
    return ver_ClienteID(ID)


def actCliente(data):
    return act_Cliente(data)