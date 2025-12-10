# Descripción Detallada de Casos de Uso
## Inventario Emocional - Al-Anon

---

## Formato Estándar de Casos de Uso

Cada caso de uso sigue el siguiente formato:

- **ID**: Identificador único
- **Nombre**: Título descriptivo del caso de uso
- **Actor Principal**: Usuario que inicia el caso de uso
- **Actores Secundarios**: Otros participantes
- **Descripción**: Breve explicación del propósito
- **Precondiciones**: Condiciones que deben cumplirse antes
- **Postcondiciones**: Estado del sistema después de ejecutar
- **Flujo Principal**: Secuencia normal de pasos
- **Flujos Alternativos**: Variaciones del flujo principal
- **Flujos de Excepción**: Manejo de errores

---

## CU-01: Registro de Usuario

### Información General
- **ID**: CU-01
- **Nombre**: Registro de Usuario
- **Actor Principal**: Nuevo Usuario (futuro Miembro)
- **Actores Secundarios**: Sistema
- **Descripción**: Permite a un nuevo usuario crear una cuenta en el sistema para acceder como miembro.

### Precondiciones
- El usuario debe tener acceso a la aplicación
- El usuario no debe estar previamente registrado
- La aplicación debe tener conexión a la base de datos

### Postcondiciones
- Se crea una nueva cuenta de usuario en el sistema
- El usuario puede iniciar sesión como miembro
- Se asigna el rol "miembro" al usuario
- Se envía confirmación de registro

### Flujo Principal

1. El usuario abre la aplicación y accede a la pantalla de bienvenida
2. El sistema muestra las opciones: "Iniciar Sesión" y "Registrarse"
3. El usuario selecciona "Registrarse"
4. El sistema presenta el formulario de registro con campos:
   - Nombre completo
   - Correo electrónico
   - Contraseña
   - Confirmar contraseña
5. El usuario completa todos los campos del formulario
6. El usuario presiona el botón "Crear cuenta"
7. El sistema valida los datos ingresados:
   - Email con formato válido
   - Contraseña de mínimo 8 caracteres
   - Contraseñas coinciden
8. El sistema verifica que el email no esté registrado en la base de datos
9. El sistema encripta la contraseña
10. El sistema crea el registro del usuario con rol "miembro"
11. El sistema guarda el usuario en la base de datos
12. El sistema muestra mensaje de confirmación "Registro exitoso"
13. El sistema redirige al usuario a la pantalla de login
14. Fin del caso de uso

### Flujos Alternativos

**FA-01: Email ya registrado (en paso 8)**
- 8.1. El sistema detecta que el email ya existe en la base de datos
- 8.2. El sistema muestra mensaje de error: "Este correo ya está registrado"
- 8.3. El sistema mantiene al usuario en el formulario de registro
- 8.4. Retorna al paso 5

**FA-02: Contraseñas no coinciden (en paso 7)**
- 7.1. El sistema detecta que las contraseñas no coinciden
- 7.2. El sistema muestra mensaje: "Las contraseñas no coinciden"
- 7.3. El sistema limpia los campos de contraseña
- 7.4. Retorna al paso 5

**FA-03: Email con formato inválido (en paso 7)**
- 7.1. El sistema detecta formato de email inválido
- 7.2. El sistema muestra mensaje: "Ingrese un correo electrónico válido"
- 7.3. El sistema resalta el campo de email en rojo
- 7.4. Retorna al paso 5

**FA-04: Contraseña muy corta (en paso 7)**
- 7.1. El sistema detecta que la contraseña tiene menos de 8 caracteres
- 7.2. El sistema muestra mensaje: "La contraseña debe tener al menos 8 caracteres"
- 7.3. El sistema resalta el campo de contraseña
- 7.4. Retorna al paso 5

### Flujos de Excepción

**FE-01: Error de conexión a base de datos (en paso 11)**
- 11.1. El sistema no puede conectar con la base de datos
- 11.2. El sistema muestra mensaje: "Error de conexión. Intente nuevamente"
- 11.3. El sistema registra el error en el log
- 11.4. Retorna al paso 5

