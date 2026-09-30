# -*- coding: utf-8 -*-
from lib import *
def s10():
    css='''.hd{padding:0 20px;display:flex;align-items:center;gap:12px}.hd h1{font-size:24px;font-weight:800}.hd span{margin-left:auto;font-size:12px;color:var(--sub)}
.sec{margin:6px 16px 0;padding:9px 14px}.sec h3{font-size:15px;font-weight:800;display:flex;justify-content:space-between;align-items:baseline}.sec h3 small{font-size:11.5px;color:var(--sub);font-weight:600}
.stg{display:flex;align-items:center;margin-top:9px}.stg .s{flex:1;text-align:center}.stg .s b{display:block;font-size:22px;line-height:1.1}.stg .s span{font-size:12px;font-weight:700}
.stg .ar{color:var(--gray);font-size:18px;flex:none;width:12px;text-align:center}
.gb{display:flex;align-items:center;gap:8px;margin-top:6px;font-size:13px;font-weight:800}.gb .g{width:26px;height:26px;border-radius:9px;color:#fff;font:400 15px/26px WenKai;text-align:center;flex:none}
.gb .b{flex:1;height:16px;border-radius:9px;background:var(--gray2);display:flex;overflow:hidden}.gb .b i{display:block;height:100%}.gb em{font-style:normal;font-size:11.5px;color:var(--sub);width:34px;text-align:right;font-weight:700}
.leg{display:flex;gap:10px;font-size:11px;color:var(--sub);margin-top:7px}.leg span:before{content:'';display:inline-block;width:9px;height:9px;border-radius:3px;margin-right:4px;background:var(--c)}
.rings{display:flex;justify-content:space-between;margin-top:8px}.rings div{text-align:center;font:400 14px WenKai;display:flex;flex-direction:column;align-items:center;gap:4px}
.two{display:flex;gap:10px;margin:6px 16px 0}.two .sec{margin:0;flex:1;min-width:0}
.mb{margin:6px 16px 0;padding:9px 14px;display:flex;align-items:center;gap:12px;background:linear-gradient(135deg,#FF8FA8,#FF6B8B);color:#fff;border-radius:24px;box-shadow:0 5px 0 #D63A5F}
.mb .ic{width:44px;height:44px;border-radius:15px;background:#fff;color:var(--pink);font:400 25px/44px WenKai;text-align:center}.mb b{font-size:17px;display:block}.mb span{font-size:12px;opacity:.95}.mb .go{margin-left:auto;background:#fff;color:var(--pink);font-weight:800;font-size:13px;border-radius:99px;padding:6px 12px}'''
    b=statusbar()+'<div class="hd"><div class="back">‹</div><h1>我的进步</h1><span>五年级 · 本周</span></div>'
    b+='''<div class="card sec"><h3>从不会到掌握<small>全部 29 首 · 示例数据</small></h3><div class="stg">
<div class="s"><b style="color:#B9B0A3">9</b><span style="color:#8C7B6B">不会</span></div><div class="ar">›</div>
<div class="s"><b style="color:#E5A800">6</b><span style="color:#B98100">在学</span></div><div class="ar">›</div>
<div class="s"><b style="color:#4DA3FF">5</b><span style="color:#1E78D8">会了</span></div><div class="ar">›</div>
<div class="s"><b style="color:#3FBF7F">9</b><span style="color:#1F9A5E">已掌握</span></div></div></div>'''
    b+=f'<div class="card sec"><h3>五年级上册 · 每首掌握度<small>点击进入复习</small></h3><div class="rings">'
    for n,p,c in [('示儿',35,'#FFC93C'),('题临安邸',68,'#4DA3FF'),('己亥杂诗',96,'#3FBF7F'),('山居秋暝',8,'#B9B0A3'),('枫桥夜泊',30,'#FFC93C')]:
        b+=f'<div>{ring(p,54,c,label=str(p),sw=7)}{n}</div>'
    b+='</div></div>'
    b+='<div class="card sec"><h3>按年级进度<small>已掌握 / 总数</small></h3>'
    for g,col,segs,t in [('一','#FF6B8B',(60,40,0,0),'3/3'),('二','#FF8A3D',(30,30,20,20),'2/8'),('三','#E5A800',(15,30,25,30),'2/6'),('四','#3FBF7F',(35,35,20,10),'1/6'),('五','#4DA3FF',(60,20,10,10),'1/6')]:
        pass
    rows=[('一','#FF6B8B',(0,0,0,100),'3/3'),('二','#FF8A3D',(37,25,13,25),'2/8'),('三','#E5A800',(33,17,17,33),'2/6'),('四','#3FBF7F',(50,17,17,16),'1/6'),('五','#4DA3FF',(17,33,33,17),'1/6')]
    cols=['#E3DDD2','#FFC93C','#4DA3FF','#3FBF7F']
    for g,c,seg,t in rows:
        b+=f'<div class="gb"><div class="g" style="background:{c}">{g}</div><div class="b">'+''.join(f'<i style="width:{w}%;background:{cols[i]}"></i>' for i,w in enumerate(seg))+f'</div><em>{t}</em></div>'
    b+='<div class="leg"><span style="--c:#E3DDD2">不会</span><span style="--c:#FFC93C">在学</span><span style="--c:#4DA3FF">会了</span><span style="--c:#3FBF7F">已掌握</span></div></div>'
    # 7 days + curve
    days=[('三',2),('四',3),('五',1),('六',4),('日',3),('一',0),('二',5)]
    bars=''.join(f'<div style="flex:1;text-align:center"><div style="height:{v*9+3}px;background:{"#FF8A3D" if i==6 else "#FFD0A3"};border-radius:6px;margin:0 4px"></div><div style="font-size:10.5px;color:var(--sub);margin-top:3px">{d}</div></div>' for i,(d,v) in enumerate(days))
    b+=f'<div class="two"><div class="card sec"><h3>近 7 天闯关<small>关</small></h3><div style="display:flex;align-items:flex-end;height:66px;margin-top:6px">{bars}</div></div>'
    b+='''<div class="card sec"><h3>复习曲线<small>会忘 → 再记</small></h3><svg width="100%" height="76" viewBox="0 0 150 76" style="margin-top:4px"><path d="M4 12 C 22 12, 26 58, 52 62" fill="none" stroke="#D9D0C2" stroke-width="3" stroke-dasharray="4 4" stroke-linecap="round"/><path d="M4 12 C 18 14, 22 44, 40 46 L40 14 C 58 18, 64 40, 84 42 L84 14 C 104 18, 112 30, 140 30" fill="none" stroke="#3FBF7F" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="40" cy="14" r="4.5" fill="#FF8A3D"/><circle cx="84" cy="14" r="4.5" fill="#FF8A3D"/><text x="3" y="74" font-size="9" fill="#8C7B6B">今天</text><text x="34" y="74" font-size="9" fill="#8C7B6B">明天</text><text x="76" y="74" font-size="9" fill="#8C7B6B">3天</text><text x="118" y="74" font-size="9" fill="#8C7B6B">7天</text></svg></div></div>'''
    b+='<div class="mb"><div class="ic">错</div><div><b>错题本</b><span>12 个待复习 · 今天要复习 4 个</span></div><div class="go">去复习 ›</div></div>'
    b+=tabbar(3)+tag_demo()
    return page('10 进度可视化',b,css)
