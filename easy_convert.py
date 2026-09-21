# -*- coding: utf-8 -*-
"""
=== 簡易晶晶體轉換工具 ===

使用方式：
1. 建立一個文字檔 input.txt
2. 把您的德文原文貼進去
3. 每一行就是一個段落，空行會保留
4. 對話行直接貼上即可
5. *** 會自動變成分隔線
6. 執行: python3 easy_convert.py input.txt page6.html "Kapitel 4" "Die vielen Seiten von Shadow Garden?!"

這個工具會：
- 自動把所有德文詞標記為紫色互動詞
- 用 auto_convert.py 的 WORD_MAP 把虛詞轉成藍色中文
- 您之後只需要手動檢查翻譯是否正確
"""

import re
import sys
import os

WORD_MAP = {
    'Ich': '我', 'ich': '我', 'mich': '自己', 'mir': '我',
    'mein': '我的', 'meine': '我的', 'meinem': '我的', 'meinen': '我的', 'meiner': '我的', 'meines': '我的',
    'du': '你', 'Du': '你', 'dein': '你的', 'deine': '你的', 'deinem': '你的', 'deinen': '你的', 'dir': '你', 'dich': '你',
    'er': '他', 'Er': '他', 'sie': '她', 'Sie': '她', 'es': '它', 'Es': '它',
    'wir': '我們', 'Wir': '我們', 'ihr': '她的', 'Ihr': '你們',
    'sein': '是', 'seine': '他的', 'seinem': '他的', 'seinen': '他的', 'seiner': '他的',
    'ihm': '他', 'ihn': '他', 'ihnen': '他們',
    'sich': '自己', 'selbst': '自己',
    'der': '該', 'die': '該', 'das': '該', 'den': '該', 'dem': '該', 'des': '的',
    'Der': '該', 'Die': '該', 'Das': '那',
    'ein': '一個', 'Ein': '一個', 'eine': '一個', 'Eine': '一個', 'einem': '一個', 'einen': '一個', 'einer': '一個',
    'nicht': '不', 'Nicht': '不', 'kein': '沒有', 'keine': '沒有', 'keinen': '沒有', 'keiner': '沒有',
    'nichts': '什麼都不', 'niemand': '沒有人',
    'und': '和', 'Und': '和', 'oder': '或', 'Oder': '或',
    'aber': '但是', 'Aber': '但是', 'doch': '然而', 'Doch': '然而', 'jedoch': '然而',
    'sondern': '而是', 'denn': '因為', 'Denn': '因為', 'weil': '因為',
    'dass': '說', 'ob': '是否',
    'als': '當', 'Als': '當', 'wenn': '當', 'Wenn': '如果',
    'obwohl': '雖然',
    'in': '在', 'In': '在', 'an': '在', 'An': '在', 'auf': '在',
    'aus': '從', 'Aus': '從', 'von': '的', 'Von': '從',
    'mit': '用', 'Mit': '用', 'nach': '之後', 'Nach': '之後',
    'zu': '去', 'Zu': '去', 'für': '為了', 'Für': '為了',
    'durch': '透過', 'über': '關於', 'bei': '在', 'Bei': '在', 'um': '為了',
    'gegen': '對抗', 'unter': '在……下', 'ohne': '沒有',
    'vor': '在……前', 'hinter': '在……後',
    'neben': '旁邊', 'seit': '自從', 'bis': '直到', 'Bis': '直到',
    'am': '在', 'Am': '在', 'im': '在', 'Im': '在',
    'ins': '進入', 'zum': '到', 'zur': '到', 'vom': '從',
    'ist': '是', 'war': '是', 'sind': '是', 'waren': '是',
    'wird': '將會', 'wurde': '被', 'würde': '會',
    'hat': '有', 'hatte': '有', 'haben': '有', 'habe': '有', 'hatten': '有',
    'bin': '是', 'bist': '是',
    'kann': '能', 'konnte': '能', 'können': '能', 'könnte': '可能',
    'muss': '必須', 'musste': '必須', 'müssen': '必須',
    'will': '想要', 'wollte': '想要', 'wollen': '想要',
    'soll': '應該', 'sollte': '應該', 'sollten': '應該',
    'darf': '可以', 'durfte': '可以',
    'ließ': '讓', 'wurden': '被', 'worden': '被',
    'hätte': '會有', 'hätten': '會有', 'wäre': '會是',
    'kam': '來了', 'ging': '去了', 'sah': '看見了', 'gab': '給了',
    'stand': '站著', 'lag': '躺著', 'saß': '坐著',
    'hielt': '握住', 'trat': '走進', 'zog': '拉',
    'nahm': '拿了', 'blieb': '留下', 'begann': '開始',
    'dachte': '想著', 'wusste': '知道', 'kannte': '認識',
    'glaubte': '相信', 'versuchte': '嘗試',
    'machte': '做了', 'sagte': '說道', 'fragte': '問道',
    'so': '如此', 'So': '如此', 'auch': '也', 'Auch': '也',
    'nur': '只', 'Nur': '只', 'schon': '已經', 'noch': '還', 'Noch': '還',
    'immer': '總是', 'sehr': '非常', 'viel': '很多', 'mehr': '更多',
    'hier': '這裡', 'Hier': '這裡', 'dort': '那裡', 'da': '因為',
    'dann': '然後', 'Dann': '然後', 'also': '所以', 'Also': '所以',
    'jetzt': '現在', 'Jetzt': '現在', 'nun': '現在',
    'bereits': '已經', 'wieder': '再次', 'fast': '幾乎',
    'ganz': '完全', 'gar': '根本', 'wohl': '大概',
    'gerade': '正好', 'sogar': '甚至', 'sofort': '立刻',
    'endlich': '終於', 'eigentlich': '其實',
    'vielleicht': '也許', 'bestimmt': '一定',
    'wirklich': '真的', 'natürlich': '當然',
    'plötzlich': '突然', 'Plötzlich': '突然',
    'einfach': '簡單地', 'genau': '正好', 'leise': '輕聲地',
    'ja': '嘛', 'Ja': '是', 'nein': '不', 'Nein': '不',
    'trotzdem': '儘管如此', 'deshalb': '因此', 'Deshalb': '因此',
    'außerdem': '此外',
    'wie': '像', 'Wie': '如何', 'was': '什麼', 'Was': '什麼',
    'wer': '誰', 'Wer': '誰', 'wo': '哪裡', 'Wo': '哪裡',
    'warum': '為什麼',
    'dieser': '這個', 'diese': '這些', 'diesem': '這個', 'diesen': '這些', 'dieses': '這個',
    'jeder': '每個', 'alle': '所有', 'alles': '一切',
    'man': '人們', 'Man': '人們',
    'jemand': '某人', 'etwas': '某些',
    'davon': '從中', 'daran': '關於此', 'damit': '為此',
    'darauf': '對此', 'einmal': '一次', 'mal': '一次',
    'beide': '兩個', 'beiden': '兩個',
    'andere': '其他', 'anderen': '其他',
    'hast': '有', 'wirst': '將會', 'inzwischen': '如今',
}