**FE-02: Campos vacíos (en paso 7)**
- 7.1. El sistema detecta que hay campos vacíos
- 7.2. El sistema muestra mensaje: "Todos los campos son obligatorios"
- 7.3. El sistema resalta los campos vacíos
- 7.4. Retorna al paso 5

---

## CU-02: Iniciar Sesión

### Información General
- **ID**: CU-02
- **Nombre**: Iniciar Sesión
- **Actor Principal**: Miembro o Administrador
- **Actores Secundarios**: Sistema
- **Descripción**: Permite a usuarios registrados autenticarse en el sistema según su rol.

### Precondiciones
- El usuario debe estar registrado en el sistema
- La aplicación debe tener conexión a la base de datos
- El usuario debe tener una cuenta activa

### Postcondiciones
- Se crea una sesión activa para el usuario
- El usuario accede al dashboard correspondiente a su rol
- Se registra la fecha y hora del inicio de sesión

### Flujo Principal

1. El usuario abre la aplicación
2. El sistema muestra la pantalla de bienvenida
3. El usuario selecciona "Iniciar Sesión como Miembro" o "Iniciar Sesión como Admin"
4. El sistema presenta el formulario de login con campos:
   - Correo electrónico
   - Contraseña
5. El usuario ingresa sus credenciales
6. El usuario presiona el botón "Entrar"
7. El sistema valida el formato de los datos
8. El sistema busca el usuario en la base de datos por email
9. El sistema verifica que la contraseña coincida con el hash almacenado
10. El sistema verifica que el rol del usuario coincida con el tipo de login seleccionado
11. El sistema crea un token de sesión
12. El sistema registra el login en el log de auditoría
13. El sistema redirige al usuario:
    - Si es miembro → Dashboard Miembro
    - Si es admin → Dashboard Administrador
14. Fin del caso de uso

### Flujos Alternativos

**FA-01: Credenciales incorrectas (en paso 9)**
- 9.1. El sistema detecta que la contraseña no coincide
- 9.2. El sistema incrementa el contador de intentos fallidos
- 9.3. El sistema muestra mensaje: "Credenciales incorrectas"
- 9.4. Si intentos < 3, retorna al paso 5
- 9.5. Si intentos >= 3, ir a FE-02

**FA-02: Usuario no encontrado (en paso 8)**
- 8.1. El sistema no encuentra el email en la base de datos
- 8.2. El sistema muestra mensaje: "Usuario no registrado"
- 8.3. El sistema ofrece opción "Registrarse"
- 8.4. Retorna al paso 5 o va a CU-01

**FA-03: Rol incorrecto (en paso 10)**
- 10.1. El sistema detecta que el rol no coincide con el tipo de login
- 10.2. El sistema muestra mensaje: "No tiene permisos para este tipo de acceso"
- 10.3. El sistema sugiere el tipo de login correcto
- 10.4. Retorna al paso 3

### Flujos de Excepción

**FE-01: Error de conexión (en paso 8)**
- 8.1. El sistema no puede acceder a la base de datos
- 8.2. El sistema muestra mensaje: "Error de conexión. Intente nuevamente"
- 8.3. El sistema registra el error en el log
- 8.4. Retorna al paso 5

**FE-02: Cuenta bloqueada (en paso FA-01.5)**
- 1. El sistema detecta 3 intentos fallidos consecutivos
- 2. El sistema bloquea temporalmente la cuenta (15 minutos)
- 3. El sistema muestra mensaje: "Cuenta bloqueada temporalmente por seguridad"
- 4. El sistema registra el bloqueo en el log
- 5. Fin del caso de uso

**FE-03: Cuenta desactivada (en paso 9)**
- 9.1. El sistema detecta que la cuenta está inactiva
- 9.2. El sistema muestra mensaje: "Su cuenta ha sido desactivada. Contacte al administrador"
- 9.3. Fin del caso de uso

---

## CU-03: Registrar Inventario Emocional

