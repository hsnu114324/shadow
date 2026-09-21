# -*- coding: utf-8 -*-
"""
=== 自動轉換工具 ===

將 HTML 檔案中所有未標記的德文虛詞自動轉換成藍色中文互動 span。

使用方式：
    python3 auto_convert.py page4.html

這個腳本會：
1. 找出所有未被 <span class="d"> 或 <span class="c"> 包裹的德文單字
2. 如果是已知的虛詞（代名詞、冠詞、介詞等），轉成藍色中文
3. 如果是未知的德文詞，標記為「（德）」供您手動補上翻譯
4. 產生報告，顯示有多少詞需要手動處理
"""

import re
import sys

# ─── 德文虛詞 → 繁體中文 對照表 ───
# 您可以自行擴充這個字典
WORD_MAP = {
    # 人稱代名詞
    'Ich': '我', 'ich': '我', 'mich': '自己', 'mir': '我',
    'mein': '我的', 'meine': '我的', 'meinem': '我的', 'meinen': '我的', 'meiner': '我的', 'meines': '我的',
    'du': '你', 'Du': '你', 'dein': '你的', 'deine': '你的', 'deinem': '你的', 'deinen': '你的', 'dir': '你', 'dich': '你',
    'er': '他', 'Er': '他', 'sie': '她', 'Sie': '她', 'es': '它', 'Es': '它',
    'wir': '我們', 'Wir': '我們', 'ihr': '她的', 'Ihr': '你們',
    'sein': '是', 'seine': '他的', 'seinem': '他的', 'seinen': '他的', 'seiner': '他的',
    'ihm': '他', 'ihn': '他', 'ihnen': '他們',
    'sich': '自己', 'selbst': '自己', 'Selbst': '甚至',
    # 冠詞
    'der': '該', 'die': '該', 'das': '該', 'den': '該', 'dem': '該', 'des': '的',
    'Der': '該', 'Die': '該', 'Das': '那',
    'ein': '一個', 'Ein': '一個', 'eine': '一個', 'Eine': '一個', 'einem': '一個', 'einen': '一個', 'einer': '一個',
    # 否定
    'nicht': '不', 'Nicht': '不', 'kein': '沒有', 'keine': '沒有', 'keinen': '沒有', 'keiner': '沒有',
    'nichts': '什麼都不', 'niemand': '沒有人', 'Niemand': '沒有人',
    # 連接詞
    'und': '和', 'Und': '和', 'oder': '或', 'Oder': '或',
    'aber': '但是', 'Aber': '但是', 'doch': '然而', 'Doch': '然而', 'jedoch': '然而',
    'sondern': '而是', 'weder': '既不',
    'denn': '因為', 'Denn': '因為', 'weil': '因為',
    'dass': '說', 'ob': '是否',
    'als': '當', 'Als': '當', 'wenn': '當', 'Wenn': '如果',
    'obwohl': '雖然', 'Obwohl': '雖然',
    # 介詞
    'in': '在', 'In': '在', 'an': '在', 'An': '在', 'auf': '在',
    'aus': '從', 'Aus': '從', 'von': '的', 'Von': '從',
    'mit': '用', 'Mit': '用', 'nach': '之後', 'Nach': '之後',
    'zu': '去', 'Zu': '去', 'für': '為了', 'Für': '為了',
    'durch': '透過', 'Durch': '透過', 'über': '關於', 'Über': '關於',
    'bei': '在', 'Bei': '在', 'um': '為了',
    'gegen': '對抗', 'unter': '在……下', 'Unter': '在……下',
    'zwischen': '之間', 'ohne': '沒有', 'Ohne': '沒有',
    'vor': '在……前', 'Vor': '在……前', 'hinter': '在……後',
    'neben': '旁邊', 'seit': '自從', 'Seit': '自從', 'außer': '除了',
    'bis': '直到', 'Bis': '直到',
    # 縮合介詞
    'am': '在', 'Am': '在', 'im': '在', 'Im': '在',
    'ins': '進入', 'zum': '成為', 'zur': '到', 'Zum': '到',
    'vom': '從', 'ans': '到', 'aufs': '在',
    # 助動詞/動詞
    'ist': '是', 'war': '是', 'sind': '是', 'waren': '是',
    'wird': '將會', 'wurde': '變成了', 'würde': '會', 'würden': '會',
    'hat': '有', 'hatte': '有', 'haben': '有', 'habe': '有', 'hatten': '有',
    'bin': '是', 'bist': '是',
    'kann': '能', 'konnte': '能', 'können': '能', 'könnte': '可能', 'konnten': '能',
    'muss': '必須', 'musste': '必須', 'müssen': '必須',
    'will': '想要', 'wollte': '想要', 'wollen': '想要', 'wollten': '想要',
    'soll': '應該', 'sollte': '應該', 'sollten': '應該',
    'darf': '可以', 'durfte': '可以', 'dürfen': '可以',
    'ließ': '讓', 'ließen': '讓',
    'wurden': '被', 'worden': '被',
    'hätte': '會有', 'hätten': '會有', 'wäre': '會是', 'wären': '會是',
    # 常見動詞過去式
    'kam': '來了', 'ging': '去了', 'sah': '看見了', 'gab': '給了',
    'fand': '找到了', 'stand': '站著', 'saß': '坐著', 'lag': '躺著',
    'lief': '跑', 'hielt': '握住', 'trat': '走進', 'zog': '拉',
    'schlug': '打', 'traf': '擊中', 'brach': '斷了', 'fiel': '掉落',
    'nahm': '拿了', 'blieb': '留下', 'begann': '開始', 'bekam': '得到',
    'verlor': '失去', 'sprach': '說了', 'rief': '喊了',
    'dachte': '想著', 'wusste': '知道', 'kannte': '認識',
    'glaubte': '相信', 'erkannte': '認出', 'versuchte': '嘗試',
    'beschloss': '決定', 'suchte': '尋找', 'brauchte': '需要',
    'machte': '做了', 'brachte': '帶來', 'sagte': '說道',
    'fragte': '問道', 'hörte': '聽到', 'suchte': '尋找',
    # 副詞
    'so': '如此', 'So': '如此', 'auch': '也', 'Auch': '也',
    'nur': '只', 'Nur': '只', 'schon': '已經', 'noch': '還', 'Noch': '還',
    'immer': '總是', 'Immer': '總是', 'nie': '從不', 'niemals': '永不',
    'sehr': '非常', 'viel': '很多', 'mehr': '更多',
    'hier': '這裡', 'Hier': '這裡', 'dort': '那裡', 'da': '因為',
    'dann': '然後', 'Dann': '然後', 'also': '所以', 'Also': '所以',
    'jetzt': '現在', 'Jetzt': '現在', 'nun': '現在',
    'bereits': '已經', 'wieder': '再次', 'fast': '幾乎', 'Fast': '幾乎',
    'ganz': '完全', 'gar': '根本', 'etwa': '大約', 'wohl': '大概',
    'eben': '剛才', 'gerade': '正好', 'sogar': '甚至', 'sofort': '立刻',
    'endlich': '終於', 'eigentlich': '其實', 'überhaupt': '根本',
    'übrigens': '順帶一提', 'vielleicht': '也許', 'bestimmt': '一定',
    'wirklich': '真的', 'Wirklich': '真的', 'tatsächlich': '確實',
    'natürlich': '當然', 'plötzlich': '突然', 'Plötzlich': '突然',
    'einfach': '簡單地', 'genau': '正好', 'leise': '輕聲地',
    'zwar': '雖然', 'ja': '嘛', 'Ja': '是', 'nein': '不', 'Nein': '不',
    'trotzdem': '儘管如此', 'Trotzdem': '儘管如此',
    'deshalb': '因此', 'Deshalb': '因此', 'daher': '因此',
    'außerdem': '此外', 'Außerdem': '此外',
    # 疑問詞
    'wie': '像', 'Wie': '如何', 'was': '什麼', 'Was': '什麼',
    'wer': '誰', 'Wer': '誰', 'wo': '哪裡', 'Wo': '哪裡',
    'warum': '為什麼', 'Warum': '為什麼',
    'woher': '從哪裡', 'Woher': '從哪裡',
    # 指示詞
    'dieses': '這個', 'dieser': '這個', 'diese': '這些', 'diesem': '這個', 'diesen': '這些',
    'Dieser': '這個', 'Diese': '這些', 'Dieses': '這個',
    'jeder': '每個', 'jede': '每個', 'jedem': '每個', 'jeden': '每個',
    'alle': '所有', 'Alle': '所有', 'alles': '一切',
    'Man': '人們', 'man': '人們',
    'jemand': '某人', 'jemanden': '某人', 'etwas': '某些',
    # 其他
    'davon': '從中', 'daran': '關於此', 'damit': '為此', 'Damit': '為此',
    'dazu': '為此', 'darauf': '對此', 'darum': '為此',
    'einmal': '一次', 'mal': '一次',
    'beide': '兩個', 'beiden': '兩個',
    'andere': '其他', 'anderen': '其他', 'anderes': '其他',
    'solche': '這樣的', 'einige': '一些', 'Einige': '一些',
    'statt': '而非', 'anstatt': '而非',
    'sofort': '立刻', 'Sofort': '立刻',
    'kurz': '短暫地', 'Kurz': '短暫地',
    'hast': '有', 'habt': '有',
    'wirst': '將會',
    'inzwischen': '如今',
}


