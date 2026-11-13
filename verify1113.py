import sys
from playwright.sync_api import sync_playwright
site=sys.argv[1]; qs=sys.argv[2].split('|')
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--headless=new"])
    pg=b.new_page(); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: m.type=='error' and errs.append(m.text))
    pg.goto(site); pg.wait_for_timeout(1500)
    print('cards',len(pg.query_selector_all('.c')),pg.title())
    print([pg.inner_text('.c:nth-child(%d) .n'%i)[:50] for i in range(1,4)])
    vis=lambda: pg.evaluate("document.querySelectorAll('.c:not(.h)').length")
    for q in qs:
        pg.fill('#q',q); pg.wait_for_timeout(150); print('search',q,vis())
    pg.fill('#q',''); pg.wait_for_timeout(150); print('all',vis())
    bs=pg.query_selector_all('#f button[data-k]')
    for bt in bs[1:4]:
        bt.click(); pg.wait_for_timeout(150); print('filter',bt.inner_text(),vis())
    bs[0].click()
    c=pg.locator('.c').first; c.locator('.ni').click(); print('checked',c.locator('.nic').is_checked(),pg.inner_text('#nib'))
    c.locator('.ni').click()
    print('errors',errs); b.close()