### Información General
- **ID**: CU-03
- **Nombre**: Registrar Inventario Emocional
- **Actor Principal**: Miembro
- **Actores Secundarios**: Sistema
- **Descripción**: Permite al miembro completar y guardar su inventario emocional diario.
- **Extiende**: CU-02 (Requiere estar autenticado)

### Precondiciones
- El miembro debe haber iniciado sesión (CU-02)
- El miembro debe estar en el Dashboard
- Debe tener conexión a Internet

### Postcondiciones
- Se guarda un nuevo inventario emocional en la base de datos
- El inventario queda asociado al usuario y a la fecha actual
- El historial del usuario se actualiza
- Los datos quedan disponibles para generar estadísticas

### Flujo Principal

1. El miembro desde el Dashboard selecciona "Nuevo Inventario"
2. El sistema verifica la sesión activa
3. El sistema muestra el formulario de inventario con secciones:
   - Resentimientos
   - Defectos de carácter
   - Miedos
   - Responsabilidades
4. **Sección Resentimientos:**
   - 4.1. El miembro presiona "+ Agregar Resentimiento"
   - 4.2. El sistema muestra campos:
     - Persona o situación
     - Causa (¿por qué me molesta?)
     - Afecta a (autoestima, seguridad, relaciones, etc.)
   - 4.3. El miembro completa los campos
   - 4.4. El miembro puede agregar más resentimientos (repetir 4.1-4.3)
5. **Sección Defectos de Carácter:**
   - 5.1. El sistema muestra lista de defectos comunes
   - 5.2. El miembro selecciona los que identifica (checkbox)
   - 5.3. El miembro puede agregar otros escribiéndolos
6. **Sección Miedos:**
   - 6.1. El sistema muestra campo de texto
   - 6.2. El miembro escribe sus miedos reconocidos
7. **Sección Responsabilidades:**
   - 7.1. El sistema muestra campo de texto largo
   - 7.2. El miembro reflexiona y escribe su parte de responsabilidad
8. El miembro presiona el botón "Guardar Inventario"
9. El sistema valida que al menos una sección esté completa
10. El sistema crea un objeto Inventario con:
    - ID único
    - Fecha actual
    - ID del miembro
    - Datos de todas las secciones
11. El sistema guarda el inventario en MongoDB
12. El sistema muestra mensaje: "Inventario guardado exitosamente"
13. El sistema redirige al Dashboard o al Historial
14. Fin del caso de uso

### Flujos Alternativos

**FA-01: Guardar borrador (en paso 8)**
- 8.1. El miembro presiona "Guardar como borrador"
- 8.2. El sistema guarda el inventario con estado "borrador"
- 8.3. El sistema permite editar el borrador después
- 8.4. Retorna al Dashboard

**FA-02: Cancelar inventario (en cualquier paso)**
- 1. El miembro presiona "Cancelar"
- 2. El sistema muestra confirmación: "¿Descartar cambios?"
- 3. Si confirma:
   - 3.1. El sistema descarta los datos
   - 3.2. Retorna al Dashboard
- 4. Si cancela:
   - 4.1. El sistema mantiene al usuario en el formulario

**FA-03: Agregar múltiples resentimientos (en paso 4.4)**
- 4.4.1. El miembro puede agregar hasta 10 resentimientos
- 4.4.2. Si intenta agregar más de 10:
   - Sistema muestra: "Máximo 10 resentimientos por inventario"
- 4.4.3. El miembro puede eliminar resentimientos agregados

### Flujos de Excepción

**FE-01: Formulario vacío (en paso 9)**
- 9.1. El sistema detecta que no hay datos en ninguna sección
- 9.2. El sistema muestra mensaje: "Debe completar al menos una sección"
- 9.3. Retorna al paso 4

**FE-02: Error al guardar (en paso 11)**
- 11.1. El sistema no puede guardar en la base de datos
- 11.2. El sistema muestra mensaje: "Error al guardar. Intente nuevamente"
- 11.3. El sistema mantiene los datos en el formulario
- 11.4. El sistema registra el error en el log
- 11.5. Retorna al paso 8

