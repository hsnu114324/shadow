# -*- coding: utf-8 -*-
files = ['index.html', 'page2.html', 'page3.html', 'page4.html', 'page5.html', 'page6.html']

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        print(f'⚠️  {fname} 不存在')
        continue

    if 'page7.html' in html:
        print(f'✅ {fname} 已有 page7 連結')
        continue

    marker = 'Kapitel 4 小說</a>'
    idx = html.find(marker)
    if idx == -1:
        print(f'⚠️  {fname} 找不到 Kapitel 4 標記')
        continue

    insert_pos = idx + len(marker)

    if fname == 'index.html':
        link = '    <a href="page7.html" style="color:var(--accent);text-decoration:none;padding:0.4rem 1.2rem;border:1px solid rgba(192,132,252,0.3);border-radius:6px;font-size:0.85rem;">Kapitel 5 小說</a>'
    else:
        link = '    <a href="page7.html">Kapitel 5 小說</a>'

    html = html[:insert_pos] + '\n' + link + html[insert_pos:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'✅ {fname} 已更新')
