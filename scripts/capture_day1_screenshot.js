import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';

(async () => {
  fs.mkdirSync('evidence/screenshots', { recursive: true });
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 1000 } });
  
  await page.goto('http://localhost:3000/#day/1', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  // Locate the architecture SVG wrapper inside the academic section
  const acadSec = await page.$('#sec-acad');
  const diagWrapper = acadSec ? await acadSec.$('.svg-diagram-wrapper') : null;
  
  if (diagWrapper) {
    await diagWrapper.scrollIntoViewIfNeeded();
    await page.waitForTimeout(500);
    await diagWrapper.screenshot({ path: 'evidence/screenshots/day01-simon-svg-element.png' });
    console.log('Saved element screenshot: evidence/screenshots/day01-simon-svg-element.png');
  }

  // Also take full screenshot with the diagram in view
  await page.screenshot({ path: 'evidence/screenshots/day01-svg-browser.png' });
  console.log('Saved page screenshot: evidence/screenshots/day01-svg-browser.png');

  await browser.close();
})();
