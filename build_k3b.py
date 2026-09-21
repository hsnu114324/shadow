# -*- coding: utf-8 -*-
"""Kapitel 3 第二部分：追加剩餘內容到 page5.html"""
import re

TARGET = 'page5.html'

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

lines = []

# ─── Iris running through city ───
lines.append(L(
    D('Was in aller Welt passiert hier?','到底發生了什麼事？')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('rannte','跑著'),
    D('spät','深'), C('在','in'), C('那個','der'),
    D('Nacht','夜裡'), C('透過','durch'), C('那個','die'),
    D('Stadt','城市'), C('和','und'), C('她的','ihr'),
    D('rotes','紅色的'), D('Haar','頭髮'),
    D('flatterte','飄動著'), C('在','im'), D('Wind','風中'), '。'
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('hatte','有'), D('gehört','聽說'), '，',
    C('一個','ein'), D('ganzes','整棟'), D('Gebäude','建築物'),
    C('是','sei'), D('zweigeteilt worden','被切成兩半了'), '。',
    D('Zuerst','起初'), D('hatte','有'), C('她','sie'),
    C('那些','den'), D('Berichten','報告'), C('不','nicht'),
    D('glauben wollen','想相信'), '，',
    C('然而','doch'), C('之後','nachdem'), C('她','sie'),
    C('自己','sich'), D('leicht','稍微'),
    D('misstrauisch','懷疑地'), C('在','auf'),
    C('那個','den'), D('Weg','路'), D('gemacht hatte','出發了'), '，',
    D('erfuhr','得知了'), C('她','sie'), C('總是','immer'),
    C('更多','mehr'), D('dergleichen','類似的事'), '。'
))
lines.append('')

lines.append(L(
    C('在','In'), C('那整個','der ganzen'), D('Hauptstadt','王都'),
    D('fanden','正在發生'), D('groß angelegte','大規模的'), '，',
    D('simultane','同時的'), D('Angriffe','攻擊'), D('statt',''), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), D('dauerte','花了'), C('不','nicht'),
    D('lange','很久'), '，', C('直到','bis'), C('她','sie'),
    C('去','zu'), C('這個','diesem'), D('Schluss','結論'),
    D('gekommen war','得出了'), '。',
    D('Allerdings','然而'), D('stimmte','不對勁'),
    C('用','mit'), C('那些','den'), D('Zielen','目標'),
    C('的','der'), D('Angriffe','攻擊'), C('某些','etwas'),
    C('不','nicht'), '。',
    C('一個','Ein'), D('Handelshaus','商行'), '，',
    C('一個','ein'), D('Lagerhaus','倉庫'), '，',
    C('一個','ein'), D('Restaurant','餐廳'), C('和','und'),
    C('那個','die'), D('Privatresidenz','私邸'),
    C('一個','eines'), D('Adligen','貴族的'), '...',
    C('她們','Sie'), D('hatten','有'), C('沒有','keine'),
    D('Verbindung','關聯'), D('zueinander','彼此'), '。',
    C('那些','Die'), D('Angriffe','攻擊'), C('是','waren'),
    C('沒有','ohne'), D('Zweifel','疑問'), D('gut','好地'),
    D('geplant','計畫的'), '，', C('但是','aber'),
    C('她們的','ihr'), D('Zweck','目的'), C('是','war'),
    D('Iris','Iris'), C('不','nicht'), D('klar','清楚'), '。'
))
lines.append('')