**FE-03: Sesión expirada (en paso 2)**
- 2.1. El sistema detecta que la sesión expiró
- 2.2. El sistema muestra mensaje: "Su sesión ha expirado. Inicie sesión nuevamente"
- 2.3. El sistema redirige a la pantalla de login
- 2.4. Fin del caso de uso

**FE-04: Sin conexión (en paso 11)**
- 11.1. El sistema detecta que no hay conexión a Internet
- 11.2. El sistema muestra mensaje: "Sin conexión. Los datos se guardarán cuando haya Internet"
- 11.3. El sistema guarda temporalmente en almacenamiento local
- 11.4. Cuando haya conexión, sincroniza automáticamente

---

## CU-04: Consultar Historial

### Información General
- **ID**: CU-04
- **Nombre**: Consultar Historial
- **Actor Principal**: Miembro
- **Actores Secundarios**: Sistema
- **Descripción**: Permite al miembro visualizar sus inventarios emocionales anteriores.
- **Extiende**: CU-02 (Requiere autenticación)

### Precondiciones
- El miembro debe haber iniciado sesión
- El miembro debe tener al menos un inventario registrado

### Postcondiciones
- El miembro visualiza su historial de inventarios
- Se puede acceder al detalle de cada inventario

### Flujo Principal

1. El miembro desde el Dashboard selecciona "Mi Historial"
2. El sistema verifica la sesión activa
3. El sistema consulta la base de datos por inventarios del usuario
4. El sistema ordena los inventarios por fecha (más reciente primero)
5. El sistema muestra una lista con tarjetas que incluyen:
   - Fecha del inventario
   - Número de resentimientos
   - Resumen breve (primeras líneas)
6. El miembro visualiza la lista de inventarios
7. El miembro selecciona un inventario para ver el detalle
8. El sistema recupera el inventario completo de la base de datos
9. El sistema muestra la vista detallada con todas las secciones:
   - Fecha completa
   - Todos los resentimientos
   - Defectos de carácter
   - Miedos
   - Reflexión sobre responsabilidad
10. El miembro lee el contenido completo
11. Fin del caso de uso

### Flujos Alternativos

**FA-01: Filtrar por fecha (en paso 6)**
- 6.1. El miembro presiona el ícono de filtro
- 6.2. El sistema muestra selector de rango de fechas
- 6.3. El miembro selecciona fecha inicio y fecha fin
- 6.4. El miembro presiona "Aplicar filtro"
- 6.5. El sistema filtra y muestra solo inventarios en ese rango
- 6.6. Continúa en paso 6

**FA-02: Eliminar inventario (en paso 9)**
- 9.1. El miembro presiona el ícono de eliminar
- 9.2. El sistema muestra confirmación: "¿Eliminar este inventario?"
- 9.3. Si confirma:
   - 9.3.1. El sistema elimina el inventario de la base de datos
   - 9.3.2. El sistema muestra mensaje: "Inventario eliminado"
   - 9.3.3. El sistema actualiza la lista
   - 9.3.4. Retorna al paso 5
- 9.4. Si cancela, mantiene el inventario

**FA-03: Exportar inventario (en paso 9)**
- 9.1. El miembro presiona "Exportar"
- 9.2. El sistema genera un PDF con el contenido completo
- 9.3. El sistema descarga el archivo al dispositivo
- 9.4. El sistema muestra mensaje: "Archivo guardado"

**FA-04: Sin inventarios (en paso 3)**
- 3.1. El sistema no encuentra inventarios del usuario
- 3.2. El sistema muestra mensaje: "Aún no tienes inventarios registrados"
- 3.3. El sistema muestra botón "Crear primer inventario"
- 3.4. Si el miembro presiona el botón, va a CU-03
- 3.5. Fin del caso de uso

### Flujos de Excepción

