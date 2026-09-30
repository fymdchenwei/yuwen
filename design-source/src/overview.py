# -*- coding: utf-8 -*-
# 生成 overview-portrait.png / overview-landscape.png(按类别分行,每行过长自动换行)
import asyncio,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from playwright.async_api import async_playwright
import build as B
O=B.OUT
def groups(L):
    g={}
    for c,n,_ in L: g.setdefault(c,[]).append(n)
    return g
def page(kind,L,iw,pw,title,sub):
    h=('<html><head><meta charset="utf-8"><style>body{margin:0;background:#FFF9EC;font-family:"Noto Sans CJK SC";color:#3B2F2F;padding:40px 48px;width:%dpx}h1{font-size:44px;margin:0}p.s{font-size:20px;color:#8C7B6B;margin:6px 0 24px}.g{margin-bottom:30px}.g h2{font-size:26px;margin:0 0 12px;color:#E2622A}.r{display:flex;gap:22px;flex-wrap:wrap}.i{text-align:center;font-size:14px;font-weight:700;width:%dpx}.i img{width:%dpx;display:block;border-radius:24px;box-shadow:0 8px 24px rgba(140,110,70,.25);margin-bottom:8px}</style></head><body><h1>%s</h1><p class="s">%s</p>')%(pw,iw,iw,title,sub)
    for c,ns in groups(L).items():
        h+=f'<div class="g"><h2>{c}({len(ns)} 屏)</h2><div class="r">'
        for n in ns: h+=f'<div class="i"><img src="file://{O}/png/{kind}/{n}.png">{n}</div>'
        h+='</div></div>'
    return h+'</body></html>'
async def main():
    jobs=[('portrait',B.P,300,2000,'每日 15 分钟 · 竖版界面总览(390×844)','五类练习按行排列 · 所有数字均为“示例数据” · 示例文本为原创 · 三年级上册古诗三首“未核实”'),
          ('landscape',B.L,560,1800,'每日 15 分钟 · 横版界面总览(844×390)','与竖版同一套设计语言 · 侧边栏导航 · 所有数字均为“示例数据”')]
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for kind,L,iw,pw,t,s in jobs:
            f=f'{O}/html/overview-{kind}.html'; open(f,'w',encoding='utf-8').write(page(kind,L,iw,pw,t,s))
            pg=await b.new_page(viewport={'width':pw+96,'height':800},device_scale_factor=1.5)
            await pg.goto('file://'+f); await pg.wait_for_timeout(800)
            await pg.screenshot(path=f'{O}/overview-{kind}.png',full_page=True); await pg.close()
        await b.close()
asyncio.run(main())
