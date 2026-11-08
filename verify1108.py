from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--headless=new"])
    pg=b.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: m.type=='error' and errs.append(m.text))
    pg.goto('file:///workspace/ai-news-site/index.html'); pg.wait_for_timeout(1500)
    print('cards',len(pg.query_selector_all('.c')),pg.title())
    print([pg.inner_text('.c:nth-child(%d) .n'%i)[:50] for i in range(1,6)])
    vis=lambda: pg.evaluate("document.querySelectorAll('.c:not(.h)').length")
    for sel in pg.query_selector_all('#f button')[:3]: print(sel.inner_text())
    bs=pg.query_selector_all('#f button[data-k]');
    for bt in bs[1:3]: bt.click(); print(bt.inner_text(),vis())
    bs[0].click()
    for q in ['SpaceXSI','Antigravity 2.29','做夢','勉強','Data Cloud','Kimi K3.1','Copilot Chat','ThinkingBox','Cosmos 3','Box Context']:
        pg.fill('#q',q); pg.wait_for_timeout(200); print('search',q,vis())
    pg.fill('#q',''); pg.wait_for_timeout(200); print('all',vis())
    c=pg.locator('.c').first; c.locator('.ni').click(); print('checked',c.locator('.nic').is_checked(),pg.inner_text('#nib'))
    print('errors',errs); b.close()