**FE-01: Error al cargar (en paso 3)**
- 3.1. El sistema no puede acceder a la base de datos
- 3.2. El sistema muestra mensaje: "Error al cargar historial. Intente nuevamente"
- 3.3. El sistema ofrece botón "Reintentar"
- 3.4. Si presiona reintentar, vuelve al paso 3

**FE-02: Inventario no encontrado (en paso 8)**
- 8.1. El sistema no puede recuperar el inventario específico
- 8.2. El sistema muestra mensaje: "Este inventario ya no está disponible"
- 8.3. El sistema actualiza la lista eliminando la referencia
- 8.4. Retorna al paso 5

---

## CU-05: Ver Estadísticas

### Información General
- **ID**: CU-05
- **Nombre**: Ver Estadísticas
- **Actor Principal**: Miembro
- **Actores Secundarios**: Sistema
- **Descripción**: Permite visualizar gráficos y análisis de patrones emocionales.
- **Extiende**: CU-02

### Precondiciones
- El miembro debe haber iniciado sesión
- El miembro debe tener al menos 3 inventarios registrados

### Postcondiciones
- Se generan y muestran gráficos de tendencias
- El miembro puede identificar patrones emocionales

### Flujo Principal

1. El miembro desde el Dashboard selecciona "Estadísticas"
2. El sistema verifica la sesión activa
3. El sistema cuenta los inventarios del usuario
4. El sistema recupera todos los inventarios del usuario
5. El sistema analiza los datos:
   - Frecuencia de emociones
   - Defectos de carácter más comunes
   - Miedos recurrentes
   - Tendencias en el tiempo
6. El sistema genera gráficos usando Matplotlib:
   - Gráfico de líneas: Emociones en el tiempo
   - Gráfico de barras: Defectos más frecuentes
   - Gráfico circular: Distribución de miedos
   - Resumen numérico del período
7. El sistema muestra la pantalla de estadísticas con los gráficos
8. El miembro visualiza los gráficos y análisis
9. Fin del caso de uso

### Flujos Alternativos

**FA-01: Cambiar período (en paso 8)**
- 8.1. El miembro selecciona un período diferente:
   - Última semana
   - Último mes
   - Últimos 3 meses
   - Personalizado
- 8.2. El sistema filtra los datos según el período
- 8.3. El sistema regenera los gráficos
- 8.4. Continúa en paso 7

**FA-02: Pocos inventarios (en paso 3)**
- 3.1. El sistema detecta menos de 3 inventarios
- 3.2. El sistema muestra mensaje: "Necesitas al menos 3 inventarios para generar estadísticas"
- 3.3. El sistema muestra progreso: "Llevas X de 3 inventarios"
- 3.4. El sistema ofrece botón "Crear inventario"
- 3.5. Fin del caso de uso

### Flujos de Excepción

**FE-01: Error al generar gráficos (en paso 6)**
- 6.1. El sistema tiene error al procesar los datos
- 6.2. El sistema muestra mensaje: "Error al generar estadísticas"
- 6.3. El sistema registra el error en el log
- 6.4. El sistema ofrece botón "Reintentar"

---

## CU-06: Participar en Chat

### Información General
- **ID**: CU-06
- **Nombre**: Participar en Chat
- **Actor Principal**: Miembro
- **Actores Secundarios**: Sistema, Otros Miembros
- **Descripción**: Permite enviar y recibir mensajes en el chat general.
- **Extiende**: CU-02

### Precondiciones
- El miembro debe haber iniciado sesión
- Debe tener conexión a Internet activa

### Postcondiciones
- Los mensajes enviados son visibles para todos los miembros
- Los mensajes se almacenan en la base de datos

### Flujo Principal

1. El miembro desde el Dashboard selecciona "Chat General"
2. El sistema verifica la sesión activa
3. El sistema conecta al servicio de chat en tiempo real
4. El sistema carga los últimos 50 mensajes
5. El sistema muestra la interfaz del chat:
   - Lista de mensajes (arriba)
   - Campo de texto (abajo)
   - Botón enviar
