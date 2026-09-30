# -*- coding: utf-8 -*-
from lib import *

def medal(color1,color2,ch,size=110,locked=False,ribbon=True):
    if locked:
        return f'<div style="width:{size}px;height:{size}px;position:relative"><div style="position:absolute;inset:8% 8% 8% 8%;border-radius:50%;background:#E8E2D8;border:4px dashed #CFC6B8;display:flex;align-items:center;justify-content:center">{lk(size*0.34,"#BDB5A8")}</div></div>'
    return f'''<div style="width:{size}px;height:{size}px;position:relative">
<i style="position:absolute;left:24%;top:62%;width:20%;height:38%;background:#FF6B8B;transform:rotate(14deg);border-radius:0 0 4px 4px;clip-path:polygon(0 0,100% 0,100% 100%,50% 82%,0 100%)"></i>
<i style="position:absolute;left:56%;top:62%;width:20%;height:38%;background:#FF8FA8;transform:rotate(-14deg);border-radius:0 0 4px 4px;clip-path:polygon(0 0,100% 0,100% 100%,50% 82%,0 100%)"></i>
<div style="position:absolute;inset:0 0 14% 0;border-radius:50%;background:linear-gradient(145deg,{color1},{color2});box-shadow:0 {size*0.04}px 0 rgba(0,0,0,.18),inset 0 0 0 {size*0.05}px rgba(255,255,255,.45);display:flex;align-items:center;justify-content:center;color:#fff;font:400 {size*0.46}px WenKai;text-shadow:0 2px 0 rgba(0,0,0,.18)">{ch}</div></div>'''

def s08():  # popup
    css='''.ov{position:absolute;inset:0;background:rgba(59,47,47,.55)}
.pop{position:absolute;left:28px;right:28px;top:150px;padding:78px 20px 20px;text-align:center;background:#fff;border-radius:34px;box-shadow:0 8px 0 rgba(255,138,61,.3)}
.pop .m{position:absolute;left:50%;top:-70px;margin-left:-80px}
.pop h2{font-size:27px;font-weight:800;color:var(--orange)}.pop .pn{font:400 30px WenKai;margin-top:6px}.pop .pl{font-size:13px;color:var(--sub);margin-top:2px}
.conf i{position:absolute;display:block;border-radius:3px}
.st3{margin:12px 0 4px;display:flex;justify-content:center;gap:8px}
.sts{display:flex;gap:8px;margin-top:12px}.sts div{flex:1;background:#FFF6E0;border-radius:16px;padding:8px 0;font-size:11.5px;color:var(--sub)}.sts b{display:block;font-size:20px;color:var(--ink)}
.bt{margin-top:14px;height:52px;border-radius:18px;color:#fff;font-size:18px;font-weight:800;display:flex;align-items:center;justify-content:center}
'''
    conf=''.join(f'<i style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{c};transform:rotate({r}deg)"></i>' for x,y,w,h,c,r in [(30,80,10,18,'#FFC93C',20),(90,40,8,14,'#FF6B8B',-30),(310,70,10,18,'#4DA3FF',40),(340,130,8,14,'#3FBF7F',10),(60,180,9,16,'#8E7CFF',-20),(330,190,10,10,'#FFC93C',0),(150,90,8,8,'#3FBF7F',0),(250,50,9,15,'#FF8A3D',30),(20,140,8,8,'#4DA3FF',0),(370,60,8,14,'#FF6B8B',60),(200,20,8,8,'#FFC93C',0)])
    # blurred background: simple level screen hint
    bg='<div style="position:absolute;inset:0;background:linear-gradient(#FFF3D1,#FFF6E0)"></div>'
    b=bg+'<div class="ov"></div><div class="conf">'+conf+'</div>'+statusbar().replace('class="sb"','class="sb" style="color:#fff"')
    b+=f'''<div class="pop"><div class="m">{medal('#FF9DB0','#FF5F86','题',160)}</div>
<h2>整首通关!</h2><div class="pn">《题临安邸》</div><div class="pl">五年级上册 · 林升〔宋〕</div>
<div class="st3">{stars(3,3,34)}</div><div style="font-size:14px;font-weight:800;color:#B26A1A">获得徽章「西湖小诗人」</div>
<div class="sts"><div><b>4/4</b>关卡</div><div><b>1</b>次错题</div><div><b>+30</b>星星</div></div>
<div class="bt" style="background:var(--orange);box-shadow:0 5px 0 #E2622A">查看徽章墙</div>
<div class="bt" style="background:#fff;color:var(--orange);margin-top:10px;height:46px;box-shadow:inset 0 0 0 3px var(--orange2)">挑战下一首:山居秋暝</div></div>'''
    b+=tag_demo().replace('#B5A793','#E6DCCB')
    return page('08 通关徽章弹窗',b,css)

