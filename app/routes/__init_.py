from flask import Flask
from app.routes.login.login import * 
from app.routes.Indicadores.indicadores import *
from app.routes.Configuracion.Modulos import *
from app.routes.Catalogos.Usuarios import *
from app.routes.Catalogos.Empresas import *
from app.routes.Catalogos.Sucursales import *
from app.routes.Catalogos.Vehiculos import *
from app.routes.Catalogos.Perfiles import *
from app.routes.Catalogos.Almacenes import *
from app.routes.Catalogos.Destinos import *
from app.routes.Filtros.Filtros import *
from app.routes.Catalogos.Equipos import *
from app.routes.Comercial.Reservas.Reservas import *
from app.routes.Comercial.Reservas.ReservasD import *
from app.routes.Comercial.Paqueteria.Paqueteria import *
from app.routes.Exploradores.RutasExplorador import *
from app.routes.Exploradores.PaqueteriaRExplorador import *
from app.routes.Exploradores.PaqueteriaEntrega import *
from app.routes.Catalogos.Rutas import *
from app.routes.Catalogos.Choferes import *
from app.routes.Catalogos.Agentes import *
from app.routes.Whatsapp.whatsapp import *
from app.routes.Logistica.Rutas.Rutas import *
from app.routes.Logistica.PreciosRuta.PreciosRuta import *
from app.routes.Catalogos.Pasajeros import *
from app.routes.Catalogos.Clientes import *