6. El miembro lee los mensajes existentes
7. El miembro escribe un mensaje en el campo de texto (máx. 500 caracteres)
8. El miembro presiona el botón "Enviar"
9. El sistema valida el mensaje:
   - No está vacío
   - No excede 500 caracteres
   - No contiene palabras prohibidas
10. El sistema crea un objeto Mensaje con:
    - ID único
    - ID del usuario
    - Contenido
    - Fecha y hora actual
11. El sistema guarda el mensaje en MongoDB
12. El sistema transmite el mensaje a todos los usuarios conectados
13. El sistema actualiza la interfaz mostrando el nuevo mensaje
14. Otros miembros conectados reciben el mensaje en tiempo real
15. Fin del caso de uso (el miembro puede seguir en el chat)

### Flujos Alternativos

**FA-01: Recibir mensajes en tiempo real (proceso continuo)**
- 1. Mientras el miembro está en el chat
- 2. El sistema escucha constantemente por nuevos mensajes
- 3. Cuando otro miembro envía un mensaje
- 4. El sistema lo recibe y lo muestra automáticamente
- 5. Se reproduce un sonido de notificación (opcional)

**FA-02: Límite de caracteres (en paso 9)**
- 9.1. El sistema detecta más de 500 caracteres
- 9.2. El sistema muestra contador en rojo
- 9.3. El sistema deshabilita el botón enviar
- 9.4. El miembro debe reducir el texto
- 9.5. Retorna al paso 7

**FA-03: Mensaje vacío (en paso 9)**
- 9.1. El sistema detecta que el mensaje está vacío
- 9.2. El sistema mantiene el botón enviar deshabilitado
- 9.3. No se permite enviar

### Flujos de Excepción

**FE-01: Sin conexión (en paso 3)**
- 3.1. El sistema no puede conectar al servicio de chat
- 3.2. El sistema muestra mensaje: "Sin conexión al chat. Verifique su Internet"
- 3.3. El sistema ofrece botón "Reintentar"
- 3.4. Fin del caso de uso

**FE-02: Contenido inapropiado (en paso 9)**
- 9.1. El sistema detecta palabras prohibidas o contenido ofensivo
- 9.2. El sistema muestra advertencia: "El mensaje contiene contenido no permitido"
- 9.3. El sistema no envía el mensaje
- 9.4. El sistema registra el intento en el log
- 9.5. Retorna al paso 7

**FE-03: Rate limiting (en paso 10)**
- 10.1. El sistema detecta más de 10 mensajes en 1 minuto
- 10.2. El sistema bloquea temporalmente al usuario (1 minuto)
- 10.3. El sistema muestra: "Ha enviado demasiados mensajes. Espere un momento"
- 10.4. El sistema registra el evento
- 10.5. Retorna al paso 7 después del bloqueo

---

## CU-07: Gestionar Usuarios (Admin)

### Información General
- **ID**: CU-07
- **Nombre**: Gestionar Usuarios
- **Actor Principal**: Administrador
- **Actores Secundarios**: Sistema, Usuarios
- **Descripción**: Permite al admin listar, editar, desactivar y eliminar usuarios.
- **Extiende**: CU-02

### Precondiciones
- El administrador debe haber iniciado sesión
- Debe tener permisos de administrador

### Postcondiciones
- Los cambios en usuarios se reflejan en la base de datos
- Se registran todas las acciones en el log de auditoría

### Flujo Principal

1. El admin desde Dashboard Admin selecciona "Gestionar Usuarios"
2. El sistema verifica permisos de administrador
3. El sistema consulta todos los usuarios en la base de datos
4. El sistema muestra tabla con columnas:
   - ID
   - Nombre
   - Email
   - Fecha de registro
   - Rol (miembro/admin)
   - Estado (activo/inactivo)
   - Acciones (editar, desactivar, eliminar)
5. El admin visualiza la lista completa
6. El admin selecciona un usuario específico
7. El admin elige una acción:
   - **Editar**: Ir a FA-01
   - **Desactivar**: Ir a FA-02
   - **Eliminar**: Ir a FA-03
8. Fin del caso de uso

### Flujos Alternativos

