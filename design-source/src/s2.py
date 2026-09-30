# -*- coding: utf-8 -*-
from lib import *

def s04():  # level path 示儿
    css='''.hd{padding:0 16px;display:flex;align-items:center;gap:12px}.hd .bc{font-size:12px;color:var(--sub)}.hd h1{font-size:26px;font-weight:800;font-family:WenKai;font-weight:400;line-height:1.15}
.hd .who{font-size:12.5px;color:var(--sub)}.pr{margin-left:auto;text-align:center}
.info{margin:10px 16px 0;padding:10px 14px;display:flex;align-items:center;gap:12px}.info .bar{flex:1;height:12px;background:var(--gray2);border-radius:9px;overflow:hidden}.info .bar i{display:block;width:25%;height:100%;background:var(--green);border-radius:9px}
.info b{font-size:13px}.info .bd{width:36px;height:36px;border-radius:50%;background:var(--gray2);display:flex;align-items:center;justify-content:center;font:400 18px WenKai;color:var(--gray)}
.map{position:absolute;left:0;right:0;top:172px;bottom:78px}
.map svg.path{position:absolute;left:0;top:0}
.lv{position:absolute;width:300px;display:flex;align-items:center;gap:12px}
.lv .nd{width:66px;height:66px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px;color:#fff;position:relative}
.lv .tx{background:#fff;border-radius:18px;padding:8px 12px;box-shadow:0 3px 0 rgba(140,110,70,.12);min-width:0;flex:1}
.lv .tx .k{font:400 19px WenKai;letter-spacing:1px;white-space:nowrap}.lv .tx .s{font-size:11.5px;color:var(--sub);margin-top:2px;display:flex;justify-content:space-between;align-items:center}
.lv.done .nd{background:var(--green);box-shadow:0 5px 0 #2A9A63}
.lv.cur .nd{background:var(--orange);box-shadow:0 5px 0 #E2622A;width:78px;height:78px;font-size:32px}
.lv.cur .nd:before{content:'';position:absolute;inset:-9px;border-radius:50%;border:4px solid rgba(255,138,61,.35)}
.lv.cur .tx{border:3px solid var(--orange);padding:6px 10px}
.lv.lock .nd{background:#D8D1C6;box-shadow:0 5px 0 #BDB5A8}.lv.lock .tx{background:rgba(255,255,255,.7);color:var(--gray)}
.lv.lock .tx .k{color:#B9B0A3}
.go{position:absolute;right:-2px;top:-28px;background:var(--pink);color:#fff;font-size:12px;font-weight:800;padding:2px 9px;border-radius:99px;white-space:nowrap}
.fin{position:absolute;width:300px;display:flex;align-items:center;gap:12px}
.fin .bg{width:66px;height:66px;border-radius:50%;background:#EFEAE2;border:4px dashed #D0C7B8;display:flex;align-items:center;justify-content:center}
'''
    b=statusbar()+f'<div class="hd"><div class="back">‹</div><div><div class="bc">练习项 › 逐句填空 › 五年级</div><h1>示儿</h1><div class="who">五年级上册 · 陆游〔宋〕</div></div><div class="pr">{ring(25,58,"#FF8A3D",label="1/4",sw=8)}</div></div>'
    b+='<div class="card info"><b>通关进度</b><div class="bar"><i></i></div><div class="bd">徽</div></div>'
    b+='<div class="map">'
    tops=[10,140,270,400]; lefts=[30,70,30,70]
    pts=[(l+33,t+33) for l,t in zip(lefts,tops)]
    d=f"M{pts[0][0]} {pts[0][1]}"
    for (x1,y1),(x2,y2) in zip(pts,pts[1:]):
        d+=f" C {x1+ (60 if x1<x2 else -60)} {y1+50}, {x2+(-60 if x1<x2 else 60)} {y2-50}, {x2} {y2}"
    b+=f'<svg class="path" width="390" height="594" viewBox="0 0 390 594"><path d="{d}" fill="none" stroke="#FFD9A8" stroke-width="10" stroke-linecap="round" stroke-dasharray="1 18"/></svg>'
    def lv(i,cls,k,s,extra):
        return f'<div class="lv {cls}" style="top:{tops[i]}px;left:{lefts[i]}px"><div class="nd">{extra}</div><div class="tx"><div class="k">{k}</div><div class="s">{s}</div></div></div>'
    b+=lv(0,'done','死去元知万事空','第 1 关 · 已通关 '+stars(3,3,14),ck(34))
    b+=lv(1,'cur','但悲不见<span class="mask" style="width:66px;height:24px;vertical-align:-5px"></span>','第 2 关 · 闯关中','2<span class="go">当前关</span>')
    b+=lv(2,'lock','王师北定中原日','第 3 关 · 未解锁',lk(30))
    b+=lv(3,'lock','家祭无忘告乃翁','第 4 关 · 未解锁',lk(30))
    b+='</div>'
    b+='<div style="position:absolute;left:16px;right:16px;bottom:92px;z-index:7;background:var(--orange);color:#fff;border-radius:20px;text-align:center;padding:13px;font-size:19px;font-weight:800;box-shadow:0 5px 0 #E2622A">开始第 2 关</div>'
    b+=tabbar(1)+tag_demo()
    return page('04 闯关关卡路径',b,css)