lines.append(L(
    D('Tatsache','事實'), C('是','war'), C('然而','jedoch'), '，',
    C('說','dass'), C('那整個','die gesamte'), D('Hauptstadt','王都'),
    D('bebte','震動著'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Ritterorden','騎士團'), D('wurde','被'),
    C('在','in'), D('aller Eile','匆忙地'),
    D('mobilisiert','動員了'), C('和','und'),
    C('那個','die'), D('Evakuierung','疏散'),
    D('wichtiger','重要的'), D('Persönlichkeiten','人物'),
    D('begann','開始了'), '。'
))
lines.append('')

lines.append(L(
    D('Irgendetwas','某件事'), D('passierte','正在發生'),
    C('這裡','hier'), C('和','und'), C('它','es'), C('是','war'),
    C('沒有','kein'), D('gewöhnlicher','普通的'),
    D('Vorfall','事件'), '。',
    C('那','Das'), D('sagte','告訴了'), C('她','ihr'),
    C('她的','ihr'), D('Bauchgefühl','直覺'), '。'
))
lines.append('')

# ─── Monster encounter ───
lines.append(L(
    C('然而','Doch'), D('plötzlich','突然'),
    D('erreichte','傳到了'), C('一個','ein'),
    D('Schrei','喊聲'), C('她的','ihre'), D('Ohren','耳朵'), '。'
))
lines.append('')

lines.append(L(
    D('„E-Ein Monster!!','「一……一個怪物！！'),
    D('Wir brauchen Verstärkung ...!!"','我們需要增援……！！」')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('änderte','改變了'), C('她的','ihren'),
    D('Kurs','方向'), C('和','und'), D('rannte','跑向了'),
    C('在','in'), C('那個','die'), D('Richtung','方向'),
    C('的','des'), D('Schreis','喊聲'), '。',
    C('那裡','dort'), D('fand','找到了'), C('她','sie'),
    C('那個','besagtes'), D('Monster','怪物'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), C('是','war'), C('一個','ein'),
    D('widerlicher','噁心的'), D('Koloss','巨像'), '，',
    C('一個','ein'), D('Ungeheuer','怪物'), '。'
))
lines.append('')

lines.append(L(
    D('„Was zum Teufel ist das?"','「那到底是什麼東西？」')
))
lines.append('')

lines.append(L(
    D('flüsterte','低語著'), D('Iris','Iris'),
    C('和','und'), D('setzte sich','動了起來'),
    C('在','in'), D('Bewegung',''), '。'
))
lines.append('')

lines.append(L(
    D('„Zieht euch zurück!"','「退後！」')
))
lines.append('')

lines.append(L(
    C('用','Mit'), C('一個','einer'), D('fließenden','流暢的'),
    D('Bewegung','動作'), D('zog','拔出了'), C('她','sie'),
    C('她的','ihr'), D('Schwert','劍'), C('和','und'),
    C('用','mit'), C('一個','einem'), D('hellen','明亮的'),
    D('Strahl','光芒'), C('在','in'), C('那個','der'),
    D('Dunkelheit','黑暗中'), D('stieß','刺穿了'),
    C('她','sie'), C('透過','durch'), C('那個','den'),
    D('Torso','軀幹'), C('的','des'), D('Monsters','怪物的'), '。'
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('zerteilte','劈開了'), C('它','es'), '。'
))
lines.append('')

lines.append(L(
    C('用','Mit'), C('只','nur'), C('一個','einem'),
    D('Schlag','一擊'), D('spaltete','劈開了'), C('她','sie'),
    C('這個','dieses'), D('gewaltige','巨大的'), D('Monster','怪物'), '。'
))
lines.append('')

lines.append(L(
    D('„Seid ihr verletzt?"','「你們受傷了嗎？」'), '，',
    D('rief','喊道'), D('Iris','Iris'), C('那些','den'),
    D('Rittern','騎士們'), C('去','zu'), '。'
))
lines.append('')

lines.append(L(
    D('„Prinzessin Iris! Ihr habt uns gerettet ...!"','「Iris公主殿下！您救了我們……！」'),
    D('„Ihr seid unglaublich, Prinzessin Iris!','「您太厲害了，Iris公主殿下！'),
    D('Mit nur einem Schlag habt Ihr dieses Monster besiegt!"','只用一擊就打倒了這個怪物！」')
))
lines.append('')

lines.append(L(
    D('„Acht von uns wurden getötet."','「我們有八個人被殺了。」')
))
lines.append('')

lines.append(L(
    C('在','Beim'), D('Anblick','看見'), C('的','der'),
    D('verstümmelten','殘缺不全的'), D('Leichen','屍體'),
    D('zitterten','顫抖著'), D('Iris\'','Iris的'),
    D('weinrote','酒紅色的'), D('Augen','眼睛'),
    C('在','vor'), D('Trauer','悲傷'), '。'
))
lines.append('')

lines.append(L(
    D('„Prinzessin Iris!"','「Iris公主殿下！」'), '，',
    D('rief','喊道'), D('plötzlich','突然'),
    C('一個','einer'), C('的','der'), D('Ritter','騎士'),
    C('和','und'), D('deutete','指向了'), C('在','hinter'),
    C('她','sie'), '。'
))
lines.append('')

lines.append(L(
    D('„Was zum ...?!"','「什麼……？！」')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('zog','拔出了'), C('如此','so'),
    D('schnell','快'), C('她','sie'), D('konnte','可以'),
    C('她的','ihr'), D('Schwert','劍'), '，',
    D('drehte sich um','轉過身'), C('和','und'), '...',
    D('kollidierte','撞上了'), C('用','mit'), C('那個','dem'),
    D('rechten','右'), D('Arm','手臂'), C('的','des'),
    D('Monsters','怪物的'), '。'
))
lines.append('')

lines.append(L(
    D('„Gah ...!"','「啊……！」')
))
lines.append('')

lines.append(L(
    D('„Es regeneriert sich ...?"','「它在再生……？」')
))
lines.append('')

lines.append(L(
    D('„Bleibt zurück"','「退後」'), '，',
    D('befahl','命令道'), D('Iris','Iris'), C('那些','den'),
    D('verstörten','驚恐的'), D('Rittern','騎士們'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Schlag','攻擊'), C('是','war'),
    D('schnell','快'), '，', D('kraftvoll','有力'),
    C('和','und'), D('schwer','沉重的'), '—',
    C('但是','aber'), D('einfallslos','缺乏創意'), '。'
))
lines.append('')

lines.append(L(
    D('„Doch nur ein Monster."','「終究只是個怪物。」')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('setzte','發動了'), C('去','zu'),
    C('一個','einem'), D('unerbittlichen','無情的'),
    D('Gegenangriff','反擊'), D('an',''), '。',
    C('她','Sie'), D('schlitzte','割開了'), C('那些','die'),
    D('Arme','手臂'), C('的','des'), D('Monsters','怪物'),
    D('auf',''), '，', D('trennte','砍斷了'),
    C('它的','seine'), D('Beine','腿'), D('ab',''),
    C('和','und'), D('enthauptete','斬首了'), C('它','es'), '。'
))
lines.append('')

lines.append(L(
    C('但是','Aber'), C('它','es'), D('half','幫助了'),
    C('什麼都不','nichts'), '。'
))
lines.append('')

lines.append(L(
    D('„Es regeneriert sich immer noch?!"','「它還在再生？！」')
))
lines.append('')

lines.append(L(
    D('„Das könnte eine Weile dauern."','「這可能要花一段時間。」')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('gab','放棄了'), C('那個','die'),
    D('Hoffnung','希望'), C('在','auf'), C('一個','einen'),
    D('schnellen','快速的'), D('Sieg','勝利'), D('auf',''),
    C('和','und'), D('beschloss','決定'), '，',
    C('這個','diesen'), D('Kampf','戰鬥'), D('ernst','認真地'),
    C('去','zu'), D('nehmen','對待'), '。'
))
lines.append('')

lines.append(L(
    D('Verlieren','輸'), C('是','war'), C('為了','für'),
    C('她','sie'), C('沒有','keine'), D('Option','選項'), '。'
))
lines.append('')

# ─── Alpha appears ───
lines.append(L(
    C('但是','Aber'), C('然後','dann'), D('erklang','響起了'),
    C('一個','ein'), D('schriller','尖銳的'), D('Ton','聲音'),
    C('和','und'), D('Iris','Iris'), D('wurde','被'),
    C('那個','das'), D('Schwert','劍'), C('從','aus'),
    C('那些','den'), D('Händen','手中'),
    D('geschlagen','打掉了'), '。'
))
lines.append('')

lines.append(L(
    D('„Kannst du nicht sehen, wie sie leidet?','「你難道看不到她有多痛苦嗎？'),
    D('Wieso verstehst du das nicht?"','你為什麼不理解呢？」')
))
lines.append('')

lines.append(L(
    C('它','Es'), C('是','war'), C('一個','eine'),
    D('Frau','女人'), C('在','in'), C('一個','einem'),
    D('pechschwarzen','漆黑的'), D('Bodysuit','緊身衣'), '。'
))
lines.append('')

lines.append(L(
    D('„Wer bist du?"','「你是誰？」'), '，',
    D('fragte','問道'), D('Iris','Iris'), '。'
))
lines.append('')

lines.append(L(
    D('„Alpha."','「Alpha。」')
))
lines.append('')

lines.append(L(
    D('Mehr','更多'), D('sagte','說'), C('那個','die'),
    D('Frau','女人'), C('不','nicht'), C('和','und'),
    D('wandte','轉過了'), D('Iris','Iris'), C('那個','den'),
    D('Rücken','背'), C('去','zu'), '。'
))
lines.append('')

lines.append(L(
    D('„Warte, was zur Hölle hast du vor?','「等等，你到底想幹什麼？'),
    D('Wenn du ein Feind des Ordens bist, werden wir keine Gnade ..."','如果你是騎士團的敵人，我們不會手下留情……」'),
    D('„Feind ..?"','「敵人……？」'), '，',
    D('unterbrach','打斷了'), D('Alpha','Alpha'),
    D('Iris','Iris'), C('和','und'), D('lachte','笑了'), '。'
))
lines.append('')

lines.append(L(
    D('„Wieso lachst du?"','「你為什麼笑？」')
))
lines.append('')

lines.append(L(
    D('„Feind ...','「敵人……'),
    D('Weißt du überhaupt, wovon du da redest?','你到底知不知道自己在說什麼？'),
    D('Ein Narr, der von nichts weiß, sollte dieses Wort nicht einmal in den Mund nehmen.','一個什麼都不知道的傻瓜連這個詞都不該說出口。'),
    D('Wie eingebildet."','多麼自以為是。」')
))
lines.append('')

lines.append(L(
    D('„Du verdammte..!"','「你這個該死的……！」')
))
lines.append('')

lines.append(L(
    D('Iris\'','Iris的'), D('Magie','魔力'),
    D('schwoll an','暴漲了'), '。'
))
lines.append('')

lines.append(L(
    D('Alpha','Alpha'), D('warf','投了'), C('然而','jedoch'),
    C('不','nicht'), C('一次','einmal'), C('一個','einen'),
    D('Blick','目光'), C('在','auf'), D('Iris','Iris'), '。',
    C('用','Mit'), C('那個','dem'), D('Rücken','背部'),
    C('去','zu'), C('她','ihr'), D('sagte','說道'), C('她','sie'), '：',
    D('„Das Publikum sollte sich von der Bühne fernhalten.','「觀眾應該遠離舞台。'),
    D('Also komm uns nicht in die Quere."','所以別妨礙我們。」')
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('beendete','結束了'), C('她的','ihren'),
    D('Satz','句子'), C('和','und'), D('ging','走向了'),
    D('langsam','慢慢地'), C('在','auf'), C('那個','das'),
    D('Monster','怪物'), C('去','zu'), '。'
))
lines.append('')

lines.append(L(
    D('„Publikum..?"','「觀眾……？」')
))
lines.append('')

lines.append(L(
    D('„Du armes Ding.','「你這可憐的東西。'),
    D('Das muss wehgetan haben."','那一定很痛吧。」'),
    D('Alpha','Alpha'), D('lief','走著'), D('weiter','繼續'),
    C('和','und'), D('redete','說著'), C('用','mit'),
    C('那個','dem'), D('Monster','怪物'), '。'
))
lines.append('')

lines.append(L(
    D('„Du musst nicht mehr leiden.','「你不必再受苦了。'),
    D('Nicht mehr traurig sein."','不必再難過了。」'),
    C('她的','Ihr'), D('pechschwarzes','漆黑的'), D('Schwert','劍'),
    D('verlängerte sich','延長了'), C('和','und'), D('wurde','變得'),
    D('größer','更大'), C('比','als'), D('Alpha','Alpha'), C('自己','selbst'), '。'
))
lines.append('')

lines.append(L(
    D('„Alles wird gut."','「一切都會好起來的。」')
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('machte','邁了'), D('einfach','只是'),
    C('一個','einen'), D('Schritt','一步'), C('往','nach'),
    D('vorn','前'), C('和','und'), D('schnitt','切開了'),
    C('那個','das'), D('Monster','怪物'), D('entzwei','成兩半'), '。'
))
lines.append('')

lines.append(L(
    C('沒有人','Niemand'), D('hatte','有'), C('它','es'),
    D('kommen sehen','看到它來'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('riesige','巨大的'), D('Körper','身體'),
    C('的','des'), D('Monsters','怪物'), D('fiel','倒塌了'),
    C('在','in'), C('自己','sich'), D('zusammen',''), '。',
    C('他','Er'), D('schrumpfte','縮小了'), '，',
    D('stieß','散發出了'), D('weißen','白色的'), D('Dampf','蒸汽'),
    D('aus',''), C('和','und'), D('wurde','變得'),
    C('如此','so'), D('klein','小'), C('像','wie'),
    C('那個','der'), C('一個','eines'), D('Mädchens','女孩的'), '。',
    C('從','Aus'), C('它的','seiner'), D('linken','左'),
    D('Hand','手中'), D('fiel','掉落了'), C('一個','ein'),
    D('Kurzschwert','短劍'), '。'
))
lines.append('')

lines.append(L(
    C('在','An'), C('它的','dessen'), D('Griff','握柄上'),
    C('是','war'), C('一個','ein'), D('roter','紅色的'),
    D('Juwel','寶石'), D('befestigt','鑲嵌著'), '。'
))
lines.append('')

lines.append(L(
    C('在','Auf'), C('他','ihm'), D('stand','寫著'), '：',
    D('Für meine geliebte Tochter Milia.','獻給我摯愛的女兒Milia。')
))
lines.append('')

lines.append(L(
    D('„Möge dein nächstes Leben ... ein glückliches sein."','「願你的來世……是幸福的。」'),
    C('用','Mit'), C('這些','diesen'), D('Worten','話語'),
    D('verschwand','消失了'), D('Alpha','Alpha'),
    C('在','in'), C('那個','der'), D('weißen','白色的'),
    D('Dampfwolke','蒸汽雲中'), '。'
))
lines.append('')

lines.append(L(
    C('從','Aus'), C('那個','der'), D('Ferne','遠方'),
    D('erschallte','響起了'), D('Donnergrollen','雷鳴'), '。',
    D('Iris','Iris'), D('stand','站著'), C('只','nur'),
    D('fassungslos','呆呆地'), C('那裡','da'), '，',
    D('durchnässt','渾身濕透'), C('從','vom'), D('Regen','雨水'), '。'
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('zitterte','顫抖著'), '。'
))
lines.append('')

lines.append(L(
    D('„Alexia..."','「Alexia……」'), '，',
    D('murmelte','喃喃說道'), C('她','sie'), '。',
    D('„Alexia, bitte sei in Sicherheit ..."','「Alexia，請你平安……」'),
    D('Iris','Iris'), D('hob','撿起了'), C('她的','ihr'),
    D('Schwert','劍'), D('auf',''), C('和','und'),
    D('begann','開始'), C('去','zu'), D('laufen','跑'), '。'
))

lines.append(BRK())

# ─── Alexia meets Zenon ───
lines.append(L(
    D('„W-Was machst du hier...?!"','「你……你在這裡做什麼……？！」')
))
lines.append('')

lines.append(L(
    D('Blondes','金色的'), D('Haar','頭髮'), '，',
    D('gepflegtes','整潔的'), D('Gesicht','臉'),
    C('和','und'), C('一個','ein'), D('selbstbewusstes','自信的'),
    D('Lächeln','微笑'), '。',
    C('沒有','Kein'), D('anderer','其他的'), C('比','als'),
    D('Herr Zenon','Zenon大人'), D('stand','站在'),
    C('在','vor'), C('她','ihr'), '。'
))
lines.append('')

lines.append(L(
    D('„Da bin ich aber erleichtert.','「那我就放心了。'),
    D('Ich dachte schon immer, dass du verrückt bist.','我一直覺得你是瘋子。'),
    D('Wer hätte gedacht, dass ich recht habe"','誰能想到我是對的呢」'), '，',
    D('sagte','說道'), D('Alexia','Alexia'), '。'
))
lines.append('')

lines.append(L(
    D('„Vielleicht hast du recht.','「也許你是對的。'),
    D('Aber solange ich dein Blut bekomme, macht das keinen Unterschied."','但只要我得到你的血，就沒有差別。」')
))
lines.append('')

lines.append(L(
    D('„Immer dieses Gerede über Blut.','「老是在說血的事。'),
    D('Hast du zu viel über Vampire gelesen?"','你看了太多吸血鬼的書嗎？」'),
    D('„Du liegst gar nicht mal so weit daneben."','「你猜得其實不遠。」')
))
lines.append('')

lines.append(L(
    D('„Spar dir die Erklärungen.','「省下你的解釋吧。'),
    D('Mich interessiert so okkultes Zeug nicht."','我對那種神秘學的東西沒興趣。」'),
    D('„Zu schade."','「太可惜了。」')
))
lines.append('')

lines.append(L(
    D('„Du weißt bestimmt, dass hier bald die Ritter eintreffen werden, oder?','「你肯定知道騎士們很快就會趕到這裡，對吧？'),
    D('Das ist dein Ende."','你完了。」'),
    D('„Ende? Was genau soll hier enden?"','「完了？到底什麼要完了？」'), '，',
    D('fragte','問道'), D('Zenon','Zenon'), C('用','mit'),
    C('那個','dem'), D('gleichen','同樣'), D('selbstbewussten','自信的'),
    D('Lächeln','微笑'), '。'
))
lines.append('')

lines.append(L(
    D('„Dir werden dein Posten und dein Ansehen genommen und man wird dich hinrichten.','「你會被剝奪職位和名譽然後被處死。'),
    D('Ich selbst werde die Guillotine auf dich fallen lassen."','我會親自讓斷頭台落在你身上。」')
))
lines.append('')

lines.append(L(
    D('„Das wird alles nicht passieren.','「那些都不會發生。'),
    D('Ich werde mit dir durch den Geheimgang entkommen."','我會帶著你通過密道逃走。」')
))
lines.append('')

lines.append(L(
    D('„Wie romantisch von dir, aber leider hasse ich dich zutiefst."','「你真浪漫，但可惜我打從心底討厭你。」')
))
lines.append('')

# ─── Alexia vs Zenon fight ───
lines.append(L(
    D('„Die Runde? Ist das ein Klub für Verrückte oder so?"','「圓桌？那是瘋子俱樂部之類的嗎？」')
))
lines.append('')

lines.append(L(
    D('„Mir egal. Ich hab\'s satt, über Blut zu reden."','「我不管。我受夠了談血的事了。」'),
    D('„Ich werde dich umbringen."','「我要殺了你。」')
))
lines.append('')

lines.append(L(
    D('Alexias','Alexia的'), D('energischer','有力的'),
    D('Schlag','攻擊'), D('signalisierte','宣告了'),
    C('那個','den'), D('Beginn','開始'), C('的','des'),
    D('Kampfes','戰鬥的'), '。'
))
lines.append('')

lines.append(L(
    D('„Da ist wohl jemand wütend."','「有人生氣了呢。」')
))
lines.append('')

lines.append(L(
    D('Zenon','Zenon'), D('wehrte','擋住了'), C('那個','den'),
    D('Hieb','攻擊'), C('正好','gerade'), C('還','noch'),
    D('rechtzeitig','及時地'), D('ab',''),
    C('和','und'), D('parierte','格擋了'), C('也','auch'),
    D('Alexias','Alexia的'), D('nächste','下一波'),
    D('Angriffe','攻擊'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), C('是','war'), C('在','im'),
    D('Nachteil','劣勢'), '。'
))
lines.append('')

lines.append(L(
    D('„Kaum sehen wir uns ein paar Tage nicht, kämpfst du auf einmal mit billigen Schwertern?"','「才幾天不見，你就用起廉價的劍來戰鬥了？」')
))
lines.append('')

lines.append(L(
    D('„Du weißt, was man sagt:','「你知道俗話怎麼說：'),
    D('Ein wahrer Meister sucht sich sein Schwert nicht aus."','真正的大師不會挑劍。」')
))
lines.append('')

lines.append(L(
    D('„Verstehe. Für einen Meister gilt das vielleicht."','「我懂。對大師來說也許是那樣。」'),
    D('Zenon','Zenon'), D('lachte','笑了'), '。',
    D('„Aber du bist nur Durchschnitt.','「但你只是平庸。'),
    D('Als dein Lehrer kann ich dir das versichern."','作為你的老師我可以向你保證。」')
))
lines.append('')

lines.append(L(
    D('„Dann sieh gut hin.','「那你看好了。'),
    D('Sieh selbst, ob ich wirklich so durchschnittlich bin."','看看我是不是真的那麼平庸。」')
))
lines.append('')

lines.append(L(
    D('„Haaaaaaaah!!!"','「哈啊啊啊啊啊！！！」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Schlag','攻擊'), D('hatte','有'),
    D('große Ähnlichkeit','很大的相似之處'), C('用','mit'),
    D('Prinzessin Iris\'','Iris公主的'), D('Schwertkunst','劍術'), '。'
))
lines.append('')

lines.append(L(
    C('去','Zum'), D('ersten Mal','第一次'),
    D('verschwand','消失了'), C('那個','das'), D('Lächeln','微笑'),
    C('從','aus'), D('Zenons','Zenon的'), D('Gesicht','臉上'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), C('是','war'), C('在','im'),
    D('Vorteil','優勢'), '。'
))
lines.append('')

lines.append(L(
    C('一個','Ein'), D('einzelner','一條'), D('roter','紅色的'),
    D('Strich','線'), D('erschien','出現了'),
    C('在','auf'), D('Zenons','Zenon的'), D('Wange','臉頰上'), '。'
))
lines.append('')

lines.append(L(
    D('„Erstaunlich."','「驚人。」')
))
lines.append('')

lines.append(L(
    D('„Du wirst es bereuen, mich zu unterschätzen"','「你會後悔小看我的」'), '，',
    D('drohte','威脅道'), D('Alexia','Alexia'), '。'
))
lines.append('')

lines.append(L(
    D('„Sicher, du hast mich überrascht,','「確實，你讓我吃了一驚，'),
    D('aber es war lediglich eine billige Imitation.','但那不過是廉價的模仿。'),
    D('Du bist noch weit entfernt vom Original."','你離原版還差得遠呢。」')
))
lines.append('')

# ─── Zenon powers up ───
lines.append(L(
    D('„Aber wenn wir schon dabei sind,','「但既然已經到了這步，'),
    D('sollte ich mich wohl auch ein wenig anstrengen"','我也應該稍微努力一下了」'), '，',
    D('sagte','說道'), D('Zenon','Zenon'), '。'
))
lines.append('')

lines.append(L(
    D('„Lass mich dir eines sagen.','「讓我告訴你一件事。'),
    D('Bis jetzt habe ich vor Außenstehenden noch nie meine wahre Stärke gezeigt.','到目前為止我從未在外人面前展示過我的真正實力。'),
    D('Die Stärke, die du jetzt sehen wirst, ist die des nächsten Ritters der Runde."','你現在將看到的，是下一位圓桌騎士的力量。」')
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Luft','空氣'), D('bebte','震動了'), '。'
))
lines.append('')

lines.append(L(
    C('她們','Sie'), D('befanden sich','處於'),
    C('在','auf'), D('komplett','完全'), D('anderen','不同的'),
    D('Niveaus','水平'), '。'
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('sah','看見了'), C('沒有','keinen'),
    D('Weg','方法'), '，', C('這個','dieses'),
    D('Schwert','劍'), D('abzuwehren','去抵擋'), '。'
))
lines.append('')

lines.append(L(
    D('Alexias','Alexia的'), D('Schwert','劍'), D('wurde','被'),
    D('einseitig','一面倒地'), D('zerstört','摧毀了'),
    C('和','und'), D('zerbrach','碎裂了'), '。'
))
lines.append('')

lines.append(L(
    D('„Du wirst nie so sein wie deine Schwester."','「你永遠不會像你姐姐一樣。」'),
    C('一個','Eine'), D('einzelne','一滴'), D('Träne','淚水'),
    D('löste sich','滑落了'), C('從','aus'), C('她的','ihrem'),
    D('Auge','眼中'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich werde dich mitnehmen."','「我會帶走你的。」')
))
lines.append('')

# ─── Shadow arrives ───
lines.append(L(
    C('然而','Doch'), C('然後','dann'), '。'
))
lines.append('')

lines.append(L(
    D('Klack Klack','喀嗒 喀嗒')
))
lines.append('')

lines.append(L(
    C('一個','Ein'), D('Geräusch','聲音'), D('hallte','迴盪著'),
    C('從','von'), C('那個','der'), D('Treppe','樓梯'),
    C('在','hinter'), D('Zenon','Zenon'), D('wider',''), '。'
))
lines.append('')

lines.append(L(
    D('Klack Klack Klack Klack','喀嗒 喀嗒 喀嗒 喀嗒')
))
lines.append('')

lines.append(L(
    C('一個','Ein'), D('Mann','男人'), C('用','mit'),
    C('一個','einem'), D('langen','長長的'),
    D('pechschwarzen','漆黑的'), D('Mantel','斗篷'), '。'
))
lines.append('')

lines.append(L(
    D('„Ein pechschwarz gekleideter Mann ...','「一個穿著漆黑衣服的男人……'),
    D('Bist du dieser Streuner, der in letzter Zeit die Hand des Kults gebissen hat?"','你就是最近一直在咬教團的那個流浪者嗎？」')
))
lines.append('')

lines.append(L(
    D('„Mein Name ist Shadow.','「我的名字是Shadow。'),
    D('Jener, der im Schatten lauert und die Schatten jagt..."','潛伏於陰影之中，追獵陰影之人……」')
))
lines.append('')

lines.append(L(
    C('他的','Seine'), D('Stimme','聲音'), C('是','war'),
    D('tief','低沉'), C('和','und'), D('leise','輕柔的'), '，',
    C('好像','als'), D('käme','來自'), C('她','sie'),
    C('從','aus'), C('那個','dem'), D('Abgrund','深淵'),
    C('自己','selbst'), '。'
))
lines.append('')

# ─── Shadow vs Zenon ───
lines.append(L(
    D('„Wo ist dieses mächtige Mitglied?"','「那個厲害的成員在哪裡？」')
))
lines.append('')

lines.append(L(
    D('Zenons','Zenon的'), D('Gesicht','臉'),
    D('verzog sich','扭曲了'), C('在','vor'),
    D('Demütigung','屈辱'), '。'
))
lines.append('')

lines.append(L(
    D('„Wie ist das möglich ..?!"','「這怎麼可能……？！」')
))
lines.append('')

lines.append(L(
    D('Shadow','Shadow'), D('wollte sich','就是'), D('einfach','不'),
    C('不','nicht'), D('bewegen','動'), '。'
))
lines.append('')

lines.append(L(
    D('„Was ist los, nächster Ritter der Runde?"','「怎麼了，下一位圓桌騎士？」')
))
lines.append('')

lines.append(L(
    D('„UNTERSCHÄTZ MICH NICHT!!!"','「不要小看我！！！」')
))
lines.append('')

lines.append(L(
    D('Schreiend','吼叫著'), D('ging','衝向了'),
    D('Zenon','Zenon'), C('在','auf'), D('Shadow','Shadow'), D('los',''), '。'
))
lines.append('')

lines.append(L(
    C('然而','Doch'), C('沒有','kein'), D('einzelner','一個'),
    D('Stich','刺擊'), C('和','und'), C('沒有','kein'),
    D('einzelner','一個'), D('Schlag','攻擊'),
    D('konnte','能'), D('Shadow','Shadow'),
    D('erreichen','觸及到'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('beobachtete','觀察著'),
    C('那個','den'), D('Kampf','戰鬥'), D('voller','充滿'),
    D('Entsetzen','恐懼'), '。',
    C('它','Es'), C('是','war'), '，', C('好像','als würde'),
    C('自己','sich'), C('一個','ein'), D('Kind','孩子'),
    C('對抗','gegen'), C('一個','einen'), D('Erwachsenen','成年人'),
    D('auflehnen','反抗'), '。'
))
lines.append('')

lines.append(L(
    D('Unbewusst','不知不覺地'), D('hatte','有'),
    D('Alexia','Alexia'), D('angefangen','開始了'), '，',
    C('那個','dem'), D('Training','訓練'),
    C('用','mit'), C('那些','den'), D('Augen','眼睛'),
    C('去','zu'), D('folgen','追蹤'), '。',
    C('因為','Denn'), C('那個','die'), D('Schwertkunst','劍術'),
    C('是','war'), '...'
))
lines.append('')

lines.append(L(
    D('Durchschnittsschwertkunst.','平庸的劍術。')
))
lines.append('')

lines.append(L(
    C('它','Es'), C('是','war'), C('那個','die'),
    D('perfektionierte','完美化的'), D('Form','形式'),
    C('的','von'), D('Alexias','Alexia的'),
    D('Schwertkunst','劍術'), '。'
))
lines.append('')

lines.append(L(
    D('„Unglaublich..."','「不可思議……」')
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('liebte','愛著'),
    C('這個','diese'), D('Schwertkunst','劍術'), '。'
))
lines.append('')

# ─── Zenon defeated ───
lines.append(L(
    D('„Gah... Verdammt..!"','「啊……可惡……！」')
))
lines.append('')

lines.append(L(
    D('Zenon','Zenon'), D('flog','飛了'), C('透過','durch'),
    C('那個','die'), D('Luft','空中'), C('和','und'),
    D('knallte','摔在了'), C('在','auf'), C('那個','den'),
    D('Boden','地上'), '。'
))
lines.append('')

lines.append(L(
    D('„D-Du Bastard!','「你……你這混蛋！'),
    D('Wer zum Teufel bist du ...?','你到底是誰……？'),
    D('Wieso versteckst du deine Identität, wenn du so viel Macht hast?!"','你有這麼大的力量為什麼要隱藏身分？！」')
))
lines.append('')

lines.append(L(
    D('„Wir sind Shadow Garden.','「我們是Shadow Garden。'),
    D('Jene, die im Schatten lauern und die Schatten jagen.','潛伏於陰影之中，追獵陰影之人。'),
    D('Uns gibt es nur zu diesem Zweck."','我們只為此目的而存在。」')
))
lines.append('')

# ─── Zenon takes pill ───
lines.append(L(
    D('„Na gut.','「好吧。'),
    D('Wenn du es unbedingt darauf ankommen lassen willst,','如果你一定要逼到這步的話，'),
    D('dann werde ich es dir zeigen."','那我就給你看看。」'),
    D('Zenon','Zenon'), D('holte','拿出了'), C('一個','eine'),
    D('rote','紅色的'), D('Pille','藥丸'), C('從','aus'),
    C('他的','seiner'), D('Tasche','口袋'), '。'
))
lines.append('')

lines.append(L(
    D('„Dritte Erweckung."','「第三覺醒。」')
))
lines.append('')

lines.append(L(
    C('一個','Ein'), D('Sturm','風暴'), C('從','aus'),
    D('Magie','魔力'), D('bildete sich','形成了'),
    C('在','um'), D('Zenon','Zenon'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich werde dir zeigen, was wahre Macht ist."','「我要讓你看看什麼是真正的力量。」')
))
lines.append('')

lines.append(L(
    D('„Hässlich."','「醜陋。」')
))
lines.append('')

lines.append(L(
    D('„Wie hässlich"','「多麼醜陋」'), '，',
    D('sprach','說道'), D('Shadow','Shadow'), C('在','im'),
    D('selben','同一'), D('Moment','瞬間'), '。'
))
lines.append('')

lines.append(L(
    C('她們','Sie'), D('teilten','共享著'), C('她們的','ihre'),
    D('Schwertkunst','劍術'), C('和','und'), C('她們的','ihre'),
    D('Gedanken','想法'), '。'
))
lines.append('')

lines.append(L(
    D('„Maße dir nicht an, dies als wahre Macht zu bezeichnen.','「你不配把這稱為真正的力量。'),
    D('Das beleidigt die wirklich Mächtigen."','那是在侮辱真正強大的人。」')
))
lines.append('')

lines.append(L(
    D('„Geliehene Macht ist nicht der Weg zu wahrer Stärke."','「借來的力量不是通往真正強大的道路。」')
))
lines.append('')

# ─── I am Atomic ───
lines.append(L(
    C('去','Zum'), D('ersten Mal','第一次'), C('在','an'),
    C('這個','diesem'), D('Tag','日子'), D('erhöhte','提高了'),
    D('Shadow','Shadow'), C('他的','seine'), D('magische','魔法'),
    D('Kraft','力量'), '。'
))
lines.append('')

lines.append(L(
    C('他的','Seine'), D('stärker werdende','增強的'),
    D('Magie','魔力'), D('manifestierte sich','顯現為'),
    C('在','in'), D('Form','形式'), D('blau-violetter','藍紫色的'),
    D('Linien','線條'), '。'
))
lines.append('')

lines.append(L(
    D('„Wie schön ..."','「多麼美麗……」')
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('bewunderte','讚嘆著'), C('她們','sie'), '。'
))
lines.append('')

lines.append(L(
    D('„Was ... ist das ….?"','「那……那是什麼……？」')
))
lines.append('')

lines.append(L(
    D('„Das ist wahre Macht ...','「這是真正的力量……'),
    D('Brenne den Anblick in deine Augen."','把這景象刻進你的眼睛裡。」')
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Magie','魔力'), D('sammelte sich','聚集在了'),
    C('在','auf'), C('那個','der'), D('pechschwarzen','漆黑的'),
    D('Klinge','刀刃上'), C('和','und'), D('gravierte','刻下了'),
    C('一個','ein'), D('Muster','圖案'), D('hinein',''), '。',
    C('一個','Eine'), D('Spirale','螺旋'), '，', C('那個','die'),
    C('總是','immer'), C('更多','mehr'), D('Magie','魔力'),
    D('bündelte','匯聚了'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Klinge','刀刃'),
    D('beherbergte','蘊含著'), C('一個','eine'),
    D('entsetzliche','恐怖的'), D('Kraft','力量'), '。'
))
lines.append('')

lines.append(L(
    D('„Das ist mein Magnum Opus"','「這是我的最高傑作」'), '，',
    D('sprach','說道'), D('Shadow','Shadow'), C('現在','nun'), '，',
    D('hob','舉起了'), C('他的','sein'), D('Schwert','劍'),
    C('和','und'), D('positionierte sich','擺好了姿勢'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Stellung','架勢'), C('為了','für'),
    C('一個','einen'), D('Stich','刺擊'), '。'
))
lines.append('')

lines.append(L(
    D('„H-Hör auf..."','「住……住手……」')
))
lines.append('')

lines.append(L(
    D('Alles','一切'), D('zitterte','顫抖著'), '。'
))
lines.append('')

lines.append(L(
    C('也','Auch'), D('Alexia','Alexia'), D('hatte','有'),
    D('angefangen','開始了'), C('去','zu'), D('zittern','顫抖'), '。',
    C('但是','Aber'), C('她','sie'), D('wusste','知道'), '，',
    C('說','dass'), C('它','es'), C('不','nicht'), C('從','aus'),
    D('Angst','恐懼'), D('geschah','發生'), '，',
    C('而是','sondern'), C('在','vor'), D('Freude','喜悅'), '。'
))
lines.append('')

lines.append(L(
    C('那','Das'), C('是','war'), C('那個','der'),
    D('Endpunkt','終點'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Perfektion','完美'), C('的','des'),
    D('Schwertes','劍的'), '。'
))
lines.append('')

lines.append(L(
    D('„Sieh gut hin..."','「看好了……」')
))
lines.append('')

lines.append(L(
    D('„Ultimative Technik: I. am. Atomic."','「究極技：I. am. Atomic。」'),
    C('和','Und'), D('wurde','被'), D('entfesselt','釋放了'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Welt','世界'), D('verstummte','沉默了'), '。'
))
lines.append('')

lines.append(L(
    C('一個','Ein'), D('Strom','洪流'), C('從','aus'),
    D('Licht','光'), D('verschlang','吞噬了'),
    D('Zenon','Zenon'), '。',
    C('那些','Die'), D('Wände','牆壁'), '，',
    C('那個','die'), D('Erde','大地'), '，',
    D('alles','一切'), D('wurde','被'), D('durchbohrt','貫穿了'),
    C('和','und'), D('verschlungen','吞噬了'), '。'
))
lines.append('')

lines.append(L(
    C('直到','Bis'), C('他','er'), D('schließlich','最終'),
    D('explodierte','爆炸了'), '。'
))
lines.append('')

lines.append(L(
    C('一個','Ein'), D('Muster','圖案'), C('從','aus'),
    D('Licht','光'), D('zeichnete sich','繪製在了'),
    C('在','in'), C('那個','den'), D('Himmel','天空中'),
    C('和','und'), C('那個','die'), D('Königliche Hauptstadt','王都'),
    D('wurde','被'), D('blau-violett','藍紫色地'),
    D('gefärbt','染上了'), '。'
))
lines.append('')

lines.append(L(
    D('Zenon','Zenon'), D('hatte sich','已經'),
    C('在','in'), D('Nichts','虛無'), D('aufgelöst','消散了'), '，',
    C('沒有','ohne'), C('也','auch'), C('只','nur'),
    C('一個','ein'), D('Staubkorn','灰塵'),
    C('去','zu'), D('hinterlassen','留下'), '。'
))
lines.append('')

lines.append(L(
    D('Shadows','Shadow的'), D('pechschwarzer','漆黑的'),
    D('Mantel','斗篷'), D('flatterte','飄動了'),
    C('還','noch'), C('一次','einmal'), C('和','und'),
    C('他','er'), D('verschwand','消失了'), '。'
))

lines.append(BRK())

# ─── I am Atomic backstory ───
lines.append(L(
    C('它','Es'), D('gab','有'), C('一次','einmal'),
    C('一個','einen'), D('Mann','男人'), '，',
    C('那個','der'), C('那個','die'), D('Atombombe','原子彈'),
    D('herausforderte','挑戰了'), '。'
))
lines.append('')

lines.append(L(
    C('他','Er'), D('trainierte','鍛鍊了'), C('他的','seinen'),
    D('Körper','身體'), '，', D('stählte','磨練了'),
    C('他的','seinen'), D('Geist','精神'), C('和','und'),
    D('beherrschte','掌握了'), D('viele','很多'),
    D('Fähigkeiten','技能'), '。'
))
lines.append('')

lines.append(L(
    C('但是','Aber'), C('那個','die'), D('Atombombe','原子彈'),
    C('是','war'), C('總是','immer'), C('還','noch'),
    D('viel zu weit','太過遙遠'), C('的','von'),
    C('他','ihm'), D('entfernt',''), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('gefundene','找到的'), D('Antwort','答案'),
    D('lautete','是'), '：',
    C('人們','Man'), D('musste','必須'), D('einfach','就'),
    C('自己','selbst'), C('到','zur'), D('Atombombe','原子彈'),
    D('werden','成為'), '。'
))
lines.append('')

lines.append(L(
    C('從','Aus'), C('這個','dieser'), D('simplen','簡單的'),
    D('Antwort','答案'), D('wurde','誕生了'), C('那個','die'),
    D('ultimative Technik','究極技'), D('I am Atomic','I am Atomic'), '。',
    C('她','Sie'), D('entfaltete','釋放了'), C('一個','eine'),
    D('buchstäblich','字面上的'), D('atomare','原子級的'),
    D('Kraft','力量'), '！'
))

lines.append(BRK())

# ─── Alexia and Iris reunion ───
lines.append(L(
    D('„Alexia ... Alexia...!!"','「Alexia……Alexia……！！」')
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('erkannte','認出了'),
    C('那個','die'), D('Stimme','聲音'), '。'
))
lines.append('')

lines.append(L(
    D('„Schwester ... Iris ..."','「姐姐……Iris……」'), '，',
    D('rief','喊道'), C('她','sie'), C('和','und'),
    D('begann','開始了'), C('去','zu'), D('rennen','跑'), '。'
))
lines.append('')

lines.append(L(
    D('„Alexia! Alexia!"','「Alexia！Alexia！」')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('rannte','跑向了'), C('在','auf'),
    C('她','sie'), C('去','zu'), '。'
))
lines.append('')

lines.append(L(
    D('„Schwester ... I-Ich ..."','「姐姐……我……我……」')
))
lines.append('')

lines.append(L(
    D('Bevor','在……之前'), C('她','sie'), D('weitersprechen','繼續說'),
    D('konnte','可以'), '，', D('schlang','環住了'),
    D('Iris','Iris'), C('她的','ihre'), D('Arme','手臂'),
    C('在','um'), C('她','sie'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich bin so froh, dass du am Leben bist .. wirklich."','「我真高興你還活著……真的。」'),
    D('Iris\'','Iris的'), D('Umarmung','擁抱'),
    D('wurde','變得'), C('總是','immer'), D('fester','更緊'), '。'
))
lines.append('')

lines.append(L(
    D('Zaghaft','猶豫地'), D('drückte','回抱了'),
    D('Alexia','Alexia'), C('她','sie'), D('zurück',''), '。'
))
lines.append('')

lines.append(L(
    D('„Tut mir leid, ich bin bestimmt ganz kalt."','「對不起，我一定很冷。」'),
    D('Alexia','Alexia'), D('schüttelte','搖了搖'),
    C('在','an'), D('Iris\'','Iris的'), D('Brust','胸前'),
    C('那個','den'), D('Kopf','頭'), '。',
    C('她','Sie'), D('konnte','能'), C('那些','die'),
    D('Tränen','淚水'), C('不','nicht'), C('更多','mehr'),
    D('unterdrücken','壓抑住了'), '。'
))

lines.append(BRK())

# ─── Epilogue - on the roof ───
lines.append(L(
    C('在','Im'), D('Frühsommer','初夏'),
    D('standen','站著'), C('一個','eine'),
    D('Schülerin','女學生'), C('和','und'), C('一個','ein'),
    D('Schüler','男學生'), C('在','auf'), C('那個','dem'),
    D('Dach','屋頂'), C('的','der'), D('Akademie','學院上'), '。'
))
lines.append('')

lines.append(L(
    D('„Der Vorfall scheint noch viel tiefer zu gehen,','「這個事件似乎比想像中更深，'),
    D('aber oberflächlich wurde er erst einmal für gelöst erklärt."','但表面上暫時被宣布解決了。」')
))
lines.append('')

lines.append(L(
    D('„Klar, übertreib es nur nicht"','「好，只是別太勉強」'), '，',
    D('sagte','說道'), C('那個','der'), D('Junge','男孩'), '。'
))
lines.append('')

lines.append(L(
    D('„Du bist also entlastet.','「所以你被洗清嫌疑了。'),
    D('Tut mir leid, dass du da mit reingezogen wurdest."','對不起讓你被牽連了。」'),
    D('„Schon in Ordnung."','「沒關係。」')
))
lines.append('')

lines.append(L(
    D('„Warte. Ich muss dir noch zwei Dinge sagen."','「等等。我還有兩件事要跟你說。」')
))
lines.append('')

lines.append(L(
    D('„Erstens:','「第一：'),
    D('Ich wollte mich einfach nur bei dir bedanken.','我只是想謝謝你。'),
    D('Du hast damals gesagt, dass du meine Schwertkunst magst.','你那時候說過你喜歡我的劍術。'),
    D('Ich weiß, das kommt etwas spät, aber danke."','我知道有點晚了，但謝謝你。」')
))
lines.append('')

lines.append(L(
    D('„Ich habe meine Schwertkunst auch lieben gelernt.','「我也學會了愛我的劍術。'),
    D('Obwohl ich das nicht dir zu verdanken habe."','雖然這不是你的功勞。」'),
    D('„War der letzte Teil echt notwendig?"','「最後那句話真的有必要嗎？」'),
    D('„Ich sage nur die Wahrheit."','「我只是說實話。」')
))
lines.append('')

lines.append(L(
    D('„Und zweitens?"','「第二呢？」')
))
lines.append('')

lines.append(L(
    D('„Nun ...','「嗯……'),
    D('Wir haben ja nur wegen Zenon so getan, als wären wir zusammen,','我們只是因為Zenon才假裝在一起的，'),
    D('und jetzt, da er tot ist ..."','而現在他死了……」'),
    D('„Bin ich endlich frei"','「我終於自由了」'), '，',
    D('beendete','結束了'), C('那個','der'), D('Junge','男孩'),
    C('她的','ihren'), D('Satz','句子'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich hatte jedoch einen Vorschlag ..."','「不過我有一個建議……」'),
    D('„Also ... Wenn du kein Problem damit hättest ..."','「就是……如果你不介意的話……」')
))
lines.append('')

lines.append(L(
    D('„Dachte ich mir ... Wir könnten ja noch ein wenig weitermachen ..."','「我在想……我們可以繼續假裝一下……」'), '，',
    D('sagte','說道'), C('它','es'), C('用','mit'),
    D('leiser','輕柔的'), D('Stimme','聲音'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Junge','男孩'), D('lächelte','微笑著'),
    C('那個','das'), D('Mädchen','女孩'), D('breit','燦爛地'), D('an',''), '。'
))
lines.append('')

lines.append(L(
    D('„Nein danke"','「不了謝謝」'), '，',
    D('sagte','說道'), C('他','er'), C('和','und'),
    D('zeigte','對'), C('那個','dem'), D('Mädchen','女孩'),
    C('那個','den'), D('Mittelfinger','中指'), '。'
))
lines.append('')

lines.append(L(
    C('人們','Man'), D('hörte','聽到了'), C('只','nur'),
    C('還','noch'), '，', C('像','wie'), C('一個','ein'),
    D('Schwert','劍'), D('gezogen wurde','被拔出'), '。'
))
lines.append('')

lines.append(L(
    C('在','Am'), D('Abend','傍晚'), D('fanden','發現了'),
    C('一些','ein paar'), D('Schüler','學生們'),
    C('在','auf'), C('那個','dem'), D('Dach','屋頂'),
    C('一個','eine'), D('Blutlache','血泊'), D('vor',''), '。'
))
lines.append('')

lines.append(L(
    C('一個','Eine'), D('Leiche','屍體'), D('wurde','被'),
    C('在','in'), C('那個','der'), D('Nähe','附近'),
    C('然而','jedoch'), C('不','nicht'), D('gefunden','找到'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Fall','案件'), D('ging','成為了'),
    D('später','後來'), C('作為','als'),
    D('Der Mord ohne Leiche','無屍體謀殺案'),
    C('在','in'), C('那些','die'), D('sieben Mysterien','七大不可思議'),
    C('的','der'), D('Schule','學校'), D('ein',''), '。'
))

lines.append(BRK())

# ─── Epilogue: Alexia asks about apology + Schokolade scene ───
# This is very long, summarizing key parts
lines.append(L(
    D('Eines Tages','有一天'), D('stellte','問了'),
    D('Alexia','Alexia'), C('她的','ihrer'), D('Schwester','姐姐'),
    D('Iris','Iris'), C('一個','eine'), D('seltsame','奇怪的'),
    D('Frage','問題'), '。'
))
lines.append('')

lines.append(L(
    D('„Weißt du, wie man sich am besten entschuldigt,','「你知道怎麼道歉最好，'),
    D('sodass einem todsicher vergeben wird?"','讓別人一定會原諒你嗎？」')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('entschied','決定'), '，',
    C('那個','das'), D('Offensichtliche','顯而易見的'),
    C('去','zu'), D('sagen','說'), '：',
    D('„So eine Entschuldigung gibt es nicht."','「這樣的道歉是不存在的。」')
))
lines.append('')

lines.append(L(
    D('„Ich hasse es sowieso, mich zu entschuldigen"','「反正我討厭道歉」'), '，',
    D('sagte','說道'), D('Alexia','Alexia'), '。'
))
lines.append('')

lines.append(L(
    C('然而','Doch'), D('Iris','Iris'), D('hatte','有'),
    C('一個','eine'), D('neue','新的'), D('Mission','使命'), '。',
    C('她','Sie'), D('musste','必須'), C('某些','etwas'),
    C('為了','für'), C('她的','ihre'), D('Schwester','妹妹'),
    D('unternehmen','做點什麼'), '。'
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('beschloss','決定'), '，',
    C('自己','sich'), C('在','auf'), C('一個','ein'),
    D('Gerücht','傳聞'), C('去','zu'), D('verlassen','依靠'), '。',
    C('在','An'), C('她們的','ihrem'), D('ersten','第一個'),
    D('gemeinsamen','共同的'), D('freien Tag','休息日'),
    D('lud','邀請了'), C('她','sie'), D('Alexia','Alexia'),
    D('ein',''), '，', C('用','mit'), C('她','ihr'),
    C('在','in'), C('一個','ein'), D('Kaufhaus','百貨公司'),
    C('去','zu'), D('gehen','去'), '。'
))
lines.append('')

lines.append(L(
    D('„Was ist das hier für ein Ort, Iris?"','「這是什麼地方，Iris？」'),
    D('„Das Kaufhaus einer gewissen Mitsugoshi-Handelsgesellschaft."','「某個Mitsugoshi商會的百貨公司。」')
))
lines.append('')

lines.append(L(
    C('那裡','Da'), D('tauchte','出現了'), C('在','vor'),
    C('兩人','den beiden'), C('一個','eine'),
    D('wunderschöne','美麗的'), D('Elfe','精靈'),
    C('用','mit'), D('indigoblauem','靛藍色的'),
    D('Haar','頭髮'), D('auf',''), '。'
))
lines.append('')

lines.append(L(
    D('„Mein Name ist Luna und ich bin die Vorsitzende der Mitsugoshi-Handelsgesellschaft.','「我叫Luna，我是Mitsugoshi商會的會長。'),
    D('Dies hier ist unsere neueste Schokolade."','這是我們最新的巧克力。」')
))
lines.append('')

lines.append(L(
    D('„Dies ist ein Produkt, das wir erst kürzlich auf den Markt gebracht haben und Trüffel nennen."','「這是我們最近才推出市場的產品，叫做松露巧克力。」')
))
lines.append('')

lines.append(L(
    C('當','Als'), C('那些','die'), D('Trüffel','松露巧克力'),
    C('那些','die'), D('Zungen','舌頭'), C('的','der'),
    D('Schwestern','姊妹'), D('berührten','觸碰到了'), '，',
    D('leuchteten','亮了起來'), C('兩者','beider'),
    D('Gesichter','臉'), D('auf',''), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), C('像','wie'), D('Iris','Iris'),
    D('kauften','買了'), D('lauter','好多'),
    D('Schokoladen','巧克力'), D('verschiedener','不同的'),
    D('Sorten','口味'), '。'
))
lines.append('')

# ─── Tanga scene (abbreviated) ───
lines.append(L(
    D('Schließlich','最後'), D('wurde','被'),
    C('兩人','den beiden'), C('一個','ein'), D('kleines','小小的'),
    D('Stück Stoff','一塊布'), C('在','vor'), C('那個','die'),
    D('Nase','鼻子前'), D('gehalten','拿到了'), '。'
))
lines.append('')

lines.append(L(
    D('„Was ist das...?"','「這是什麼……？」')
))
lines.append('')

lines.append(L(
    D('„Das ist Damenunterwäsche"','「這是女性內衣」'), '，',
    D('erklärte','解釋道'), D('Luna','Luna'),
    D('höflich','禮貌地'), D('lächelnd','微笑著'), '。'
))
lines.append('')

lines.append(L(
    D('„Es ist ein Produkt namens Tanga."','「這是一種叫做丁字褲的產品。」')
))
lines.append('')

lines.append(L(
    D('„Ich habe Vertrauen in meinen Po!"','「我對我的屁股有信心！」')
))
lines.append('')

lines.append(L(
    D('„D-Darum geht es hier doch gar nicht!"','「根……根本不是那個問題！」')
))
lines.append('')

lines.append(L(
    D('„S-S-So eine unanständige Unterwäsche ziemt sich nicht für eine Prinzessin!"','「這……這……這麼不雅的內衣不適合公主穿！」')
))
lines.append('')

lines.append(L(
    D('„Ich habe Vertrauen in meinen Po!"','「我對我的屁股有信心！」')
))
lines.append('')

lines.append(L(
    D('„Okay, dann kaufe ich sie!"','「好，那我買了！」'),
    D('„Vielen Dank für Ihren Einkauf!"','「感謝您的購買！」')
))
lines.append('')

lines.append(L(
    D('„Vergiss es, ich verbiete es!!"','「想都別想，我禁止！！」'), '，',
    D('sagte','說道'), D('Iris','Iris'), '。',
    D('„Ich werde nicht zulassen, dass eine Prinzessin von Midgar solch unanständige Unterwäsche trägt!"','「我不會允許Midgar的公主穿這麼不雅的內衣！」')
))
lines.append('')

lines.append(L(
    D('„Wenn meine Schwester sagt, dass sie Tangas nicht anerkennt,','「如果我姐姐說她不認可丁字褲，'),
    D('dann lass ich es eben sein."','那我就算了。」'),
    D('„Okay, dann kaufe ich sie!"','「好，那我買了！」'),
    D('„Vielen Dank für Ihren Einkauf!"','「感謝您的購買！」')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('sah','看著'), C('那個','das'),
    D('lächelnde','微笑的'), D('Gesicht','臉'),
    C('她的','ihrer'), D('kleinen','小'), D('Schwester','妹妹'),
    C('和','und'), D('dachte sich','心想'), C('也','auch'),
    C('用','mit'), C('一個','einem'), D('Lächeln','微笑'), '：',
    D('Na ja, wie auch immer.','算了，管她呢。')
))

lines.append(BRK())

# ═══════════════════════════════════════════
# 追加到 page5.html
# ═══════════════════════════════════════════

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = ''.join(l + '\n' for l in lines)

content = content.replace('</main>', new_content + '</main>')

with open(TARGET, 'w', encoding='utf-8') as f:
    f.write(content)

d_count = len(re.findall(r'<span class="d">', content))
c_count = len(re.findall(r'<span class="c">', content))
print(f'✅ 已追加第二部分到 {TARGET}')
print(f'   德文詞 (.d): {d_count}')
print(f'   中文詞 (.c): {c_count}')
if d_count + c_count > 0:
    print(f'   德文佔比: {d_count/(d_count+c_count)*100:.1f}%')