**FA-01: Editar usuario (en paso 7)**
- 7.1. El admin presiona "Editar"
- 7.2. El sistema muestra formulario con datos actuales:
   - Nombre
   - Email
   - Rol
   - Estado
- 7.3. El admin modifica los campos permitidos
- 7.4. El admin presiona "Guardar cambios"
- 7.5. El sistema valida los nuevos datos
- 7.6. El sistema actualiza el usuario en la base de datos
- 7.7. El sistema registra el cambio en el log de auditoría
- 7.8. El sistema muestra mensaje: "Usuario actualizado exitosamente"
- 7.9. El sistema actualiza la tabla
- 7.10. Retorna al paso 5

**FA-02: Desactivar/Activar usuario (en paso 7)**
- 7.1. El admin presiona "Cambiar estado"
- 7.2. El sistema muestra confirmación: "¿Desactivar este usuario?"
- 7.3. El admin confirma
- 7.4. El sistema cambia el estado del usuario a "inactivo"
- 7.5. El sistema cierra todas las sesiones activas del usuario
- 7.6. El sistema registra la acción en el log
- 7.7. El sistema muestra mensaje: "Usuario desactivado"
- 7.8. El sistema actualiza la tabla
- 7.9. Retorna al paso 5

**FA-03: Eliminar usuario (en paso 7)**
- 7.1. El admin presiona "Eliminar"
- 7.2. El sistema muestra advertencia: "ATENCIÓN: Esta acción es irreversible. ¿Eliminar usuario y todos sus datos?"
- 7.3. El admin debe confirmar escribiendo "ELIMINAR"
- 7.4. El admin confirma
- 7.5. El sistema elimina:
   - El usuario
   - Todos sus inventarios
   - Todos sus mensajes de chat
- 7.6. El sistema registra la eliminación en el log
- 7.7. El sistema muestra mensaje: "Usuario eliminado permanentemente"
- 7.8. El sistema actualiza la tabla
- 7.9. Retorna al paso 5

**FA-04: Buscar usuario (en paso 5)**
- 5.1. El admin escribe en la barra de búsqueda
- 5.2. El sistema filtra en tiempo real por:
   - Nombre
   - Email
   - ID
- 5.3. El sistema muestra solo usuarios que coincidan
- 5.4. Continúa en paso 5

### Flujos de Excepción

**FE-01: Intentar eliminar a sí mismo (en FA-03.3)**
- 3.1. El sistema detecta que el admin intenta eliminarse
- 3.2. El sistema muestra error: "No puede eliminar su propia cuenta"
- 3.3. Cancela la acción
- 3.4. Retorna al paso 5

**FE-02: Sin permisos (en paso 2)**
- 2.1. El sistema detecta que el usuario no es administrador
- 2.2. El sistema muestra mensaje: "Acceso denegado"
- 2.3. El sistema redirige al Dashboard correspondiente
- 2.4. Fin del caso de uso

---

## CU-08: Moderar Chat (Admin)

### Información General
- **ID**: CU-08
- **Nombre**: Moderar Chat
- **Actor Principal**: Administrador
- **Actores Secundarios**: Sistema, Miembros
- **Descripción**: Permite al admin supervisar y moderar mensajes del chat.
- **Extiende**: CU-02

### Precondiciones
- El administrador debe haber iniciado sesión
- Debe tener permisos de moderación

### Postcondiciones
- Mensajes inapropiados son eliminados
- Usuarios infractores son advertidos o sancionados
- Todas las acciones quedan registradas

### Flujo Principal

1. El admin desde Dashboard Admin selecciona "Moderar Chat"
2. El sistema verifica permisos de moderación
3. El sistema muestra la interfaz de moderación con:
   - Panel de mensajes recientes
   - Filtros (por usuario, por fecha, por reportes)
   - Historial de moderación
4. El admin visualiza los mensajes del chat
5. El admin identifica un mensaje inapropiado
6. El admin selecciona el mensaje
7. El admin elige una acción:
   - **Eliminar mensaje**: Ir a FA-01
   - **Advertir usuario**: Ir a FA-02
   - **Suspender usuario**: Ir a FA-03
