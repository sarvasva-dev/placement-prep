import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    
    # Listen to console
    page.on('console', lambda msg: print(f"CONSOLE: {msg.text}"))
    page.on('pageerror', lambda err: print(f"PAGE ERROR: {err}"))
    
    print("--- TEST 1: Direct navigation to http://localhost:8000/#day/1#sec-pyq ---")
    page.goto('http://localhost:8000/#day/1#sec-pyq')
    page.wait_for_timeout(1000)
    
    scroll_1 = page.evaluate('() => window.pageYOffset || document.documentElement.scrollTop')
    active_1 = page.locator('.day-toc-bar .tab-btn.active').inner_text().strip()
    box_pyq = page.locator('#sec-pyq').bounding_box()
    print(f"Scroll Y: {scroll_1}")
    print(f"Active Tab: '{active_1}'")
    print(f"#sec-pyq relative Y to viewport: {box_pyq['y']}")
    
    assert scroll_1 > 2000, f"Expected scroll_1 > 2000, got {scroll_1}"
    assert "University PYQ" in active_1, f"Expected active tab to be University PYQs, got {active_1}"
    assert 70 <= box_pyq['y'] <= 250, f"Expected #sec-pyq to be positioned visibly below sticky headers (70-250px), got {box_pyq['y']}"
    print(">>> TEST 1 PASSED!\n")
    
    print("--- TEST 2: Click all 14 TOC buttons in Day 1 sequentially ---")
    toc_btns = page.locator('.day-toc-bar .tab-btn')
    btn_count = toc_btns.count()
    print(f"Found {btn_count} TOC buttons.")
    
    for i in range(btn_count):
        btn = toc_btns.nth(i)
        btn_text = btn.inner_text().strip()
        target = btn.get_attribute('data-target')
        
        btn.click()
        page.wait_for_timeout(400)
        
        scroll_pos = page.evaluate('() => window.pageYOffset || document.documentElement.scrollTop')
        active_tab = page.locator('.day-toc-bar .tab-btn.active').inner_text().strip()
        target_el = page.locator(f"#{target}")
        tbox = target_el.bounding_box()
        
        print(f"  [{i:2d}] Clicked '{btn_text}' -> Scroll Y: {scroll_pos:5.0f} | Active: '{active_tab[:22]}' | Target Y: {tbox['y']:5.1f}")
        assert active_tab == btn_text, f"Expected active tab '{btn_text}', got '{active_tab}'"
        
    print(">>> TEST 2 PASSED!\n")
    
    print("--- TEST 3: In-place hash change from #sec-pyq to #sec-coding-probs ---")
    page.evaluate("() => window.location.hash = '#day/1#sec-coding-probs'")
    page.wait_for_timeout(500)
    scroll_3 = page.evaluate('() => window.pageYOffset || document.documentElement.scrollTop')
    active_3 = page.locator('.day-toc-bar .tab-btn.active').inner_text().strip()
    print(f"Scroll Y: {scroll_3}, Active Tab: '{active_3}'")
    assert "Coding Problems" in active_3, f"Expected Coding Problems, got {active_3}"
    print(">>> TEST 3 PASSED!\n")
    
    print("--- TEST 4: Navigation to Day 2 and section jumping ---")
    page.goto('http://localhost:8000/#day/2#sec-dsa-pattern')
    page.wait_for_timeout(1000)
    scroll_4 = page.evaluate('() => window.pageYOffset || document.documentElement.scrollTop')
    active_4 = page.locator('.day-toc-bar .tab-btn.active').inner_text().strip()
    print(f"Day 2 Scroll Y: {scroll_4}, Active Tab: '{active_4}'")
    assert "DSA Pattern" in active_4, f"Expected DSA Pattern on Day 2, got {active_4}"
    print(">>> TEST 4 PASSED!\n")

    # Take screenshot of Day 1 at #sec-pyq
    page.goto('http://localhost:8000/#day/1#sec-pyq')
    page.wait_for_timeout(1000)
    page.screenshot(path='evidence/screenshots/day_01_sec_pyq_repaired.png')
    print("Saved evidence screenshot: evidence/screenshots/day_01_sec_pyq_repaired.png")

    browser.close()
