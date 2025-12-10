# Documentación Web - Inventario Emocional App

![Al-Anon Logo](assets/Logo.png)

Esta carpeta contiene la documentación completa del proyecto **Inventario Emocional** en formato de página web, diseñada con la identidad visual de **Al-Anon**.

## 📁 Estructura de Archivos

```
documentacion-web/
│
├── index.html                  # Página principal de documentación
├── README.md                   # Este archivo
│
├── assets/
│   ├── Logo.png                # Logo oficial de Al-Anon
│   ├── css/
│   │   └── styles.css          # Estilos con paleta de colores Al-Anon
│   └── js/
│       └── script.js           # Funcionalidad interactiva
│
├── casos-de-uso-markdown/      # Archivos markdown originales
│   └── [archivos .md]
│
└── casos-de-uso-pdf/           # PDFs de casos de uso
    ├── CU-01-Registro-Usuario.pdf
    ├── CU-02-Iniciar-Sesion.pdf
    ├── CU-03-Registrar-Inventario.pdf
    ├── CU-04-Consultar-Historial.pdf
    ├── CU-05-Ver-Estadisticas.pdf
    ├── CU-06-Chat-General.pdf
    ├── CU-07-Gestionar-Usuarios.pdf
    ├── CU-08-Moderar-Chat.pdf
    └── README.pdf
```

## 🚀 Cómo usar la documentación

### Opción 1: Abrir directamente en el navegador

1. Navega a la carpeta `documentacion-web`
2. Haz doble clic en `index.html`
3. Se abrirá automáticamente en tu navegador predeterminado

### Opción 2: Usar un servidor local (recomendado)

Para una mejor experiencia, especialmente si vas a agregar los PDFs:

**Con Python:**
```bash
cd documentacion-web
python -m http.server 8000
```

Luego abre en tu navegador: `http://localhost:8000`

**Con Node.js (npx):**
```bash
cd documentacion-web
npx serve
```

**Con VS Code:**
- Instala la extensión "Live Server"
- Click derecho en `index.html` → "Open with Live Server"

## 📄 PDFs de Casos de Uso

✅ **Todos los PDFs ya están generados y listos para usar**

Los archivos están ubicados en `casos-de-uso-pdf/` y son accesibles directamente desde la página web haciendo clic en "Ver PDF" en la tabla de casos de uso.

## ✨ Características de la Documentación

- ✅ **Identidad visual de Al-Anon**: Logo y paleta de colores oficial
- ✅ Diseño moderno y responsive (se adapta a móviles)
- ✅ Navegación suave entre secciones con efecto sticky
- ✅ 8 PDFs de casos de uso integrados y accesibles
- ✅ Secciones completas:
  - Descripción general del proyecto
  - Arquitectura del sistema (MVC)
  - Funcionalidades principales con iconos
  - Requisitos funcionales y no funcionales
  - Casos de uso detallados con enlaces directos a PDFs
  - Tecnologías utilizadas
  - Guía de instalación paso a paso
- ✅ Botón para copiar código de snippets
- ✅ Botón "volver arriba" flotante
- ✅ Animaciones suaves al hacer scroll
- ✅ Footer con branding de Al-Anon

## 🎨 Personalización

### Paleta de colores Al-Anon

La página usa la paleta oficial de Al-Anon definida en `assets/css/styles.css`:

```css
:root {
    --primary-color: #436B8B;      /* Azul principal de Al-Anon */
    --secondary-color: #5B8AAF;    /* Azul más claro */
    --accent-color: #E8E4D9;       /* Beige/crema del logo */
    --dark-blue: #2C4A61;          /* Azul oscuro */
    --success-color: #27ae60;      /* Verde para confirmaciones */
}
```

Si necesitas personalizar los colores, edita estas variables en `assets/css/styles.css`.

### Agregar más secciones

Añade nuevas secciones en `index.html` siguiendo la estructura:

```html
<section id="nueva-seccion" class="section">
    <div class="container">
        <h2 class="section-title">Título de la Sección</h2>
        <div class="content-card">
            <!-- Tu contenido aquí -->
        </div>
    </div>
</section>
```

No olvides agregar el enlace en el menú de navegación.

## 📱 Compatibilidad

- ✅ Chrome, Firefox, Safari, Edge (últimas versiones)
- ✅ Dispositivos móviles (responsive)
- ✅ Tablets
- ✅ Impresión (Ctrl+P para imprimir documentación)

## 💡 Notas Importantes

1. **PDFs de Casos de Uso**: Los enlaces apuntan a la carpeta `casos-de-uso/`. Asegúrate de que tus PDFs estén allí con los nombres correctos.

2. **Independencia**: Esta carpeta es completamente independiente del proyecto principal. Puedes compartirla, hospedarla en web, o enviarla sin incluir el código fuente.

3. **Sin dependencias externas pesadas**: Solo usa Font Awesome desde CDN para los iconos. Todo lo demás está incluido.

## 🌐 Publicar en línea

Puedes publicar esta documentación en:

- **GitHub Pages**: Sube a un repositorio y activa GitHub Pages
- **Netlify**: Arrastra la carpeta al panel de Netlify
- **Vercel**: Deploy automático desde repositorio
- **Cualquier hosting web**: Sube los archivos via FTP

## 📞 Soporte

Si necesitas ayuda para personalizar la documentación o agregar nuevas secciones, consulta los comentarios en los archivos CSS y JavaScript.

---

**Creado para el proyecto Inventario Emocional - Al-Anon**