PY={'举':'jǔ','头':'tóu','望':'wàng','明':'míng','月':'yuè'}
def fill_screen(state):
    css='''.top{display:flex;align-items:center;gap:10px;padding:0 16px}.top .x{width:34px;height:34px;border-radius:12px;background:#fff;color:var(--sub);display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700}
.top .pb{flex:1;height:14px;background:var(--gray2);border-radius:9px;overflow:hidden}.top .pb i{display:block;height:100%;width:62%;background:var(--green);border-radius:9px}
.top .hp{font-size:17px;color:var(--pink);font-weight:800;letter-spacing:1px}
.sub{padding:8px 20px 0;display:flex;justify-content:space-between;align-items:baseline}.sub b{font:400 22px WenKai}.sub span{font-size:12.5px;color:var(--sub)}
.poem{margin:8px 16px 0;padding:12px 14px 10px;text-align:center;position:relative}
.ln{padding:6px 0}.ln .cs{display:flex;justify-content:center;gap:6px}.ln .c{width:52px;text-align:center}.ln .c small{display:block;font-size:12px;color:var(--sub);height:15px;line-height:15px}.ln .c span{display:block;font:400 38px/46px WenKai;height:46px}
.ln.prev .c span{font-size:26px;line-height:32px;height:32px;color:#8C7B6B}.ln.prev .c small{display:none}
.ln.prev .cs{gap:2px}.ln.prev .c{width:36px}
.ln.next .c span{font-size:26px;line-height:32px;height:32px;color:#D0C7B8}.ln.next .c small{display:none}.ln.next .cs{gap:2px}.ln.next .c{width:36px}
.ln.cur{background:#FFF8E6;border-radius:18px;margin:2px -4px;padding:6px 4px}
.slot{width:52px;height:56px;border:3px dashed var(--orange);border-radius:14px;background:var(--yellow2);margin-top:-4px;display:flex;align-items:center;justify-content:center;font:400 36px WenKai;color:var(--ink)}
.slot.ok{border:3px solid var(--green);background:var(--green2);color:#1F9A5E}.slot.bad{border:3px solid var(--pink);background:var(--pink2);color:#D63A5F}
.slot.act{box-shadow:0 0 0 4px rgba(255,138,61,.25)}
.tag{position:absolute;left:14px;top:12px}
.opts{position:absolute;left:16px;right:16px;bottom:96px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.op{height:58px;border-radius:18px;background:#fff;box-shadow:0 5px 0 #E6DDCC;display:flex;align-items:center;justify-content:center;font:400 34px WenKai;position:relative}
.op.used{background:#EFEAE2;color:#CFC6B8;box-shadow:none;transform:translateY(4px)}
.btn{position:absolute;left:16px;right:16px;bottom:22px;height:56px;border-radius:20px;color:#fff;font-size:20px;font-weight:800;display:flex;align-items:center;justify-content:center}
.fb{position:absolute;left:0;right:0;bottom:0;border-radius:30px 30px 0 0;padding:16px 20px 24px;z-index:8}
.fb .t{display:flex;align-items:center;gap:10px;font-size:22px;font-weight:800}.fb .ic{width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.fb p{font-size:14px;margin-top:6px;line-height:1.5}
.fb .row{display:flex;gap:10px;margin-top:12px}.fb .row div{flex:1;height:52px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:800}
.say{position:absolute;left:16px;right:16px;top:404px;display:flex;align-items:center;gap:10px}.say .bub{background:#fff;border-radius:18px;padding:8px 13px;font-size:14px;font-weight:700;position:relative;flex:1;line-height:1.4}
.say .bub:before{content:'';position:absolute;left:-7px;top:16px;border:8px solid transparent;border-left:0;border-right-color:#fff}
.dim{position:absolute;inset:0;background:rgba(59,47,47,.0)}
'''
    def line(txt,pys,cls,slots=None):
        cs=''
        for i,ch in enumerate(txt):
            if slots and i in slots:
                st,content=slots[i]
                cs+=f'<div class="c"><small>{pys[i]}</small><div class="slot {st}">{content}</div></div>'
            else:
                cs+=f'<div class="c"><small>{pys[i]}</small><span>{ch}</span></div>'
        return f'<div class="ln {cls}"><div class="cs">{cs}</div></div>'
    def line_s(txt,cls):
        return f'<div class="ln {cls}"><div class="cs">'+''.join(f'<div class="c"><span>{c}</span></div>' for c in txt)+'</div></div>'
    l3='举头望明月'; py=['jǔ','tóu','wàng','míng','yuè']
    if state=='working':
        sl={3:('ok','明'),4:('act','')}
    elif state=='ok':
        sl={3:('ok','明'),4:('ok','月')}
    else:
        sl={3:('bad','日'),4:('ok','月')}
    for k in sl:
        pass
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i></i></div><div class="hp">♥♥♥</div></div>'
    b+='<div class="sub"><b>静夜思</b><span>一年级下册 · 李白〔唐〕</span></div>'
    b+='<div class="card poem"><span class="chip c-mem tag">纯记忆</span><div style="height:16px"></div>'
    b+=line_s('床前明月光','prev')+line_s('疑是地上霜','prev')
    b+=line(l3,py,'cur',sl)
    b+=line_s('低头思故乡','next')
    b+='<div style="font-size:11.5px;color:var(--sub);margin-top:2px">第 3 关 / 共 4 关 · 补全被遮住的字</div></div>'
    if state=='working':
        b+=f'<div class="say">{mascot(56)}<div class="bub">想一想:抬头看到的是什么?<br>点下面的字,填进空格里。</div></div>'
        opts=['星','明','日','月','光','霜']
        b+='<div class="opts">'+''.join(f'<div class="op{" used" if o=="明" else ""}">{o}</div>' for o in opts)+'</div>'
        b+='<div class="btn" style="background:#D8D1C6;box-shadow:0 5px 0 #BDB5A8">检 查</div>'
    elif state=='ok':
        opts=['星','明','日','月','光','霜']
        used={'明','月'}
        b+='<div class="opts" style="bottom:250px">'+''.join(f'<div class="op{" used" if o in used else ""}">{o}</div>' for o in opts)+'</div>'
        b+=f'<div class="fb" style="background:#DDF6E8"><div class="t" style="color:#1F9A5E"><div class="ic" style="background:var(--green)">{ck(24)}</div>答对啦!真棒!<span style="margin-left:auto;line-height:0">{stars(3,3,22)}</span></div><p style="color:#256B47">举头望明月,低头思故乡。<br>你已经连对 3 关,下一关解锁了!</p><div class="row"><div style="background:var(--green);box-shadow:0 5px 0 #2A9A63;color:#fff">下一关 ›</div></div></div>'
        b=b.replace('<div class="say">','<div class="say">')
    else:
        opts=['星','明','日','月','光','霜']
        used={'日','月'}
        b+='<div class="opts" style="bottom:300px">'+''.join(f'<div class="op{" used" if o in used else ""}">{o}</div>' for o in opts)+'</div>'
        b+=f'<div class="fb" style="background:#FFE1E8"><div class="t" style="color:#D63A5F"><div class="ic" style="background:var(--pink)">{cr(22)}</div>差一点点,再想想<span style="margin-left:auto;font-size:15px">♥♥♡</span></div><p style="color:#8E2C46">正确答案:<b style="font:400 24px WenKai;color:#D63A5F">明月</b>　"举头望<b>明月</b>",抬头望着天上的明亮的月亮。</p><div style="margin-top:10px;background:#fff;border-radius:16px;padding:9px 12px;display:flex;align-items:center;gap:10px;font-size:14px;font-weight:700;color:#8E2C46"><span style="width:28px;height:28px;border-radius:9px;background:var(--orange);color:#fff;font:400 16px/28px WenKai;text-align:center">错</span><span style="flex:1">这一句已自动加入错题本<br><small style="font-weight:500;color:var(--sub)">明天、3 天后会再考你一次</small></span></div><div class="row"><div style="background:#fff;color:var(--pink);box-shadow:0 4px 0 #F5C2CD">看错题本</div><div style="background:var(--pink);box-shadow:0 5px 0 #D63A5F;color:#fff">再试一次</div></div></div>'
    b+=tag_demo() if state=='working' else ''
    return b,css

def s05():
    b,css=fill_screen('working'); return page('05 填空作答中',b,css)
def s06():
    b,css=fill_screen('ok'); return page('06 答对反馈',b,css)
def s07():
    b,css=fill_screen('bad'); return page('07 答错反馈加入错题本',b,css)
