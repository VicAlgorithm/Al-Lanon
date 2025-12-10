# Diagramas UML

Esta carpeta contiene los diagramas UML del proyecto Inventario Emocional.

## 📁 Archivos Esperados

### Diagrama de Casos de Uso
- **Nombre:** `diagrama-casos-uso.png`
- **Descripción:** Diagrama que muestra los actores (Miembro y Administrador) y sus casos de uso asociados
- **Formato recomendado:** PNG, JPG o SVG
- **Tamaño recomendado:** 1200px de ancho mínimo para buena calidad

### Diagramas de Secuencia

Cada diagrama debe mostrar el flujo de interacciones entre objetos para un caso de uso específico:

1. **secuencia-registro.png** - Proceso de registro de un nuevo usuario
2. **secuencia-login.png** - Proceso de inicio de sesión (miembro/admin)
3. **secuencia-inventario.png** - Proceso de registro del inventario emocional
4. **secuencia-historial.png** - Consulta de inventarios anteriores
5. **secuencia-chat.png** - Comunicación en tiempo real en el chat
6. **secuencia-admin.png** - Operaciones administrativas de gestión de usuarios

## 🎨 Recomendaciones

### Herramientas para Crear Diagramas UML
- **PlantUML** - Diagramas desde código
- **Draw.io / diagrams.net** - Editor visual online
- **Lucidchart** - Herramienta profesional
- **Visual Paradigm** - Suite completa de UML
- **StarUML** - Software de escritorio

### Estilo Visual
- Usa colores consistentes con la paleta de Al-Anon:
  - Azul principal: `#436B8B`
  - Azul secundario: `#5B8AAF`
- Fuente clara y legible (Arial, Helvetica)
- Fondo blanco o transparente
- Bordes definidos para mejor visibilidad

### Formato de Imágenes
- **Formato:** PNG con fondo transparente o blanco (preferido)
- **Resolución:** Mínimo 1200px de ancho
- **DPI:** 150-300 para impresión de calidad
- **Peso:** Optimizar para web (< 500KB por imagen)

## 🔧 Cómo Implementar los Diagramas

Una vez que tengas tus imágenes listas:

1. **Guarda las imágenes** en esta carpeta siguiendo la nomenclatura exacta indicada arriba
2. **Edita el archivo HTML** (`documentacion-web/index.html`)
3. **Busca las secciones comentadas** que dicen:
   ```html
   <!-- Cuando tengas el diagrama, descomenta:
   <img src="assets/diagramas/[nombre-archivo].png" alt="..." class="diagram-image">
   -->
   ```
4. **Descomenta las líneas** de imagen y **elimina** el `<div class="diagram-placeholder">`

### Ejemplo de Cambio:

**Antes:**
```html
<div class="diagram-placeholder">
    <i class="fas fa-image"></i>
    <p>Diagrama de Casos de Uso</p>
    <span class="placeholder-text">Coloca tu imagen en: ...</span>
</div>
<!-- Cuando tengas el diagrama, descomenta:
<img src="assets/diagramas/diagrama-casos-uso.png" alt="Diagrama de Casos de Uso" class="diagram-image">
-->
```

**Después:**
```html
<img src="assets/diagramas/diagrama-casos-uso.png" alt="Diagrama de Casos de Uso" class="diagram-image">
```

## ✅ Checklist

- [ ] Diagrama de Casos de Uso completo
- [ ] Diagrama de Secuencia: Registro de Usuario
- [ ] Diagrama de Secuencia: Iniciar Sesión
- [ ] Diagrama de Secuencia: Registrar Inventario
- [ ] Diagrama de Secuencia: Consultar Historial
- [ ] Diagrama de Secuencia: Chat en Tiempo Real
- [ ] Diagrama de Secuencia: Gestionar Usuarios (Admin)
- [ ] Todos los diagramas están optimizados para web
- [ ] Se actualizó el HTML para mostrar las imágenes

---

**Nota:** Los placeholders actuales muestran visualmente dónde irán los diagramas, facilitando la maquetación de la documentación mientras se crean los diagramas UML.
