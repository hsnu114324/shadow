# -*- coding: utf-8 -*-
import re

files = ['index.html', 'page2.html', 'page3.html', 'page4.html', 'page5.html', 'page6.html']

page6_link_inline = '    <a href="page6.html" style="color:var(--accent);text-decoration:none;padding:0.4rem 1.2rem;border:1px solid rgba(192,132,252,0.3);border-radius:6px;font-size:0.85rem;">Kapitel 4 小說</a>'
page6_link_css = '    <a href="page6.html">Kapitel 4 小說</a>'
page6_link_active = '    <a href="page6.html" class="active">Kapitel 4 小說</a>'

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print(f'⚠️  {fname} 不存在，跳過')
        continue

    if 'page6.html' in html:
        print(f'✅ {fname} 已有 page6 連結')
        continue

    if fname == 'index.html':
        link = page6_link_inline
        marker = 'Kapitel 3 小說</a>'
    else:
        if fname == 'page6.html':
            link = page6_link_active
        else:
            link = page6_link_css
        marker = 'Kapitel 3 小說</a>'

    idx = html.find(marker)
    if idx == -1:
        print(f'⚠️  {fname} 找不到導航標記')
        continue

    insert_pos = idx + len(marker)
    html = html[:insert_pos] + '\n' + link + html[insert_pos:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'✅ {fname} 已更新導航')
