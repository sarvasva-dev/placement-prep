import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    
    page.goto('http://localhost:8000/#day/1')
    page.wait_for_timeout(1000)
    
    btn_pyq = page.locator('.day-toc-bar .tab-btn:has-text("2. University PYQs")')
    print("Clicking '2. University PYQs'...")
    btn_pyq.click()
    
    # Sample scroll position and active button every 200ms for 3 seconds
    for t in range(15):
        page.wait_for_timeout(200)
        s = page.evaluate('() => window.pageYOffset || document.documentElement.scrollTop')
        act = page.locator('.day-toc-bar .tab-btn.active').inner_text().strip()
        print(f"Time +{(t+1)*200}ms -> Scroll Y: {s}, Active Tab: '{act}'")
        
    browser.close()
