# -*- coding: utf-8 -*-
"""
=== Kapitel 4 晶晶體建構工具 ===

使用方式：
1. 在下方 lines 列表中填入您的內容（參考格式說明）
2. 執行: python3 build_k4.py
3. 接著執行: python3 auto_convert.py page6.html

=== 格式說明 ===

D('德文', '中文翻譯')  → 紫色德文詞，hover 顯示中文
C('中文', '德文原文')  → 藍色中文詞，hover 顯示德文
L(...)                 → 一行內容（多個 D/C 組合）
S('標題文字')           → 場景標題
BRK()                  → 分隔線 * * *

重點：
- 只需要用 D() 標記「關鍵內容詞」（名詞、動詞、形容詞等）
- 用 C() 標記您想手動控制的中文詞
- 像 ich, der, und, in, zu 這些虛詞可以不標記，
  auto_convert.py 會自動處理
- 標點符號直接寫即可（不需要包在 D 或 C 裡）
- 整句對話可以包成一個 D() 或 C()

範例：
lines.append(L(
    C('我','Ich'), D('schwang','揮著'), C('在','unter'),
    C('一個','einem'), D('sonnigen','晴朗的'), D('Himmel','天空下'),
    C('我的','mein'), D('Holzschwert','木劍'), '。'
))
"""

import re

OUTPUT_FILE = 'page6.html'

def D(de, zh):
    return f'<span class="d">{de}<span class="t">{zh}</span></span>'

def C(zh, de):
    return f'<span class="c">{zh}<span class="t">{de}</span></span>'

def L(*parts):
    return '<div class="line">' + ' '.join(str(p) for p in parts) + '</div>'

def S(text):
    return f'<span class="scene">{text}</span>'

def BRK():
    return '<div class="break">* * *</div>'

# ═══════════════════════════════════════════
# 在這裡填入您的內容
# ═══════════════════════════════════════════

lines = []

lines.append(S('Kapitel 4: Die vielen Seiten von Shadow Garden?!'))
lines.append('')

# ─── 範例：前兩句 ───

lines.append(L(
    C('那個','Der'), D('Sommer','夏天'), C('是','ist'),
    D('bald','快'), C('在那裡','da'), '。'
))
lines.append('')

lines.append(L(
    D('Gut gelaunt','心情愉快地'), D('schwang','揮著'),
    C('我','ich'), C('在','unter'), C('一個','einem'),
    D('sonnigen','晴朗的'), D('Himmel','天空'),
    C('我的','mein'), D('Holzschwert','木劍'), '。'
))
lines.append('')

# ─── 請繼續在下方添加更多行 ───
# lines.append(L(
#     C('我','Ich'), D('befand','發現'), C('自己','mich'),
#     C('正好','gerade'), C('再次','wieder'), C('在','in'),
#     C('我的','meinem'), D('alten','舊的'), D('Praxiskurs','實習課'), '。'
# ))
#
# lines.append(BRK())  # 用於 *** 分隔線
#
# 對話可以整句包裝：
# lines.append(L(
#     D('„Und? Was ist mit dir und Alexia passiert?"','「然後呢？你和Alexia怎麼了？」'), '，',
#     D('fragte','問道'), D('Lu','Lu'), '。'
# ))


# ═══════════════════════════════════════════
# 以下為建構邏輯，不需要修改
# ═══════════════════════════════════════════

NAV_LINKS = [
    ('index.html', '第一集 字幕', False),
    ('page2.html', 'Prolog 小說', False),
    ('page3.html', 'Kapitel 1 小說', False),
    ('page4.html', 'Kapitel 2 小說', False),
    ('page5.html', 'Kapitel 3 小說', False),
    ('page6.html', 'Kapitel 4 小說', True),
]

nav_html = '\n    '.join(
    f'<a href="{href}"{" class=\"active\"" if active else ""}>{label}</a>'
    for href, label, active in NAV_LINKS
)

html = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>陰の実力者になりたくて！— Kapitel 4 晶晶體</title>
<style>
  :root {{ --bg: #0d0d0d; --de: #c084fc; --de-glow: rgba(192, 132, 252, 0.15); --zh: #7ec8e3; --zh-glow: rgba(126, 200, 227, 0.15); --tooltip-bg: #2a2a40; --accent: #c084fc; --border: #333; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: var(--bg); color: #d4d4d4; font-family: 'Segoe UI','Noto Sans TC','Noto Sans',Arial,sans-serif; line-height: 2.2; }}
  header {{ text-align: center; padding: 3rem 1rem 2rem; background: linear-gradient(180deg,#16213e 0%,var(--bg) 100%); border-bottom: 1px solid var(--border); }}
  header h1 {{ font-size: 1.8rem; color: var(--accent); margin-bottom: .5rem; }}
  header p {{ font-size: .95rem; color: #888; }}
  nav {{ display: flex; justify-content: center; gap: 1rem; margin-top: 1.2rem; flex-wrap: wrap; }}
  nav a {{ color: var(--accent); text-decoration: none; padding: .4rem 1.2rem; border: 1px solid rgba(192,132,252,.3); border-radius: 6px; font-size: .85rem; transition: background .2s; }}
  nav a:hover, nav a.active {{ background: rgba(192,132,252,.15); }}
  nav a.active {{ border-color: var(--accent); font-weight: 600; }}
  .hint-box {{ display: inline-block; background: rgba(192,132,252,.08); border: 1px solid rgba(192,132,252,.2); border-radius: 6px; padding: .6rem 1rem; margin-top: 1rem; font-size: .82rem; color: #aaa; }}
  main {{ max-width: 860px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }}
  .line {{ padding: .35rem .8rem; border-radius: 6px; margin-bottom: .5rem; transition: background .2s; font-size: 1.05rem; }}
  .line:hover {{ background: rgba(255,255,255,.03); }}
  .scene {{ display: block; color: var(--accent); font-size: .78rem; text-transform: uppercase; letter-spacing: 2px; margin: 2.2rem 0 .6rem; padding: 0 .8rem; opacity: .7; }}
  .break {{ margin: 1.8rem 0; text-align: center; color: #555; letter-spacing: 6px; }}
  .d {{ position: relative; color: var(--de); cursor: pointer; padding: 1px 2px; border-radius: 3px; transition: background .2s, color .15s; }}
  .d:hover {{ background: var(--de-glow); color: #e2bdff; }}
  .c {{ position: relative; color: var(--zh); cursor: pointer; padding: 1px 2px; border-radius: 3px; transition: background .2s, color .15s; }}
  .c:hover {{ background: var(--zh-glow); color: #b0e8f7; }}
  .d .t, .c .t {{ visibility: hidden; opacity: 0; position: absolute; bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%); background: var(--tooltip-bg); padding: 6px 14px; border-radius: 6px; font-size: .88rem; white-space: nowrap; max-width: 400px; white-space: normal; text-align: center; box-shadow: 0 4px 16px rgba(0,0,0,.5); pointer-events: none; z-index: 100; transition: opacity .2s, visibility .2s; border: 1px solid rgba(255,255,255,.1); font-weight: normal; }}
  .d .t {{ color: var(--zh); }}
  .c .t {{ color: var(--de); }}
  .d .t::after, .c .t::after {{ content: ''; position: absolute; top: 100%; left: 50%; transform: translateX(-50%); border: 6px solid transparent; border-top-color: var(--tooltip-bg); }}
  .d:hover .t, .c:hover .t {{ visibility: visible; opacity: 1; }}
  @media (max-width: 600px) {{ .line {{ font-size: .95rem; }} header h1 {{ font-size: 1.4rem; }} .d .t, .c .t {{ left: 0; transform: none; max-width: 280px; }} }}
</style>
</head>
<body>
<header>
  <h1>陰の実力者になりたくて！</h1>
  <p>The Eminence in Shadow — Kapitel 4 晶晶體</p>
  <nav>
    {nav_html}
  </nav>
  <div class="hint-box">
    <span style="color:var(--de);">紫色</span> = Deutsch (hover → 中文) ｜ <span style="color:var(--zh);">藍色</span> = 中文 (hover → Deutsch) ｜ 所有文字皆可互動
  </div>
</header>
<main>

{''.join(l + chr(10) for l in lines)}
</main>
</body>
</html>'''

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'✅ 已產生 {OUTPUT_FILE}')

d_count = len(re.findall(r'<span class="d">', html))
c_count = len(re.findall(r'<span class="c">', html))
print(f'   德文詞 (.d): {d_count}')
print(f'   中文詞 (.c): {c_count}')
if d_count + c_count > 0:
    print(f'   德文佔比: {d_count/(d_count+c_count)*100:.1f}%')
print(f'')
print(f'📌 下一步：執行以下命令來自動轉換白色德文虛詞為藍色中文：')
print(f'   python3 auto_convert.py {OUTPUT_FILE}')
