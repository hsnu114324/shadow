# -*- coding: utf-8 -*-
import re, collections

MAP3 = {
    'Durch': '透過', 'darüber': '關於此', 'traf': '打中了', 'Verstehe': '明白了',
    'Mein': '我的', 'vergessen': '忘記了', 'Wesen': '存在', 'besser': '更好',
    'handelte': '是', 'gleiche': '同樣的', 'Minuten': '分鐘', 'besten': '最好的',
    'immerhin': '畢竟', 'Gespräch': '對話', 'nachts': '夜間',
    'Einen': '一個', 'ans': '到', 'Selbst': '即使', 'führte': '帶著',
    'wegen': '因為', 'fürs': '為了', 'her': '過來', 'A-Also': '那個',
    'Sache': '事情', 'deren': '她的', 'Wirklich': '真的',
    'blau-violette': '藍紫色的', 'blau-violettes': '藍紫色的', 'blau-violetten': '藍紫色的',
    'blau-violetter': '藍紫色的',
    'Körper': '身體', 'Lebens': '生命的', 'einige': '一些', 'echt': '真的',
    'jede': '每一個', 'Sind': '是', 'einzige': '唯一的',
    'Shadows': '闇影的', 'Etwas': '某些', 'sei': '是',
    'weg': '走', 'schaffte': '做到了',
    'Hälften': '兩半', 'sehen': '看', 'konnte': '能夠',
    'dich': '你', 'werden': '會', 'Doch': '然而',
    'Gedanken': '心裡', 'Kampf': '戰鬥',
    'Stelle': '原地', 'zusammen': '一起',
    'Denn': '因為', 'Davon': '關於這',
    'anderen': '其他的', 'alle': '所有', 'alles': '一切',
    'Genau': '正是', 'genau': '正好',
    'sein': '他的', 'Sein': '他的',
    'war': '曾是', 'wird': '將會', 'wurde': '被', 'würde': '會',
    'erst': '才', 'Erst': '首先',
    'mich': '我', 'mir': '我',
    'sich': '自己', 'Sich': '自己',
    'bereits': '已經', 'wieder': '再次', 'immer': '總是',
    'auch': '也', 'Auch': '也',
    'so': '如此', 'So': '如此',
    'noch': '還', 'Noch': '還',
    'schon': '已經', 'nur': '只',
    'hier': '這裡', 'Hier': '這裡',
    'dort': '那裡', 'da': '那裡',
    'dann': '然後', 'Dann': '然後',
    'nun': '現在', 'Nun': '那麼',
    'sehr': '非常',
    'tief': '深深地',

    'Shadow-Garden-Betrüger': '冒牌Shadow Garden',
    'Midgar-Magieritterakademie': '密德迦爾魔法騎士學院',
    'Magieritterakademie': '魔法騎士學院',

    'dachte': '想著', 'wusste': '知道',
    'kannte': '認識', 'glaubte': '相信',
    'sagte': '說道', 'fragte': '問道',

    'stehen': '站著', 'stand': '站著', 'standen': '站著',
    'kniete': '跪著', 'lag': '躺著',
    'kam': '來了', 'ging': '走了',
    'sah': '看著', 'gab': '給了',
    'ließ': '讓', 'nahm': '拿了',
    'blieb': '留下了', 'begann': '開始了',

    'fiel': '掉了',
    'darauf': '在上面', 'darin': '裡面',
    'davon': '從中', 'damit': '用此',
    'dazu': '為此', 'davor': '在那之前',
    'daran': '對此',

    'irgendetwas': '什麼東西', 'irgendwas': '什麼東西',
    'irgendeiner': '某個', 'irgendeinem': '某個',

    'Schluss': '結束', 'Anfang': '開始',
    'Glauben': '信任', 'Miene': '表情',
    'Worte': '話', 'Frage': '問題',
    'Stimme': '聲音', 'Blick': '目光',
    'Ruhe': '安靜', 'Stille': '寂靜',
    'Seite': '側面',

    'oben': '上面', 'unten': '下面',
    'hinten': '後面', 'vorne': '前面',
    'draußen': '外面', 'drinnen': '裡面',

    'anders': '不同', 'gleichen': '相同的',
    'nächste': '下一個', 'nächsten': '下一個',
    'letzte': '最後的', 'letzten': '最後的',
    'erste': '第一個', 'erster': '第一個',

    'Danach': '之後', 'Damals': '當時',
    'Daraufhin': '於是', 'Nachdem': '在……之後',
    'Bevor': '在……之前', 'Während': '當……時',
    'Sobald': '一旦', 'Obwohl': '雖然',
    'Falls': '如果', 'Sofern': '只要',

    'bald': '很快', 'spät': '遲', 'früh': '早',

    'Aber': '但是', 'aber': '但是',
    'doch': '然而', 'jedoch': '然而',
    'trotzdem': '儘管如此',
    'deshalb': '因此', 'Deshalb': '因此',

    'Ja': '是', 'ja': '嘛',
    'Nein': '不', 'nein': '不',

    'Wie': '怎麼', 'Was': '什麼',
    'wer': '誰', 'Wer': '誰',
    'wo': '哪裡', 'Wo': '哪裡',

    'welche': '哪些', 'welchem': '哪個',
    'manchen': '某些',

    'natürlich': '當然', 'eigentlich': '其實',
    'plötzlich': '突然', 'Plötzlich': '突然',
    'endlich': '終於', 'sofort': '立刻',
    'sogar': '甚至', 'gerade': '正好',
    'wirklich': '真的', 'bestimmt': '一定',
    'vielleicht': '也許', 'einfach': '簡單地',
    'fast': '幾乎', 'ganz': '完全',
    'gar': '根本', 'wohl': '大概',

    'Tut': '抱', 'leid': '歉',
    'Danke': '謝謝', 'Bitte': '請',
    'Vielen': '非常', 'Dank': '感謝',

    'saß': '坐著', 'hing': '掛著',
    'rang': '掙扎著', 'schlief': '睡著了',
    'rief': '叫道', 'lief': '跑了',
    'hielt': '握住',
    'schnalzte': '嘖了嘖舌',
    'eilte': '趕來了',
    'erregt': '激動',
    'erstaunt': '驚訝',

    'einander': '彼此', 'aneinander': '互相',
    'zueinander': '對彼此',

    'bislang': '到目前為止', 'keineswegs': '絕不',
    'durchaus': '完全', 'ohnehin': '反正',
    'schließlich': '畢竟', 'letztendlich': '最終',
    'gelegentlich': '偶爾', 'wahrscheinlich': '大概',
    'tatsächlich': '事實上', 'vermutlich': '大概',
    'offenbar': '顯然', 'offensichtlich': '明顯地',
    'anscheinend': '看來',

    'Kopfsteinpflaster': '鵝卵石路',

    'Pechschwarzen': '漆黑', 'Pechschwarze': '漆黑的',

    'Goldmünzen': '金幣',

    'Morde': '謀殺案',

    'Schwertkampf': '劍術比賽',
    'Nebencharakter': '配角',
    'Scharlachrote': '緋紅',
    'Scharlachroten': '緋紅的',
    'Diaboloskult': '惡魔教團',
    'Diaboloskults': '惡魔教團的',

    'Haken': '鉤拳',
    'Magengrube': '胃部',
    'Ohnmacht': '昏厥',
    'Krankenstation': '醫務室',
    'Krankenzimmer': '病房',
    'Schulgebäude': '校舍',
    'Lehrerin': '女老師',
    'zusammengebrochen': '倒下了',
    'Einheit': '部隊',
    'bilden': '組建',
    'beobachteten': '觀察著',
    'schwänzten': '翹了',
    'restlichen': '剩下的',
    'Ausgangssperre': '宵禁',
    'Wohnheim': '宿舍',
    'Sekretariat': '教務處',
    'Paare': '對戰組合',
    'Kämpfe': '比賽',
    'Mitsugoshi-Kaufhaus': '三越百貨',
}

with open('page6.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_unknown(m):
    word = m.group(1)
    if word in MAP3:
        zh = MAP3[word]
        return f'<span class="d">{word}<span class="t">{zh}</span></span>'
    return m.group(0)

html = re.sub(
    r'<span class="d">([^<]+)<span class="t">（德）</span></span>',
    replace_unknown,
    html
)

d_count = len(re.findall(r'<span class="d">', html))
c_count = len(re.findall(r'<span class="c">', html))
unknown = len(re.findall(r'（德）', html))

with open('page6.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'✅ 第三輪翻譯修補完成')
print(f'   德文詞 (.d): {d_count}')
print(f'   中文互動詞 (.c): {c_count}')
if d_count + c_count > 0:
    print(f'   德文佔比: {d_count/(d_count+c_count)*100:.1f}%')
print(f'   仍需手動翻譯: {unknown}')

if unknown > 0:
    remaining = re.findall(r'<span class="d">([^<]+)<span class="t">（德）</span></span>', html)
    cc = collections.Counter(remaining)
    print(f'\n   剩餘未翻譯詞 (前30)：')
    for w, cnt in cc.most_common(30):
        print(f'     {cnt:3d}  {w}')
