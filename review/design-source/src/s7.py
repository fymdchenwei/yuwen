# -*- coding: utf-8 -*-
from lib import *
from s5 import BASE,CAT,STEPS,CATROWS,hdr_home
from s3 import medal
LAND=BASE+'''.pg{position:absolute;left:66px;right:0;top:0;bottom:0;padding:14px 18px 0}
.pgn{position:absolute;left:66px;right:0;top:0;bottom:0}
.col{position:absolute;top:14px;bottom:10px}
.btn{height:44px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:800;color:#fff}
'''
def lpage(title,body,css,rail_on=0):
    return page(title,body+rail(rail_on)+tag_demo().replace('bottom:3px','bottom:1px'),LAND+css,land=True)

def l_home():
    css='''.today{padding:12px 16px 12px;background:linear-gradient(135deg,#FF9A4D,#FF7A3D);color:#fff;border-radius:24px;box-shadow:0 5px 0 #E2622A}
.today .t{display:flex;justify-content:space-between;font-weight:800;font-size:16px}.today .t span{font-size:13px;font-weight:600}
.pbar{height:10px;border-radius:9px;background:rgba(255,255,255,.35);margin:8px 0 2px;overflow:hidden}.pbar i{display:block;height:100%;width:20%;background:#fff;border-radius:9px}
.stp{display:flex;margin-top:9px}.stp>div{flex:1;text-align:center;font-size:12px;font-weight:700;position:relative;line-height:1.3}
.stp b{display:flex;width:26px;height:26px;margin:0 auto 3px;border-radius:50%;background:rgba(255,255,255,.3);align-items:center;justify-content:center;font-size:13px}
.stp>div:not(:last-child):after{content:'';position:absolute;top:12px;left:calc(50% + 19px);right:calc(-50% + 19px);height:2px;background:rgba(255,255,255,.5)}
.stp .done b{background:#fff}.stp .cur b{background:#fff;color:#E2622A;box-shadow:0 0 0 4px rgba(255,255,255,.45)}.stp small{display:block;font-size:10.5px;font-weight:600;opacity:.92}
.go{margin-top:10px;background:#fff;color:#E2622A;border-radius:16px;text-align:center;padding:9px;font-weight:800;font-size:15px}
.cat{padding:7px 10px;display:flex;align-items:center;gap:9px;height:56px;margin-bottom:8px}.cat .n{font-size:14.5px;font-weight:800;white-space:nowrap}.cat .d{font-size:11px;color:var(--sub);margin-top:1px;white-space:nowrap}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:0 8px}
.soon{border:2.5px dashed #D9CDB8;border-radius:20px;padding:7px 10px;display:flex;align-items:center;gap:9px;color:#9A8B78;background:rgba(255,255,255,.55);height:56px}.soon b{font-size:14px;display:block}.soon .d{font-size:11px}'''
    b=statusbar().replace('class="sb"','class="sb" style="padding-left:92px"')
    b='<div class="sb" style="position:absolute;left:66px;right:0;top:0;height:30px;padding:8px 26px 0;font-size:13px"><span>9:41</span><span class="r"></span></div>'
    b+='<div class="col" style="left:84px;width:300px;top:32px">'+hdr_home(True).replace('padding:0','padding:0')
    b+='<div class="today" style="margin-top:10px"><div class="t">今日 15 分钟计划<span>已完成 3 / 15 分钟</span></div><div class="pbar"><i></i></div><div class="stp">'
    for c,n,l,m in STEPS:
        b+=f'<div class="{c}"><b>{ck(15,"#FF8A3D") if c=="done" else n}</b>{l}<small>{m}</small></div>'
    b+='</div><div class="go">继续 · 古诗词《示儿》第 2 关</div></div></div>'
    b+='<div class="col" style="left:400px;right:16px;top:32px"><div style="font-size:16px;font-weight:800;margin-bottom:8px;display:flex;justify-content:space-between;align-items:baseline">五类练习<span style="font-size:11.5px;color:var(--sub);font-weight:500">想多练哪个,就点哪个</span></div><div class="g2">'
    short={'poem':'填空闯关','dict':'听读音·纸上写','read':'划依据句才得分','idiom':'接龙+释义','lit':'5 题快问快答'}
    for k,d,chip,cc in CATROWS:
        g,col,n=CAT[k]
        b+=f'<div class="card cat"><div class="ic" style="background:{col};width:34px;height:34px;line-height:34px;font-size:19px;border-radius:12px">{g}</div><div style="min-width:0"><div class="n">{n[:6]}</div><div class="d">{short[k]}</div></div></div>'
    b+='<div class="soon"><div class="ic" style="background:#D9CDB8;width:34px;height:34px;line-height:34px;font-size:19px;border-radius:12px">作</div><div style="min-width:0"><b>习作素材</b><span class="d">即将上线</span></div></div></div></div>'
    return lpage('L1 横版首页',b,css,0)