def replace_bare_text(match_text):
    """將未標記的文字轉換成 .c span"""
    if not re.sub(r'[\s，。、！？：；「」……——＊\.\!\?\,\;\:\(\)\-\uff5c]+', '', match_text):
        return match_text
    result = []
    tokens = re.findall(r'[A-Za-zÄÖÜäöüß\-]+|[^\sA-Za-zÄÖÜäöüß\-]+|\s+', match_text)
    for token in tokens:
        stripped = token.strip()
        if stripped in WORD_MAP:
            zh = WORD_MAP[stripped]
            result.append(f'<span class="c">{zh}<span class="t">{stripped}</span></span>')
        elif stripped and re.match(r'^[A-Za-zÄÖÜäöüß]', stripped):
            result.append(f'<span class="d">{stripped}<span class="t">（德）</span></span>')
        else:
            result.append(token)
    return ''.join(result)


def process_line(line_match):
    """處理一行 div.line 內容"""
    line_content = line_match.group(1)
    parts = []
    i = 0
    while i < len(line_content):
        span_match = re.match(r'<span class="[dc]">', line_content[i:])
        if span_match:
            depth = 0
            j = i
            while j < len(line_content):
                if line_content[j:].startswith('<span'):
                    depth += 1
                    j += line_content[j:].index('>') + 1
                elif line_content[j:].startswith('</span>'):
                    depth -= 1
                    j += len('</span>')
                    if depth == 0:
                        break
                else:
                    j += 1
            parts.append(('span', line_content[i:j]))
            i = j
        else:
            next_span = re.search(r'<span class="[dc]">', line_content[i:])
            if next_span:
                bare = line_content[i:i+next_span.start()]
                parts.append(('bare', bare))
                i = i + next_span.start()
            else:
                parts.append(('bare', line_content[i:]))
                i = len(line_content)
    
    result = []
    for ptype, ptext in parts:
        if ptype == 'bare':
            result.append(replace_bare_text(ptext))
        else:
            result.append(ptext)
    return f'<div class="line">{"".join(result)}</div>'


