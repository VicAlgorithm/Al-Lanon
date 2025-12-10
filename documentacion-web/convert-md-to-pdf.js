const markdownpdf = require("markdown-pdf");
const fs = require("fs");
const path = require("path");

// Lista de archivos markdown a convertir
const markdownFiles = [
    "Documento-Requisitos.md",
    "Descripcion-Casos-Uso.md",
    "Manual-Usuario.md"
];

// Opciones de configuración para el PDF
const options = {
    paperFormat: "A4",
    paperOrientation: "portrait",
    paperBorder: "2cm",
    cssPath: path.join(__dirname, "assets", "css", "pdf-styles.css")
};

console.log("Iniciando conversión de archivos Markdown a PDF...\n");

// Convertir cada archivo
markdownFiles.forEach((file) => {
    const inputPath = path.join(__dirname, file);
    const outputPath = path.join(__dirname, file.replace(".md", ".pdf"));

    if (!fs.existsSync(inputPath)) {
        console.log(`❌ Error: No se encontró el archivo ${file}`);
        return;
    }

    console.log(`🔄 Convirtiendo: ${file}...`);

    markdownpdf(options)
        .from(inputPath)
        .to(outputPath, function () {
            console.log(`✅ Generado: ${file.replace(".md", ".pdf")}\n`);
        });
});

console.log("Proceso de conversión completado.");
