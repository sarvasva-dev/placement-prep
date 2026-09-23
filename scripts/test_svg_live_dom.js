import { chromium } from 'playwright';
import fs from 'fs';

const TEST_DAYS = [
  { day: 1, name: 'Herbert Simon 4-Phase Model', expectedText: '1. INTELLIGENCE' },
  { day: 2, name: '3-Tier DSS Architecture', expectedText: 'DATA SUBSYSTEM' },
  { day: 3, name: 'JVM Architecture', expectedText: 'CLASSLOADER' },
  { day: 4, name: 'OSI 7-Layer Reference Model', expectedText: 'LAYER 7' },
  { day: 5, name: 'Bisection Method', expectedText: 'BISECTION' },
  { day: 6, name: 'Java Thread Lifecycle', expectedText: 'RUNNABLE' },
  { day: 7, name: 'Nonaka SECI Spiral', expectedText: 'SOCIALIZATION' },
  { day: 8, name: 'Java Exception Hierarchy', expectedText: 'THROWABLE' },
  { day: 9, name: 'TCP/IP Architecture', expectedText: 'TCP/IP' },
  { day: 10, name: 'Newton-Raphson Method', expectedText: 'NEWTON-RAPHSON' },
  { day: 11, name: 'Data Warehouse 3-Tier Architecture', expectedText: 'WAREHOUSE' },
  { day: 12, name: 'Collections Hierarchy', expectedText: 'COLLECTION' },
  { day: 13, name: 'CRC Polynomial Division', expectedText: 'CRC' },
  { day: 14, name: 'JDBC Architecture', expectedText: 'JDBC' },
  { day: 15, name: 'Gauss Elimination', expectedText: 'GAUSS' }
];

(async () => {
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const results = [];

  for (const test of TEST_DAYS) {
    console.log(`Testing Day ${test.day}: ${test.name}...`);
    await page.goto(`http://localhost:3000/#day/${test.day}`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(600);

    const check = await page.evaluate((expected) => {
      const acadSec = document.getElementById('sec-acad');
      if (!acadSec) return { error: 'sec-acad not found' };
      const svg = acadSec.querySelector('svg');
      const diagramBox = acadSec.querySelector('.diagram-box');
      const pre = acadSec.querySelector('pre.diagram-box, pre:not(.code-pre)');

      if (!svg) return { error: 'No SVG element in #sec-acad' };
      const box = svg.getBoundingClientRect();
      const rectCount = svg.querySelectorAll('rect').length;
      const pathCount = svg.querySelectorAll('path').length;
      const lineCount = svg.querySelectorAll('line').length;
      const textContent = svg.textContent;

      return {
        hasSvg: true,
        hasDiagramBox: !!diagramBox,
        hasPre: !!pre,
        width: box.width,
        height: box.height,
        viewBox: svg.getAttribute('viewBox'),
        rectCount,
        pathCount,
        lineCount,
        containsExpectedText: textContent.includes(expected),
        containsAsciiArt: textContent.includes('+---') || textContent.includes('+===')
      };
    }, test.expectedText);

    const passed = check.hasSvg && !check.hasDiagramBox && !check.hasPre && 
                   check.width > 0 && check.height > 0 && 
                   (check.rectCount > 0 || check.pathCount > 0) &&
                   !check.containsAsciiArt;

    results.push({
      day: test.day,
      name: test.name,
      passed,
      check
    });

    console.log(`  -> Day ${test.day}: ${passed ? 'PASS' : 'FAIL'} (w: ${check.width}px, h: ${check.height}px, rects: ${check.rectCount}, paths: ${check.pathCount}, ascii: ${check.containsAsciiArt})`);
  }

  await browser.close();

  fs.writeFileSync('evidence/live_browser_dom_report.json', JSON.stringify({
    timestamp: new Date().toISOString(),
    totalTested: results.length,
    allPassed: results.every(r => r.passed),
    results
  }, null, 2));

  console.log('\nReport written to evidence/live_browser_dom_report.json');
})();
