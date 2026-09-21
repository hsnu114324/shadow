# -*- coding: utf-8 -*-
"""
把一些已轉為中文的虛詞改回德文顯示（保留互動功能），以提高德文佔比到>50%。
只挑選不影響閱讀理解的虛詞。
"""
import re

CONVERT_BACK = {
    '該': None,  # der/die/das - 冠詞改回德文
    '一個': None,  # ein/eine - 不定冠詞
    '和': None,  # und
    '在': None,  # in/an/auf/bei/am/im
    '從': None,  # aus/von
    '用': None,  # mit
    '去': None,  # zu
    '到': None,  # zum/zur
    '進入': None,  # ins
    '的': None,  # des/von
}

with open('page6.html', 'r', encoding='utf-8') as f:
    html = f.read()

count_converted = 0

for zh_word in CONVERT_BACK:
    pattern = f'<span class="c">{re.escape(zh_word)}<span class="t">([^<]+)</span></span>'
    matches = list(re.finditer(pattern, html))
    half = len(matches) // 2
    
    converted = 0
    for i, m in enumerate(matches):
        if i >= half:
            break
        de_word = m.group(1)
        old = m.group(0)
        new = f'<span class="d">{de_word}<span class="t">{zh_word}</span></span>'
        html = html.replace(old, new, 1)
        converted += 1
    
    count_converted += converted

d_count = len(re.findall(r'<span class="d">', html))
c_count = len(re.findall(r'<span class="c">', html))

with open('page6.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'✅ 德文佔比調整完成')
print(f'   轉換了 {count_converted} 個詞回德文顯示')
print(f'   德文詞 (.d): {d_count}')
print(f'   中文互動詞 (.c): {c_count}')
if d_count + c_count > 0:
    print(f'   德文佔比: {d_count/(d_count+c_count)*100:.1f}%')
