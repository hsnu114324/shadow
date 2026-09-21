# -*- coding: utf-8 -*-
import re

OUTPUT_FILE = 'page5.html'

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

lines.append(S('Kapitel 3: Der Vorhang hebt sich!'))
lines.append('')

# ─── Paragraph 1 ───
lines.append(L(
    C('我','Ich'), C('是','war'), D('tagelang','好幾天'),
    C('在','in'), C('一個','einer'), D('Art','一種'),
    D('Gefängnis','監獄'), D('verhört worden','被審問'),
    C('和','und'), D('wurde','被'), C('現在','nun'), '，',
    C('在','am'), D('fünften Abend','第五天晚上'), '，',
    D('endlich','終於'), D('entlassen','釋放了'), '。'
))
lines.append('')

lines.append(L(
    D('„Komm schon, lauf schneller!"','「快點，走快一點！」')
))
lines.append('')

# ─── Paragraph 2 ───
lines.append(L(
    C('我','Ich'), D('wurde','被'), D('grob','粗暴地'),
    C('從','von'), D('hinten','後面'), D('geschubst','推了一把'), '，',
    C('從','aus'), C('那個','dem'), D('Gebäude','建築物'),
    D('geworfen','丟了出來'), '，',
    C('當','und als'), C('我','ich'), C('在','am'),
    D('Boden','地上'), D('lag','躺著'), '，',
    D('schmiss','扔了'), C('人們','man'), C('我','mir'),
    C('我的','meine'), D('Sachen','東西'), D('hinterher','丟過來'), '。',
    C('因為','Da'), C('我','ich'), C('什麼都不','nichts'),
    C('除了','als'), D('Unterwäsche','內衣'),
    C('在','am'), D('Leib','身上'), D('trug','穿著'), '，',
    D('zog','穿上了'), C('我','ich'), C('我','mir'),
    C('我的','meine'), D('Kleidung','衣服'),
    C('和','und'), D('Schuhe','鞋子'), C('再次','wieder'), C('上','an'), '。',
    C('那','Das'), D('dauerte','花了'), C('一點','ein wenig'), '，',
    C('因為','da'), C('她們','sie'), C('我','mir'),
    C('在','an'), C('兩','beiden'), D('Händen','手上'),
    C('那些','die'), D('Fingernägel','指甲'),
    D('gezogen hatten','拔掉了'), '。'
))
lines.append('')

# ─── Paragraph 3 ───
lines.append(L(
    C('我','Ich'), D('atmete','呼吸了'), C('一次','einmal'),
    D('tief','深深地'), D('durch','地'),
    C('和','und'), D('machte','踏上了'), C('自己','mich'),
    C('在','auf'), C('那個','den'), D('Heimweg','回家的路'), '。',
    C('我','Ich'), D('zog','引來了'), C('如此','so'),
    C('一些','einige'), D('Blicke','目光'), C('在','auf'), C('自己','mich'), '，',
    C('什麼','was'), C('當然','natürlich'), C('在','an'),
    C('我的','meinem'), D('blutverschmierten','血跡斑斑的'),
    C('和','und'), D('zusammengeschlagenen','被打腫的'),
    D('Äußeren','外貌'), D('lag','的緣故'), '。'
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('atmete','呼吸了'), C('還','noch'),
    C('一次','einmal'), D('durch','地'), '。'
))
lines.append('')

lines.append(L(
    D('„Ganz ruhig, ganz ruhig.','「冷靜，冷靜。'),
    D('Verlier','別失去'),
    C('因為','wegen'), C('如此','so'), C('一個','einer'),
    D('Kleinigkeit','小事'), C('只是','bloß'),
    C('不','nicht'), C('那個','die'), D('Fassung.','鎮定。」')
))
lines.append('')

# ─── Paragraph 4 ───
lines.append(L(
    C('我','Ich'), D('versuchte','試著'),
    C('如此','so'), D('gut','好'), C('它','es'), D('ging','可能'),
    C('不','nicht'), C('在','an'), C('那些','die'),
    D('Gesichter','臉孔'), C('的','der'), D('Ritter','騎士們'),
    C('去','zu'), D('denken','想'), '，',
    C('那些','die'), C('我','mich'), D('verhört hatten','審問過的'), '，',
    C('和','und'), D('redete','說著'), C('我','mir'),
    C('自己','selbst'), D('Mut','勇氣'), C('去','zu'), '。'
))
lines.append('')

lines.append(L(
    D('„Sie haben nur ihre Arbeit gemacht."','「他們只是在做他們的工作。」')
))
lines.append('')

# ─── Paragraph 5 ───
lines.append(L(
    C('那些','Die'), D('blauen Flecken','瘀青'),
    C('是','waren'), C('只','nur'),
    D('oberflächliche','表面的'), D('Wunden','傷口'),
    C('和','und'), C('我的','meine'), D('gezogenen','被拔掉的'),
    D('Fingernägel','指甲'), D('konnte','能夠'),
    C('我','ich'), C('在','im'), D('Nu','一瞬間'),
    C('再次','wieder'), D('heilen','治好'), '，',
    C('如果','wenn'), C('我','ich'), D('wollte','想的話'), '。',
    C('我','Ich'), D('durfte','不可以'), C('它','es'),
    C('只','nur'), C('不','nicht'), '，',
    C('為了','um'), C('繼續','weiter'), C('我的','meine'),
    D('Rolle','角色'), C('作為','als'), D('Nebencharakter','配角'),
    C('去','zu'), D('spielen','扮演'), '。'
))
lines.append('')

lines.append(L(
    D('„Genau, ich bin die Ruhe in Person."','「沒錯，我是鎮定本人。」')
))
lines.append('')

lines.append(L(
    D('Ganz ruhig.','冷靜。')
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('holte','吸了'), C('還','noch'),
    C('一個','ein'), D('weiteres Mal','再一次'),
    D('geräuschvoll','大聲地'), D('Luft','氣'), '。'
))
lines.append('')

# ─── Paragraph 6 ───
lines.append(L(
    C('我的','Meine'), D('Sicht','視線'), C('是','war'),
    D('mittlerweile','此時'), C('再次','wieder'),
    D('klar','清楚的'), C('和','und'), C('我','ich'),
    D('bemerkte','注意到了'), C('一些','ein paar'),
    D('verdächtige','可疑的'), D('Schatten','影子'),
    C('在','hinter'), C('我','mir'), C('後面',''), '。'
))
lines.append('')

lines.append(L(
    D('‚Zwei Verfolger also."','「兩個跟蹤者啊。」')
))
lines.append('')

# ─── Paragraph 7 ───
lines.append(L(
    D('Alexias','Alexia的'), D('Entführung','綁架'),
    C('是','war'), C('還','noch'), C('總是','immer'),
    D('ungeklärt','未解決的'), C('和','und'), C('那個','die'),
    D('Suche','搜索'), C('在','nach'), C('她','ihr'),
    D('dauerte an','持續著'), '。',
    C('我','Ich'), C('是','war'), C('不','nicht'),
    C('如此','so'), D('naiv','天真'), C('去','zu'),
    D('glauben','相信'), '，',
    C('我','ich'), C('是','sei'), C('現在','jetzt'),
    D('entlastet','被洗清嫌疑了'), '。',
    C('她們','Sie'), D('hatten','有'), C('我','mich'),
    C('只','nur'), C('從','aus'), D('Mangel','缺乏'),
    C('在','an'), D('Beweisen','證據'), D('entlassen','釋放的'), '，',
    C('然而','doch'), D('verdächtigten','懷疑著'), C('我','mich'),
    C('之後','nach'), C('像','wie'), C('之前','vor'), '。'
))
lines.append('')

lines.append(L(
    D('Niedergeschlagen','沮喪'), C('和','und'),
    D('erschöpft','疲憊地'), D('ging','走'),
    C('我','ich'), C('去','zum'),
    D('Wohnheim','宿舍'), D('zurück','回去了'), '。'
))
lines.append('')