def l_fill():
    css='''.top{position:absolute;left:84px;right:16px;top:12px;display:flex;align-items:center;gap:10px}
.top .x{width:32px;height:32px;border-radius:12px;background:#fff;color:var(--sub);display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:700}
.top .pb{flex:1;height:12px;background:var(--gray2);border-radius:9px;overflow:hidden}.top .pb i{display:block;height:100%;width:62%;background:var(--green);border-radius:9px}.top .hp{color:var(--pink);font-weight:800;font-size:16px}
.poem{position:absolute;left:84px;width:400px;top:56px;bottom:14px;padding:10px 12px;text-align:center}
.ln{display:flex;justify-content:center;gap:4px}.ln .c{width:50px;text-align:center}.ln .c small{display:block;font-size:11.5px;color:var(--sub);height:14px;line-height:14px}.ln .c span{display:block;font:400 34px/40px WenKai;height:40px}
.pv .c{width:32px}.pv .c span{font-size:22px;line-height:28px;height:28px;color:#8C7B6B}.pv{margin:2px 0}.nx .c{width:32px}.nx .c span{font-size:22px;line-height:28px;height:28px;color:#D0C7B8}
.cur{background:#FFF8E6;border-radius:16px;padding:4px;margin:4px -2px}
.slot{width:50px;height:52px;border:3px dashed var(--orange);border-radius:13px;background:var(--yellow2);margin-top:-3px;display:flex;align-items:center;justify-content:center;font:400 32px WenKai;box-shadow:0 0 0 4px rgba(255,138,61,.25)}
.slot.ok{border:3px solid var(--green);background:var(--green2);color:#1F9A5E;box-shadow:none}
.rt{position:absolute;left:504px;right:16px;top:56px;bottom:14px}
.opts{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}.op{height:56px;border-radius:18px;background:#fff;box-shadow:0 5px 0 #E6DDCC;display:flex;align-items:center;justify-content:center;font:400 32px WenKai}.op.used{background:#EFEAE2;color:#CFC6B8;box-shadow:none;transform:translateY(4px)}'''
    b='<div class="top"><div class="x">×</div><div class="pb"><i></i></div><div class="hp">♥♥♥</div></div>'
    b+='<div class="card poem"><div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:4px"><span class="chip c-mem">纯记忆</span><span style="font:400 18px WenKai">静夜思 <span style="font:500 11.5px \'Noto Sans CJK SC\';color:var(--sub)">李白〔唐〕</span></span></div>'
    def sl(t,c): return f'<div class="ln {c}">'+''.join(f'<div class="c"><span>{x}</span></div>' for x in t)+'</div>'
    b+=sl('床前明月光','pv')+sl('疑是地上霜','pv')
    py=['jǔ','tóu','wàng','míng','yuè']
    cs=''
    for i,ch in enumerate('举头望明月'):
        if i==3: cs+=f'<div class="c"><small>{py[i]}</small><div class="slot ok">明</div></div>'
        elif i==4: cs+=f'<div class="c"><small>{py[i]}</small><div class="slot"></div></div>'
        else: cs+=f'<div class="c"><small>{py[i]}</small><span>{ch}</span></div>'
    b+=f'<div class="ln cur">{cs}</div>'+sl('低头思故乡','nx')
    b+='<div style="font-size:11.5px;color:var(--sub);margin-top:2px">第 3 关 / 共 4 关 · 补全被遮住的字</div></div>'
    b+='<div class="rt"><div class="say" style="display:flex;gap:9px;align-items:center;margin-bottom:12px">'+mascot(44)+'<div style="background:#fff;border-radius:16px;padding:7px 11px;font-size:13px;font-weight:700;line-height:1.4">抬头看到的是什么?<br>点下面的字,填进空格。</div></div><div class="opts">'
    for o in ['星','明','日','月','光','霜']: b+=f'<div class="op{" used" if o=="明" else ""}">{o}</div>'
    b+='</div><div class="btn" style="margin-top:14px;background:#D8D1C6;box-shadow:0 5px 0 #BDB5A8;height:50px">检 查</div></div>'
    return lpage('L2 横版填空作答',b,css,1)