def s09():
    css='''.hd{padding:0 20px;display:flex;align-items:center;gap:12px}.hd h1{font-size:24px;font-weight:800}
.sum{margin:10px 16px 0;padding:12px 16px;display:flex;align-items:center;gap:14px}.sum .big{font-size:34px;font-weight:800;color:var(--orange);line-height:1}.sum small{font-size:12px;color:var(--sub)}
.tabs{display:flex;gap:8px;padding:12px 16px 4px}.tabs div{padding:6px 14px;border-radius:99px;background:#fff;font-weight:800;font-size:13.5px;color:var(--sub)}.tabs .on{background:var(--ink);color:#fff}
.gt{padding:8px 20px 6px;display:flex;justify-content:space-between;align-items:baseline}.gt b{font-size:16px}.gt span{font-size:12px;color:var(--sub)}
.wall{display:grid;grid-template-columns:repeat(3,1fr);gap:8px 10px;padding:0 16px}
.bd{height:132px;padding:10px 4px 6px;text-align:center;display:flex;flex-direction:column;align-items:center}
.bd b{font:400 16px WenKai;margin-top:2px;white-space:nowrap}.bd small{font-size:11px;color:var(--sub);margin-top:1px}
.bd.lk b{color:#B9B0A3}'''
    E=[('#FFD84D','#FF9F1C','静','静夜思'),('#7FE0B0','#2FB57A','池','池上'),('#8FCBFF','#3D8FEA','小','小池')]
    F=[('#FF9DB0','#FF5F86','示','示儿'),('#C1B6FF','#7C68F0','题','题临安邸'),('#FFB27A','#F0641E','己','己亥杂诗'),None,None,None]
    b=statusbar()+'<div class="hd"><div class="back">‹</div><h1>我的徽章墙</h1></div>'
    b+=f'<div class="card sum">{ring(48,64,"#FF8A3D",label="14/29",sw=8)}<div><div class="big">14 枚</div><small>已获得 · 共 29 枚(示例数据)</small></div><div style="margin-left:auto;text-align:right;font-size:12px;color:var(--sub)">再得 2 枚<br><b style="color:var(--pink)">解锁「小诗人」称号</b></div></div>'
    b+='<div class="tabs"><div>一年级</div><div>二年级</div><div>三年级</div><div>四年级</div><div class="on">全部</div></div>'
    b+='<div class="gt"><b>一年级下册</b><span>3 / 3</span></div><div class="wall">'
    for c1,c2,ch,n in E:
        b+=f'<div class="card bd">{medal(c1,c2,ch,74)}<b>{n}</b><small>已获得</small></div>'
    b+='</div><div class="gt" style="padding-top:10px"><b>五年级上册</b><span>2 / 6</span></div><div class="wall">'
    names=[('示儿',None,'闯关中 1/4'),('题临安邸',('#FF9DB0','#FF5F86','题'),''),('己亥杂诗',('#FFB27A','#F0641E','己'),''),('山居秋暝',None,'闯关中 2/8'),('枫桥夜泊',None,'未获得'),('早春呈水部…',None,'未获得')]
    for n,m,sm in names:
        if m: b+=f'<div class="card bd">{medal(m[0],m[1],m[2],74)}<b>{n}</b><small>已获得</small></div>'
        else: b+=f'<div class="card bd lk">{medal("","","",74,True)}<b>{n}</b><small>{sm}</small></div>'
    b+='</div>'
    b=b.replace('<div class="gt" style="padding-top:10px"><b>五年级上册</b><span>2 / 6</span></div><div class="wall">','<div class="gt" style="padding-top:10px"><b>五年级上册</b><span>2 / 6</span></div><div class="wall" id="w5">')
    b+=tabbar(3)+tag_demo()
    return page('09 徽章墙',b,css)
