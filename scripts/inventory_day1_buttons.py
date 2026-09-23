import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.goto('http://localhost:8000/#day/1')
    page.wait_for_timeout(1000)
    
    buttons = page.locator('button')
    print(f"Total buttons found on Day 1: {buttons.count()}")
    for i in range(buttons.count()):
        btn = buttons.nth(i)
        txt = btn.inner_text().strip().replace('\n', ' ')
        cls = btn.get_attribute('class') or ''
        btn_id = btn.get_attribute('id') or ''
        target = btn.get_attribute('data-target') or ''
        print(f"  [{i:3d}] id='{btn_id}' class='{cls}' data-target='{target}' text='{txt[:45]}'")
        
    browser.close()