def l_path():
    css='''.hd{position:absolute;left:84px;right:16px;top:12px;display:flex;align-items:center;gap:12px}.hd .back{flex:none}.hd .bc{font-size:11.5px;color:var(--sub)}.hd h1{font:400 24px WenKai;line-height:1.1}
.hd .pr{margin-left:auto}
.map{position:absolute;left:84px;width:470px;top:70px;bottom:10px}
.lv{position:absolute;display:flex;align-items:center;gap:10px}
.nd{width:56px;height:56px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:22px;color:#fff;position:relative}
.tx{background:#fff;border-radius:16px;padding:6px 10px;box-shadow:0 3px 0 rgba(140,110,70,.12);width:118px}.tx .k{font:400 15px WenKai;white-space:nowrap}.tx .s{font-size:10.5px;color:var(--sub);margin-top:1px;white-space:nowrap}
.done .nd{background:var(--green);box-shadow:0 5px 0 #2A9A63}.cur .nd{background:var(--orange);box-shadow:0 5px 0 #E2622A;width:66px;height:66px;font-size:28px}
.cur .nd:before{content:'';position:absolute;inset:-8px;border-radius:50%;border:4px solid rgba(255,138,61,.35)}
.cur .tx{border:3px solid var(--orange);padding:4px 8px}.lock .nd{background:#D8D1C6;box-shadow:0 5px 0 #BDB5A8}.lock .tx{background:rgba(255,255,255,.7)}.lock .k{color:#B9B0A3}
.go{position:absolute;right:-6px;top:-24px;background:var(--pink);color:#fff;font-size:11px;font-weight:800;padding:2px 8px;border-radius:99px;white-space:nowrap}
.side{position:absolute;left:580px;right:16px;top:70px;padding:12px 14px}'''
    b='<div class="hd"><div class="back">‹</div><div><div class="bc">古诗词 › 逐句填空 › 五年级</div><h1>示儿</h1></div><div class="pr">'+ring(25,50,"#FF8A3D",label="1/4",sw=7)+'</div></div>'
    b+='<div class="map">'
    pos=[(4,10),(150,120),(8,200),(150,270)]
    # zigzag two-column: use grid-ish positions
    pos=[(0,4),(190,4),(0,150),(190,150)]
    pts=[(x+28,y+33) for x,y in pos]
    b+=f'<svg style="position:absolute;left:0;top:0" width="470" height="260" viewBox="0 0 470 260"><path d="M28 37 L 218 37 C 290 37, 290 100, 218 100 L 100 100 C 20 100, 20 183, 28 183 L 218 183" fill="none" stroke="#FFD9A8" stroke-width="8" stroke-linecap="round" stroke-dasharray="1 15"/></svg>'
    def lv(i,cls,k,s,ex):
        x,y=pos[i]; return f'<div class="lv {cls}" style="left:{x}px;top:{y}px"><div class="nd">{ex}</div><div class="tx"><div class="k">{k}</div><div class="s">{s}</div></div></div>'
    b+=lv(0,'done','死去元知万事空','第 1 关 · 已通关',ck(30))
    b+=lv(1,'cur','但悲不见___','第 2 关 · 闯关中','2<span class="go">当前关</span>')
    b+=lv(2,'lock','王师北定中原日','第 3 关 · 未解锁',lk(26))
    b+=lv(3,'lock','家祭无忘告乃翁','第 4 关 · 未解锁',lk(26))
    b+='</div>'
    b+=f'<div class="card side"><div style="font-size:14px;font-weight:800">通关进度</div><div style="height:12px;background:var(--gray2);border-radius:9px;margin:8px 0;overflow:hidden"><i style="display:block;width:25%;height:100%;background:var(--green);border-radius:9px"></i></div><div style="font-size:12px;color:var(--sub)">通关后获得徽章</div><div style="display:flex;justify-content:center;margin:6px 0">{medal("#FF9DB0","#FF5F86","示",62)}</div><div class="btn" style="background:var(--orange);box-shadow:0 5px 0 #E2622A">开始第 2 关</div></div>'
    return lpage('L3 横版闯关路径',b,css,1)

