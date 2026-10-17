# Build /workspace/ai-news/index.html from data.json + img/*.jpg (run fetch_img.py first)
import base64, html, json
D = "/workspace/ai-news"
items = json.load(open(f"{D}/data.json", encoding="utf-8"))
items.sort(key=lambda x: x["date"], reverse=True)
assert all(x["date"] >= "2026-09-01" for x in items)
N = len(items)
def img(k):
    return "data:image/jpeg;base64," + base64.b64encode(open(f"{D}/img/{k}.jpg", "rb").read()).decode()
e = html.escape
cards = []
for i, it in enumerate(items, 1):
    m, d = it["date"][5:7].lstrip("0"), it["date"][8:10].lstrip("0")
    meta = f'{it["co"]}・{it["types"][0]}・{m}/{d}'
    tags = " ".join("#co-" + c for c in it["cos"]) + " " + " ".join("#ty-" + t for t in it["types"])
    cards.append(f'<a class="c" href="{e(it["url"])}" target="_blank" rel="noopener" data-date="{it["date"]}"><img src="{img(it["id"])}" alt="{e(it["title"])}" loading="lazy"><div class="t"><div class="n">{i}. {e(it["title"])}</div><div class="m">{e(meta)}</div><p>{e(it["intro"])}</p><span class="k">{e(tags)} {e(it["co"])} {e(it["kw"])} {it["date"]}</span></div></a>')
cos = [("全部", "")] + [(c, "#co-" + c) for c in ["OpenAI", "Google", "Anthropic", "Meta", "Microsoft", "Apple", "Amazon", "NVIDIA", "xAI", "中國大廠", "其他"]]
tys = [("不限類型", "")] + [(t, "#ty-" + t) for t in ["模型", "產品", "價格方案", "投資合作", "晶片", "政策"]]
cb = "".join(f'<button data-k="{e(k)}"{" class=on" if not k else ""}>{e(n)}</button>' for n, k in cos)
pb = "".join(f'<button data-p="{e(k)}"{" class=on" if not k else ""}>{e(n)}</button>' for n, k in tys)
CSS = '''body{margin:0;font-family:-apple-system,"PingFang TC","Noto Sans TC",sans-serif;background:#111;color:#eee}h1{font-size:22px;padding:20px 16px 4px;margin:0}.s{color:#999;padding:0 16px 12px;font-size:13px}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;padding:0 16px 24px}.c{background:#1c1c1c;border-radius:12px;overflow:hidden;text-decoration:none;color:inherit;display:block}
.c img{width:100%;height:200px;object-fit:cover;display:block;background:#000}.t{padding:10px 12px 14px}.n{font-weight:700;font-size:16px}.m{color:#f5a623;font-size:12px;margin:4px 0}p{margin:6px 0 0;font-size:14px;line-height:1.5;color:#ccc}.k{display:none}.f{position:sticky;top:0;z-index:5;background:#111;display:flex;flex-wrap:wrap;gap:8px;padding:10px 16px 12px;border-bottom:1px solid #222;margin-bottom:12px}.f button{background:#1c1c1c;color:#ddd;border:1px solid #333;border-radius:999px;padding:6px 14px;font-size:14px;cursor:pointer;font-family:inherit}.f button:hover{border-color:#666}.f button.on{background:#f5a623;color:#111;border-color:#f5a623;font-weight:700}.f .pr{flex-basis:100%;display:flex;flex-wrap:wrap;gap:8px}.f .pr button.on{background:#3a8f5c;border-color:#3a8f5c;color:#fff}.f .cnt{color:#888;font-size:13px;align-self:center;margin-left:4px}.c.h{display:none}.sb{flex-basis:100%;display:flex;gap:8px;margin-bottom:2px}.sb input{flex:1;min-width:0;background:#1c1c1c;color:#eee;border:1px solid #333;border-radius:10px;padding:9px 12px;font-size:16px;font-family:inherit}.sb input:focus{outline:none;border-color:#f5a623}.sb button{flex:none}#em{display:none;color:#888;text-align:center;padding:30px 16px}'''
JS = '''(function(){var bs=document.querySelectorAll('#f button[data-k]'),ps=document.querySelectorAll('#f button[data-p]'),cs=document.querySelectorAll('.c'),cnt=document.getElementById('cnt'),q=document.getElementById('q'),em=document.getElementById('em'),cat='',typ='';
function run(){var ts=q.value.trim().toLowerCase().split(/\\s+/).filter(Boolean),n=0;
cs.forEach(function(c){var k=c.querySelector('.k').textContent,t=(c.querySelector('.t').textContent+' '+c.href).toLowerCase();var ok=(!cat||k.indexOf(cat+' ')>=0)&&(!typ||k.indexOf(typ+' ')>=0)&&ts.every(function(w){return t.indexOf(w)>=0});c.classList.toggle('h',!ok);if(ok)n++});
cnt.textContent=n+' 則';em.style.display=n?'none':'block';}
bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.classList.remove('on')});b.classList.add('on');cat=b.dataset.k;run();});});
ps.forEach(function(b){b.addEventListener('click',function(){ps.forEach(function(x){x.classList.remove('on')});b.classList.add('on');typ=b.dataset.p;run();});});
q.addEventListener('input',run);document.getElementById('qc').addEventListener('click',function(){q.value='';run();q.focus();});})();'''
H = f'''<!DOCTYPE html><html lang="zh-Hant-TW"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>大廠 AI 消息 {N} 則 2026-10-17</title><style>
{CSS}</style></head>
<body><h1>大廠 AI 消息 {N} 則</h1><div class="s">2026-10-17 更新・只收 2026 年 9 月以後・點卡片看原始報導</div><div class="f" id="f"><div class="sb"><input id="q" type="search" placeholder="搜尋公司、模型、關鍵字（例：GPT-6、Claude、降價、台灣）" autocomplete="off"><button id="qc" type="button">清除</button></div>{cb}<div class="pr">{pb}<span class="cnt" id="cnt">{N} 則</span></div></div><div id="em">找不到符合的消息，換個關鍵字試試</div><div class="g">{"".join(cards)}</div><script>
{JS}
</script></body></html>'''
open(f"{D}/index.html", "w", encoding="utf-8").write(H)
print(N, len(H))
