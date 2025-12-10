const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    console.log('Iniciando generación de diagrama de Gantt...');

    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // Set viewport to wide enough for the gantt chart
    await page.setViewport({ width: 1400, height: 1200 });

    // Navigate to the HTML file
    const htmlPath = 'file://' + path.join(__dirname, 'gantt-chart.html');
    console.log('Cargando HTML desde:', htmlPath);

    await page.goto(htmlPath, { waitUntil: 'networkidle0' });

    // Take screenshot
    const outputPath = path.join(__dirname, 'assets', 'diagramas', 'diagrama-gantt.png');
    await page.screenshot({
        path: outputPath,
        fullPage: true
    });

    console.log('✅ Diagrama de Gantt generado exitosamente:', outputPath);

    await browser.close();
})();