8. Fin del caso de uso

### Flujos Alternativos

**FA-01: Eliminar mensaje (en paso 7)**
- 7.1. El admin presiona "Eliminar mensaje"
- 7.2. El sistema muestra confirmación: "¿Eliminar este mensaje?"
- 7.3. El admin confirma
- 7.4. El sistema elimina el mensaje de la base de datos
- 7.5. El sistema actualiza el chat para todos los usuarios
- 7.6. El sistema registra:
   - ID del mensaje eliminado
   - Contenido del mensaje
   - Usuario autor
   - Admin que eliminó
   - Fecha y hora
- 7.7. El sistema muestra mensaje: "Mensaje eliminado"
- 7.8. Retorna al paso 4

**FA-02: Advertir usuario (en paso 7)**
- 7.1. El admin presiona "Advertir usuario"
- 7.2. El sistema muestra formulario para motivo de advertencia
- 7.3. El admin escribe el motivo
- 7.4. El admin confirma
- 7.5. El sistema registra la advertencia en el perfil del usuario
- 7.6. El sistema envía notificación al usuario con el motivo
- 7.7. El sistema registra la acción en el log de moderación
- 7.8. El sistema muestra mensaje: "Usuario advertido"
- 7.9. Retorna al paso 4

**FA-03: Suspender usuario (en paso 7)**
- 7.1. El admin presiona "Suspender usuario"
- 7.2. El sistema muestra opciones de suspensión:
   - Temporal (1 día, 7 días, 30 días)
   - Permanente
- 7.3. El admin selecciona el tipo y duración
- 7.4. El admin escribe el motivo
- 7.5. El admin confirma
- 7.6. El sistema actualiza el estado del usuario a "suspendido"
- 7.7. El sistema cierra la sesión del usuario
- 7.8. El sistema impide que el usuario acceda al chat
- 7.9. El sistema envía notificación al usuario
- 7.10. El sistema registra la suspensión en el log
- 7.11. El sistema muestra mensaje: "Usuario suspendido"
- 7.12. Retorna al paso 4

**FA-04: Ver historial de moderación (en paso 4)**
- 4.1. El admin presiona "Historial"
- 4.2. El sistema muestra lista de acciones de moderación:
   - Mensajes eliminados
   - Usuarios advertidos
   - Usuarios suspendidos
   - Admin responsable
   - Fecha y hora
- 4.3. El admin puede filtrar por fecha, usuario o admin
- 4.4. Retorna al paso 4

### Flujos de Excepción

**FE-01: Sin permisos (en paso 2)**
- 2.1. El sistema detecta que el usuario no tiene permisos de moderación
- 2.2. El sistema muestra mensaje: "Acceso denegado"
- 2.3. El sistema redirige al dashboard
- 2.4. Fin del caso de uso

**FE-02: Mensaje ya eliminado (en FA-01.4)**
- 4.1. El sistema detecta que el mensaje ya fue eliminado
- 4.2. El sistema muestra mensaje: "Este mensaje ya no existe"
- 4.3. El sistema actualiza la vista
- 4.4. Retorna al paso 4

---

## Resumen de Casos de Uso

| ID | Caso de Uso | Actor | Complejidad | Prioridad |
|---|---|---|---|---|
| CU-01 | Registro de Usuario | Nuevo Usuario | Media | Alta |
| CU-02 | Iniciar Sesión | Miembro/Admin | Baja | Alta |
| CU-03 | Registrar Inventario | Miembro | Alta | Alta |
| CU-04 | Consultar Historial | Miembro | Media | Media |
| CU-05 | Ver Estadísticas | Miembro | Media | Media |
| CU-06 | Participar en Chat | Miembro | Media | Alta |
| CU-07 | Gestionar Usuarios | Admin | Alta | Media |
| CU-08 | Moderar Chat | Admin | Media | Media |

---

**Versión**: 1.0
**Última actualización**: Diciembre 2024