def l_read():
    css='''.top{position:absolute;left:84px;right:16px;top:10px;display:flex;align-items:center;gap:10px}
.top .x{width:30px;height:30px;border-radius:11px;background:#fff;color:var(--sub);display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:700}.top .pb{flex:1;height:12px;background:var(--gray2);border-radius:9px;overflow:hidden}.top .pb i{display:block;height:100%;width:25%;background:var(--green);border-radius:9px}.top .rt{font-size:12.5px;font-weight:800;color:var(--sub)}
.pass{position:absolute;left:84px;width:460px;top:50px;bottom:12px;padding:10px 14px}
.pass h2{font:400 19px WenKai;text-align:center}.pass .sub{text-align:center;font-size:11px;color:var(--sub);margin:1px 0 4px}
.pass p{font:400 16.5px/29px WenKai;text-align:justify}
.sn{border-radius:6px;padding:2px 1px}.no{display:inline-block;width:15px;height:15px;border-radius:50%;background:var(--gray2);color:var(--sub);font:700 10px/15px 'Noto Sans CJK SC';text-align:center;vertical-align:3px;margin-right:2px;font-style:normal}
.sn.sel{background:#FFE477;box-shadow:0 2px 0 #F0B62A}.sn.sel .no{background:var(--orange);color:#fff}
.q{position:absolute;left:560px;right:16px;top:50px;padding:10px 12px}.q .h{font-size:14px;font-weight:800;line-height:1.45}
.q .o div{margin-top:7px;height:34px;border-radius:12px;background:var(--gray2);display:flex;align-items:center;padding-left:12px;font-size:13.5px;font-weight:800;color:var(--sub)}.q .o .on{background:var(--blue2);color:#1E78D8;box-shadow:inset 0 0 0 2.5px var(--blue)}
.rule{position:absolute;left:560px;right:16px;top:212px;padding:7px 10px;border-radius:14px;background:var(--yellow2);color:#8A6200;font-size:12px;font-weight:700;line-height:1.4}
.two{position:absolute;left:560px;right:16px;bottom:12px;display:flex;gap:8px}.two .btn{height:46px;font-size:16px}'''
    from s5 import SENT
    b='<div class="top"><div class="x">×</div><div class="pb"><i></i></div><span class="chip" style="background:#FFF1C4;color:#B98100">示例文本 · 原创</span><div class="rt">第 1 / 2 题</div></div>'
    p=''.join(f'<span class="sn{" sel" if i in (1,4) else ""}"><i class="no">{i}</i>{s}</span>' for i,s in enumerate(SENT,1))
    b+=f'<div class="card pass"><h2>清晨的牵牛花</h2><div class="sub">点一句就划上,再点取消</div><p>{p}</p></div>'
    b+='<div class="card q"><div class="h">问题:牵牛花一般在什么时候开放?</div><div class="o"><div class="on">A 清晨</div><div>B 中午</div><div>C 傍晚</div></div></div>'
    b+='<div class="rule">先划出依据句,再提交才能得分。已划 2 句(第 1、4 句)</div>'
    b+='<div class="two"><div class="btn wh" style="width:70px;box-shadow:inset 0 0 0 2.5px var(--orange2)">清除</div><div class="btn gn" style="flex:1">提交答案</div></div>'
    return lpage('L4 横版阅读理解划句',b,css,1)

