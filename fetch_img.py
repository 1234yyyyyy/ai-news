# Download og:image for each item in data.json -> img/<id>.jpg (480px wide). Placeholder if none.
import json, re, html, hashlib, os, subprocess, io, sys
from PIL import Image, ImageDraw, ImageFont
D = "/workspace/ai-news"; UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
os.makedirs(f"{D}/img", exist_ok=True); os.makedirs(f"{D}/raw/pages", exist_ok=True)
items = json.load(open(f"{D}/data.json"))
COLORS = {"OpenAI":"#10a37f","Google":"#4285f4","Anthropic":"#d97757","Meta":"#0866ff","Microsoft":"#00a4ef","Apple":"#888888","Amazon":"#ff9900","NVIDIA":"#76b900","xAI":"#444444","中國大廠":"#d0312d","其他":"#8e44ad"}
FONT = [f for f in ["/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc","/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"] if os.path.exists(f)][0]
def page(url):
    fn = f"{D}/raw/pages/{hashlib.md5(url.encode()).hexdigest()[:10]}.html"
    if not os.path.exists(fn) or os.path.getsize(fn) < 1000:
        subprocess.run(["curl","-sL","-m","30","-A",UA,"-o",fn,url])
    return open(fn, errors="ignore").read() if os.path.exists(fn) else ""
def og(s, base):
    m = re.search(r'<meta[^>]+(?:property|name)="og:image"[^>]+content="([^"]+)"', s) or re.search(r'<meta[^>]+content="([^"]+)"[^>]+(?:property|name)="og:image"', s)
    if not m: return None
    u = html.unescape(m.group(1))
    if u.startswith("//"): u = "https:" + u
    if u.startswith("/"): u = re.match(r"https?://[^/]+", base).group(0) + u
    return u
def placeholder(it, out):
    col = COLORS.get(it["cos"][0], "#555")
    im = Image.new("RGB", (480, 270), col); d = ImageDraw.Draw(im)
    f1 = ImageFont.truetype(FONT, 46); f2 = ImageFont.truetype(FONT, 20)
    t = it["co"]; w = d.textlength(t, font=f1); d.text(((480-w)/2, 95), t, font=f1, fill="white")
    s = "AI 消息"; w2 = d.textlength(s, font=f2); d.text(((480-w2)/2, 165), s, font=f2, fill="#ffffffcc")
    im.save(out, "JPEG", quality=82)
force = "--force" in sys.argv
for it in items:
    out = f"{D}/img/{it['id']}.jpg"
    if os.path.exists(out) and not force: continue
    u = None if it.get("noOg") else og(page(it["url"]), it["url"]); ok = False
    if u:
        r = subprocess.run(["curl","-sL","-m","30","-A",UA,u], capture_output=True)
        try:
            im = Image.open(io.BytesIO(r.stdout)); im.load()
            if im.mode in ("RGBA","LA","P"):
                im = im.convert("RGBA"); bg = Image.new("RGB", im.size, (0,0,0)); bg.paste(im, mask=im.split()[-1]); im = bg
            im = im.convert("RGB")
            if im.width > 480: im = im.resize((480, round(im.height*480/im.width)), Image.LANCZOS)
            if im.width >= 200: im.save(out, "JPEG", quality=80, optimize=True); ok = True
        except Exception as e:
            print("  img fail", it["id"], e)
    if not ok: placeholder(it, out)
    print(("OG " if ok else "PH ") + it["id"], u or "")
