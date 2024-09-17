from flask import Flask
from app.routes.login.login import login_bp 
from app.routes.Indicadores.indicadores import verIndicadores_bp 
from app.routes.Configuracion.Modulos import verModulos_bp, verModuloID_bp, actModulo_bp, eliminarModulo_bp
from app.routes.Catalogos.Usuarios import usuarios_bp, usuariosResumen_bp, actUsuario_bp, verUsuarioID_bp
from app.routes.Catalogos.Empresas import empresas_bp, empresasResumen_bp, actEmpresa_bp, verEmpresaID_bp
from app.routes.Catalogos.Sucursales import sucursales_bp, sucursalResumen_bp, actSucursal_bp, verSucursalID_bp
from app.routes.Catalogos.Vehiculos import vehiculos_bp, vehiculoResumen_bp, actVehiculo_bp, verVehiculoID_bp
from app.routes.Catalogos.Perfiles import verPerfiles_bp, verPerfilID_bp, actPerfil_bp
from app.routes.Catalogos.Almacenes import almacenes_bp, almacenResumen_bp, actAlmacen_bp, verAlmacenID_bp
from app.routes.Catalogos.Destinos import destinos_bp, destinoResumen_bp, actDestino_bp, verDestinoID_bp
from app.routes.Filtros.Filtros import verFiltrosCatalogos_bp, verFiltrosModulo_bp
from app.routes.Comercial.Reservas.Reservas import verReservas_bp, nvaReserva_bp
from app.routes.Comercial.Reservas.ReservasD import *
from app.routes.Exploradores.RutasExplorador import verExploradorRutas_bp, verExploradorRutasID_bp
from app.routes.Catalogos.Rutas import rutas_bp, rutasResumen_bp, actRuta_bp, verHorarios_bp, actHorarioRuta_bp, verRutasHorarios_bp, eliminarRutaHorario_bp
from app.routes.Catalogos.Choferes import choferes_bp, choferesResumen_bp, actChoferes_bp, verChoferID_bp

def register_routes(app: Flask):
    # Login
    app.register_blueprint(login_bp)

    # Indicadores
    app.register_blueprint(verIndicadores_bp)
    
    # Configuracion modulos
    app.register_blueprint(verModulos_bp)
    app.register_blueprint(verModuloID_bp)
    app.register_blueprint(actModulo_bp)
    app.register_blueprint(eliminarModulo_bp)

    # Catalogo Usuarios

    app.register_blueprint(usuarios_bp)
    app.register_blueprint(usuariosResumen_bp)
    app.register_blueprint(actUsuario_bp)
    app.register_blueprint(verUsuarioID_bp)

    ##Catalogo Perfiles

    app.register_blueprint(verPerfiles_bp)  
    app.register_blueprint(verPerfilID_bp)  
    app.register_blueprint(actPerfil_bp)  

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

    # Catalogo Sucursales

    app.register_blueprint(sucursales_bp)
    app.register_blueprint(sucursalResumen_bp)
    app.register_blueprint(actSucursal_bp)
    app.register_blueprint(verSucursalID_bp)

    # Catalogo Vehiculos
    app.register_blueprint(vehiculos_bp)
    app.register_blueprint(vehiculoResumen_bp)
    app.register_blueprint(actVehiculo_bp)
    app.register_blueprint(verVehiculoID_bp)

    # Catalogo Almacenes
    
    app.register_blueprint(almacenes_bp)
    app.register_blueprint(almacenResumen_bp)
    app.register_blueprint(actAlmacen_bp)
    app.register_blueprint(verAlmacenID_bp)

    # Catalogo Destinos

    app.register_blueprint(destinos_bp)
    app.register_blueprint(destinoResumen_bp)
    app.register_blueprint(actDestino_bp)
    app.register_blueprint(verDestinoID_bp)



    # Explorador rutas
    app.register_blueprint(verExploradorRutas_bp)
    app.register_blueprint(verExploradorRutasID_bp)
    
    #Catalogo de Rutas 
    app.register_blueprint(rutas_bp)
    app.register_blueprint(rutasResumen_bp)
    app.register_blueprint(actRuta_bp)
    app.register_blueprint(verHorarios_bp)
    app.register_blueprint(actHorarioRuta_bp)
    app.register_blueprint(verRutasHorarios_bp)
    app.register_blueprint(eliminarRutaHorario_bp)

    #Catalogo de Choferes
    app.register_blueprint(choferes_bp)
    app.register_blueprint(choferesResumen_bp)
    app.register_blueprint(actChoferes_bp)
    app.register_blueprint(verChoferID_bp)
    
