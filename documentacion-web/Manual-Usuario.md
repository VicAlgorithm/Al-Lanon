# Manual de Usuario
## Inventario Emocional - Al-Anon

---

![Al-Anon Logo](assets/Logo.png)

**Versión**: 1.0
**Fecha**: Diciembre 2024
**Destinado a**: Miembros y Administradores de Al-Anon

---

## Tabla de Contenido

1. [Introducción](#introducción)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Inicio de Sesión](#inicio-de-sesión)
5. [Funciones para Miembros](#funciones-para-miembros)
6. [Funciones para Administradores](#funciones-para-administradores)
7. [Preguntas Frecuentes](#preguntas-frecuentes)
8. [Soporte](#soporte)

---

## Introducción

Bienvenido a **Inventario Emocional**, la aplicación móvil diseñada específicamente para miembros de Al-Anon. Esta herramienta te permite:

- Registrar tu inventario emocional diario de manera estructurada
- Consultar tu historial de registros
- Visualizar patrones y tendencias emocionales
- Conectar con otros miembros a través del chat grupal
- Llevar un seguimiento de tu proceso de recuperación

### ¿Qué es un Inventario Emocional?

El inventario emocional es una práctica fundamental en Al-Anon que consiste en registrar:
- **Resentimientos**: Personas o situaciones que nos han afectado
- **Defectos de carácter**: Comportamientos propios que queremos mejorar
- **Miedos**: Temores que nos limitan
- **Responsabilidades**: Nuestra parte en las situaciones

---

## Requisitos del Sistema

### Dispositivos Compatibles
- **Android**: Versión 8.0 (Oreo) o superior
- **iOS**: Versión 12 o superior
- **Tablets**: Compatible con diseño responsive

### Requisitos Adicionales
- Conexión a Internet (WiFi o datos móviles)
- Al menos 100 MB de espacio disponible
- Pantalla mínima de 4.5 pulgadas recomendada

---

## Instalación

### Opción 1: Instalación desde Archivo APK (Android)

1. Descarga el archivo `InventarioEmocional.apk`
2. En tu dispositivo Android, ve a **Configuración > Seguridad**
3. Activa la opción **"Fuentes desconocidas"** o **"Instalar aplicaciones desconocidas"**
4. Abre el archivo APK descargado
5. Toca **"Instalar"**
6. Espera a que la instalación se complete
7. Toca **"Abrir"** para iniciar la aplicación

### Opción 2: Instalación desde Código Fuente

Si tienes acceso al código fuente:

```bash
# Clonar repositorio
git clone <URL_REPOSITORIO>
cd AppAlanon

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python main.py
```

---

## Inicio de Sesión

### Primera Vez - Registro de Usuario

1. Abre la aplicación
2. En la pantalla de bienvenida, toca **"Registrarse"**
3. Completa el formulario:
   - **Nombre completo**: Tu nombre real o apodo
   - **Correo electrónico**: Un email válido (será tu usuario)
   - **Contraseña**: Mínimo 8 caracteres
   - **Confirmar contraseña**: Repite la contraseña
4. Toca **"Crear cuenta"**
5. Recibirás un mensaje de confirmación
6. Serás redirigido automáticamente a la pantalla de login

### Iniciar Sesión - Miembro

1. En la pantalla de bienvenida, toca **"Iniciar Sesión como Miembro"**
2. Ingresa tu **correo electrónico**
3. Ingresa tu **contraseña**
4. Toca **"Entrar"**
5. Accederás al Dashboard de Miembro

### Iniciar Sesión - Administrador

1. En la pantalla de bienvenida, toca **"Iniciar Sesión como Admin"**
2. Ingresa las credenciales de administrador
3. Toca **"Entrar"**
4. Accederás al Dashboard de Administrador

---

## Funciones para Miembros

### 1. Dashboard Principal

Al iniciar sesión, verás el **Dashboard** con las siguientes opciones:

- **Nuevo Inventario**: Registra un inventario del día
- **Mi Historial**: Consulta inventarios anteriores
- **Estadísticas**: Visualiza gráficos y patrones
- **Chat General**: Comunícate con otros miembros
- **Cerrar Sesión**: Sal de tu cuenta

---

### 2. Registrar Inventario Emocional

#### Paso 1: Acceder al Formulario
- Desde el Dashboard, toca **"Nuevo Inventario"**
- Se abrirá el formulario de inventario

#### Paso 2: Completar Resentimientos
Para cada resentimiento, completa:
1. **Persona o situación**: ¿Quién o qué te molestó?
2. **Causa**: ¿Por qué te molestó?
3. **Afecta a**: ¿Qué parte de ti se vio afectada?
   - Autoestima
   - Seguridad personal
   - Relaciones personales
   - Seguridad emocional
   - Relaciones sexuales

Puedes agregar múltiples resentimientos usando el botón **"+ Agregar Resentimiento"**

#### Paso 3: Identificar Defectos de Carácter
Selecciona los defectos que reconoces en ti:
- Egoísmo
- Deshonestidad
- Miedo
- Inconsideración
- Orgullo
- Envidia
- Pereza
- Ira
- Gula
- Lujuria

También puedes escribir otros que no aparezcan en la lista.

#### Paso 4: Reconocer Miedos
Escribe los miedos que identificas:
- Miedo al rechazo
- Miedo al fracaso
- Miedo a la soledad
- Miedo a perder el control
- Otros miedos personales

#### Paso 5: Parte de Responsabilidad
Reflexiona y escribe tu parte de responsabilidad en la situación:
- ¿Qué pudiste haber hecho diferente?
- ¿Cómo contribuiste a la situación?
- ¿Qué puedes aprender de esto?

#### Paso 6: Guardar
- Toca **"Guardar Inventario"**
- Recibirás un mensaje de confirmación
- El inventario se guardará con la fecha actual

---

### 3. Consultar Historial

#### Ver Todos los Inventarios
1. Desde el Dashboard, toca **"Mi Historial"**
2. Verás una lista de todos tus inventarios ordenados por fecha (más reciente primero)
3. Cada tarjeta muestra:
   - Fecha del inventario
   - Número de resentimientos registrados
   - Resumen breve

#### Filtrar por Fecha
1. En la pantalla de Historial, toca el ícono de **filtro**
2. Selecciona un rango de fechas:
   - Fecha inicio
   - Fecha fin
3. Toca **"Aplicar filtro"**
4. Solo se mostrarán inventarios dentro del rango

#### Ver Detalle Completo
1. Toca sobre cualquier tarjeta de inventario
2. Se abrirá la vista detallada mostrando:
   - Todos los resentimientos
   - Defectos de carácter identificados
   - Miedos reconocidos
   - Reflexión sobre responsabilidad

---

### 4. Ver Estadísticas

#### Acceder a Estadísticas
1. Desde el Dashboard, toca **"Estadísticas"**
2. La pantalla puede tardar unos segundos en cargar los gráficos

#### Gráficos Disponibles

**Gráfico 1: Emociones en el Tiempo**
- Muestra la evolución de tus emociones
- Eje X: Fechas
- Eje Y: Intensidad/Frecuencia
- Útil para identificar patrones

**Gráfico 2: Defectos de Carácter Más Frecuentes**
- Gráfico de barras
- Muestra qué defectos identificas más seguido
- Te ayuda a enfocarte en áreas de mejora

**Gráfico 3: Miedos Recurrentes**
- Gráfico circular
- Porcentaje de cada tipo de miedo
- Identifica tus miedos principales

**Gráfico 4: Resumen del Mes**
- Estadísticas generales del último mes
- Total de inventarios registrados
- Promedio de resentimientos por día
- Tendencias generales

#### Cambiar Período
1. Toca el selector de período (arriba a la derecha)
2. Selecciona:
   - Última semana
   - Último mes
   - Últimos 3 meses
   - Último año
   - Personalizado
3. Los gráficos se actualizarán automáticamente

---

### 5. Chat General

#### Acceder al Chat
1. Desde el Dashboard, toca **"Chat General"**
2. Verás los mensajes recientes de la comunidad

#### Enviar un Mensaje
1. Escribe tu mensaje en el campo de texto (parte inferior)
2. Máximo 500 caracteres por mensaje
3. Toca el botón de **"Enviar"** (ícono de papel)
4. Tu mensaje aparecerá en la conversación

#### Visualizar Mensajes
- Los mensajes se muestran en orden cronológico
- Cada mensaje muestra:
  - Nombre del usuario
  - Contenido del mensaje
  - Hora de envío
- Los mensajes se actualizan en tiempo real

#### Normas del Chat
- Respeta a todos los miembros
- No compartas información personal sensible
- Mantén un lenguaje respetuoso
- Sigue los principios de Al-Anon
- Los administradores pueden moderar mensajes inapropiados

---

### 6. Cerrar Sesión

1. Desde cualquier pantalla, toca el menú (tres líneas)
2. Selecciona **"Cerrar Sesión"**
3. Confirma la acción
4. Serás redirigido a la pantalla de bienvenida

---

## Funciones para Administradores

### 1. Dashboard de Administrador

Al iniciar sesión como administrador, verás:

- **Gestionar Usuarios**: Ver, editar, desactivar usuarios
- **Moderar Chat**: Revisar y eliminar mensajes inapropiados
- **Estadísticas del Sistema**: Ver métricas generales
- **Configuración**: Opciones avanzadas

---

### 2. Gestionar Usuarios

#### Listar Todos los Usuarios
1. Desde el Dashboard Admin, toca **"Gestionar Usuarios"**
2. Verás una tabla con todos los usuarios:
   - ID
   - Nombre
   - Email
   - Fecha de registro
   - Estado (activo/inactivo)

#### Buscar Usuario
1. Usa la barra de búsqueda (parte superior)
2. Puedes buscar por:
   - Nombre
   - Email
   - ID
3. Los resultados se filtran en tiempo real

#### Editar Usuario
1. Toca sobre el usuario que deseas editar
2. Toca el botón **"Editar"**
3. Modifica los campos permitidos:
   - Nombre
   - Email
   - Estado (activo/inactivo)
4. Toca **"Guardar cambios"**
5. Recibirás confirmación

#### Desactivar/Activar Usuario
1. Selecciona un usuario
2. Toca el botón **"Cambiar estado"**
3. Confirma la acción
4. Un usuario inactivo no podrá iniciar sesión

#### Eliminar Usuario
1. Selecciona un usuario
2. Toca el botón **"Eliminar"** (ícono de basura)
3. **ATENCIÓN**: Esta acción es irreversible
4. Confirma la eliminación
5. Se borrarán:
   - La cuenta del usuario
   - Sus inventarios
   - Sus mensajes

---

### 3. Moderar Chat

#### Ver Todos los Mensajes
1. Desde el Dashboard Admin, toca **"Moderar Chat"**
2. Verás todos los mensajes del chat general

#### Eliminar Mensaje Inapropiado
1. Identifica el mensaje inapropiado
2. Toca sobre el mensaje
3. Selecciona **"Eliminar mensaje"**
4. Confirma la acción
5. El mensaje se eliminará para todos los usuarios

#### Advertir a un Usuario
1. Toca sobre el mensaje del usuario
2. Selecciona **"Advertir usuario"**
3. El usuario recibirá una notificación
4. La advertencia queda registrada en el log

#### Ver Historial de Moderación
1. En la pantalla de Moderar Chat
2. Toca **"Historial"** (arriba a la derecha)
3. Verás:
   - Mensajes eliminados
   - Usuarios advertidos
   - Fecha y hora de cada acción
   - Administrador que ejecutó la acción

---

### 4. Estadísticas del Sistema

#### Ver Métricas Generales
1. Desde el Dashboard Admin, toca **"Estadísticas"**
2. Verás:
   - Total de usuarios registrados
   - Usuarios activos (último mes)
   - Total de inventarios registrados
   - Promedio de inventarios por usuario
   - Mensajes enviados en el chat

#### Exportar Reportes
1. En la pantalla de Estadísticas
2. Toca **"Exportar"** (arriba a la derecha)
3. Selecciona formato:
   - PDF
   - CSV
   - Excel
4. El reporte se descargará a tu dispositivo

---

## Preguntas Frecuentes

### Sobre la Cuenta

**P: ¿Puedo cambiar mi correo electrónico?**
R: Actualmente no es posible cambiar el email. Si necesitas hacerlo, contacta a un administrador.

**P: Olvidé mi contraseña, ¿qué hago?**
R: En la pantalla de login, toca "Olvidé mi contraseña" y sigue las instrucciones para recuperarla.

**P: ¿Puedo usar la misma cuenta en varios dispositivos?**
R: Sí, puedes iniciar sesión en múltiples dispositivos con la misma cuenta.

### Sobre los Inventarios

**P: ¿Puedo editar un inventario después de guardarlo?**
R: Actualmente no se pueden editar inventarios guardados. Si cometiste un error, puedes crear uno nuevo.

**P: ¿Cuántos inventarios puedo registrar?**
R: No hay límite. Puedes registrar tantos como necesites.

**P: ¿Puedo eliminar un inventario?**
R: Sí, en la vista de detalle del inventario, toca el ícono de basura y confirma.

### Sobre el Chat

**P: ¿Los mensajes son privados?**
R: No, el chat general es visible para todos los miembros. No compartas información personal sensible.

**P: ¿Puedo enviar mensajes privados?**
R: La versión actual solo incluye chat general. Los mensajes privados están en desarrollo.

**P: ¿Qué pasa si envío un mensaje inapropiado?**
R: Los administradores pueden eliminar el mensaje y advertirte. Reincidencias pueden resultar en suspensión.

### Sobre Privacidad y Seguridad

**P: ¿Mis datos están seguros?**
R: Sí, usamos encriptación para contraseñas y comunicaciones. Tus datos nunca se comparten con terceros.

**P: ¿Quién puede ver mis inventarios?**
R: Solo tú puedes ver tus inventarios. Ni siquiera los administradores tienen acceso.

**P: ¿Puedo exportar mis datos?**
R: Sí, desde la pantalla de Historial, toca "Exportar" para descargar tus inventarios en formato PDF.

### Problemas Técnicos

**P: La aplicación se cierra inesperadamente, ¿qué hago?**
R:
1. Cierra completamente la aplicación
2. Reinicia tu dispositivo
3. Actualiza a la última versión
4. Si persiste, contacta soporte

**P: No carga el chat, ¿qué verifico?**
R:
1. Verifica tu conexión a Internet
2. Cierra y vuelve a abrir la aplicación
3. Verifica que no haya mantenimiento programado

**P: Los gráficos no se ven bien, ¿por qué?**
R: Puede ser que no tengas suficientes inventarios registrados. Se requieren al menos 3 para generar estadísticas.

---

## Soporte

### Contacto
Si tienes problemas técnicos o preguntas que no están cubiertas en este manual:

- **Email de soporte**: soporte@inventarioemocional.com
- **Horario de atención**: Lunes a Viernes, 9:00 AM - 6:00 PM

### Recursos Adicionales
- **Al-Anon**: https://al-anon.org/
- **Documentación técnica**: Ver carpeta `documentacion-web/`
- **Código fuente**: Disponible para desarrolladores

---

## Apéndice

### Principios de Al-Anon

Este sistema está diseñado para apoyar tu trabajo con los principios de Al-Anon:

1. **Admitir nuestra impotencia** ante el alcohol
2. **Creer** en un Poder Superior
3. **Decidir** poner nuestras vidas en manos de Dios
4. **Hacer un inventario moral** de nosotros mismos (esto es lo que facilita la app)
5. **Admitir** nuestros defectos
6. **Estar dispuestos** a que Dios los elimine
7. **Pedir humildemente** que elimine nuestros defectos
8. **Hacer una lista** de personas a quienes hemos dañado
9. **Reparar el daño** causado
10. **Continuar el inventario** personal
11. **Mejorar nuestro contacto** con Dios
12. **Llevar este mensaje** a otros

### Glosario

- **Dashboard**: Pantalla principal con opciones del sistema
- **Inventario**: Registro diario de emociones y reflexiones
- **Resentimiento**: Sentimiento negativo hacia personas o situaciones
- **Defecto de carácter**: Comportamiento propio que queremos mejorar
- **CRUD**: Operaciones básicas (Crear, Leer, Actualizar, Eliminar)

---

**Última actualización**: Diciembre 2024
**Versión del manual**: 1.0
**Versión de la aplicación**: 1.0

---

© 2024 Inventario Emocional - Al-Anon
Este manual es para uso exclusivo de miembros de Al-Anon y con fines educativos.