def l_prog():
    css='''.c1{position:absolute;left:84px;width:236px;top:12px;bottom:12px}.c2{position:absolute;left:334px;width:228px;top:12px;bottom:12px}.c3{position:absolute;left:576px;right:16px;top:12px;bottom:12px}
.sec{padding:9px 12px;margin-bottom:8px}.sec h3{font-size:14px;font-weight:800;display:flex;justify-content:space-between;align-items:baseline}.sec h3 small{font-size:10.5px;color:var(--sub);font-weight:600}
.top3{display:flex;gap:6px;margin-top:6px}.top3>div{flex:1;text-align:center;background:#FFF6E0;border-radius:14px;padding:5px 0;font-size:10.5px;color:var(--sub);font-weight:700}.top3 b{display:block;font-size:18px;color:var(--ink)}
.wk{display:flex;justify-content:space-between;margin-top:8px}.wk div{text-align:center;font-size:10px;color:var(--sub);font-weight:700}.wk i{display:flex;width:26px;height:26px;border-radius:50%;margin:0 auto 2px;align-items:center;justify-content:center;background:var(--gray2);font-style:normal}
.wk .d i{background:var(--green)}.wk .t i{background:#fff;box-shadow:0 0 0 3px var(--orange);color:var(--orange);font-weight:800;font-size:11px}
.cr{display:flex;align-items:center;gap:6px;margin-top:8px;font-size:12px;font-weight:800}.cr .g{width:24px;height:24px;border-radius:8px;color:#fff;font:400 14px/24px WenKai;text-align:center;flex:none}
.cr .nm{width:78px;flex:none;white-space:nowrap}.cr .b{flex:1;height:12px;border-radius:9px;background:var(--gray2);overflow:hidden}.cr .b i{display:block;height:100%;border-radius:9px}
.bgs{display:grid;grid-template-columns:1fr 1fr;gap:4px 0;margin-top:4px}.bgs>div{text-align:center;font-size:11px;font-weight:700;display:flex;flex-direction:column;align-items:center}'''
    b='<div class="c1"><div class="card sec"><h3>连续打卡<small>每天 15 分钟</small></h3><div class="top3"><div><b style="color:var(--orange)">5 天</b>当前</div><div><b>12 天</b>最长</div></div><div class="wk">'+''.join(f'<div class="{c}"><i>{ck(13) if c=="d" else ("今" if c=="t" else "")}</i>{n}</div>' for n,c in [('日','d'),('一','d'),('二','d'),('三','d'),('四','t'),('五',''),('六','')])+'</div></div>'
    b+='<div class="card sec" style="background:linear-gradient(135deg,#FF8FA8,#FF6B8B);color:#fff;display:flex;align-items:center;gap:10px"><div style="width:36px;height:36px;border-radius:12px;background:#fff;color:var(--pink);font:400 21px/36px WenKai;text-align:center">错</div><div style="flex:1"><b style="font-size:14.5px;display:block">错题本</b><span style="font-size:11px">12 待复习 · 已毕业 7</span></div></div></div>'
    b+='<div class="c2"><div class="card sec" style="height:100%"><h3>五类练习进度<small>示例数据</small></h3>'
    for k,pct in [('poem',31),('dict',55),('read',20),('idiom',42),('lit',36)]:
        g,col,n=CAT[k]
        b+=f'<div class="cr"><div class="g" style="background:{col}">{g}</div><div class="nm">{n[:6]}</div><div class="b"><i style="width:{pct}%;background:{col}"></i></div></div><div style="font-size:10.5px;color:var(--sub);margin:1px 0 0 30px">{ {"poem":"9/29 首","dict":"44/80 词","read":"2/10 篇","idiom":"21/50 个","lit":"18/50 题"}[k]}</div>'
    b+='</div></div>'
    b+='<div class="c3"><div class="card sec" style="height:100%"><h3>成就徽章<small>8 / 20 枚 · 示例</small></h3><div class="bgs">'
    for c1,c2,ch,n,lock in [('#FFD84D','#FF9F1C','连','连续 5 天',0),('#7FE0B0','#2FB57A','写','听写 10 词',0),('#8FCBFF','#3D8FEA','据','找到依据',0),('','','','连续 7 天',1)]:
        b+=f'<div>{medal(c1,c2,ch,58,bool(lock))}<span style="{"color:#B9B0A3" if lock else ""}">{n}</span></div>'
    b+='</div><div style="margin-top:6px;font-size:11px;color:var(--sub);text-align:center">再连续 2 天解锁「连续 7 天」</div></div></div>'
    return lpage('L5 横版进度与徽章',b,css,3)
