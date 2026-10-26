# -*- coding: utf-8 -*-
"""渲染 naval-thinking 的技能市场预览图（3 张）。"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))
BG = (11, 11, 12)
FG = (243, 240, 232)
MUT = (139, 139, 133)
ACC = (150, 186, 200)   # 冷蓝灰，区别于 Dan Koe 的暖琥珀
LINE = (42, 42, 42)

EN_B = r"C:\Windows\Fonts\georgiab.ttf"
EN = r"C:\Windows\Fonts\georgia.ttf"
CN_B = r"C:\Windows\Fonts\msyhbd.ttc"
CN = r"C:\Windows\Fonts\msyh.ttc"


def F(p, s):
    return ImageFont.truetype(p, s)


def canvas(w, h):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    for x in range(0, w, 80):
        d.line([(x, 0), (x, h)], fill=(20, 20, 21))
    for y in range(0, h, 80):
        d.line([(0, y), (w, y)], fill=(20, 20, 21))
    return img, d


def cover():
    w, h = 1600, 900
    img, d = canvas(w, h)
    m = 96
    d.text((m, 78), "SKILL PREVIEW  /  THINKING SYSTEM", font=F(EN, 22), fill=MUT)
    d.line([(m, 130), (m + 120, 130)], fill=ACC, width=3)
    d.text((m, 186), "Naval", font=F(EN_B, 180), fill=FG)
    d.text((m + 6, 392), "思想操作系统", font=F(CN_B, 92), fill=FG)
    d.text((m + 10, 520), "五个底层判断 · 四个模型 · 十条启发式 · 三种模式", font=F(CN, 34), fill=MUT)
    d.line([(m, 640), (w - m, 640)], fill=LINE, width=1)
    stats = [("19", "章宝典全书"), ("237", "篇 nav.al"), ("362", "条推文")]
    x = m
    for num, label in stats:
        d.text((x, 690), num, font=F(EN_B, 64), fill=FG)
        d.text((x, 772), label, font=F(CN, 26), fill=MUT)
        x += 400
    d.text((m + 1200, 700), "58 条语录", font=F(CN_B, 30), fill=ACC)
    d.text((m + 1200, 742), "带章节或推文直链", font=F(CN, 22), fill=MUT)

    rx = 1130
    d.text((rx, 196), "四个模型", font=F(CN, 26), fill=ACC)
    for i, name in enumerate(["财富四要素", "四种运气", "决策启发式", "幸福四支柱"], 1):
        yy = 250 + (i - 1) * 76
        d.text((rx, yy), "0%d" % i, font=F(EN, 26), fill=MUT)
        d.text((rx + 60, yy - 4), name, font=F(CN, 34), fill=FG)
    d.text((rx, 806), "naval-thinking  ·  v1.0.0", font=F(EN, 22), fill=MUT)
    img.save(os.path.join(OUT, "01-cover-16x9.png"), optimize=True)


def poster():
    w, h = 1080, 1440
    img, d = canvas(w, h)
    m = 80
    d.text((m, 70), "NAVAL  /  SKILL", font=F(EN, 20), fill=MUT)
    d.text((m, 120), "把一本宝典", font=F(CN_B, 64), fill=FG)
    d.text((m, 200), "变成一套判断", font=F(CN_B, 64), fill=FG)
    d.text((m, 300), "他只说一句，然后转身离开。这里还原那一句之前的推理。", font=F(CN, 25), fill=MUT)
    d.line([(m, 360), (w - m, 360)], fill=LINE, width=1)
    items = [
        ("01", "财富四要素", "专属知识 × 杠杆 × 责任 → 把自己产品化"),
        ("02", "四种运气", "盲运 / 勤奋 / 敏锐 / 人格，后两种可以造"),
        ("03", "决策启发式", "决定不了就是否；势均力敌，走上坡路"),
        ("04", "幸福四支柱", "选择、当下、平静、欲望即契约"),
    ]
    y = 410
    for num, name, desc in items:
        d.text((m, y), num, font=F(EN_B, 34), fill=ACC)
        d.text((m + 70, y - 6), name, font=F(CN_B, 40), fill=FG)
        d.text((m + 70, y + 56), desc, font=F(CN, 23), fill=MUT)
        y += 168
    d.line([(m, 1105), (w - m, 1105)], fill=LINE, width=1)
    d.text((m, 1140), "19 章宝典 ｜ 237 篇 nav.al ｜ 362 条推文", font=F(CN, 24), fill=MUT)
    d.text((m, 1190), "17 份访谈 ｜ 57 条视频 ｜ 58 条语录带直链", font=F(CN, 24), fill=MUT)
    d.text((m, 1300), "naval-thinking  ·  v1.0.0", font=F(EN, 20), fill=MUT)
    img.save(os.path.join(OUT, "02-poster-3x4.png"), optimize=True)


def grid():
    w, h = 1600, 900
    img, d = canvas(w, h)
    m = 80
    d.text((m, 56), "FOUR MODELS", font=F(EN, 20), fill=MUT)
    d.text((m, 92), "四个可操作模型", font=F(CN_B, 52), fill=FG)
    cards = [
        ("01  财富四要素", ["专属知识：无法被培训", "杠杆：代码与媒体无需许可", "责任：以自己名字承担风险", "产品化：Productize Yourself"]),
        ("02  四种运气", ["盲运：不可控", "勤奋运：不停搅动", "敏锐运：深到能看见", "人格运：性格成为命运"]),
        ("03  决策启发式", ["决定不了，答案就是否", "势均力敌，走上坡路", "可逆快定，不可逆慢定", "只玩长期游戏"]),
        ("04  幸福四支柱", ["幸福是选择，也是技能", "需要当下：不反刍不预演", "需要平静：peace 不是 joy", "欲望是自选的不快乐"]),
    ]
    cw, ch, gap = 700, 300, 34
    for i, (title, bullets) in enumerate(cards):
        cx = m + (i % 2) * (cw + gap)
        cy = 190 + (i // 2) * (ch + gap)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=(17, 17, 18), outline=(38, 38, 38))
        d.text((cx + 34, cy + 28), title, font=F(CN_B, 34), fill=FG)
        d.line([(cx + 34, cy + 84), (cx + cw - 34, cy + 84)], fill=(38, 38, 38))
        for j, b in enumerate(bullets):
            yy = cy + 108 + j * 46
            d.text((cx + 34, yy), "·", font=F(CN_B, 24), fill=ACC)
            d.text((cx + 58, yy), b, font=F(CN, 24), fill=MUT)
    d.text((m, h - 52), "naval-thinking  ·  references/01–05", font=F(EN, 20), fill=MUT)
    img.save(os.path.join(OUT, "03-models-16x9.png"), optimize=True)


if __name__ == "__main__":
    cover(); poster(); grid()
    for f in sorted(os.listdir(OUT)):
        if f.endswith(".png"):
            print(f, "%.1f KB" % (os.path.getsize(os.path.join(OUT, f)) / 1024))
