from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--headless=new"])
    pg=b.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: m.type=='error' and errs.append(m.text))
    pg.goto('file:///workspace/ai-news-site/index.html'); pg.wait_for_timeout(1500)
    print('cards',len(pg.query_selector_all('.c')),pg.title())
    print([pg.inner_text('.c:nth-child(%d) .n'%i)[:60] for i in range(1,6)])
    vis=lambda: pg.evaluate("document.querySelectorAll('.c:not(.h)').length")
    for q in ['Web Search API','Fable 5.2','AWS Marketplace','阿布達比','GR00T 2','TPU 8tx','Instagram 年齡','記憶摘要','Rebellions','Astra 暗中']:
        pg.fill('#q',q); pg.wait_for_timeout(200); print('search',q,vis())
    pg.fill('#q',''); pg.wait_for_timeout(200); print('all',vis())
    c=pg.locator('.c').first; c.locator('.ni').click(); print('checked',c.locator('.nic').is_checked(),pg.inner_text('#nib'))
    print('errors',errs); b.close()