def process_word(word):
    stripped = word.strip()
    if not stripped:
        return word
    if stripped in WORD_MAP:
        zh = WORD_MAP[stripped]
        return f'<span class="c">{zh}<span class="t">{stripped}</span></span>'
    elif re.match(r'^[A-Za-zÄÖÜäöüß]', stripped):
        return f'<span class="d">{stripped}<span class="t">（德）</span></span>'
    else:
        return word

def process_line_text(text):
    text = text.strip()
    if not text:
        return ''
    if text == '***':
        return '<div class="break">* * *</div>'

    tokens = re.findall(r"[A-Za-z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\u00DF''\-]+|[^\sA-Za-z\u00C4\u00D6\u00DC\u00E4\u00F6\u00FC\u00DF''\-]+|\s+", text)
    result = []
    for token in tokens:
        result.append(process_word(token))
    return '<div class="line">' + ''.join(result) + '</div>'

def main():
    if len(sys.argv) < 3:
        print('使用方式: python3 easy_convert.py input.txt output.html [章節標題] [副標題]')
        print('範例: python3 easy_convert.py input.txt page6.html "Kapitel 4" "Die vielen Seiten"')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    chapter = sys.argv[3] if len(sys.argv) > 3 else 'Kapitel'
    subtitle = sys.argv[4] if len(sys.argv) > 4 else ''

    with open(input_file, 'r', encoding='utf-8') as f:
        raw_lines = f.readlines()

    content_lines = []
    for line in raw_lines:
        line = line.rstrip('\n')
        processed = process_line_text(line)
        if processed:
            content_lines.append(processed)
        else:
            content_lines.append('')

    nav_links = [
        ('index.html', '第一集 字幕', False),
        ('page2.html', 'Prolog 小說', False),
        ('page3.html', 'Kapitel 1 小說', False),
        ('page4.html', 'Kapitel 2 小說', False),
        ('page5.html', 'Kapitel 3 小說', False),
        ('page6.html', 'Kapitel 4 小說', output_file == 'page6.html'),
    ]

    nav_html = '\n    '.join(
        f'<a href="{href}"{" class=\"active\"" if active else ""}>{label}</a>'
        for href, label, active in nav_links
    )

    html = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>陰の実力者になりたくて！— {chapter} 晶晶體</title>
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
  <p>The Eminence in Shadow — {chapter} 晶晶體</p>
  <nav>
    {nav_html}
  </nav>
  <div class="hint-box">
    <span style="color:var(--de);">紫色</span> = Deutsch (hover → 中文) ｜ <span style="color:var(--zh);">藍色</span> = 中文 (hover → Deutsch) ｜ 所有文字皆可互動
  </div>
</header>
<main>
<span class="scene">{chapter}: {subtitle}</span>

{''.join(l + chr(10) for l in content_lines)}
</main>
</body>
</html>'''

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    d_count = len(re.findall(r'<span class="d">', html))
    c_count = len(re.findall(r'<span class="c">', html))
    unknown = len(re.findall(r'（德）', html))

    print(f'✅ 已產生 {output_file}')
    print(f'   德文詞 (.d): {d_count}')
    print(f'   中文互動詞 (.c): {c_count}')
    if d_count + c_count > 0:
        print(f'   德文佔比: {d_count/(d_count+c_count)*100:.1f}%')
    print(f'   需要手動翻譯的詞（標記為「（德）」）: {unknown}')
    print()
    if unknown > 0:
        print(f'⚠️  有 {unknown} 個德文詞需要手動翻譯')
        print(f'   在 {output_file} 中搜尋「（德）」來找到它們')
    else:
        print(f'🎉 所有詞彙都已自動翻譯！')

if __name__ == '__main__':
    main()
