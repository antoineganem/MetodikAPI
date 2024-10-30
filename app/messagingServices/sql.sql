CREATE TABLE UsuariosWhatsapp (
    UsuarioID INT IDENTITY(1,1) PRIMARY KEY,    -- IDENTITY para autoincremento
    wa_id VARCHAR(50) UNIQUE,                   -- wa_id único
    Nombre NVARCHAR(100),                       -- NVARCHAR para soporte Unicode
    FechaRegistro DATETIME DEFAULT GETDATE()    -- GETDATE() para fecha actual
);

CREATE TABLE Conversaciones (
    MensajeID INT IDENTITY(1,1) PRIMARY KEY,    -- IDENTITY para autoincremento
    UsuarioID INT,                              -- Clave foránea a UsuariosWhatsapp
    Remitente VARCHAR(10) CHECK (Remitente IN ('cliente', 'bot', 'agente')),   -- Validación de valores permitidos
    Mensaje NVARCHAR(MAX),                      -- NVARCHAR(MAX) para texto largo
    FechaEnvio DATETIME DEFAULT GETDATE(),      -- Fecha de envío con valor por defecto
    TipoMensaje VARCHAR(10) CHECK (TipoMensaje IN ('texto', 'imagen', 'archivo')),  -- Validación de tipos de mensaje
    Leido Bit DEFAULT 0
);


---Store procedures para insertar datos y crear usuarios

Create Procedure spLeerMensajesPorWaID
    @wa_id VARCHAR(50)
AS
BEGIN
    Select C.MensajeID, C.Remitente, C.Mensaje, C.FechaEnvio, C.TipoMensaje
	From Conversaciones C
	Inner join UsuariosWhatsapp U on C.UsuarioID = U.UsuarioID
	where u.wa_id = @wa_id
	Order by C.fechaEnvio;
END;

CREATE PROCEDURE spLeerTodosLosMensajes
AS
BEGIN
    SELECT 
        ISNULL(C.MensajeID, '') AS MensajeID,
        ISNULL(C.Remitente, '') AS Remitente,
        ISNULL(C.Mensaje, '') AS Mensaje,
        ISNULL(C.FechaEnvio, '') AS FechaEnvio,
        ISNULL(C.TipoMensaje, '') AS TipoMensaje,
        ISNULL(U.UsuarioID, '') AS UsuarioID,
        ISNULL(U.Telefono, '') AS Telefono,
        ISNULL(U.Nombre, '') AS Nombre,
        ISNULL(U.wa_id, '') AS wa_id
    FROM Conversaciones C
    INNER JOIN UsuariosWhatsapp U ON C.UsuarioID = U.UsuarioID
    ORDER BY C.FechaEnvio;
END;

ALTER PROCEDURE spActMensajesWAPP
    @wa_id VARCHAR(50),
    @Nombre NVARCHAR(50),
    @Mensaje NVARCHAR(MAX),
    @Remitente VARCHAR(10),
    @TipoMensaje VARCHAR(10)
AS
BEGIN
    -- Variables para manejar transacciones y errores
    DECLARE @UsuarioID INT;
    DECLARE @ErrorMessage NVARCHAR(4000);
    DECLARE @ErrorSeverity INT;
    DECLARE @ErrorState INT;

    BEGIN TRY
        -- Inicio de la transacción
        BEGIN TRANSACTION;

        -- Verificar si el usuario ya existe en la tabla UsuariosWhatsapp
        SELECT @UsuarioID = UsuarioID 
        FROM UsuariosWhatsapp 
        WHERE wa_id = @wa_id;

        -- Si no existe, agregar el usuario a la tabla UsuariosWhatsapp
        IF @UsuarioID IS NULL
        BEGIN
            INSERT INTO UsuariosWhatsapp (wa_id, Nombre )
            VALUES (@wa_id, @Nombre )
            
            -- Obtener el UsuarioID del nuevo usuario insertado
            SET @UsuarioID = SCOPE_IDENTITY();
        END

        -- Insertar el mensaje en la tabla Conversaciones
        INSERT INTO Conversaciones (UsuarioID, Remitente, Mensaje, TipoMensaje, FechaEnvio)
        VALUES (@UsuarioID, @Remitente, @Mensaje, @TipoMensaje, GETDATE());

        -- Completar la transacción
        COMMIT TRANSACTION;

        -- Devolver un mensaje de éxito
        SELECT 'Todo está bien. Mensaje agregado exitosamente.' AS Mensaje;
    END TRY
    BEGIN CATCH
        -- Deshacer la transacción en caso de error
        ROLLBACK TRANSACTION;

        -- Obtener información del error
        SELECT 
            @ErrorMessage = ERROR_MESSAGE(),
            @ErrorSeverity = ERROR_SEVERITY(),
            @ErrorState = ERROR_STATE();

        -- Devolver el error
        RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
    END CATCH;
END;

CREATE PROCEDURE spVerUsuariosWAPP
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        u.UsuarioID,
        u.wa_id,
        u.Nombre,
        MAX(c.FechaEnvio) AS UltimoMensajeFecha,
        c.Mensaje AS UltimoMensaje,
        c.Leido AS UltimoMensajeLeido
    FROM 
        UsuariosWhatsapp u
    LEFT JOIN 
        Conversaciones c ON u.UsuarioID = c.UsuarioID
    WHERE
        c.FechaEnvio = (
            SELECT MAX(FechaEnvio) 
            FROM Conversaciones 
            WHERE UsuarioID = u.UsuarioID
        )
    GROUP BY 
        u.UsuarioID, u.wa_id, u.Nombre, c.Mensaje, c.Leido
    ORDER BY 
        UltimoMensajeFecha DESC;
END;