# ─── Paragraph 8 ───
lines.append(L(
    C('那時','Da'), D('vernahm','聽到了'), C('我','ich'),
    C('在','auf'), C('一次','einmal'), C('一個','ein'),
    D('Geräusch','聲音'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich warte ..."','「我在等……」')
))
lines.append('')

lines.append(L(
    C('一個','Ein'), D('leises','輕柔的'), '，',
    D('kaum','幾乎不'), D('hörbares','聽得見的'),
    D('Flüstern','低語'), D('erreichte','傳到了'),
    C('我的','meine'), D('Ohren','耳朵'), '。',
    C('一個','Ein'), D('schwacher','微弱的'),
    D('Duft','香味'), C('的','von'), D('Parfüm','香水'),
    D('weckte','喚醒了'), C('我的','meine'),
    D('Erinnerungen','記憶'), '。'
))
lines.append('')

lines.append(L(
    D('„Alpha ...?"','「Alpha……？」')
))
lines.append('')

lines.append(L(
    C('那條','Die'), D('Straße','街道'), C('是','war'),
    D('voller','滿是'), D('Menschen','人'), '，',
    C('但是','aber'), C('她','sie'), C('是','war'),
    D('nirgendwo','哪裡都不'), C('去','zu'), D('sehen','看見'), '。'
))

lines.append(BRK())

# ─── After *** - In seinem Zimmer ───
lines.append(L(
    C('當','Als'), C('我','ich'), C('在','in'),
    C('我的','meinem'), D('Zimmer','房間'), C('是','war'),
    C('和','und'), C('那個','das'), D('Licht','燈'),
    D('anmachte','打開了'), '，',
    D('tauchte','出現了'), C('從','aus'), C('那個','der'),
    D('Dunkelheit','黑暗中'), C('一個','ein'),
    D('Mädchen','女孩'), D('auf','了'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich habe etwas zu essen hier."','「我這裡有東西吃。」')
))
lines.append('')

lines.append(L(
    C('她的','Ihr'), D('schwarzer','黑色的'),
    D('Bodysuit','緊身衣'), D('schmiegte sich','緊貼著'),
    D('perfekt','完美地'), C('在','an'), C('她的','ihren'),
    D('Körper','身體'), C('和','und'), D('betonte','強調了'),
    C('她的','ihre'), D('weiblichen','女性的'), D('Kurven','曲線'), '。',
    C('在','In'), C('那個','der'), D('Hand','手中'),
    D('hielt','拿著'), C('她','sie'), C('一個','ein'),
    D('dick','厚厚的'), C('用','mit'), D('Thunfisch','鮪魚'),
    D('belegtes','夾的'), D('Sandwich','三明治'), '。',
    C('它','Es'), D('stammte','來自'), C('從','aus'),
    C('一個','einem'), D('berühmten','著名的'),
    D('Restaurant','餐廳'), C('的','der'),
    D('Königlichen Hauptstadt','王都'), '：',
    D('McThunalds','麥鮪勞'), '。'
))
lines.append('')

lines.append(L(
    D('„Danke.','「謝謝。'),
    D('Es ist schon ziemlich lange her.','已經好久了。'),
    D('Wo ist denn Beta?"','Beta在哪裡？」')
))
lines.append('')

lines.append(L(
    C('在','Auf'), D('Alpha','Alpha'), C('是','war'),
    C('總是','immer'), D('Verlass','可靠的'), '。',
    C('總是','Immer'), C('當','wenn'), C('我','ich'),
    C('她','ihr'), D('Dinge','事情'), D('überließ','交給了'), '，',
    D('zauberte','變出了'), C('她','sie'), C('我','mir'),
    C('直到','bis'), C('到','zum'), D('nächsten Tag','第二天'),
    C('那個','die'), D('beste','最好的'), D('Bühne','舞台'), '。',
    C('在','In'), C('那個','der'), D('Zwischenzeit','這段時間'),
    D('würde','會'), C('我','ich'), D('schlafen','睡覺'), '...',
    C('或者','oder'), '，', D('äh','呃'), '...',
    C('我','Ich'), D('meine','是說'), C('當然','natürlich'), '，',
    D('Kräfte sammeln','積蓄力量'), '。'
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('machte','趕緊'), C('自己','mich'),
    D('schnell','快速地'), C('在','über'), C('那個','das'),
    D('Sandwich','三明治'), D('her','吃了起來'), '，',
    C('因為','da'), C('我','ich'), C('那些','die'),
    D('letzten fünf Tage','過去五天'), C('如此','so'),
    D('gut wie','幾乎'), C('什麼都不','nichts'),
    D('gegessen hatte','沒吃東西'), '。'
))
lines.append('')

lines.append(L(
    D('Eigentlich','其實'), D('sollte','應該'),
    D('Beta','Beta'), C('現在','gerade'),
    C('我的','meine'), D('Assistentin','助手'), C('是','sein'), '。'
))
lines.append('')

lines.append(L(
    D('„Beta hat mich kontaktiert.','「Beta聯繫了我。'),
    D('Sie sagte, die Situation sei ziemlich eskaliert."','她說情況相當嚴重了。」')
))
lines.append('')

lines.append(L(
    D('Alpha','Alpha'), D('setzte sich','坐到了'),
    C('在','auf'), C('我的','mein'), D('Bett','床上'),
    C('和','und'), D('schlug','翹起了'), C('那些','die'),
    D('Beine','腿'), D('übereinander','交叉'), '。'
))
lines.append('')

lines.append(L(
    C('她的','Ihr'), D('blondes','金色的'), D('Haar','頭髮'),
    D('glänzte','閃耀著'), C('總是','immer'), C('還','noch'),
    C('像','wie'), D('früher','從前'), C('和','und'),
    C('她的','ihre'), D('schönen','美麗的'), D('blauen','藍色的'),
    D('Augen','眼睛'), D('strahlten','散發著'),
    C('某些','etwas'), D('Nostalgisches','懷舊的東西'), D('aus',''), '。',
    C('我','Ich'), D('hatte','有'), C('她','sie'),
    C('一個','eine'), D('ganze','整整'), D('Weile','一段時間'),
    C('不','nicht'), D('gesehen','見過'), C('和','und'),
    C('她','sie'), D('sah','看起來'), D('inzwischen','如今'),
    D('viel','很多'), D('reifer','更成熟'), D('aus','了'), '。'
))
lines.append('')

lines.append(L(
    D('„Das könnte man so sagen."','「可以這麼說吧。」')
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('kaute','嚼著'), C('正好','gerade'),
    C('在','auf'), C('那個','dem'), D('letzten','最後的'),
    D('Bissen','一口'), D('herum',''), '。',
    C('那時','Da'), D('zeigte','指了'), D('Alpha','Alpha'),
    C('在','hinter'), C('我','mich'), C('和','und'),
    D('sagte','說'), '：',
    D('„Da drüben steht Wasser."','「那邊有水。」')
))
lines.append('')

lines.append(L(
    D('„Oh, danke."','「喔，謝謝。」')
))
lines.append('')

lines.append(L(
    C('在','In'), C('一個','einem'), D('Zug','一口氣'),
    D('schüttete','倒了'), C('我','ich'), C('那整個','das gesamte'),
    D('Wasser','水'), C('從','aus'), C('那個','dem'),
    D('Glas','杯子'), C('進入','in'), C('我的','meinen'),
    D('Mund','嘴裡'), '。'
))
lines.append('')

lines.append(L(
    D('„Hach, genau das habe ich gebraucht."','「啊，這正是我需要的。」')
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('zog','脫了'), C('我的','meine'),
    D('Schuhe','鞋子'), C('和','und'), D('Jacke','外套'),
    D('aus',''), C('和','und'), D('hüpfte','跳上了'),
    C('進入','ins'), D('Bett','床'), '。'
))
lines.append('')

lines.append(L(
    D('„Hey, du solltest dich wenigstens umziehen."','「喂，你至少應該換個衣服。」'),
    D('„Kann nicht, muss schlafen."','「不行，必須睡覺。」')
))
lines.append('')

lines.append(L(
    D('„Weißt du überhaupt, was hier vor sich geht?"','「你到底知不知道這裡發生了什麼事？」')
))
lines.append('')

lines.append(L(
    D('„Du schaffst das schon."','「你可以搞定的。」')
))
lines.append('')

lines.append(L(
    D('Alpha','Alpha'), D('seufzte','嘆了口氣'),
    D('verärgert','惱怒地'), '。'
))
lines.append('')

lines.append(L(
    D('„Wenn das so weitergeht, werden sie dich für schuldig erklären."','「如果繼續這樣下去，他們會判你有罪的。」')
))
lines.append('')

lines.append(L(
    D('„Stimmt."','「對啊。」')
))
lines.append('')

lines.append(L(
    C('如果','Wenn'), C('那個','der'), D('Schuldige','罪犯'),
    C('不','nicht'), D('bald','很快'), D('gefunden wurde','被找到'), '，',
    D('würden','會'), C('她們','sie'), D('todsicher','必定'),
    C('那個','den'), D('Verdächtigsten','最大嫌疑犯'),
    D('hinrichten','處刑'), '。'
))
lines.append('')

lines.append(L(
    C('某人','Jemand'), C('從','aus'), C('那個','der'),
    D('königlichen Familie','王族'), D('wurde','被'),
    D('entführt','綁架了'), '，',
    C('所以','also'), D('musste','必須'), C('某人','jemand'),
    D('hingerichtet werden','被處刑'), '。'
))
lines.append('')

lines.append(L(
    D('Das Mittelalter ist echt krass.','中世紀真的太誇張了。')
))
lines.append('')

lines.append(L(
    D('„Wach gefälligst auf.','「給我醒一醒。'),
    D('Es gibt noch mehr Sandwiches."','還有更多三明治。」')
))
lines.append('')

lines.append(L(
    D('„Bin ich doch schon längst."','「我早就醒了。」')
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('nahm','接過了'), C('從','von'),
    D('Alpha','Alpha'), C('一個','ein'), D('weiteres','另一個'),
    D('Sandwich','三明治'), D('entgegen',''), '。'
))
lines.append('')

lines.append(L(
    D('„Es gibt eine Verschwörung und du sollst als Täter gebrandmarkt werden."','「有一個陰謀，你會被當作犯人。」')
))
lines.append('')

lines.append(L(
    D('„Ach so?','「這樣啊？'),
    D('Ich ende doch sowieso als Täter."','反正我遲早會被當作犯人。」')
))
lines.append('')

lines.append(L(
    D('„Sie wollen die Sache schnell unter den Teppich kehren.','「他們想把事情趕快壓下去。'),
    D('Der arme Sohn eines Barons wäre genau der richtige Sündenbock."','一個可憐的男爵之子正是完美的替罪羊。」')
))
lines.append('')

lines.append(L(
    D('„Na klar, so würde ich das auch machen."','「當然，我也會這麼做。」'),
    D('„Wir dürfen dem Orden nicht trauen."','「我們不能信任騎士團。」'),
    D('„Hat der Kult auch mit der ganzen Sache zu tun?"','「教團也跟整件事有關嗎？」'),
    D('„Ja, ohne jeden Zweifel.','「是的，毫無疑問。'),
    D('Der Kult steckt ganz klar hinter der Entführung der Prinzessin.','教團很明顯就是綁架公主的幕後黑手。'),
    D('Sie wollten jemanden mit hoher Konzentration an Heldenblut."','他們想要一個擁有高濃度勇者之血的人。」')
))
lines.append('')

lines.append(L(
    D('Alpha','Alpha'), D('gab sich','還在'),
    C('總是','immer'), C('還','noch'), D('Mühe','努力'), '，',
    C('在','bei'), C('我的','meinem'), D('Spielchen','遊戲'),
    D('mitzumachen','配合'), '。',
    C('那','Das'), C('是','war'), C('真的','wirklich'),
    D('nett','體貼'), C('的','von'), C('她','ihr'), '。'
))
lines.append('')

lines.append(L(
    D('„Lebt sie noch?"','「她還活著嗎？」')
))
lines.append('')

lines.append(L(
    D('„Na klar.','「當然了。'),
    D('Tut mir leid, dass ich dein Sandwich gegessen habe."','抱歉吃了你的三明治。」')
))
lines.append('')

lines.append(L(
    D('„Wenn sie tot wäre, könnte man ihr kein Blut mehr abnehmen."','「如果她死了，就沒辦法再抽她的血了。」')
))
lines.append('')

lines.append(L(
    D('„Ergibt Sinn."','「有道理。」')
))
lines.append('')

lines.append(L(
    D('„Ich verstehe jedoch nicht, wieso du mit der Prinzessin unbedingt Pärchen spielen musstest"','「但是我不明白，你為什麼非要跟公主裝情侶」'),
    '，', D('sagte','說道'), D('Alpha','Alpha'), C('和','und'),
    D('blickte','看著'), D('argwöhnisch','滿腹狐疑地'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich würde uns nicht unbedingt als Pärchen bezeichnen."','「我不會把我們稱為情侶。」')
))
lines.append('')

lines.append(L(
    D('„Es muss einen Grund gegeben haben.','「一定有原因的。'),
    D('Etwas, das du uns nicht sagen kannst."','某些你不能告訴我們的事。」')
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('verstummte','沉默了'),
    C('和','und'), D('wandte','轉開了'), C('我的','meinen'),
    D('Blick','目光'), C('從','von'), D('Alpha','Alpha'), D('ab',''), '，',
    C('那個','die'), D('versuchte','試著'), '，',
    C('我的','meine'), D('Motive','動機'),
    C('去','zu'), D('durchschauen','看穿'), '。',
    C('當然','Natürlich'), D('hatte','有'), C('我','ich'),
    C('沒有','keine'), D('guten','好的'), D('Motive','動機'),
    C('或','oder'), D('Gründe','理由'), C('為了','für'),
    C('那個','die'), D('Beziehung','關係'), C('跟','mit'),
    D('Alexia','Alexia'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich versteh schon.','「我懂了。'),
    D('Du heckst hinter unser aller Rücken schon wieder etwas Grandioses aus."','你又在我們所有人背後策劃什麼宏大的計畫了。」')
))
lines.append('')

lines.append(L(
    C('如果','Wenn'), C('她','sie'), C('然而','doch'),
    C('只','nur'), D('wüsste','知道'), '，',
    C('說','dass'), C('我','ich'), D('absolut','絕對'),
    D('gar nichts','什麼都不'), D('plane','計畫'), '。'
))
lines.append('')

lines.append(L(
    D('„Aber du musst uns ein bisschen mehr vertrauen.','「但你必須多信任我們一點。'),
    D('Hättest du uns vorher informiert, hätten wir diese ganze Situation vermeiden können.','如果你事先通知我們，就可以避免這整個狀況。'),
    D('Denkst du nicht?"','你不覺得嗎？」'),
    D('„Sch-Schon in Ordnung."','「好……好的。」')
))
lines.append('')

lines.append(L(
    D('„Das hoffe ich doch.','「我也希望如此。'),
    D('Es ist unsere Aufgabe, dir zu folgen, verstehst du?"','跟隨你是我們的使命，你明白嗎？」'),
    D('Alpha','Alpha'), D('lächelte','微笑著'), '，',
    C('當','als'), C('她','sie'), C('那','das'), D('sagte','說'), '。'
))
lines.append('')

lines.append(L(
    D('„Wenn diese ganze Sache vorbei ist, kannst du mich zu McThunalds einladen.','「等這整件事結束後，你可以請我去麥鮪勞。'),
    D('Das zweite Sandwich vorhin war eigentlich meins."','剛才第二個三明治其實是我的。」')
))
lines.append('')

lines.append(L(
    D('„Kein Problem."','「沒問題。」')
))
lines.append('')

lines.append(L(
    D('Alpha','Alpha'), D('stand auf','站了起來'), '，',
    D('öffnete','打開了'), C('那個','das'), D('Fenster','窗戶'),
    C('和','und'), D('stellte','放了'), C('一個','einen'),
    D('Fuß','腳'), D('hinein','進去'), '。',
    C('她的','Ihre'), D('schmale','纖細的'), D('Hüfte','腰'),
    D('drehte sich','轉了過去'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich geh dann mal.','「那我走了。'),
    D('Halte dich erst einmal bedeckt."','先低調行事。」'),
    D('„Verstanden.','「明白了。'),
    D('Was ist der Plan?"','計畫是什麼？」')
))
lines.append('')

lines.append(L(
    D('„Verstärkung rufen.','「叫增援。'),
    D('Wir haben nicht genug Leute in der Königlichen Hauptstadt.','我們在王都沒有足夠的人手。'),
    D('Ich muss noch Delta rufen."','我還需要叫Delta來。」')
))
lines.append('')

lines.append(L(
    D('„Du rufst Delta?"','「你要叫Delta？」')
))
lines.append('')

lines.append(L(
    D('„Sie vermisst dich sehr."','「她很想你。」')
))
lines.append('')

lines.append(L(
    D('Delta','Delta'), '，',
    C('那個','die'), D('Unberechenbare','無法預測的人'), '—',
    C('或者','oder'), D('eher','更準確說'), D('Delta','Delta'), '，',
    C('那個','das'), D('Himmelfahrtskommando','敢死隊'), '。',
    D('Kurzum','總之'), '：',
    C('她','Sie'), C('是','war'), C('一個','ein'),
    D('Dummkopf','笨蛋'), '，',
    C('那個','der'), D('verdammt gut','非常好地'),
    D('kämpfen konnte','能戰鬥'), '。'
))
lines.append('')

lines.append(L(
    C('我們的','Unser'), D('letztes','最後的'), D('Treffen','見面'),
    C('是','war'), C('已經','schon'), C('一個','eine'),
    D('Weile','一段時間'), D('her','以前'), C('和','und'),
    C('如此','so'), D('hatte','有'), C('我','ich'),
    C('沒有','kein'), D('Problem','問題'), C('用','damit'), '，',
    C('所有','alle'), D('wiederzusehen','再次見面'), '。'
))
lines.append('')

lines.append(L(
    D('Allerdings','但是'), D('hoffte','希望'), C('我','ich'),
    D('inständig','衷心地'), '，',
    C('說','dass'), C('我的','meine'), D('früheren','以前的'),
    D('Gefährtinnen','同伴們'), C('現在','jetzt'),
    C('一個','ein'), D('normales','正常的'), C('和','und'),
    D('ehrliches','誠實的'), D('Leben','生活'), D('führten','過著'), '。'
))
lines.append('')

lines.append(L(
    D('„Wenn alles so weit ist, erkläre ich dir die Details.','「等一切準備好了，我會跟你說明細節。'),
    D('Bis dann."','到時候見。」')
))
lines.append('')

lines.append(L(
    D('Alpha','Alpha'), D('lächelte','微笑了'),
    C('一個','ein'), D('letztes Mal','最後一次'), '，',
    D('verbarg','藏起了'), C('她的','ihr'), D('Gesicht','臉'),
    C('在','unter'), C('那個','dem'), D('Anzug','裝束'),
    C('和','und'), D('verschwand','消失在了'),
    C('進入','in'), C('那個','die'), D('Nacht','夜色中'), '。'
))

lines.append(BRK())

# ─── Scene: Princess Iris ───
lines.append(L(
    D('„War das alles?"','「就這些嗎？」')
))
lines.append('')

lines.append(L(
    D('fragte','問道'), C('一個','eine'), D('schöne','美麗的'),
    D('Frau','女人'), C('用','mit'), D('feuerrotem','火紅的'),
    D('Haar','頭髮'), '。',
    C('她的','Ihr'), D('glattes','順滑的'), D('rotes','紅色的'),
    D('Haar','頭髮'), '，', C('那個','das'), C('她','ihr'),
    C('在','über'), C('那個','den'), D('Rücken','背部'),
    D('fiel','垂下'), '，', D('glänzte','閃耀著'),
    C('在','im'), D('Kerzenlicht','燭光中'), C('和','und'),
    C('她的','ihre'), D('weinroten','酒紅色的'),
    D('Augen','眼睛'), D('richteten sich','注視著'),
    C('在','auf'), C('那些','die'), D('Unterlagen','文件'), '，',
    C('那些','die'), C('在','vor'), C('她','ihr'), C('在','auf'),
    C('那個','dem'), D('Schreibtisch','書桌上'), D('lagen','放著'), '。'
))
lines.append('')

lines.append(L(
    C('在','Bei'), C('這個','diesem'), D('würdevollen','端莊'),
    C('和','und'), D('schönen','美麗的'), D('Anblick','景象'),
    D('errötete','臉紅了'), C('那個','der'),
    D('Ritter','騎士'), '，', C('那個','der'),
    C('她','ihr'), C('那些','die'), D('Dokumente','文件'),
    D('gebracht hatte','送來的'), '。'
))
lines.append('')

lines.append(L(
    D('„D-Das ist alles, Prinzessin Iris.','「這……這就是全部了，Iris公主殿下。'),
    D('Wir werden nun unsere Ermittlungen fortsetzen."','我們現在會繼續調查。」')
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('nickte','點了點頭'),
    C('和','und'), D('ließ','讓'), C('那個','den'),
    D('Ritter','騎士'), D('abtreten','退下了'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Tür','門'), D('schloss sich','關上了'),
    C('和','und'), C('只','nur'), C('還','noch'),
    D('Iris','Iris'), C('和','und'), C('一個','ein'),
    D('weiterer','另一個'), D('Mann','男人'), C('用','mit'),
    D('gepflegtem','整潔的'), D('blondem','金色的'),
    D('Haar','頭髮'), D('blieben','留在了'),
    C('在','im'), D('Raum','房間裡'), D('zurück',''), '。'
))
lines.append('')

lines.append(L(
    D('„Marquis Zenon, vielen Dank für Eure Hilfe in dieser Angelegenheit."','「Zenon侯爵，非常感謝您在此事上的協助。」')
))
lines.append('')

lines.append(L(
    D('„Der Vorfall hat sich auf dem Gelände der Akademie ereignet,','「事件發生在學院的範圍內，'),
    D('also bin ich auch dafür verantwortlich.','所以我也有責任。'),
    D('Außerdem sorge ich mich um Alexias Wohlergehen..."','此外我也擔心Alexia的安危……」'),
    D('Zenon','Zenon'), D('sah','看著'), C('去','zu'),
    D('Boden','地面'), C('和','und'), D('biss sich','咬著'),
    D('verdrossen','懊惱地'), C('在','auf'), C('那些','die'),
    D('Lippen','嘴唇'), '。'
))
lines.append('')

lines.append(L(
    D('„...im Moment ist er unser Hauptverdächtiger.','「……目前他是我們的主要嫌疑犯。'),
    D('Angesichts seiner Fähigkeiten glaube ich jedoch nicht,','但考慮到他的能力，我不認為'),
    D('dass er eine direkte Konfrontation mit Alexia hätte gewinnen können"','他能在與Alexia的正面對決中獲勝」'), '，',
    D('sagte','說道'), D('Zenon','Zenon'), '，',
    C('那個','der'), D('sorgfältig','仔細地'),
    C('在','über'), C('他的','seine'), D('Worte','話語'),
    D('nachdachte','思考著'), '。'
))
lines.append('')

lines.append(L(
    D('„Wenn dem so ist, dann hatte er entweder Komplizen oder irgendeine Droge.','「如果是那樣的話，他要麼有同夥，要麼有某種藥物。'),
    D('Aber beim Verhör durch die Ritter hat er alles abgestritten.','但在騎士的審問中他全部否認了。'),
    D('Ist er wirklich so verdächtig?"','他真的那麼可疑嗎？」'),
    D('„Ich möchte ihm auch glauben. Wirklich."','「我也想相信他。真的。」'),
    D('Iris','Iris'), D('nickte','點了點頭'),
    C('和','und'), D('kniff','瞇起了'), C('那些','die'),
    D('Augen','眼睛'), D('zusammen',''), '。'
))
lines.append('')

lines.append(L(
    D('„Ich habe einen vertrauenswürdigen Ritter auf ihn angesetzt.','「我已經派了一個可信任的騎士去監視他。'),
    D('Warten wir auf seinen Bericht."','我們等他的報告吧。」')
))
lines.append('')

lines.append(L(
    D('„Ich hoffe, dass Alexia in Sicherheit ist"','「我希望Alexia平安無事」'), '，',
    D('sagte','說道'), D('Zenon','Zenon'), '，',
    D('verbeugte sich','鞠了一躬'), C('和','und'),
    D('verließ','離開了'), C('那個','den'), D('Raum','房間'), '。'
))
lines.append('')

# ─── Claire scene ───
lines.append(L(
    C('正當','Gerade als'), D('Zenon','Zenon'), C('那個','die'),
    D('Tür','門'), D('schließen wollte','正要關上'), '，',
    D('schlüpfte','溜進了'), C('一個','ein'),
    D('Mädchen','女孩'), C('進入','in'), C('那個','den'),
    D('Raum','房間'), '。'
))
lines.append('')

lines.append(L(
    D('„Prinzessin Iris! Bitte hört mich an!"','「Iris公主殿下！請聽我說！」'),
    D('„Claire! Was machst du denn hier?!','「Claire！你在這裡做什麼？！'),
    D('Bitte verzeiht, Prinzessin.','請恕罪，公主殿下。'),
    D('Ich werde sie sofort von hier wegbringen."','我會馬上把她帶走。」'),
    D('Zenon','Zenon'), D('versuchte','試著'), '，',
    C('那個','das'), D('dunkelhaarige','黑髮的'),
    D('Mädchen','女孩'), C('去','zu'), D('packen','抓住'), '，',
    C('那個','das'), C('自己','sich'), D('hereingeschlichen hatte','偷溜進來的'), '，',
    C('和','und'), C('再次','wieder'), C('從','aus'), C('那個','dem'),
    D('Zimmer','房間'), C('去','zu'), D('bringen','帶出去'), '。'
))
lines.append('')

lines.append(L(
    D('„Marquis Zenon, wer ist das?"','「Zenon侯爵，這位是？」'), '，',
    D('fragte','問道'), D('Iris','Iris'), C('和','und'),
    D('stoppte','阻止了'), C('他','ihn'), '。'
))
lines.append('')

lines.append(L(
    D('„Sie ist ..."','「她是……」')
))
lines.append('')

lines.append(L(
    D('„Claire Kagenou!','「Claire Kagenou！'),
    D('Die große Schwester von Cid Kagenou!"','Cid Kagenou的姐姐！」'), '，',
    D('fiel','打斷了'), C('他','ihm'), D('Claire','Claire'),
    C('進入','ins'), D('Wort','話'), '。'
))
lines.append('')

lines.append(L(
    D('„Claire!','「Claire！'),
    D('S-Sie ist eine fleißige Schülerin an der Akademie','她……她是學院裡勤奮的學生'),
    D('und befindet sich derzeit auf Probe im Orden."','目前正在騎士團實習中。」')
))
lines.append('')

lines.append(L(
    D('„Ich verstehe ...','「我明白了……'),
    D('Also gut, ich werde mir anhören, was du zu sagen hast."','好吧，我會聽聽你想說什麼。」'),
    D('„Vielen Dank!"','「非常感謝！」')
))
lines.append('')

lines.append(L(
    D('Claire Kagenou','Claire Kagenou'), D('trat','走到'),
    D('vor','前面'), C('和','und'), D('wandte sich','轉向'),
    C('在','an'), D('Iris','Iris'), '。'
))
lines.append('')

lines.append(L(
    D('„Mein Bruder würde niemals Prinzessin Alexia entführen!','「我的弟弟絕對不會綁架Alexia公主！'),
    D('Es muss sich um einen Irrtum handeln!"','這一定是誤會！」')
))
lines.append('')

lines.append(L(
    D('„Die Ritter untersuchen den Fall sorgfältig, um alle Irrtümer auszuschließen.','「騎士們正在仔細調查此案，以排除所有錯誤。'),
    D('Es ist noch nicht sicher, dass dein Bruder der Entführer ist."','還不確定你弟弟就是綁架犯。」')
))
lines.append('')

lines.append(L(
    D('„Aber wenn sie den wahren Schuldigen nicht finden, werden sie meinen Bruder hinrichten!"','「但如果他們找不到真正的犯人，就會處死我弟弟！」'),
    D('„Die Ritter untersuchen den Fall sorgfältig.','「騎士們正在仔細調查。'),
    D('Niemand wird wegen eines Irrtums hingerichtet."','沒有人會因為誤判而被處死。」')
))
lines.append('')

lines.append(L(
    D('„Aber...!"','「但是……！」')
))
lines.append('')

lines.append(L(
    D('„Claire!"','「Claire！」')
))
lines.append('')

lines.append(L(
    D('Claire','Claire'), D('versuchte','試著'),
    D('verzweifelt','絕望地'), '，', C('去','zu'),
    D('Iris','Iris'), D('vorzudringen','衝上前去'), '，',
    C('然而','doch'), D('Zenon','Zenon'), D('hielt','攔住了'),
    C('她','sie'), D('auf',''), '。'
))
lines.append('')

lines.append(L(
    D('„Jetzt hör schon auf.','「你夠了。'),
    D('Ich verstehe, wie du dich fühlst,','我理解你的感受，'),
    D('aber wenn du so weitermachst, beleidigst du den Orden."','但如果你繼續這樣做，你是在侮辱騎士團。」')
))
lines.append('')

lines.append(L(
    D('„Verdammt..!"','「可惡……！」')
))
lines.append('')

lines.append(L(
    D('Claire','Claire'), D('blickte','看了看'),
    D('zuerst','先'), C('去','zu'), D('Zenon','Zenon'), '，',
    C('然後','dann'), C('去','zu'), D('Iris','Iris'), '。'
))
lines.append('')

lines.append(L(
    D('„Wenn ihm irgendetwas zustoßen sollte ...!"','「如果他發生了什麼事的話……！」'),
    D('„Claire! Kein Wort mehr!"','「Claire！不准再多說一個字！」'), '，',
    D('unterbrach','打斷了'), D('Zenon','Zenon'),
    C('那個','das'), D('Mädchen','女孩'),
    C('和','und'), D('zerrte','拖著'), C('它','es'),
    D('gewaltsam','強行地'), C('往','nach'), D('draußen','外面'), '，',
    C('直到','bis'), C('那個','die'), D('Tür','門'),
    C('用','mit'), C('一個','einem'), D('lauten','巨大的'),
    D('Knall','砰聲'), C('在','hinter'), C('兩人','den beiden'),
    D('zukrachte','砸上了'), '。'
))
lines.append('')

lines.append(L(
    D('Iris','Iris'), D('starrte','盯著'), C('還','noch'),
    C('一個','einen'), D('Moment','片刻'), C('在','auf'),
    C('那個','die'), D('Tür','門'), C('和','und'),
    D('seufzte','嘆了口氣'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich schätze, wir empfinden alle dasselbe, wenn es um unsere Familie geht ..."','「我想，當涉及到家人時，我們都有相同的感受……」')
))
lines.append('')

lines.append(L(
    C('她','Sie'), C('是','war'), C('現在','nun'),
    D('allein','獨自的'), C('和','und'),
    D('flüsterte','低語著'), C('在','vor'), C('自己','sich'), D('hin',''), '。'
))
lines.append('')

lines.append(L(
    D('„Alexia, bitte komm heil zu uns zurück."','「Alexia，請平安回到我們身邊。」'),
    C('那些','Die'), D('Schwestern','姊妹'), C('是','waren'),
    C('一次','einmal'), C('非常','sehr'), D('gut','好地'),
    D('miteinander','互相'), D('befreundet gewesen','交好的'), '。',
    C('但是','Aber'), D('irgendwann','在某個時候'),
    D('hatten','有了'), C('她們','sie'), D('begonnen','開始'), '，',
    C('自己','sich'), D('voneinander','彼此'),
    C('去','zu'), D('entfernen','疏遠'), '。',
    C('她們','Sie'), D('hatten','有'), C('自從','seit'),
    D('Jahren','年'), C('不','nicht'), D('miteinander','互相'),
    D('gesprochen','交談過'), C('和','und'),
    D('würden','會'), C('它','es'), C('也許','vielleicht'),
    C('從不','nie'), C('再次','wieder'), '。'
))
lines.append('')

lines.append(L(
    C('當','Als'), D('Iris','Iris'), C('她的','ihre'),
    D('weinroten','酒紅色的'), D('Augen','眼睛'),
    D('schloss','閉上了'), '，',
    D('rann','流下了'), C('一個','eine'), D('einzelne','一滴'),
    D('Träne','淚水'), C('她的','ihre'), D('Wange','臉頰'),
    D('herab',''), '。'
))

lines.append(BRK())

# ─── Alexia scene ───
lines.append(L(
    C('當','Als'), D('Alexia','Alexia'), D('aufwachte','醒來了'), '，',
    D('befand','發現'), C('她','sie'), C('自己','sich'),
    C('在','in'), C('一個','einem'), D('dämmrigen','昏暗的'),
    D('Raum','房間裡'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), D('gab','有'), C('沒有','keine'),
    D('Fenster','窗戶'), C('和','und'), C('只','nur'),
    C('一個','eine'), D('einzige','唯一的'), D('Kerze','蠟燭'),
    D('spendete','提供了'), C('她','ihr'), D('Licht','光'), '。',
    C('那些','Die'), D('Wände','牆壁'), C('是','waren'),
    C('從','aus'), D('Stein','石頭的'), C('和','und'),
    C('在','an'), C('那個','der'), D('Vorderseite','前面'),
    C('的','des'), D('Raums','房間'), D('befand sich','有'),
    C('一個','eine'), D('massive','厚重的'), D('Tür','門'), '。'
))
lines.append('')

lines.append(L(
    D('„Wo bin ich ...?"','「我在哪裡……？」')
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('konnte','能'), C('自己','sich'),
    C('不','nicht'), C('更多','mehr'), C('關於此','daran'),
    D('erinnern','記得'), '，', C('什麼','was'),
    D('passiert war','發生了'), '，',
    C('之後','nachdem'), C('她','sie'), C('自己','sich'),
    C('在','auf'), C('那個','dem'), D('Rückweg','回去的路上'),
    C('從','von'), D('Hundi','Hundi'),
    D('getrennt hatte','分開了'), '。',
    C('當','Als'), C('她','sie'), D('versuchte','試著'), '，',
    C('自己','sich'), C('去','zu'), D('bewegen','移動'), '，',
    D('hörte','聽到了'), C('她','sie'), C('一個','ein'),
    D('Rasseln','嘩啦聲'), C('和','und'), C('一個','ein'),
    D('Schaben','刮擦聲'), C('的','von'), D('Metall','金屬的'), '。'
))
lines.append('')

lines.append(L(
    C('她的','Ihre'), D('Gliedmaßen','四肢'),
    C('是','waren'), C('在','an'), C('那個','die'),
    D('Wand','牆壁'), D('gekettet','被鎖住了'), '。'
))
lines.append('')

lines.append(L(
    D('„Magieversiegelnde Ketten ..."','「封印魔力的鎖鏈……」')
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('vermochte','無法'), C('沒有','keine'),
    D('Magie','魔法'), C('去','zu'), D('benutzen','使用'),
    C('和','und'), C('從','aus'), D('eigener','自己的'),
    D('Kraft','力量'), C('去','zu'), D('entkommen','逃脫'), '，',
    D('wäre','會是'), C('沒有','kein'), D('einfaches','容易的'),
    D('Unterfangen','事情'), '。'
))
lines.append('')

lines.append(L(
    C('誰','Wer'), C('在','um'), D('alles in der Welt','到底'),
    D('hatte','有'), C('她','sie'), D('entführt','綁架了'), '？',
    C('和','Und'), C('去','zu'), D('welchem','什麼'),
    D('Zweck','目的'), '？',
    D('Einfaches','簡單的'), D('Kidnapping','綁架'), '？',
    D('Erpressung','勒索'), '？',
    D('Menschenhandel','人口販賣'), '？',
    C('她','Sie'), D('dachte','想了'), C('在','an'),
    D('vieles','很多事'), '，', D('konnte','能'),
    C('自己','sich'), C('但是','aber'), C('不','nicht'),
    D('sicher','確定'), C('是','sein'), '。',
    C('她','Sie'), D('wusste','知道'), '，',
    C('說','dass'), C('她','sie'), C('雖然','zwar'),
    C('沒有','keinen'), D('Anspruch','權利'),
    C('在','auf'), C('那個','den'), D('Thron','王位'),
    D('hatte','有'), '，', C('但是','aber'), C('因為','da'),
    C('她','sie'), C('一個','eine'), D('Prinzessin','公主'),
    C('是','war'), '，', C('儘管如此','trotzdem'),
    C('一個','einen'), D('hohen','高的'), D('Wert','價值'),
    C('作為','als'), D('Geisel','人質'), D('hätte','有'), '。',
    C('在','In'), C('她的','ihrer'), D('jetzigen','目前的'),
    D('Situation','狀況'), D('würde','會'), C('她','sie'),
    C('在','auf'), C('她的','ihre'), D('Fragen','問題'),
    C('沒有','keine'), D('Antworten','答案'), D('erhalten','得到'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('hörte auf','停止了'),
    C('去','zu'), D('denken','思考'), C('和','und'),
    D('stellte','問了'), C('自己','sich'), D('plötzlich','突然'),
    C('一個','eine'), D('ganz andere','完全不同的'),
    D('Frage','問題'), '。'
))
lines.append('')

lines.append(L(
    D('Geht es Hundi gut?','Hundi還好嗎？')
))
lines.append('')

lines.append(L(
    C('她的','Ihr'), D('neuer','新的'), D('Freund','朋友'),
    C('用','mit'), C('那個','der'), D('grausamen','殘酷的'),
    D('Persönlichkeit','性格'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('mochte','喜歡'), C('他','ihn'), '，',
    C('因為','weil'), C('他','er'), C('沒有','kein'),
    D('Blatt','遮掩'), C('在','vor'), C('那個','den'),
    D('Mund','嘴'), D('nahm','有'), '。'
))
lines.append('')

lines.append(L(
    C('如果','Wenn'), C('他','er'), C('在','in'), C('那整個','das Ganze'),
    D('verwickelt wurde','被牽扯了'), '，',
    C('是','ist'), C('他','er'), D('mittlerweile','現在'),
    D('bestimmt','一定'), '...',
    C('在','An'), C('如此','so'), C('某些','etwas'),
    D('darf','可以'), C('我','ich'), C('不','nicht'),
    D('denken','想'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('schüttelte','搖了搖'),
    C('那個','den'), D('Kopf','頭'), C('和','und'),
    D('sah sich um','環顧四周'), '。'
))
lines.append('')

lines.append(L(
    D('Steinmauern','石牆'), '，', C('一個','eine'),
    D('Eisentür','鐵門'), '，', C('一個','ein'),
    D('Kerzenhalter','燭台'), C('和','und'), '...',
    C('某些','etwas'), '，', C('那個','das'),
    D('aussah','看起來'), C('像','wie'), C('一個','ein'),
    D('schwarzer','黑色的'), D('Haufen Müll','一堆垃圾'), '。',
    C('它','Es'), D('lag','躺在'), D('direkt','直接'),
    C('旁邊','neben'), D('Alexia','Alexia'), C('和','und'),
    C('是','war'), C('從','aus'), D('irgendeinem','某個'),
    D('Grund','原因'), C('用','mit'), C('一個','einer'),
    D('Kette','鎖鏈'), C('在','an'), C('那個','die'),
    D('Wand','牆壁'), D('gefesselt','拴著'), '。'
))
lines.append('')

lines.append(L(
    C('當','Als'), D('Alexia','Alexia'), C('它','es'),
    D('genauer','更仔細地'), D('betrachtete','觀察'), '，',
    D('schien','似乎'), C('它','es'), C('自己','sich'),
    C('一點','ein wenig'), C('去','zu'), D('bewegen','移動'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), D('atmete','在呼吸'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), C('是','war'), C('一個','eine'),
    D('Kreatur','生物'), '，', C('那個','die'),
    C('在','in'), C('一個','einem'), D('schwarzen','黑色的'),
    D('Lumpen','破布'), D('steckte','裹著'), '。'
))
lines.append('')

lines.append(L(
    D('„Kannst du mich hören? Verstehst du, was ich ..."','「你能聽到我嗎？你能理解我說的……」'),
    C('那個','Die'), D('Kreatur','生物'), D('bewegte sich','動了動'),
    C('和','und'), D('sah','看著'), D('Alexia','Alexia'), C('在','an'), '。',
    C('它','Es'), C('是','war'), C('一個','ein'), D('Monster','怪物'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), C('是','war'), C('那個','die'),
    D('hässlichste','最醜陋的'), '，',
    C('在','am'), D('stärksten','最嚴重地'),
    D('ausgemergelte','憔悴的'), D('Kreatur','生物'), '，',
    C('那個','die'), D('Alexia','Alexia'), D('jemals','從未'),
    C('去','zu'), D('Gesicht','臉'), D('bekommen hatte','見過'), '。'
))
lines.append('')

lines.append(L(
    C('它的','Sein'), D('schwarzes','黑色的'), '，',
    D('verwesendes','腐爛的'), D('Gesicht','臉'),
    D('hatte','有'), C('正好','gerade'), C('還','noch'),
    C('如此','so'), D('Spuren','痕跡'), C('的','von'),
    D('Augen','眼睛'), '，', D('Nase','鼻子'),
    C('和','und'), D('Mund','嘴巴'), '。',
    C('那整個','Der ganze'), D('Körper','身體'),
    C('是','war'), D('verdreht','扭曲的'),
    C('和','und'), D('aufgedunsen','浮腫的'),
    C('和','und'), C('那個','der'), D('rechte','右'),
    D('Arm','手臂'), C('的','der'), D('Kreatur','生物'),
    C('是','war'), D('länger','更長'), C('比','als'),
    C('一個','ein'), D('Bein','腿'), C('的','von'),
    D('Alexia','Alexia'), '。',
    C('那個','Der'), D('linke','左'), D('Arm','手臂'),
    D('hingegen','相反地'), C('是','war'), D('viel','很'),
    D('dünner','更瘦'), C('比','als'), D('normal','正常'),
    C('和','und'), C('用','mit'), C('那個','dem'),
    D('Torso','軀幹'), C('的','der'), D('Kreatur','生物'),
    D('verbunden','連在一起'), '，',
    C('好像','als würde'), C('他','er'), C('某些','etwas'),
    D('festhalten','緊握著'), '。'
))
lines.append('')

lines.append(L(
    D('Solch eine','如此的'), D('Abscheulichkeit','醜陋之物'),
    D('befand sich','就在'), D('direkt','直接'),
    C('旁邊','neben'), D('Alexia','Alexia'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), C('是','war'), C('在','an'),
    C('她的','ihren'), D('Gliedmaßen','四肢'),
    D('angekettet','被鎖住的'), '，',
    C('那個','das'), D('Monster','怪物'), C('是','war'),
    C('只','nur'), C('透過','durch'), C('一個','ein'),
    D('Halsband','項圈'), D('gefesselt','束縛的'), '。',
    C('如果','Wenn'), C('它','es'), C('它的','seinen'),
    D('langen','長長的'), D('Arm','手臂'),
    D('ausstreckte','伸出來'), '，',
    D('könnte','可能'), C('它','es'), D('Alexia','Alexia'),
    D('erreichen','觸及'), '。'
))
lines.append('')

lines.append(L(
    D('Atemlos','屏住呼吸'), D('wendete','轉開了'),
    D('Alexia','Alexia'), C('她的','ihren'),
    D('Blick','目光'), D('ab',''), '，',
    C('為了','um'), C('那個','die'), D('Kreatur','生物'),
    C('不','nicht'), C('去','zu'), D('provozieren','激怒'), '。'
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('beobachtete','觀察著'), C('她','sie'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('spürte','感覺到了'),
    C('那個','den'), D('Blick','目光'), C('的','des'),
    D('Monsters','怪物的'), '。'
))
lines.append('')

lines.append(L(
    C('在','Nach'), C('一個','einem'), D('Moment','片刻'),
    C('的','der'), D('Stille','寂靜'), '，',
    C('那個','der'), C('她','ihr'), C('如此','so'),
    D('vorkam','感覺'), '，', C('好像','als sei'),
    C('那個','die'), D('Zeit','時間'),
    D('stehen geblieben','停止了'), '...',
    D('rasselte','嘩啦作響'), C('那個','die'),
    D('Kette','鎖鏈'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('drehte sich um','轉過身去'), '，',
    C('但是','aber'), C('那個','das'), D('Monster','怪物'),
    D('schien','似乎'), C('自己','sich'),
    D('hingelegt zu haben','躺下了'),
    C('和','und'), D('eingeschlafen','睡著了'),
    C('去','zu'), C('是','sein'), '。',
    D('Erleichtert','鬆了一口氣'), D('atmete','呼了口氣'),
    D('Alexia','Alexia'), D('auf',''), '。'
))
lines.append('')

lines.append(L(
    C('一個','Einen'), D('Moment','片刻'), D('später','之後'),
    D('öffnete sich','打開了'), C('那個','die'), D('Tür','門'), '。'
))
lines.append('')

# ─── Man in White scene ───
lines.append(L(
    D('„Endlich. Endlich ist es so weit!"','「終於。終於到了！」'),
    C('一個','Ein'), D('dünner','瘦的'), D('Mann','男人'),
    C('在','im'), D('weißen','白色的'), D('Laborkittel','實驗袍'),
    D('betrat','走進了'), C('那個','den'), D('Raum','房間'), '。',
    C('他','Er'), D('hatte','有'), C('一個','ein'),
    D('müdes','疲憊的'), D('Gesicht','臉'),
    C('用','mit'), D('tiefen','深深的'), D('Augenringen','黑眼圈'),
    C('和','und'), D('rissigen','乾裂的'), D('Lippen','嘴唇'), '。',
    C('他的','Seine'), D('Haare','頭髮'), C('是','waren'),
    D('zerzaust','凌亂的'), C('和','und'), D('klebrig','黏膩的'),
    C('在','vor'), D('Fett','油脂'), C('和','und'),
    C('他','er'), D('stank','很臭'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('beobachtete','觀察著'),
    C('那個','den'), D('Mann','男人'), C('在','in'),
    D('aller Ruhe','從容不迫地'), '。'
))
lines.append('')

lines.append(L(
    D('„Königliches Blut, Königliches Blut, Königliches Blut."','「王族之血，王族之血，王族之血。」'),
    D('Königliches Blut','王族之血'), '。',
    C('那','Das'), D('wiederholte','重複著'),
    C('那個','der'), D('Mann in Weiß','白衣男人'),
    C('總是','immer'), C('和','und'), C('總是','immer'),
    C('再次','wieder'), C('和','und'), D('holte','拿出了'),
    C('一個','ein'), D('Gerät','裝置'), C('用','mit'),
    C('一個','einer'), D('langen','長長的'), '，',
    D('dünnen','細細的'), D('Nadel','針'), D('heraus',''), '。',
    C('用','Damit'), D('würde','會'), C('他','er'),
    C('她','ihr'), C('那個','das'), D('Blut','血'),
    D('abnehmen','抽取'), '。',
    D('Alexia','Alexia'), D('kannte','認識'),
    C('那個','das'), D('Gerät','裝置'), C('從','vom'),
    D('Hofarzt','宮廷醫生'), '，',
    C('那個','der'), C('它','es'), C('已經','schon'),
    D('öfter','經常'), C('在','bei'), C('她','ihr'),
    D('benutzt hatte','使用過'), '。'
))
lines.append('')

lines.append(L(
    C('但是','Aber'), C('她','sie'), D('wusste','知道'),
    C('總是','immer'), C('還','noch'), C('不','nicht'), '，',
    D('wieso','為什麼'), C('他','er'), C('一個','eine'),
    D('Prinzessin','公主'), D('entführen würde','要綁架'), '，',
    C('只','nur'), C('為了','um'), C('她','ihr'),
    D('Blut','血'), D('abzunehmen','去抽取'), '。'
))
lines.append('')

lines.append(L(
    D('„Darf ich etwas fragen?"','「我可以問一下嗎？」'), '，',
    D('fragte','問道'), C('她','sie'), C('用','mit'),
    D('ruhiger','平靜的'), D('Stimme','聲音'), '。'
))
lines.append('')

lines.append(L(
    D('„Hm? Hmmm?"','「嗯？嗯嗯？」')
))
lines.append('')

lines.append(L(
    C('作為','Zur'), D('Antwort','回答'), D('stöhnte','呻吟了'),
    C('那個','der'), D('Mann in Weiß','白衣男人'),
    C('只','nur'), D('seltsam','奇怪地'), '。'
))
lines.append('')

lines.append(L(
    D('„Wozu brauchst du mein Blut?"','「你要我的血做什麼？」')
))
lines.append('')

lines.append(L(
    D('„D-Dein Blut ist das Blut eines Dämons.','「你……你的血是惡魔之血。'),
    D('Und w-wir werden die Dämonen wiedererwecken."','而我……我們會復活惡魔。」'),
    D('„Ich verstehe. Was für eine wunderbare Idee."','「我懂了。多麼美妙的想法。」'),
    C('她','Sie'), D('hatte','有'), D('absolut','完全'),
    C('沒有','keine'), D('Ahnung','概念'), '，',
    D('worüber','關於什麼'), C('他','er'), D('redete','在說'), '，',
    C('然而','doch'), C('她','sie'), D('dachte sich','想著'), '，',
    C('他','er'), C('是','sei'), C('也許','vielleicht'),
    C('一個','ein'), D('Verrückter','瘋子'), '，',
    C('那個','der'), C('自己','sich'), C('太','zu'), D('viel','多'),
    C('用','mit'), D('Religion','宗教'), D('befasst hatte','沉迷了'), '。'
))
lines.append('')

lines.append(L(
    D('„Nur zapf mir nicht zu viel Blut ab.','「只是別抽太多血。'),
    D('Ich würde ungern sterben."','我不想死。」')
))
lines.append('')

lines.append(L(
    D('„Hihi-hi.','「嘻嘻嘻。'),
    D('I-Ich weiß.','我……我知道。'),
    D('Ich brauche aber viel, also komme ich jeden Tag wieder."','但我需要很多，所以我每天都會來。」')
))
lines.append('')

lines.append(L(
    D('„Okay, dann machen wir das so."','「好吧，那就這樣吧。」'),
    C('只要','Solang'), C('他','er'), D('Alexias','Alexia的'),
    D('Blut','血'), D('brauchte','需要'), '，',
    D('würde','會'), C('他','er'), C('她','sie'),
    C('不','nicht'), D('töten','殺死'), '。',
    C('她','Sie'), D('würde','會'), C('自己','sich'),
    C('他','ihm'), C('不','nicht'), D('widersetzen','反抗'), '，',
    C('而是','sondern'), D('einfach','就'), D('gehorchen','服從'), '。',
    C('她','Sie'), D('beschloss','決定'), '，',
    D('erst einmal','先'), C('在','auf'), D('Rettung','救援'),
    C('去','zu'), D('warten','等待'), '。'
))
lines.append('')

lines.append(L(
    D('„D-Das hätte niemals passieren dürfen.','「這……這本不該發生的。'),
    D('Es ist alles die Schuld dieser Idioten."','全是那些蠢貨的錯。」')
))
lines.append('')

lines.append(L(
    D('„Ich verabscheue Idioten auch über alles."','「我也最討厭蠢貨了。」'),
    D('Alexia','Alexia'), D('flüsterte','低語著'),
    C('在','vor'), C('自己','sich'), D('hin',''), '，',
    C('像','wie'), C('非常','sehr'), C('她','sie'),
    D('Idioten','蠢貨'), D('satthatte','受夠了'), '，',
    C('和','und'), D('sah','看著'), C('那個','den'),
    D('Mann in Weiß','白衣男人'), C('同時','dabei'), C('在','an'), '。'
))
lines.append('')

lines.append(L(
    D('„S-Sie haben m-meine Labore zerstört.','「他……他們毀……毀了我的實驗室。'),
    D('Dieser Idiot Olba ist als Erster draufgegangen."','那個蠢貨Olba是第一個完蛋的。」'),
    D('„Was für ein Idiot, dieser Olba."','「多蠢啊，那個Olba。」')
))
lines.append('')

lines.append(L(
    D('„Von da an haben sie noch eins und noch eins zerstört ...','「從那之後他們又毀了一個又一個……'),
    D('Aaaaaaahhh!"','啊啊啊啊啊啊！」')
))
lines.append('')

lines.append(L(
    D('„Wie schade, das muss schwer gewesen sein."','「好可惜，那一定很辛苦。」'),
    D('„Genau! Und wie!','「就是啊！可不是嗎！'),
    D('Ich war so nah dran!','我都快成功了！'),
    D('Wenn ich meine Forschung nicht bald beende,','如果我不趕快完成研究，'),
    D('werde ich e-e-exkommuniziert!"','我會被……被……被逐出教會的！」'),
    D('„Wie schrecklich!"','「多可怕啊！」')
))
lines.append('')

lines.append(L(
    D('„V-Verdammt, du nutzloses, nutzloses Ding!"','「可……可惡，你這沒用的、沒用的東西！」'),
    C('那個','Der'), D('Mann','男人'), C('在','in'), C('那個','dem'),
    D('weißen','白色的'), D('Laborkittel','實驗袍'),
    D('ging','走向了'), C('在','auf'), C('那個','die'),
    D('Kreatur','生物'), C('去','zu'), C('和','und'),
    D('begann','開始'), C('她','sie'), C('去','zu'),
    D('treten','踢'), '。',
    C('他','Er'), D('trat','踢著'), C('她','sie'),
    C('和','und'), D('stampfte','踩著'), C('也','auch'),
    C('在','auf'), C('她','ihr'), D('herum',''), '。',
    C('那個','Die'), D('Kreatur','生物'), D('rollte sich','蜷縮'),
    D('indessen','此時'), D('einfach','只是'),
    D('zusammen','起來'), C('和','und'), D('hielt still','靜靜忍受'), '。'
))
lines.append('')

lines.append(L(
    D('„Wolltest du nicht mein Blut haben?"','「你不是要我的血嗎？」')
))
lines.append('')

lines.append(L(
    D('„St-Stimmt, dein Blut,','「對……對，你的血，'),
    D('ich brauche dein Blut, um es zu vollenden."','我需要你的血來完成它。」')
))
lines.append('')

lines.append(L(
    D('„Wie schön für dich."','「那真為你高興。」')
))
lines.append('')

lines.append(L(
    C('他','Er'), D('hob','舉起了'), C('那個','das'),
    D('Gerät','裝置'), C('和','und'), D('drückte','按了'),
    C('那個','die'), D('Nadel','針'), C('對抗','gegen'),
    D('Alexias','Alexia的'), D('Arm','手臂'), '。'
))
lines.append('')

lines.append(L(
    D('„D-Das wird es vollenden.','「這……這會完成它。'),
    D('I-Ich werde niemals exkommuniziert."','我……我絕不會被逐出教會。」')
))
lines.append('')

lines.append(L(
    D('„Tu mir nicht weh."','「不要弄痛我。」')
))
lines.append('')

lines.append(L(
    C('因為','Weil'), C('我','ich'), C('你','dir'),
    C('否則','sonst'), C('進入','ins'), D('Gesicht','臉'),
    D('schlagen werde','要打你'), '，',
    D('fügte','補充道'), D('Alexia','Alexia'),
    C('在','in'), D('Gedanken','心裡'), D('hinzu',''), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Nadel','針'), D('stach','扎進了'),
    C('在','in'), C('她的','ihren'), D('Arm','手臂'), '。',
    D('Alexia','Alexia'), D('sah zu','看著'), '，',
    C('像','wie'), D('rotes','紅色的'), D('Blut','血'),
    C('那個','den'), D('Glasbehälter','玻璃容器'),
    D('füllte','充滿了'), '，',
    C('好像','als wäre'), C('它','es'), C('不','nicht'),
    C('她','ihr'), D('eigenes','自己的'), '。'
))
lines.append('')

lines.append(L(
    D('„Hihi-Hihihi ….."','「嘻嘻嘻嘻嘻……」')
))
lines.append('')

lines.append(L(
    C('當','Als'), C('那個','der'), D('Behälter','容器'),
    D('voll','滿了'), C('是','war'), '，',
    D('trug','帶走了'), C('那個','der'), D('Mann','男人'),
    C('他','ihn'), D('vorsichtig','小心地'),
    C('從','aus'), C('那個','dem'), D('Raum','房間'), '。'
))
lines.append('')

lines.append(L(
    C('當','Als'), C('自己','sich'), C('那個','die'),
    D('Tür','門'), D('schloss','關上了'), '，',
    D('stieß','發出了'), D('Alexia','Alexia'),
    C('一個','einen'), D('tiefen','深深的'),
    D('Seufzer','嘆息'), D('aus',''), '。'
))

lines.append(BRK())

# ─── Two days later, my room ───
lines.append(L(
    C('那個','Der'), D('Tag','日子'), C('是','war'),
    D('endlich','終於'), D('gekommen','到來了'), '。'
))
lines.append('')

lines.append(L(
    D('Zwei Tage','兩天'), C('在','nach'), C('我的','meiner'),
    D('Entlassung','釋放'), D('befand','發現'),
    C('我','ich'), C('自己','mich'), C('在','in'),
    C('我的','meinem'), D('Zimmer','房間'), C('在','im'),
    D('Wohnheim','宿舍'), C('和','und'), D('wählte','挑選著'),
    D('Dinge','東西'), C('從','aus'), C('我的','meiner'),
    D('Eminenz im Schatten-Kollektion','暗影實力者收藏品'), '，',
    C('那些','die'), C('我','ich'), C('為了','für'),
    C('我的','meinen'), D('großen Auftritt','盛大登場'),
    D('gebrauchen könnte','用得上的'), '。'
))
lines.append('')

lines.append(L(
    D('Zigarren','雪茄'), '？', C('為此','Dafür'),
    C('是','war'), C('我','ich'), C('還','noch'),
    C('去','zu'), D('jung','年輕'), '。',
    C('一個','Ein'), D('Vintage-Wein','年份酒'),
    C('也許','vielleicht'), '？',
    C('這個','Dieser'), C('是','war'), C('一個','ein'),
    D('900.000-Zenni-Schmuckstück','90萬Zenni的寶物'),
    C('從','aus'), D('Porteau','Porteau'),
    C('在','im'), D('Südwesten','西南部'),
    D('Frenkreichs','Frenkreich的'), '。',
    C('為了','Für'), C('那個','die'),
    D('bevorstehende','即將到來的'), D('mondlose','無月的'),
    D('Nacht','夜晚'), D('würde','會'),
    C('自己','sich'), C('那個','der'), D('perfekt','完美地'),
    D('eignen','適合'), '。',
    C('為此','Dazu'), D('passend','搭配地'),
    D('brauchte','需要'), C('我','ich'), C('還','noch'),
    C('那個','das'), D('perfekte','完美的'), D('Glas','杯子'), '：',
    C('一個','ein'), D('450.000-Zenni-Glas','45萬Zenni的杯子'),
    C('的','von'), D('Witton','Witton'), '。',
    D('Ansonsten','此外'), D('hatte','有'), C('我','ich'),
    C('還','noch'), C('一個','eine'), D('antike','古董'),
    D('Lampe','燈'), C('和','und'), C('那個','das'),
    D('Gemälde','畫作'), D('Der Schrei','吶喊'),
    C('的','von'), D('Mounk','Mounk'), '，',
    C('那個','das'), C('我','ich'), D('eines Tages','有一天'),
    D('zufällig','偶然地'), D('gefunden hatte','發現了的'),
    C('和','und'), C('現在','jetzt'), C('在','an'),
    C('我的','meiner'), D('Wand','牆上'), D('hing','掛著'), '。',
    D('Perfekt','完美'), '。'
))
lines.append('')

lines.append(L(
    D('Ahh, genau so hab ich mir das vorgestellt.','啊，就是這樣我想像中的樣子。'),
    C('我','Ich'), D('habe','有'), D('Banditen','盜賊'),
    D('gejagt','追捕過'), '，',
    C('是','bin'), C('在','auf'), C('那個','dem'),
    D('Boden','地上'), D('herumgekrochen','爬來爬去'),
    C('和','und'), D('habe','有'), D('Münzen','硬幣'),
    D('aufgesammelt','撿起來過'), '，',
    D('alles','全部'), C('為了','für'), C('這個','diesen'),
    D('Tag','日子'), '。'
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('vergoss','流下了'), C('一個','eine'),
    D('stolze','驕傲的'), D('Träne','淚水'), C('為了','für'),
    C('這個','diesen'), D('Raum','房間'), '，',
    C('那個','den'), C('我','ich'), C('用','mit'),
    C('那些','den'), D('besten Stücken','最好的收藏品'),
    C('我的','meiner'), D('Kollektion','收藏'),
    D('dekoriert hatte','裝飾過的'), '。'
))
lines.append('')

lines.append(L(
    C('現在','Jetzt'), D('musste','必須'), C('我','ich'),
    C('只','nur'), C('還','noch'), C('那個','die'),
    D('Einladung','邀請函'), '，', C('那個','die'),
    C('我','ich'), D('heute','今天'), D('erhalten hatte','收到的'), '，',
    C('在','auf'), C('那個','dem'), D('Tisch','桌子上'),
    D('platzieren','放好'), C('和','und'), D('warten','等待'), '。'
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('wartete','等待著'), '...'
))
lines.append('')

lines.append(L(
    C('和','Und'), D('wartete','等待著'), '...'
))
lines.append('')

lines.append(L(
    C('我','Ich'), D('wartete','等待著'), C('和','und'),
    D('wartete','等待著'), '...！'
))
lines.append('')

lines.append(L(
    C('直到','Bis'), C('那個','der'), D('Moment','時刻'),
    '...', D('endlich','終於'), C('在那裡','da'),
    C('是','war'), '！'
))
lines.append('')

lines.append(L(
    C('一個','Ein'), D('pechschwarz','漆黑'),
    D('bekleidetes','穿著的'), D('Mädchen','女孩'),
    D('betrat','走進了'), C('那個','den'), D('Raum','房間'),
    C('透過','durch'), C('那個','das'), D('Fenster','窗戶'),
    C('和','und'), C('我','ich'), D('murmelte','喃喃說道'), '：',
    D('„Die Zeit ist reif ...','「時機成熟了……'),
    D('Heute Nacht wird die Welt in Schatten gehüllt."','今夜世界將被籠罩在陰影之下。」'),
    D('Alles für diesen einen Tag ...','一切都是為了這一天……')
))
lines.append('')

# ─── Beta POV ───
lines.append(L(
    D('„Die Zeit ist reif ...','「時機成熟了……'),
    D('Heute Nacht wird die Welt in Schatten gehüllt."','今夜世界將被籠罩在陰影之下。」')
))
lines.append('')

lines.append(L(
    C('用','Mit'), C('這些','diesen'), D('Worten','話語'),
    D('wurde','被'), D('Beta','Beta'), D('begrüßt','迎接了'), '，',
    C('當','als'), C('她','sie'), D('Shadows','Shadow的'),
    D('Zimmer','房間'), D('betrat','走進了'), '。'
))
lines.append('')

lines.append(L(
    D('Shadow','Shadow'), D('saß','坐著'), C('用','mit'),
    C('那個','dem'), D('Rücken','背'), C('去','zu'),
    D('Beta','Beta'), C('在','im'), D('Schneidersitz','盤腿'),
    C('在','auf'), C('一個','einem'), D('Stuhl','椅子上'), '。',
    C('如此','So'), D('wirkte','看起來'), C('他','er'),
    D('schutzlos','毫無防備'), '，', C('但是','aber'),
    C('她','sie'), D('wusste','知道'), '，',
    C('說','dass'), C('什麼都不','nichts'), C('的','der'),
    D('Wahrheit','真相'), D('fernerlag','更遙遠了'), '。',
    C('在','Im'), D('Licht','光線'), C('一個','einer'),
    D('antiken','古董'), D('Lampe','燈'), D('glänzte','閃耀著'),
    C('一個','ein'), D('Weinglas','酒杯'), C('在','in'),
    C('他的','seiner'), D('Hand','手中'), '。',
    C('那個','Der'), D('Wein','酒'), '，', C('那個','den'),
    C('他','er'), D('trank','喝的'), '，', C('是','war'),
    C('的','von'), C('一個','einer'), D('erstklassigen','一流的'),
    D('Marke','品牌'), '，', C('那個','die'), C('甚至','sogar'),
    D('Beta','Beta'), D('kannte','認識'), '，',
    C('雖然','obwohl'), C('她','sie'), C('否則','sonst'),
    C('其實','eigentlich'), C('沒有','keine'), D('Ahnung','概念'),
    C('的','von'), D('Alkohol','酒精'), D('hatte','有'), '。'
))
lines.append('')

lines.append(L(
    C('她','Sie'), C('是','war'), D('erstaunt','驚訝的'), '，',
    C('說','dass'), C('那個','der'), D('Raum','房間'),
    C('用','mit'), C('一個','einer'), D('Reihe','一系列'),
    D('hochwertiger','高級的'), D('Stücke','物品'),
    D('dekoriert','裝飾'), C('是','war'), C('和','und'),
    C('甚至','sogar'), C('一個','ein'), D('berühmtes','著名的'),
    D('Gemälde','畫作'), C('在','an'), C('那個','der'),
    D('Wand','牆上'), D('hing','掛著'), '。',
    C('它','Es'), C('是','war'), D('Der Schrei','吶喊'), '，',
    C('一個','ein'), D('seltenes','稀有的'), C('和','und'),
    D('einzigartiges','獨一無二的'), D('Kunstwerk','藝術品'), '，',
    C('那個','das'), C('人們','man'), D('niemals','永遠不'),
    C('在','in'), C('那些','die'), D('Hände','手中'),
    D('bekommen konnte','能得到'), '，',
    D('egal','不管'), C('像','wie'), D('viel','多少'),
    D('Geld','錢'), C('人們','man'), C('也','auch'),
    D('anhäufte','積攢'), '。',
    D('Beta','Beta'), D('wollte','想'), C('正好','gerade'),
    D('fragen','問'), '，', C('像','wie'),
    D('Shadow','Shadow'), C('它','es'), C('在','in'),
    C('他的','seinen'), D('Besitz','手中'),
    D('gebracht hatte','弄到了'), '，',
    C('直到','bis'), C('她','sie'), D('erkannte','認識到了'), '，',
    C('像','wie'), D('sinnlos','無意義'), C('她的','ihre'),
    D('Frage','問題'), C('是','war'), '。'
))
lines.append('')

lines.append(L(
    C('他','Er'), D('hatte','有'), C('它','es'), '，',
    C('因為','weil'), C('他','er'), D('Shadow','Shadow'),
    C('是','war'), '。', D('Mehr','更多的'),
    D('Erklärungen','解釋'), D('brauchte','需要'),
    C('她','sie'), C('不','nicht'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), C('是','war'), D('selbstverständlich','理所當然的'), '，',
    C('說','dass'), D('Der Schrei','吶喊'), C('他','ihm'),
    D('gehörte','屬於'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), D('gäbe','會有'), C('沒有人','niemand'),
    D('Besseres','更好的人'), C('在','auf'), C('那個','der'),
    D('ganzen','整個'), D('Welt','世界'), '，',
    C('那個','der'), C('它','es'), D('besitzen','擁有'),
    D('könnte','可以'), '。'
))
lines.append('')

lines.append(L(
    D('„Eine in Schatten gehüllte Welt.','「一個被陰影籠罩的世界。'),
    D('Heute Nacht, wenn der Mond verschwindet, gehört uns die Welt"','今夜，當月亮消失時，世界就是我們的」'), '，',
    D('sagte','說道'), D('Beta','Beta'), '。'
))
lines.append('')

lines.append(L(
    D('Shadow','Shadow'), D('warf','投了'),
    C('一個','einen'), D('Blick','目光'), C('在','auf'),
    D('Beta','Beta'), C('和','und'), D('trank','喝了'),
    C('一個','einen'), D('Schluck','一口'), D('Wein','酒'), '。'
))
lines.append('')

lines.append(L(
    D('„Die Vorbereitungen sind abgeschlossen."','「準備工作已經完成了。」')
))
lines.append('')

lines.append(L(
    D('„Verstehe."','「明白了。」')
))
lines.append('')

lines.append(L(
    C('他','Er'), D('wusste','知道'), D('alles','一切'), '。',
    C('他的','Seine'), D('Stimme','聲音'), C('是','war'),
    C('如此','so'), D('durchdringend','有穿透力的'), '，',
    C('說','dass'), C('她','sie'), C('那個','den'),
    D('Eindruck','印象'), D('vermittelte','給人'), '，',
    C('他','er'), D('wüsste','會知道'), D('bereits','已經'),
    D('alles','一切'), '。'
))
lines.append('')

lines.append(L(
    C('什麼','Was'), D('Beta','Beta'), C('也','auch'),
    C('總是','immer'), C('還','noch'), D('sagen','說'),
    D('könnte','可能'), '，', D('hatte','有'),
    C('他','er'), D('längst','早已'), D('durchschaut','看穿了'), '。'
))
lines.append('')

lines.append(L(
    C('儘管如此','Trotzdem'), D('fuhr','繼續了'),
    D('Beta','Beta'), D('fort',''), '。',
    C('因為','Denn'), C('那','das'), C('是','war'),
    C('她的','ihr'), D('Auftrag','任務'), '。'
))
lines.append('')

lines.append(L(
    D('„Auf Alphas Befehl hin wurde das gesamte verfügbare Personal in die Hauptstadt gebracht.','「按照Alpha的命令，所有可用人員都已被調到王都。'),
    D('Hundertvierzehn stehen bereit."','一百一十四人待命。」')
))
lines.append('')

lines.append(L(
    D('„Hundertvierzehn?"','「一百一十四？」')
))
lines.append('')

lines.append(L(
    D('„...!"','「……！」')
))
lines.append('')

lines.append(L(
    C('是','Waren'), C('它','es'), D('weniger','更少'), '，',
    C('比','als'), C('他','er'), D('erwartet hatte','預期的'), '？'
))
lines.append('')

lines.append(L(
    C('在','In'), D('Anbetracht','考慮到'), C('的','der'),
    D('individuellen','個人的'), D('Kampfkraft','戰鬥力'),
    C('的','von'), D('Shadow Garden','Shadow Garden'),
    D('sollte','應該'), C('那','das'), C('其實','eigentlich'),
    C('更多','mehr'), C('比','als'), D('ausreichen','足夠'), '。'
))
lines.append('')

lines.append(L(
    C('但是','Aber'), D('Beta','Beta'), D('erkannte','認識到了'),
    D('schnell','很快'), C('她的','ihren'), D('Fehler','錯誤'), '。'
))
lines.append('')

lines.append(L(
    C('這些','Diese'), D('hundertvierzehn','一百一十四'),
    D('Personen','人'), C('是','waren'), C('在','im'),
    D('Grunde','基本上'), C('不','nicht'), C('更多','mehr'),
    C('比','als'), D('Nebencharaktere','配角們'), C('和','und'),
    C('不','nicht'), C('一次','einmal'), D('zehn Prozent','百分之十'),
    D('eigneten sich','適合'), C('為此','dafür'), '。',
    D('Heute Abend','今晚'), C('是','war'), C('嘛','nämlich'),
    C('他','er'), C('那個','der'), D('Hauptcharakter','主角'), '。',
    C('如果','Wenn'), C('它','es'), C('那個','die'),
    D('Aufgabe','任務'), C('的','von'),
    D('Nebencharakteren','配角們'), C('是','war'), '，',
    C('那個','den'), D('Hauptcharakter','主角'),
    C('去','zu'), D('unterstützen','支援'), '，',
    C('是','waren'), C('這些','diese'),
    D('hundertvierzehn','一百一十四'),
    D('fürwahr','確實'), D('viel zu wenig','太少了'), '。'
))
lines.append('')

lines.append(L(
    D('„B-Bitte verzeih ..!"','「請……請原諒……！」')
))
lines.append('')

lines.append(L(
    D('„Du hast wohl noch ein paar Extras engagiert..?"','「你大概還請了一些臨時演員吧……？」'),
    D('unterbrach','打斷了'), D('Shadow','Shadow'), C('她','sie'), '，',
    C('然而','doch'), C('她','sie'), D('wusste','知道'),
    C('不','nicht'), '，', C('什麼','was'), C('那','das'),
    D('bedeutete','意味著'), '。'
))
lines.append('')

lines.append(L(
    D('„Egal.','「算了。'),
    D('Mach dir keine Sorgen.','別擔心。'),
    D('Red weiter."','繼續說。」')
))
lines.append('')

lines.append(L(
    D('„Natürlich."','「當然。」')
))
lines.append('')

lines.append(L(
    D('Beta','Beta'), D('stellte','問了'), C('沒有','keine'),
    D('weiteren','更多的'), D('Fragen','問題'), '。',
    D('Alles','一切'), '，', C('什麼','was'), D('Shadow','Shadow'),
    D('sagte','說的'), '，', D('hatte','有'),
    D('irgendeine','某種'), D('tiefere','更深的'),
    D('Bedeutung','含義'), '，', C('那個','die'),
    C('她','sie'), C('自己','sich'), C('不','nicht'),
    C('一次','einmal'), D('vorstellen','想像'),
    D('könnte','可能'), '。',
    C('她','Sie'), D('hatte','有'), C('既不','weder'),
    C('那個','das'), D('Recht','權利'), C('還','noch'),
    C('那個','die'), D('Fähigkeit','能力'), '，',
    D('Shadow','Shadow'), D('Fragen','問題'),
    C('去','zu'), D('stellen','提出'), '。'
))
lines.append('')

lines.append(L(
    C('然而','Doch'), D('eines Tages','有一天'), '...'
))
lines.append('')

lines.append(L(
    D('Eines Tages','有一天'), D('würde','會'), D('Beta','Beta'),
    C('旁邊','neben'), C('他','ihm'), D('stehen','站著'),
    C('和','und'), C('他','ihn'), D('unterstützen','支援'), '。',
    C('那','Das'), C('是','war'), C('她的','ihr'),
    D('Traum','夢想'), '。',
    C('因此','Deshalb'), D('unterdrückte','壓抑了'),
    D('Beta','Beta'), C('那些','die'), D('Worte','話語'),
    C('在','in'), C('她的','ihrem'), D('Herzen','心中'),
    C('和','und'), D('fuhr fort','繼續了'), '。'
))
lines.append('')

lines.append(L(
    D('„Die Strategie besteht darin, alle Verstecke der Fenrir-Fraktion des Diaboloskults gleichzeitig anzugreifen.','「戰略是同時攻擊暗黑教團芬里爾派系的所有藏身處。'),
    D('Zur selben Zeit werden wir versuchen, den Spuren von Alexias Magie zu folgen','同時我們會嘗試追蹤Alexia的魔力痕跡'),
    D('und sie sofort in Sicherheit bringen, sobald wir sie finden."','一旦找到她就立刻帶她到安全的地方。」')
))
lines.append('')

lines.append(L(
    D('Shadow','Shadow'), D('nickte','點了點頭'),
    C('和','und'), D('wies','示意'), C('她','sie'),
    D('an',''), '，', D('fortzufahren','繼續'), '。'
))
lines.append('')

lines.append(L(
    D('„Gamma wird das Kommando über die Operation übernehmen,','「Gamma將負責指揮整個行動，'),
    D('während Alpha mit meiner Unterstützung die Leitung im Feld übernimmt.','Alpha在我的輔助下負責現場指揮。'),
    D('Epsilon wird für die logistische Unterstützung zuständig sein','Epsilon負責後勤支援'),
    D('und Delta mit dem ersten Angriff den Beginn der Operation signalisieren."','Delta以第一擊宣告行動開始。」')
))
lines.append('')

lines.append(L(
    D('Shadow','Shadow'), D('hob','舉起了'), C('一個','eine'),
    D('Hand','手'), C('和','und'), D('unterbrach','打斷了'),
    D('Betas','Beta的'), D('Erklärung','解釋'), '。'
))
lines.append('')

lines.append(L(
    C('在','In'), C('他的','seiner'), D('Hand','手中'),
    D('befand sich','有'), C('一個','ein'), D('einzelner','一封'),
    D('Brief','信'), '。'
))
lines.append('')

lines.append(L(
    D('„Eine Einladung."','「一封邀請函。」')
))
lines.append('')

lines.append(L(
    C('他','Er'), D('warf','丟給了'), D('Beta','Beta'),
    C('那個','den'), D('Brief','信'), C('去','zu'), '，',
    C('那個','die'), C('他','ihn'), C('沒有','ohne'),
    D('Aufforderung','要求'), C('去','zu'), D('lesen','閱讀'),
    D('begann','開始了'), '。'
))
lines.append('')

lines.append(L(
    D('„Ist das etwa ..."','「這難道是……」')
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Einladung','邀請函'), C('是','war'),
    C('如此','so'), D('schlecht','糟糕地'),
    D('verfasst','寫的'), '，', C('說','dass'),
    D('Beta','Beta'), C('在','vor'), D('Ärger','憤怒'),
    D('fassungslos','目瞪口呆'), C('是','war'), '。'
))
lines.append('')

lines.append(L(
    D('„Sag Delta, dass es mir leidtut ...','「告訴Delta，很抱歉……'),
    D('Aber ich werde diesmal selbst das Präludium übernehmen."','但這次前奏我要親自來。」'),
    D('„Natürlich, ich werd\'s ihr ausrichten."','「當然，我會轉告她。」'),
    D('„Folge mir, Beta"','「跟我來，Beta」'), '，',
    D('sagte','說道'), D('Shadow','Shadow'),
    C('和','und'), D('drehte sich um','轉過身'), '。'
))
lines.append('')

lines.append(L(
    D('„Heute Nacht wird die Welt uns kennenlernen."','「今夜世界將認識我們。」'),
    D('Beta','Beta'), D('zitterte','顫抖著'),
    C('在','vor'), D('Freude','喜悅'), '，',
    D('zusammen','一起'), C('用','mit'), C('他','ihm'),
    D('kämpfen','戰鬥'), C('去','zu'), D('können','能'), '。'
))

lines.append(BRK())

# ─── Forest scene ───
lines.append(L(
    C('那個','Der'), C('在','in'), C('那個','der'),
    D('Einladung','邀請函'), D('beschriebene','描述的'),
    D('Ort','地點'), D('lag','位於'), D('tief','深處'),
    C('在','im'), D('Wald','森林'), C('在','an'),
    C('一個','einem'), D('Pfad','小路'), '。',
    C('不','Nicht'), D('weit','遠'), D('entfernt','遠離'),
    C('的','von'), C('那個','dem'), D('Ort','地方'), '，',
    C('在','an'), C('那個','dem'), D('Alexia','Alexia'),
    D('entführt worden war','被綁架的'), '，',
    D('erschien','出現了'), D('Shadow','Shadow'),
    C('在','in'), C('他的','seiner'), D('Schuluniform','校服'), '。'
))
lines.append('')

lines.append(L(
    D('Beta','Beta'), C('是','war'), C('一個','ein'),
    D('kleines Stück','一小段距離'), C('在','hinter'),
    C('他','ihm'), C('和','und'), D('gab acht','小心翼翼'), '，',
    C('她的','ihre'), D('Präsenz','氣息'), C('去','zu'),
    D('verbergen','隱藏'), '。'
))
lines.append('')

lines.append(L(
    D('Kurze Zeit','短時間'), D('später','之後'),
    C('是','waren'), D('zwei','兩個'), D('neue','新的'),
    D('Präsenzen','氣息'), D('spürbar','可以感覺到'), '。'
))
lines.append('')

lines.append(L(
    D('Plötzlich','突然'), D('flog','飛來了'),
    C('某些','etwas'), C('在','auf'), D('Shadow','Shadow'), C('去','zu'), '。',
    C('他','Er'), D('fing','接住了'), C('它','es'),
    C('用','mit'), C('一個','einer'), D('Hand','手'),
    C('和','und'), D('betrachtete','端詳著'), C('它','es'), '。'
))
lines.append('')

lines.append(L(
    D('„Ist das ... Alexias Schuh?"','「這是……Alexia的鞋子？」')
))
lines.append('')

lines.append(L(
    D('Zwei','兩個'), D('Männer','男人'),
    D('tauchten','出現在了'), C('在','auf'), C('那個','dem'),
    D('Waldweg','森林小路'), D('auf','上'), '。'
))
lines.append('')

lines.append(L(
    D('„Hey, Freundchen.','「嘿，小子。'),
    D('Was machst du denn da mit dem Schuh von Prinzessin Alexia?"','你拿著Alexia公主的鞋子在幹什麼？」')
))
lines.append('')

lines.append(L(
    D('„Oha, oha.','「哦呀，哦呀。'),
    D('Jetzt können wir Spuren deiner Magie an dem Schuh nachweisen.','現在我們可以在鞋子上檢測到你的魔力痕跡了。'),
    D('Sieht so aus, als hätten wir unseren Entführer, Cid Kagenou."','看來我們找到了綁架犯，Cid Kagenou。」')
))
lines.append('')

lines.append(L(
    C('那兩個','Die beiden'), D('Männer','男人'),
    D('trugen','穿著'), D('unverkennbare','顯眼的'),
    D('Rüstungen','盔甲'), '。',
    C('它','Es'), C('是','waren'), D('eindeutig','明顯是'),
    C('那兩個','die beiden'), D('Ritter','騎士'), '，',
    C('那些','die'), D('Cid','Cid'), C('在','vor'),
    D('Kurzem','不久前'), D('verhört hatten','審問過的'), '。'
))
lines.append('')

lines.append(L(
    D('„Ach, so ist das also."','「啊，原來如此。」')
))
lines.append('')

lines.append(L(
    C('在','Auf'), D('Cids','Cid的'), D('Worte','話'),
    D('hin',''), D('grinste','咧嘴笑了'),
    C('那個','der'), C('一個','eine'), D('Mann','男人'),
    D('schamlos','無恥地'), '。'
))
lines.append('')

lines.append(L(
    D('„Hast du\'s endlich kapiert?"','「你終於明白了？」')
))
lines.append('')

lines.append(L(
    D('„Du hättest uns den ganzen Ärger ersparen können,','「你大可以省去我們所有的麻煩，'),
    D('wenn du einfach gestanden hättest."','如果你直接認罪的話。」')
))
lines.append('')

lines.append(L(
    D('„Und du hättest auch sehr viel weniger Schmerzen ertragen müssen."','「而且你也會少受很多苦。」')
))
lines.append('')

lines.append(L(
    C('那兩個','Die beiden'), D('Männer','男人'),
    D('zogen','拔出了'), C('她們的','ihre'), D('Schwerter','劍'),
    C('和','und'), D('gingen','走向了'), C('沒有','ohne'),
    D('Vorwarnung','預警'), C('在','auf'), D('Cid','Cid'), C('去','zu'), '。'
))
lines.append('')

lines.append(L(
    D('Was für Idioten','真是蠢貨'), '，', D('dachte','想著'),
    D('Beta','Beta'), '，', C('那個','die'),
    D('angesichts','面對'), C('的','der'), D('Dummheit','愚蠢'),
    C('的','der'), C('兩個','beiden'), D('sprachlos','無語'),
    C('是','war'), '。'
))
lines.append('')

lines.append(L(
    D('„Also, Cid Kagenou, hiermit nehmen wir dich wegen der Entführung von Prinzessin Alexia fest."','「Cid Kagenou，我們現在以綁架Alexia公主的罪名逮捕你。」')
))
lines.append('')

lines.append(L(
    D('„Widersetze dich nicht.','「不要反抗。'),
    D('Auch wenn es dir sowieso nichts bringen würde."','反正也沒用。」')
))
lines.append('')

lines.append(L(
    C('一個','Einer'), C('的','von'), C('他們','ihnen'),
    D('lachte','笑著'), C('和','und'), D('stieß','刺出了'),
    C('他的','sein'), D('Schwert','劍'), C('在','in'),
    D('Cids','Cid的'), D('Richtung','方向'), '，',
    C('然而','doch'), '...'
))
lines.append('')

lines.append(L(
    D('„Was?"','「什麼？」')
))
lines.append('')

lines.append(L(
    D('Cid','Cid'), D('stoppte','停住了'), C('那個','das'),
    D('Schwert','劍'), C('用','mit'), D('zwei','兩根'),
    D('Fingern','手指'), '。',
    C('某些','Etwas'), D('blitzte auf','閃了一下'),
    C('和','und'), D('Cid','Cid'), D('strich','劃過了'),
    C('用','mit'), C('他的','seinem'), D('rechten','右'),
    D('Fuß','腳'), C('在','über'), C('那個','den'),
    D('Hals','脖子'), C('一個','eines'), D('Ritters','騎士的'), '。'
))
lines.append('')

lines.append(L(
    D('Blut','血'), D('spritzte','噴了'), C('從','aus'),
    C('他的','seinem'), D('Hals','脖子'), '。',
    C('一個','Ein'), D('pechschwarzes','漆黑的'),
    D('Messer','刀'), D('ragte','突出來'),
    C('從','aus'), D('Cids','Cid的'), D('Fuß','腳上'), '。'
))
lines.append('')

lines.append(L(
    D('„Gah ... Agh … Ah….!!"','「嘎……啊……啊……！！」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Mann','男人'), D('hielt sich','按住了'),
    C('那個','den'), D('Hals','脖子'), C('和','und'),
    D('fiel','倒在了'), C('去','zu'), D('Boden','地上'), '。',
    C('他','Er'), D('würde','會'), D('bald','很快'),
    D('sterben','死去'), '。'
))
lines.append('')

lines.append(L(
    D('„Was war das?!"','「那是什麼？！」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('andere','另一個'), D('Mann','男人'),
    D('stürzte sich','撲向了'), D('panisch','恐慌地'),
    C('在','auf'), D('Cid','Cid'), '，',
    C('但是','aber'), C('他','er'), C('是','war'),
    D('einfach','簡直'), '...', D('reichlich','相當'),
    D('ungeschickt','笨拙'), '。'
))
lines.append('')

lines.append(L(
    D('Cid','Cid'), D('musste','只需'), C('只','nur'),
    C('他的','seinen'), D('Kopf','頭'), C('一點','ein wenig'),
    D('neigen','傾斜'), '，', C('為了','um'),
    D('auszuweichen','閃避'), '，', C('和','und'),
    D('strich','劃過了'), C('在','über'), C('那個','das'),
    D('Bein','腿'), C('的','des'), D('Ritters','騎士的'), '。'
))
lines.append('')

lines.append(L(
    D('Alles','一切'), D('unterhalb','在……之下'),
    C('他的','seines'), D('Knies','膝蓋'),
    D('wurde','被'), D('abgetrennt','切斷了'), '。'
))
lines.append('')

lines.append(L(
    D('„Aaaaaaahhhhh!!!"','「啊啊啊啊啊啊啊！！！」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Mann','男人'), D('schrie auf','慘叫著'),
    C('和','und'), D('hielt sich','按住了'), C('他的','seinen'),
    D('Stumpf','殘肢'), '，', C('從','aus'), C('那個','dem'),
    D('Blut','血'), D('sprudelte','噴湧著'), '。'
))
lines.append('')

lines.append(L(
    D('„M-Mein Bein ...!!!"','「我……我的腿……！！！」'), '，',
    D('schrie','喊叫著'), C('他','er'), C('和','und'),
    D('versuchte','試著'), C('在','vor'), D('Cid','Cid'),
    D('wegzukriechen','爬走'), '。'
))
lines.append('')

lines.append(L(
    D('„D-Du Bastard!','「你……你這混蛋！'),
    D('Glaub nicht, dass du damit ungestraft davonkommen wirst ...!','別以為你能逍遙法外……！'),
    D('W-Wenn wir sterben, werden sie dich zuerst verdächtigen!"','如……如果我們死了，他們會先懷疑你的！」')
))
lines.append('')

lines.append(L(
    D('Cid','Cid'), D('folgte','跟著'),
    D('einfach','只是'), D('langsam','慢慢地'),
    C('那個','der'), D('Blutspur','血跡'), C('的','des'),
    D('Mannes','男人的'), C('和','und'), D('näherte sich','靠近了'),
    C('他','ihm'), '。'
))
lines.append('')

lines.append(L(
    D('„V-Verdammt ..!','「可……可惡……！'),
    D('Du bist erledigt ...!','你完蛋了……！'),
    D('Erledigt...!"','完蛋了……！」'),
    C('他','Er'), D('kroch','爬著'), C('現在','nun'),
    C('只','nur'), C('還','noch'), D('verzweifelt','絕望地'),
    C('和','und'), D('unbeholfen','笨拙地'),
    C('在','über'), C('那個','den'), D('Boden','地面'), '。'
))
lines.append('')

lines.append(L(
    D('„Wenn sie morgen ... die Leichen von zwei Rittern im Wald finden ...!"','「如果他們明天……在森林裡發現兩個騎士的屍體……！」')
))
lines.append('')

# ─── Shadow transformation ───
lines.append(L(
    C('它','Es'), C('是','war'), D('Shadow','Shadow'), '，',
    D('gekleidet','穿著'), C('在','in'), D('tiefstes','最深的'),
    D('Schwarz','黑色'), '。',
    C('一個','Ein'), D('pechschwarzer','漆黑的'),
    D('Bodysuit','緊身衣'), '，', D('pechschwarze','漆黑的'),
    D('Stiefel','靴子'), '，', C('一個','ein'),
    D('pechschwarzes','漆黑的'), D('Schwert','劍'),
    C('在','in'), C('他的','seiner'), D('Hand','手中'),
    C('和','und'), C('一個','ein'), D('pechschwarzer','漆黑的'),
    D('Mantel','斗篷'), '，', C('那個','der'),
    C('在','im'), D('Wind','風中'), D('flatterte','飄動著'), '。',
    C('那個','Die'), D('Kapuze','兜帽'), C('他的','seines'),
    D('Mantels','斗篷的'), D('bedeckte','遮住了'),
    D('viel','很多'), C('的','von'), C('他的','seinem'),
    D('Gesicht','臉'), '，', C('所以','sodass'), C('那個','die'),
    D('obere Hälfte','上半部'), C('在','in'), C('那些','den'),
    D('Schatten','陰影中'), D('verborgen lag','隱藏著'),
    C('和','und'), C('只','nur'), C('那個','die'),
    D('untere','下半部'), C('從','vom'), D('Licht','光'),
    D('erreicht wurde','照到'), '。',
    C('他的','Sein'), D('Gesicht','臉'), C('是','war'),
    C('然而','jedoch'), C('透過','durch'), C('一個','eine'),
    D('Maske','面具'), D('verborgen','遮住了'), '，',
    C('那個','die'), C('在','an'), C('一個','einen'),
    D('Magier','魔法師'), D('erinnerte','讓人想起'), '，',
    D('weshalb','因此'), C('只','nur'), C('他的','sein'),
    D('Mund','嘴巴'), C('和','und'), C('他的','seine'),
    D('roten','紅色的'), D('Augen','眼睛'),
    D('sichtbar','看得見'), C('是','waren'), '。'
))
lines.append('')

lines.append(L(
    D('Beta','Beta'), D('fiel','差點'), C('在','bei'),
    C('這個','diesem'), D('würdevollen','威嚴'), C('和','und'),
    D('wunderschönen','美麗的'), D('Anblick','景象'),
    D('beinahe','幾乎'), C('在','in'), D('Ohnmacht','昏厥'), '，',
    D('zog','拿出了'), C('在','in'), D('aller Schnelle','匆忙中'),
    C('一個','ein'), C('自己','selbst'), D('verfasstes','編寫的'),
    D('Notizbuch','筆記本'), D('namens','名為'),
    D('Erzählungen von Lord Shadow','Shadow大人物語'),
    C('從','aus'), C('她的','ihrem'), D('Dekolleté','胸口'),
    C('和','und'), D('fing an','開始了'), C('去','zu'),
    D('skizzieren','素描'), '。'
))
lines.append('')

lines.append(L(
    D('„Dann bist du erledigt!"','「那你就完蛋了！」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Mann','男人'), D('kroch','爬著'),
    D('weiter','繼續'), C('和','und'), D('Cid','Cid'),
    D('folgte','跟著'), C('他','ihm'), '。'
))
lines.append('')

lines.append(L(
    D('„Mach dir darüber keine Sorgen."','「別擔心那個。」')
))
lines.append('')

lines.append(L(
    C('在','In'), C('這個','diesem'), D('Moment','瞬間'),
    D('bemerkte','注意到了'), C('那個','der'), D('Ritter','騎士'), '，',
    C('說','dass'), D('Cid','Cid'), D('bereits','已經'),
    C('在','hinter'), C('他','ihm'), C('是','war'), '。'
))
lines.append('')

lines.append(L(
    D('„B-Bitte!"','「拜……拜託！」')
))
lines.append('')

lines.append(L(
    D('Cids','Cid的'), D('rechter','右'), D('Fuß','腳'),
    D('blitzte auf','閃了一下'), '。'
))
lines.append('')

lines.append(L(
    D('„Morgen ... wird das alles schon vorüber sein."','「明天……這一切就會結束了。」'),
    C('那個','Der'), D('Kopf','頭'), C('的','des'),
    D('Mannes','男人的'), D('flog','飛了'), C('透過','durch'),
    C('那個','die'), D('Luft','空中'), '。'
))
lines.append('')

lines.append(L(
    D('Inmitten','在……之中'), C('的','des'), D('Blutbads','血海'),
    D('drehte sich','轉過了'), D('Cid','Cid'), D('um','身'), '。',
    C('他的','Sein'), D('Anblick','景象'), D('ließ','讓'),
    D('Beta','Beta'), D('erschaudern','不寒而慄'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Mann','男人'), '，', C('那個','der'),
    C('那裡','dort'), D('stand','站著'), '，',
    C('是','war'), C('不','nicht'), C('更多','mehr'),
    D('Cid','Cid'), C('在','in'), C('他的','seiner'),
    D('Schuluniform','校服'), '。'
))
lines.append('')

lines.append(L(
    C('旁邊','Neben'), C('那個','der'), D('Zeichnung','素描'),
    D('fügte','加上了'), C('她','sie'), C('那些','die'),
    D('heutigen','今天的'), D('Zitate','語錄'), C('的','von'),
    D('Lord Shadow','Shadow大人'), D('ein',''), '，',
    C('為了','um'), C('那個','die'), D('Seite','頁面'),
    C('去','zu'), D('vervollständigen','完成'), '。',
    D('Alles in allem','總共'), D('brauchte','花了'),
    C('她','sie'), C('為此','dafür'), D('fünf Sekunden','五秒鐘'), '。'
))
lines.append('')

lines.append(L(
    D('Nebenbei bemerkt','順帶一提'), '：',
    D('Betas','Beta的'), D('Zimmerwände','房間牆壁'),
    C('是','waren'), D('übersät','貼滿了'),
    C('的','von'), D('Bildern','圖片'), C('和','und'),
    D('Zitaten','語錄'), C('的','von'), D('Shadow','Shadow'), '。',
    C('那個','Das'), D('Schreiben','書寫'), C('的','von'),
    D('Erzählungen von Lord Shadow','Shadow大人物語'),
    C('在','vor'), C('那個','dem'), D('Schlafengehen','睡覺前'),
    C('是','war'), C('為了','für'), C('她','sie'),
    C('一個','ein'), D('unvergleichliches','無與倫比的'),
    D('Vergnügen','樂趣'), '。'
))
lines.append('')

lines.append(L(
    C('然而','Doch'), D('urplötzlich','突然間'),
    D('holte','拉回了'), C('一個','eine'),
    D('entfernte','遠處的'), D('Explosion','爆炸'),
    D('Beta','Beta'), C('進入','in'), C('那個','die'),
    D('Realität','現實'), D('zurück',''), '。'
))
lines.append('')

lines.append(L(
    D('„Das ist wohl Delta ...','「那大概是Delta……'),
    D('Nocturne hat begonnen.','夜曲已經開始了。'),
    D('Gehen wir, Beta."','走吧，Beta。」')
))
lines.append('')

lines.append(L(
    D('„S-Sofort! Ich komme sofort!"','「馬……馬上！我馬上來！」')
))
lines.append('')

lines.append(L(
    D('Beta','Beta'), D('schob','塞回了'), C('那個','das'),
    D('Notizbuch','筆記本'), C('再次','wieder'),
    C('在','in'), C('她的','ihr'), D('Dekolleté','胸口'),
    C('和','und'), D('lief','跑著'), C('他','ihm'),
    D('hinterher','追上去了'), '。',
    C('當然','Natürlich'), D('wusste','知道'),
    D('Shadow','Shadow'), C('什麼都不','nichts'),
    C('關於','über'), D('Betas','Beta的'),
    D('Lebenswerk','畢生事業'), '。'
))

lines.append(BRK())

# ─── Delta scene ───
lines.append(L(
    D('„W-Wer bist du?! Was willst du von uns?!"','「你……你是誰？！你想對我們怎樣？！」'),
    C('一個','Ein'), D('Meer','海'), C('的','von'), D('Blut','血'), '。'
))
lines.append('')

lines.append(L(
    C('如此','So'), D('konnte','可以'), C('人們','man'),
    C('那個','den'), D('Ort','地方'), D('beschreiben','形容'), '，',
    C('在','an'), C('那個','dem'), C('那個','der'),
    D('Mann','男人'), D('schrie','喊叫著'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), D('kam','來了'), C('從','aus'),
    C('那個','dem'), D('Nichts','虛無中'), '。'
))
lines.append('')

lines.append(L(
    C('沒有','Ohne'), D('Vorwarnung','預警'), C('和','und'),
    C('沒有','ohne'), D('Grund','理由'), D('brach','破了'),
    C('它','es'), C('透過','durch'), C('那個','die'),
    D('Wand','牆壁'), C('和','und'), D('begann','開始了'),
    C('它的','sein'), D('Massaker','屠殺'), '。'
))
lines.append('')

lines.append(L(
    C('正好','Gerade'), D('fiel','倒下了'), C('還','noch'),
    C('一個','eine'), D('Person','人'), C('那個','dem'),
    D('schwarzen','黑色的'), D('Schwert','劍'),
    C('去','zum'), D('Opfer','犧牲品'), '。'
))
lines.append('')

lines.append(L(
    C('沒有人','Keiner'), D('wollte','想'), C('更多','mehr'),
    C('對抗','gegen'), C('它','Es'), D('kämpfen','戰鬥'), '。',
    C('每個','Jeder'), D('wollte','想'), C('只','nur'), C('還','noch'),
    D('fliehen','逃跑'), '。', C('但是','Aber'), C('它','es'),
    D('gab','有'), C('只','nur'), C('一個','einen'),
    D('Ausweg','出路'), C('和','und'), C('那個','der'),
    D('lag','在'), C('在','hinter'), C('他','ihm'), '。'
))
lines.append('')

lines.append(L(
    D('„Was haben wir dir bloß angetan?!','「我們到底對你做了什麼？！'),
    D('Wir haben doch nichts gemacht!!!"','我們什麼都沒做啊！！！」')
))
lines.append('')

lines.append(L(
    C('它','Es'), D('drehte sich','轉向了'), C('去','zu'),
    C('那個','dem'), D('Mann','男人'), D('um',''),
    C('和','und'), D('lachte','笑了'), '。'
))
lines.append('')

lines.append(L(
    D('„A-Aahh …..!"','「啊……啊……！！」')
))
lines.append('')

lines.append(L(
    C('雖然','Obwohl'), C('它的','sein'), D('Gesicht','臉'),
    C('的','von'), C('一個','einer'), D('pechschwarzen','漆黑的'),
    D('Maske','面具'), D('verdeckt','遮住'), C('是','war'), '，',
    D('lächelte','微笑著'), C('它','Es'), C('儘管如此','dennoch'),
    D('grausam','殘酷地'), '。'
))
lines.append('')

lines.append(L(
    D('„H-Hilf mir...!"','「救……救我……！」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Mann','男人'), D('wurde','被'),
    C('從','vom'), D('Kopf','頭'), C('直到','bis'),
    C('到','zur'), D('Leiste','胯部'), C('在','in'),
    D('zwei Hälften','兩半'), D('gespalten','劈開了'), '。',
    C('她們','Sie'), D('fielen','倒向了'), C('在','nach'),
    D('links','左邊'), C('和','und'), D('rechts','右邊'),
    C('和','und'), C('在','in'), D('alle Richtungen','各個方向'),
    D('spritzte','噴灑著'), D('Blut','血'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), D('liebte','喜愛'), D('Blut','血'),
    C('和','und'), C('它','es'), D('gefiel','喜歡'),
    C('他','Ihm'), '，', C('在裡面','darin'), C('去','zu'),
    D('baden','沐浴'), '。',
    C('它','Es'), D('hatte','有'), C('雖然','zwar'),
    C('那個','die'), D('Form','形態'), C('一個','eines'),
    D('Mädchens','少女的'), '，', C('但是','aber'),
    C('在','in'), C('這個','diesem'), D('Moment','瞬間'),
    D('wirkte','看起來'), C('它','Es'), C('更多','mehr'),
    C('像','wie'), C('一個','ein'), D('Dämon','惡魔'), '。'
))
lines.append('')

lines.append(L(
    C('它','Es'), D('sah sich um','環顧四周'), C('和','und'),
    D('bemerkte','注意到'), '，', C('說','dass'),
    D('kaum','幾乎不'), C('還','noch'), C('某些','etwas'),
    C('的','von'), C('那個','der'), D('Beute','獵物'),
    D('übrig','剩餘的'), C('是','war'), '，',
    C('所以','also'), D('streckte','伸長了'),
    C('它','Es'), C('它的','seine'), D('Waffe','武器'), '。'
))
lines.append('')

lines.append(L(
    C('但是','Aber'), C('那','das'), C('是','war'),
    C('沒有','keine'), D('Metapher','比喻'), '，',
    D('mitnichten','絕不'), '。',
    C('它','Es'), D('verlängerte','延長了'), C('它的','sein'),
    D('Schwert','劍'), '，', C('直到','bis'), C('它','es'),
    C('那個','die'), D('entgegengesetzte','對面的'),
    D('Hauswand','房屋牆壁'), D('durchstach','刺穿了'), '。'
))
lines.append('')

lines.append(L(
    C('和','Und'), C('然後','dann'), D('schwang','揮動了'),
    C('它','Es'), C('它的','Sein'), D('Schwert','劍'), '。'
))
lines.append('')

lines.append(L(
    D('„N-Nein ..!"','「不……不要……！」')
))
lines.append('')

lines.append(L(
    C('那個','Das'), D('Gebäude','建築物'), C('和','und'),
    D('alle','所有'), '，', C('那些','die'), C('自己','sich'),
    C('在裡面','darin'), D('befanden','在的'), '，',
    D('wurden','被'), C('的','der'), D('Länge nach','縱向地'),
    D('zerschnitten','切開了'), '。'
))

lines.append(BRK())

# ─── Alpha on clock tower ───
lines.append(L(
    D('„Es hat begonnen."','「開始了。」')
))
lines.append('')

lines.append(L(
    C('從','Von'), C('那個','der'), D('Spitze','頂端'),
    C('的','des'), D('Uhrturms','鐘塔'), D('aus',''),
    D('beobachtete','觀察著'), C('一個','eine'),
    D('wunderschöne','美麗的'), D('Elfe','精靈'), '，',
    C('像','wie'), C('那個','das'), D('Gebäude','建築物'),
    D('durchtrennt wurde','被切開了'), C('和','und'),
    D('gleich','像'), C('一個','einem'), D('Kartenhaus','紙牌屋'),
    C('在','in'), C('自己','sich'), D('zusammenfiel','倒塌了'), '。',
    C('她的','Ihr'), D('langes','長長的'), D('goldenes','金色的'),
    D('Haar','頭髮'), D('wehte','飄動著'), C('在','im'),
    D('Wind','風中'), C('和','und'), D('schimmerte','閃爍著'),
    C('在','in'), C('那個','der'), D('Nacht','夜色中'), '。'
))
lines.append('')

lines.append(L(
    D('„Delta ... Immer muss sie übertreiben."','「Delta……她總是要搞得那麼誇張。」'),
    C('她','Sie'), D('seufzte','嘆了口氣'), C('和','und'),
    D('schüttelte','搖了搖'), C('那個','den'), D('Kopf','頭'), '。'
))
lines.append('')

lines.append(L(
    C('什麼','Was'), D('geschehen war','發生了的'), '，',
    C('是','war'), D('geschehen','已成定局'), '。',
    D('Alpha','Alpha'), D('überblickte','俯瞰著'),
    C('從','vom'), D('Uhrturm','鐘塔'), D('aus',''),
    C('那整個','die gesamte'), D('Königliche Hauptstadt','王都'), '。'
))
lines.append('')

lines.append(L(
    C('她們','Sie'), D('fegten','掃蕩著'), C('在','über'),
    C('那整個','die gesamte'), D('Stadt','城市'), '。',
    D('Alles','一切'), D('verlief','進行著'),
    C('像','wie'), D('geplant','計畫的'), '。',
    C('那些','Die'), D('meiste','最多的'), D('Aufmerksamkeit','注意力'),
    D('richtete sich','集中在'), C('在','auf'), D('Delta','Delta'), '，',
    C('那個','die'), C('正好','gerade'), C('一個','ein'),
    D('Gebäude','建築物'), D('abgerissen hatte','拆掉了'), '。'
))
lines.append('')

lines.append(L(
    D('„Immerhin macht Delta es uns einfacher, ungesehen zu agieren..."','「至少Delta讓我們更容易不被發現地行動……」')
))
lines.append('')

lines.append(L(
    C('如果','Wenn'), C('人們','man'), C('的','von'),
    D('all der','所有那些'), D('Zerstörung','破壞'),
    D('absah','撇開不談'), '，',
    D('hatte','有'), D('Delta','Delta'), C('真的','wirklich'),
    C('她的','ihr'), D('Bestes','最好'), D('gegeben','盡了'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich sollte mich auch langsam auf den Weg machen"','「我也該慢慢上路了」'), '，',
    D('murmelte','喃喃道'), D('Alpha','Alpha'), '，',
    C('她的','ihr'), D('Gesicht','臉'), C('的','von'),
    C('一個','einer'), D('pechschwarzen','漆黑的'),
    D('Maske','面具'), D('verdeckt','遮住'), '。'
))

lines.append(BRK())

# ─── Alexia in cell again ───
lines.append(L(
    D('Draußen ist einiges los.','外面很熱鬧。')
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('öffnete','睜開了'),
    C('去','zum'), D('ersten Mal','第一次'), C('自從','seit'),
    D('Stunden','幾個小時'), C('她的','ihre'),
    D('Augen','眼睛'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Mann in Weiß','白衣男人'),
    C('和','und'), C('一個','eine'), D('Putzfrau','清潔婦'),
    D('kamen','來'), C('作為','als'), D('einzige','唯一的'),
    D('Menschen','人'), C('在','in'), C('這個','diesen'),
    D('Raum','房間'), C('和','und'), C('如此','so'),
    D('hatte','有'), D('Alexia','Alexia'), '，',
    C('那個','die'), C('總是','immer'), C('還','noch'),
    C('在','an'), C('那個','die'), D('Wand','牆壁'),
    D('gekettet','被鎖著'), C('是','war'), '，',
    C('什麼都不','nichts'), D('Besseres','更好的'),
    C('去','zu'), D('tun','做的'), C('比','als'),
    C('去','zu'), D('schlafen','睡覺'), '。',
    C('用','Mit'), C('她的','ihrem'), D('monströsen','可怕的'),
    D('Mitbewohner','室友'), D('verstand','相處'),
    C('她','sie'), C('自己','sich'), D('recht gut','還不錯'), '，',
    C('因為','da'), C('她們','sie'), C('自己','sich'),
    D('gegenseitig','互相'), D('ignorierten','無視'), '。',
    C('那個','Der'), D('Lärm','噪音'), C('的','von'),
    D('draußen','外面'), D('wurde','變得'),
    C('總是','immer'), D('lauter','更大聲'),
    C('和','und'), D('deutete darauf hin','暗示著'), '，',
    C('說','dass'), C('某些','etwas'), D('Großes','大的事情'),
    C('在','im'), D('Gang','進行中'), C('是','war'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('dachte','想到了'),
    C('在','an'), C('她的','ihre'), D('Rettung','救援'),
    C('和','und'), D('musste','不禁'), D('lachen','笑了'), '。'
))
lines.append('')

lines.append(L(
    D('„Vielleicht brechen sie ja mit einer großen Explosion durch die Kerkerwand"','「也許他們會用一次大爆炸炸穿地牢的牆壁」'), '，',
    D('murmelte','喃喃說道'), C('她','sie'),
    D('beiläufig','隨口'), C('在','vor'), C('自己','sich'), D('hin',''), '。',
    C('她','Sie'), D('stand','站著'), C('大概','wohl'),
    C('在','unter'), D('großem','巨大的'),
    D('Stress','壓力下'), '，',
    C('因為','denn'), C('她','sie'), D('rüttelte','搖晃著'),
    C('在','an'), C('她的','ihren'), D('Ketten','鎖鏈'), '，',
    C('雖然','obwohl'), C('她','sie'), D('wusste','知道'), '，',
    C('像','wie'), D('sinnlos','無意義'), C('那','das'),
    C('是','war'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Kreatur','生物'), C('旁邊','neben'),
    C('她','ihr'), D('hob','抬起了'), C('那個','den'),
    D('Kopf','頭'), '。'
))
lines.append('')

lines.append(L(
    D('„Tut mir leid, habe ich dich geweckt?','「對不起，我吵醒你了嗎？'),
    D('Vielleicht solltest du lieber wach bleiben.','也許你最好保持清醒。'),
    D('Das könnte lustig werden."','可能會很有趣。」'),
    D('Alexia','Alexia'), D('sprach','說著話'),
    C('用','mit'), C('她','ihr'), '，',
    D('wenngleich','雖然'), C('她','sie'), D('wusste','知道'), '，',
    C('說','dass'), C('她','sie'), C('不','nicht'),
    D('antworten würde','會回答'), '。',
    C('如此','So'), C('某些','etwas'), D('löste','引起'),
    C('在','bei'), D('Menschen','人們'),
    D('Langeweile','無聊'), D('aus',''), '。'
))
lines.append('')

lines.append(L(
    D('Kurze Zeit','短時間'), D('später','之後'),
    D('hörte','聽到了'), C('她','sie'), '，',
    C('像','wie'), C('那個','die'), D('Tür','門'),
    D('aufgeschlossen wurde','被打開了'), '。',
    C('那裡','Da'), D('hatte','有'), C('它','es'),
    C('某人','jemand'), D('eilig','急忙'),
    C('和','und'), C('是','war'), D('unruhig','不安的'), '。'
))
lines.append('')

lines.append(L(
    D('„Verdammt noch mal! Verdammt!!!"','「該死！該死！！！」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Mann in Weiß','白衣男人'),
    D('öffnete','打開了'), D('überstürzt','匆忙地'),
    C('那個','die'), D('Tür','門'), C('和','und'),
    D('trat ein','走了進來'), '。'
))
lines.append('')

lines.append(L(
    D('„Guten Tag."','「你好。」')
))
lines.append('')

lines.append(L(
    D('„Nur noch ein bisschen.','「就差一點點了。'),
    D('Ich bin so nah dran!!!"','我都快成功了！！！」'),
    D('Sichtlich','明顯地'), D('unerfreut','不高興'),
    D('ignorierte','無視了'), C('他','er'), D('Alexias','Alexia的'),
    D('Begrüßung','問候'), '。'
))
lines.append('')

lines.append(L(
    D('„S-Sie sind es schon wieder!','「他……他們又來了！'),
    D('Sie sind gekommen!!!','他們來了！！！'),
    D('E-E-Es ist vorbei, vorbei, alles ist vorbei ...!"','一……一切都完了，完了，全完了……！」')
))
lines.append('')

lines.append(L(
    D('„Gib auf, es bringt nichts, sich zu widersetzen.','「放棄吧，反抗也沒用。'),
    D('Wenn du mich von meinen Fesseln befreist,','如果你解開我的束縛，'),
    D('werde ich sie bitten, zumindest dein Leben zu verschonen."','我會請他們至少饒你一命。」'),
    D('Leise','輕聲地'), D('fügte','補充道'), D('Alexia','Alexia'),
    D('hinzu',''), '：',
    D('„Aber auch nur bitten."','「只是拜託而已。」')
))
lines.append('')

lines.append(L(
    D('„D-Die werden mich nie am Leben lassen ...!','「他……他們絕不會讓我活的……！'),
    D('A-Alle sind tot!!!"','所……所有人都死了！！！」')
))
lines.append('')

lines.append(L(
    D('„Der Orden tötet nicht, wenn es nicht nötig ist.','「騎士團不會在不必要的時候殺人。'),
    D('Wenn du dich stellst, werden sie dich verschonen."','如果你自首，他們會放過你。」'),
    D('Seit wann ist der Orden so tötungswütig?','從什麼時候起騎士團這麼嗜殺了？'), '，',
    D('fragte sich','心想'), D('Alexia','Alexia'),
    C('在','in'), D('Gedanken','心裡'), '。'
))
lines.append('')

lines.append(L(
    D('„Der Ritterorden?','「騎士團？'),
    D('Die Ritter sind mir egal!','騎士我才不管！'),
    D('D-Die haben alle umgebracht,','他……他們把所有人都殺了，'),
    D('sie werden uns alle umbringen!!!"','他們會把我們全部殺掉的！！！」'),
    D('„Es ist nicht der Orden?"','「不是騎士團？」')
))
lines.append('')

lines.append(L(
    C('但是','Aber'), C('誰','wer'), C('是','war'),
    C('它','es'), C('然後','dann'), '？',
    C('不','Nein'), '，', C('它','es'), D('könnte','可能'),
    C('也','auch'), C('是','sein'), '，', C('說','dass'),
    C('他','er'), D('zuletzt','最後'), D('komplett','完全'),
    D('durchgedreht war','瘋了'), '。'
))
lines.append('')

lines.append(L(
    D('„So oder so ist es vorbei.','「不管怎樣都結束了。'),
    D('Du solltest aufgeben."','你應該放棄了。」'),
    D('„Nein, nein, nein, nein, nein, nein, NEIN!!!','「不不不不不不不！！！'),
    D('W-Wenn ich es nur beenden könnte...!!"','如……如果我能完成的話……！！」')
))
lines.append('')

# ─── Creature transforms ───
lines.append(L(
    C('那個','Der'), D('Mann','男人'), C('在','im'),
    D('Laborkittel','實驗袍'), D('kratzte sich','搔了搔'),
    C('在','am'), D('Kopf','頭'), C('和','und'),
    D('richtete','對準了'), C('他的','seine'),
    D('blutunterlaufenen','佈滿血絲的'),
    D('Augen','眼睛'), C('在','auf'), C('那個','die'),
    D('Kreatur','生物'), '。'
))
lines.append('')

lines.append(L(
    D('„I-Ich habe einen Prototyp gemacht.','「我……我做了一個原型。'),
    D('S-Sogar ein nutzloses Stück wie du könnte damit etwas anfangen."','就……就連你這種沒用的東西也能用它派上用場。」'),
    C('用','Mit'), C('這些','diesen'), D('Worten','話語'),
    D('drückte','按壓了'), C('那個','der'), D('Mann','男人'),
    C('一個','eine'), D('Nadel','針'), C('對抗','gegen'),
    C('那個','den'), D('Arm','手臂'), C('的','der'),
    D('Kreatur','生物'), '。'
))
lines.append('')

lines.append(L(
    D('„Tu das nicht.','「不要那樣做。'),
    D('Ich habe kein gutes Gefühl bei der Sache"','我對這件事有不好的預感」'), '，',
    D('sagte','說道'), D('Alexia','Alexia'),
    D('unerwartet','出乎意料地'), D('ernst','認真地'), '。'
))
lines.append('')

lines.append(L(
    C('他','Er'), D('ignorierte','無視了'), C('她','sie'),
    C('當然','natürlich'), '，', D('stach','扎進了'),
    C('那個','die'), D('Nadel','針'), C('在','in'),
    C('那個','den'), D('Arm','手臂'), C('的','der'),
    D('Kreatur','生物'), C('和','und'), D('injizierte','注射了'),
    C('她','ihr'), C('某些','etwas'), '。'
))
lines.append('')

lines.append(L(
    D('„S-Sieh gut hin!','「好……好好看著！'),
    D('Ein Fragment von Diabolos Macht!!!"','Diabolos力量的碎片！！！」'),
    D('„Wow, ich freu mich drauf."','「哇，我好期待。」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('Körper','身體'), C('的','der'),
    D('Kreatur','生物'), D('dehnte sich','膨脹了'),
    D('plötzlich','突然'), D('aus',''), '。',
    C('它的','Seine'), D('Muskeln','肌肉'), D('schwollen an','膨脹了'),
    C('和','und'), C('甚至','sogar'), C('它的','sein'),
    D('Skelett','骨骼'), D('wuchs','生長了'),
    C('和','und'), D('verlängerte sich','延長了'),
    C('總是','immer'), D('weiter','更'), '。',
    C('它的','Sein'), D('rechter','右'), D('Arm','手臂'), '，',
    C('那個','der'), D('viel zu','太過'), D('groß','大'),
    C('和','und'), D('dick','粗'), C('是','war'), '，',
    D('wurde','變得'), C('還','noch'), D('monströser','更加可怕'),
    C('和','und'), C('從中','daraus'), D('wuchsen','長出了'),
    D('lange','長長的'), D('Krallen','爪子'), '，',
    C('那些','die'), D('jeweils','每一根'),
    C('如此','so'), D('lang','長'), C('是','waren'),
    C('像','wie'), C('一個','ein'), D('menschliches','人類的'),
    D('Bein','腿'), '。',
    C('它的','Sein'), D('linker','左'), D('Arm','手臂'),
    C('是','war'), C('繼續','weiterhin'), C('在','am'),
    D('Rumpf','軀幹'), D('befestigt','固定著'), '，',
    C('好像','als würde'), C('他','er'), C('某些','etwas'),
    D('festhalten','緊握著'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Kreatur','生物'), D('gab','發出了'),
    C('一個','ein'), D('schrilles','尖銳的'),
    D('Brüllen','怒吼'), C('的','von'), C('自己','sich'), '，',
    D('beinahe','幾乎是'), C('一個','einen'),
    D('Schrei','尖叫'), '。'
))
lines.append('')

lines.append(L(
    D('„W-Wunderbar, einfach wunderbar!!!"','「太……太棒了，簡直太棒了！！！」')
))
lines.append('')

lines.append(L(
    D('„Ich bin …. überrascht."','「我……感到驚訝。」')
))
lines.append('')

lines.append(L(
    C('那些','Die'), D('Fesseln','束縛'), C('的','der'),
    D('Kreatur','生物'), D('hielten','承受住'),
    C('這個','diesem'), D('rasanten','急速的'),
    D('Wachstum','生長'), C('當然','natürlich'),
    C('不','nicht'), D('stand',''), C('和','und'),
    D('zerbarsten','碎裂了'), C('在','in'),
    D('viele','許多'), D('Einzelteile','碎片'), '。'
))
lines.append('')

lines.append(L(
    D('„Deshalb habe ich gesagt, du sollst es lassen."','「所以我才說叫你別做。」')
))
lines.append('')

lines.append(L(
    D('Quetsch','擠壓'), '...'
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('rechte','右'), D('Arm','手臂'),
    C('的','des'), D('Monsters','怪物'),
    D('hatte','已經'), C('那個','den'),
    D('Mann in Weiß','白衣男人'), D('zerdrückt','碾碎了'), '。'
))
lines.append('')

lines.append(L(
    D('„Tja, das habe ich kommen sehen."','「嗯，我就知道會這樣。」')
))
lines.append('')

lines.append(L(
    D('Alexias','Alexia的'), D('Augen','眼睛'),
    D('trafen sich','對上了'), C('用','mit'), C('那些','denen'),
    C('的','der'), D('Kreatur','生物'), '。'
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('beobachtete','觀察著'),
    C('她的','ihre'), D('Bewegungen','動作'), '。',
    C('用','Mit'), D('gefesselten','被束縛的'),
    D('Gliedmaßen','四肢'), D('konnte','能'),
    C('她','sie'), C('只','nur'), D('wenig','很少'),
    D('ausrichten','做到'), '，', C('但是','aber'),
    C('她','sie'), D('musste','必須'), C('某些','etwas'),
    D('versuchen','嘗試'), '。',
    C('她','Sie'), D('wollte','不想'), C('不','nicht'),
    C('作為','als'), D('Kollateralschaden','附帶損害'),
    C('的','der'), D('Experimente','實驗'), C('一個','irgendeines'),
    D('Wahnsinnigen','瘋子的'), D('enden','結束'), '。'
))
lines.append('')

lines.append(L(
    C('那個','Die'), D('Kreatur','生物'), D('schwang','揮動了'),
    C('她的','ihren'), D('rechten','右'), D('Arm','手臂'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('zappelte','掙扎著'),
    C('和','und'), D('drehte sich','轉動著'),
    C('如此','so'), D('gut','好'), C('她','sie'),
    D('konnte','可以'), '。'
))
lines.append('')

lines.append(L(
    C('只要','Solang'), C('她','sie'), C('一個','eine'),
    D('tödliche','致命的'), D('Verletzung','傷害'),
    D('vermeiden','避免'), D('könnte','可以'), '...！'
))
lines.append('')

lines.append(L(
    D('„…..?!"','「……？！」')
))
lines.append('')

lines.append(L(
    C('那個','Der'), D('rechte','右'), D('Arm','手臂'),
    D('flog','飛過了'), C('在','an'), D('Alexia','Alexia'),
    D('vorbei','旁邊'), C('和','und'), D('zerstörte','摧毀了'),
    C('那個','den'), D('Sockel','基座'), '，',
    C('在','an'), C('那個','dem'), C('她的','ihre'),
    D('Fesseln','束縛'), D('befestigt','固定著'), C('是','waren'), '。',
    C('也','Auch'), C('如果','wenn'), C('那個','der'),
    D('eigentliche','實際的'), D('Hieb','攻擊'),
    C('她','sie'), D('verfehlte','沒有擊中'), '，',
    D('wurde','被'), C('她','sie'), C('透過','durch'),
    C('那個','den'), D('Aufprall','衝擊力'),
    C('對抗','gegen'), C('那個','die'), D('Wand','牆壁'),
    D('geworfen','甩了出去'), C('和','und'),
    D('ohnmächtig','昏了過去'), '。'
))
lines.append('')

lines.append(L(
    D('„Agh...!"','「啊！」')
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('hatte','有'), C('自己','sich'),
    C('既不','weder'), C('某些','etwas'), D('gebrochen','骨折'),
    C('還','noch'), D('hatte','有'), C('她','sie'),
    D('erkennbare','明顯的'), D('Verletzungen','傷勢'),
    C('和','und'), D('konnte','可以'), C('自己','sich'),
    D('bewegen','移動'), '。'
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('ging sicher','確認了'), '，',
    C('說','dass'), C('她','sie'), C('不','nicht'),
    D('verletzt','受傷'), C('是','war'), '，',
    C('和','und'), D('stand','站了'), C('在','im'),
    D('Nu','一瞬間'), D('auf','起來'), '。'
))
lines.append('')

lines.append(L(
    C('然而','Doch'), C('那個','die'), D('Kreatur','生物'),
    C('是','war'), D('bereits','已經'),
    D('verschwunden','消失了'), '。'
))
lines.append('')

lines.append(L(
    C('在','An'), C('她的','ihrer'), D('Stelle','位置'),
    D('befanden sich','有'), C('只','nur'), C('還','noch'),
    C('那個','der'), D('zerstörte','被摧毀的'),
    D('Sockel','基座'), C('和','und'), C('一個','eine'),
    D('durchbrochene','被打穿的'), D('Wand','牆壁'), '。'
))
lines.append('')

lines.append(L(
    D('„Hat ... es mich gerettet...?"','「它……救了我……？」')
))
lines.append('')

lines.append(L(
    D('Ehe','在……之前'), C('自己','sich'), D('Alexia','Alexia'),
    D('wegdrehen','轉身'), D('konnte','可以'), '，',
    D('hatte','有'), C('那個','der'), D('Arm','手臂'),
    D('bereits','已經'), C('那個','die'), D('Wand','牆壁'),
    D('getroffen','擊中了'), '。',
    D('Könnte','可能'), C('它','es'), C('是','sein'), '，',
    C('說','dass'), '...', C('不','Nein'), '，',
    C('也許','vielleicht'), D('hatte','有'), C('那個','die'),
    D('Kreatur','生物'), C('她','sie'), D('einfach','只是'),
    D('verfehlt','沒打中'), '。'
))
lines.append('')

lines.append(L(
    D('„Wie auch immer."','「不管怎樣。」')
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('zog','拔出了'), C('那個','den'),
    D('Schlüssel','鑰匙'), C('從','aus'), C('那個','dem'),
    D('blutbesudelten','沾滿血的'), D('Laborkittel','實驗袍'),
    C('和','und'), D('entfernte','取下了'), C('那些','die'),
    D('magieversiegelnden','封印魔力的'), D('Ketten','鎖鏈'), '。'
))
lines.append('')

lines.append(L(
    C('現在','Nun'), D('konnte','可以'), C('她','sie'),
    C('再次','wieder'), D('Magie','魔法'), D('einsetzen','使用了'), '。',
    D('Alexia','Alexia'), D('streckte sich','伸了個懶腰'),
    C('一次','einmal'), '，', D('atmete auf','鬆了口氣'),
    C('和','und'), D('trat','走過了'), C('透過','durch'),
    C('那個','die'), D('zerstörte','被摧毀的'), D('Wand','牆壁'), '，',
    C('那個','die'), C('那個','die'), D('Kreatur','生物'),
    D('hinterlassen hatte','留下的'), '。'
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('betrat','走進了'), C('一個','einen'),
    D('langen','長長的'), '，', D('schwach','微弱地'),
    D('beleuchteten','照明的'), D('Korridor','走廊'), '。',
    D('Überall','到處'), D('verstreut','散落著'),
    D('lagen','躺著'), D('tote','死去的'),
    D('Soldaten','士兵們'), '，', C('那些','die'),
    C('的','von'), C('那個','der'), D('Kreatur','生物'),
    D('zerquetscht worden waren','被碾碎了的'), '。'
))
lines.append('')

lines.append(L(
    D('„Ich leih mir das mal aus."','「我借用一下。」')
))
lines.append('')

lines.append(L(
    D('Alexia','Alexia'), D('nahm sich','拿了'),
    C('的','von'), C('一個','einer'), C('的','der'),
    D('Leichen','屍體'), C('一個','ein'),
    D('Mithrilschwert','秘銀劍'), '。',
    C('它','Es'), C('是','war'), C('不','nicht'),
    C('的','von'), D('hoher','高'), D('Qualität','品質'), '，',
    C('但是','aber'), D('fürs Erste','暫時'),
    D('genügte','足夠了'), C('它','es'), '。'
))
lines.append('')

lines.append(L(
    C('她','Sie'), D('folgte','跟著'), C('那個','dem'),
    D('langen','長長的'), D('Korridor','走廊'),
    C('和','und'), D('ging','走了'), C('在','um'),
    C('一個','eine'), D('Ecke','轉角'), '，',
    C('那裡','wo'), C('她','sie'), C('某人','jemand'),
    D('erwartete','在等著'), '...'
))
lines.append('')

lines.append(L(
    D('„Es wäre ein ziemliches Problem für mich, wenn du jetzt einfach fliehst."','「如果你現在逃走的話，對我來說會很麻煩。」')
))
lines.append('')

lines.append(L(
    D('„W-Was machst du hier..?!"','「你……你在這裡做什麼……？！」'),
    D('Alexia','Alexia'), D('traute','不敢相信'),
    C('她的','ihren'), D('Augen','眼睛'), D('kaum','幾乎不'), '。'
))

lines.append(BRK())

# Due to extreme length, remaining content continues
# I'll write the rest of the build script using a continuation approach

# The remaining ~800 lines of text will be handled by a second part
# For now, let's output what we have and continue with more

# ═══════════════════════════════════════════
# 以下為建構邏輯，不需要修改
# ═══════════════════════════════════════════

NAV_LINKS = [
    ('index.html', '第一集 字幕', False),
    ('page2.html', 'Prolog 小說', False),
    ('page3.html', 'Kapitel 1 小說', False),
    ('page4.html', 'Kapitel 2 小說', False),
    ('page5.html', 'Kapitel 3 小說', True),
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
<title>陰の実力者になりたくて！— Kapitel 3 晶晶體</title>
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
  <p>The Eminence in Shadow — Kapitel 3 晶晶體</p>
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

print(f'✅ 已產生 {OUTPUT_FILE}（第一部分）')

d_count = len(re.findall(r'<span class="d">', html))
c_count = len(re.findall(r'<span class="c">', html))
print(f'   德文詞 (.d): {d_count}')
print(f'   中文詞 (.c): {c_count}')
if d_count + c_count > 0:
    print(f'   德文佔比: {d_count/(d_count+c_count)*100:.1f}%')
print(f'')
print(f'📌 下一步：執行以下命令來自動轉換白色德文虛詞為藍色中文：')
print(f'   python3 auto_convert.py {OUTPUT_FILE}')
