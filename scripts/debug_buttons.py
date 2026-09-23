import sys
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    
    # 1. Listen for console messages and errors
    page.on('console', lambda msg: print(f"BROWSER CONSOLE [{msg.type}]: {msg.text}"))
    page.on('pageerror', lambda err: print(f"BROWSER PAGE ERROR: {err}"))
    
    print("Navigating to http://localhost:8000/#day/1#sec-pyq...")
    sys.stdout.flush()
    page.goto('http://localhost:8000/#day/1#sec-pyq')
    page.wait_for_timeout(1500)
    
    print("URL in browser:", page.url)
    scroll_init = page.evaluate('() => window.pageYOffset || document.documentElement.scrollTop')
    print("Scroll Y initially:", scroll_init)
    
    btn_pyq = page.locator('.day-toc-bar .tab-btn:has-text("2. University PYQs")')
    print("Is 2. University PYQs visible?", btn_pyq.is_visible())
    
    print("Clicking 2. University PYQs...")
    sys.stdout.flush()
    btn_pyq.click()
    page.wait_for_timeout(1000)
    
    scroll_after = page.evaluate('() => window.pageYOffset || document.documentElement.scrollTop')
    print("Scroll Y after click:", scroll_after)
    active_after = page.locator('.day-toc-bar .tab-btn.active').inner_text().strip()
    print("Active button:", active_after)
    
    browser.close()