def main():
    if len(sys.argv) < 2:
        print('使用方式: python3 auto_convert.py <檔案名稱>')
        print('範例: python3 auto_convert.py page4.html')
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    main_start = content.index('<main>')
    main_end = content.index('</main>') + len('</main>')
    before = content[:main_start]
    main_section = content[main_start:main_end]
    after = content[main_end:]
    
    main_section = re.sub(
        r'<div class="line">(.*?)</div>',
        process_line,
        main_section,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(before + main_section + after)
    
    # 報告
    unknown = re.findall(r'<span class="d">([^<]+)<span class="t">（德）</span></span>', main_section)
    unique_unknown = sorted(set(unknown))
    
    lines_content = re.findall(r'<div class="line">(.*?)</div>', main_section, re.DOTALL)
    bare_count = 0
    for line in lines_content:
        temp = re.sub(r'<span class="t">.*?</span>', '', line)
        temp = re.sub(r'<span class="[dc]">(.*?)</span>', '', temp)
        remaining = re.sub(r'<[^>]+>', '', temp).strip()
        remaining_clean = re.sub(r'[\s，。、！？：；「」……——＊\.\!\?\,\;\:\(\)\-\uff5c]+', '', remaining)
        if remaining_clean:
            bare_count += 1
    
    d_count = len(re.findall(r'<span class="d">', main_section))
    c_count = len(re.findall(r'<span class="c">', main_section))
    
    print(f'✅ {filename} 轉換完成！')
    print(f'')
    print(f'📊 統計：')
    print(f'   德文互動詞 (.d): {d_count}')
    print(f'   中文互動詞 (.c): {c_count}')
    if d_count + c_count > 0:
        print(f'   德文佔比: {d_count/(d_count+c_count)*100:.1f}%')
    print(f'   白色殘留行數: {bare_count}')
    print(f'   未知德文詞（標記為「（德）」）: {len(unique_unknown)}')
    
    if unique_unknown:
        print(f'')
        print(f'⚠️  以下德文詞需要手動翻譯（目前顯示為「（德）」）：')
        for w in unique_unknown:
            print(f'   - {w}')
        print(f'')
        print(f'💡 修正方式：')
        print(f'   方法1: 在 auto_convert.py 的 WORD_MAP 中加入翻譯，然後重新執行')
        print(f'   方法2: 直接在 {filename} 中搜尋「（德）」手動替換')


if __name__ == '__main__':
    main()