def register_routes(app: Flask):
    # Login
    app.register_blueprint(login_bp)

    # Indicadores
    app.register_blueprint(verIndicadores_bp)
    
    # Configuracion modulos
    app.register_blueprint(verModulos_bp)
    app.register_blueprint(verModuloID_bp)
    app.register_blueprint(actModulo_bp)

    # Catalogo Usuarios

    app.register_blueprint(usuarios_bp)
    
    ##Catalogo Perfiles

    app.register_blueprint(verPerfiles_bp)  
    app.register_blueprint(verPerfilID_bp)  
    app.register_blueprint(actPerfil_bp)  
    app.register_blueprint(verModulosAcceso_bp)  
    app.register_blueprint(actAccesosPerfil_bp)  
    app.register_blueprint(crearMenus_bp)  

    ##Catalogo Empresas

    app.register_blueprint(empresas_bp)
    app.register_blueprint(empresasResumen_bp)
    app.register_blueprint(actEmpresa_bp)
    app.register_blueprint(verEmpresaID_bp)

    ##Filtros
    app.register_blueprint(verFiltrosCatalogos_bp)
    app.register_blueprint(verFiltrosModulo_bp)

    ##Reservas
    app.register_blueprint(verReservas_bp)
    app.register_blueprint(nvaReserva_bp)
    
    ##ReservasD
    app.register_blueprint(verReservaID_bp)  
    app.register_blueprint(avanzaReserva_bp)  
    app.register_blueprint(verViajesDisponibles_bp)  
    app.register_blueprint(verViajesDisponiblesVuelta_bp)  
    app.register_blueprint(actReservaD_bp)  
    app.register_blueprint(verReservaDetalle_bp)  
    app.register_blueprint(eliminarRenglonReserva_bp)  
    app.register_blueprint(afectarReserva_bp)  
    app.register_blueprint(cancelarReserva_bp)  
    app.register_blueprint(verAsientosDispoblesRuta_bp)  
    app.register_blueprint(agregarAsientosReserva_bp)  
    app.register_blueprint(guardarDatosPersonasReserva_bp)  
    app.register_blueprint(verPersonasReserva_bp)
    app.register_blueprint(agregarFormaPagoReserva_bp)    
    app.register_blueprint(cambiarSituacion_bp)  
    app.register_blueprint(verPdfReserva_bp)  

    app.register_blueprint(agregarEquipajeDetalle_bp)  
    app.register_blueprint(verEquipajeDetalle_bp)  
    app.register_blueprint(actEquipajeDetalle_bp)  
    app.register_blueprint(eliminarEquipaje_bp)  

    ##Paqueteria
    app.register_blueprint(verPaqueteria_bp)
    app.register_blueprint(nuevaPaqueteria_bp)
    
    ##PaqueteriaD
    app.register_blueprint(verPaqueteriaID_bp)
    app.register_blueprint(verArtDispPaqueteria_bp)
    app.register_blueprint(avanzarPaqueteria_bp)
    app.register_blueprint(agregarPaqueteriaDetalle_bp)
    app.register_blueprint(verPaqueteriaDetalle_bp)
    app.register_blueprint(actPaqueteriaDetalle_bp)
    app.register_blueprint(eliminarRenglonPaqueteria_bp)
    app.register_blueprint(cambiarSituacionPaqueteria_bp)
    app.register_blueprint(afectarPaqueteria_bp)
    app.register_blueprint(eliminarPaqueteria_bp)
    app.register_blueprint(cancelarPaqueteria_bp)

    # Catalogo Sucursales

    app.register_blueprint(verSucursales_bp)
    app.register_blueprint(actSucursal_bp)
    app.register_blueprint(verSucursalID_bp)

    # Catalogo Vehiculos
    app.register_blueprint(verVehiculos_bp)
    app.register_blueprint(actVehiculo_bp)
    app.register_blueprint(verVehiculoID_bp)

    # Catalogo Almacenes
    
    app.register_blueprint(almacenes_bp)
    app.register_blueprint(almacenResumen_bp)
    app.register_blueprint(actAlmacen_bp)
    app.register_blueprint(verAlmacenID_bp)

    # Catalogo Destinos

    app.register_blueprint(verDestinos_bp)
    app.register_blueprint(actDestino_bp)
    app.register_blueprint(verDestinoID_bp)

    # Catalogo Pasajeros

    app.register_blueprint(verPasajeros_bp)
    app.register_blueprint(actPasajeros_bp)
    app.register_blueprint(verPasajerosID_bp)

    # Catalogo Agentes

    app.register_blueprint(agentes_bp)
    app.register_blueprint(agentesResumen_bp)
    app.register_blueprint(actAgente_bp)
    app.register_blueprint(verAgenteID_bp)

    # Catalogo Equipos
    app.register_blueprint(verEquipos_bp)
    app.register_blueprint(verEquipoID_bp)
    app.register_blueprint(actEquipoD_bp)
    app.register_blueprint(eliminarEquipo_bp)

    # Catalogo Clientes
    app.register_blueprint(verClientes_bp)
    app.register_blueprint(verClienteID_bp)
    app.register_blueprint(actCliente_bp)

    # Explorador rutas
    app.register_blueprint(verExploradorRutas_bp)
    app.register_blueprint(verExploradorRutasID_bp)
    app.register_blueprint(VerParadasRutasExp_bp)
    app.register_blueprint(verPasajerosRuta_bp)
    
    #Explorador Paqueteria Recepcion
    app.register_blueprint(verPaqueteriaR_bp)

    #Explorador Paqueteria Entrega
    app.register_blueprint(verPaqueteriaEntrega_bp)
    
    #Catalogo de Rutas 
    app.register_blueprint(verRutas_bp)
    app.register_blueprint(verCatRutaID_bp)
    app.register_blueprint(actCatRuta_bp)
    app.register_blueprint(actDescensoRuta_bp)
    app.register_blueprint(delDescensoRuta_bp)

    #Catalogo de Choferes
    app.register_blueprint(verChoferes_bp)
    app.register_blueprint(verChoferID_bp)
    app.register_blueprint(actChoferD_bp)
    app.register_blueprint(eliminarChofer_bp)
    
    #Whatsapp api 
    app.register_blueprint(whatsapp_bp)
    app.register_blueprint(get_message_data_bp)
    app.register_blueprint(send_message_bp)
    app.register_blueprint(webhook_verify_bp)
    app.register_blueprint(webhook_bp)
    app.register_blueprint(upload_media_bp)
    app.register_blueprint(start_conversation_bp)
    app.register_blueprint(leerMensajesPorWAID_bp)
    app.register_blueprint(verUsuariosWAPP_bp)
    app.register_blueprint(marcarComoLeido_bp)
    app.register_blueprint(enviarEstadoCuenta1_bp)
    app.register_blueprint(enviarEstadoCuenta2_bp)
    app.register_blueprint(enviarEstadoCuenta3_bp)
    
    ##Configurador de rutas
    app.register_blueprint(verRutasModulo_bp)
    app.register_blueprint(nuevaRuta_bp)
    app.register_blueprint(verRutaID_bp)
    app.register_blueprint(avanzarRuta_bp)
    app.register_blueprint(verRutaDetalle_bp)
    app.register_blueprint(agregarParadaRuta_bp)
    app.register_blueprint(ActParadaRuta_bp)
    app.register_blueprint(eliminarParadaRuta_bp)
    app.register_blueprint(verParadaRutasDisponible_bp)
    app.register_blueprint(copiarRuta_bp)
    app.register_blueprint(eliminarRuta_bp)
    app.register_blueprint(cancelarRuta_bp)
    app.register_blueprint(afectarRuta_bp)
    app.register_blueprint(cambiarsituacionRuta_bp)
    
    #Precios Rutas
    app.register_blueprint(verPreciosRutas_bp)
    app.register_blueprint(actPreciosRuta_bp)
    app.register_blueprint(afectarCambioPreciosRuta_bp)
