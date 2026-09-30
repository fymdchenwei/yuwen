# -*- coding: utf-8 -*-
from lib import *

GR = {'一':('#FF6B8B','#FFE1E8'),'二':('#FF8A3D','#FFE9D6'),'三':('#E5A800','#FFF1C4'),'四':('#3FBF7F','#DDF6E8'),'五':('#4DA3FF','#DCEEFF')}
STAGE = {'不会':('c-zero','#B9B0A3'),'在学':('c-learn','#FFC93C'),'会了':('c-got','#4DA3FF'),'已掌握':('c-master','#3FBF7F')}

def s00():
    items=[
     ('填','逐句填空(闯关)','遮住诗句里的字词,点选/拼字补全','字词准确识记、默写、形近·同音字辨析','纯记忆','c-mem','v1 完整设计','c-v1','#FF8A3D'),
     ('接','看上句接下句','给出上句,选出正确的下句','句与句之间的连贯记忆,顺畅背诵','纯记忆','c-mem','后续上线','c-next','#4DA3FF'),
     ('排','诗句排序','把打乱的诗句拖回正确顺序','全诗结构、意脉与顺序的理解','记忆+理解','c-both','后续上线','c-next','#8E7CFF'),
     ('连','诗题·作者·朝代连线','把诗题、诗人、朝代连起来','文学常识的识记与关联','纯记忆','c-mem','后续上线','c-next','#FF6B8B'),
     ('释','字词释义选择','选出加点字/整句的正确意思','结合注释理解词义、诗意;古今异义','理解运用','c-und','后续上线','c-next','#3FBF7F'),
     ('听','听读跟背','听范读,跟读,再遮字背诵','朗读节奏、语感、背诵流畅度','记忆+语感','c-both','后续上线','c-next','#FFB020'),
    ]
    css='''.h{padding:2px 20px 8px}.h h1{font-size:25px;font-weight:800}.h p{font-size:12.5px;color:var(--sub);margin-top:3px}
.it{margin:0 16px 8px;padding:10px 12px;display:flex;gap:11px;align-items:flex-start;height:96px}
.ic{width:46px;height:46px;border-radius:15px;color:#fff;font-family:WenKai;font-size:25px;display:flex;align-items:center;justify-content:center;flex:none;margin-top:2px}
.it .n{font-size:16.5px;font-weight:800;display:flex;justify-content:space-between;align-items:center;gap:6px}
.it .d{font-size:12px;color:var(--sub);margin-top:2px;line-height:1.35}
.it .a{font-size:12px;margin-top:3px;color:var(--ink);line-height:1.35}.it .a b{color:#B26A1A}
.g{display:flex;gap:4px;margin-top:5px}.g i{font-style:normal;width:21px;height:19px;border-radius:7px;background:var(--gray2);font:700 11.5px/19px WenKai;text-align:center;color:var(--sub)}
.flow{margin:0 16px;background:#fff;border-radius:16px;padding:8px 12px;font-size:12.5px;font-weight:700;display:flex;justify-content:space-between;align-items:center;color:#B26A1A}
.flow span.s{background:var(--orange);color:#fff;border-radius:99px;padding:1px 9px}.flow em{color:var(--gray);font-style:normal}'''
    b=statusbar()+'<div class="h"><h1>练习项分类总览</h1><p>古诗词模块 · 6 类练习项,每类都可选择 一~五年级</p></div>'
    b+='<div class="flow" style="margin-bottom:8px"><span class="s">① 练习项</span><em>›</em><span>② 选年级</span><em>›</em><span>③ 选诗</span><em>›</em><span>④ 关卡</span></div>'
    for ic,n,d,a,t,tc,st,sc,col in items:
        g=''.join(f'<i>{x}</i>' for x in '一二三四五')
        b+=f'<div class="card it"><div class="ic" style="background:{col}">{ic}</div><div style="flex:1;min-width:0"><div class="n"><span>{n}</span><span class="chip {sc}">{st}</span></div><div class="d">{d}</div><div class="a"><b>考察:</b>{a}</div><div style="display:flex;justify-content:space-between;align-items:center"><div class="g">{g}</div><span class="chip {tc}">{t}</span></div></div></div>'
    b+='<div style="text-align:center;font-size:11px;color:#A8987F;margin-top:2px">题型属性:纯记忆 / 理解运用 / 混合 · 全部练习项共用同一套关卡、徽章、错题本</div>'
    return page('00 练习项分类总览',b,css)

def s01():
    css='''.hd{display:flex;align-items:center;gap:12px;padding:6px 20px 0}.hd h1{font-size:22px;font-weight:800}.hd p{font-size:13px;color:var(--sub);margin-top:2px}
.streak{margin-left:auto;background:#fff;border-radius:14px;padding:6px 10px;font-size:12px;font-weight:700;color:#B26A1A;text-align:center;line-height:1.3}.streak b{display:block;font-size:20px;color:var(--orange)}
.today{margin:14px 16px 0;padding:14px 16px;background:linear-gradient(135deg,#FF9A4D,#FF7A3D);color:#fff;border-radius:24px;box-shadow:0 5px 0 #E2622A}
.today .t{display:flex;justify-content:space-between;font-weight:800;font-size:16px}.today .t span{font-size:13px;font-weight:600;opacity:.95}
.bar{height:12px;border-radius:9px;background:rgba(255,255,255,.35);margin:9px 0 11px;overflow:hidden}.bar i{display:block;height:100%;width:34%;background:#fff;border-radius:9px}
.btn{background:#fff;color:#E2622A;border-radius:16px;text-align:center;padding:10px;font-weight:800;font-size:16px}
.st{display:flex;justify-content:space-between;align-items:baseline;padding:14px 20px 8px}.st b{font-size:18px}.st span{font-size:12px;color:var(--sub)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:0 16px}
.p{padding:12px;height:110px;position:relative}.p .ic{width:38px;height:38px;border-radius:13px;color:#fff;font:400 22px/38px WenKai;text-align:center}
.p .n{font-size:16px;font-weight:800;margin-top:7px}.p .d{font-size:11.5px;color:var(--sub);margin-top:1px}.p .chip{position:absolute;top:10px;right:10px;font-size:11px;padding:2px 8px}
.soon{margin:10px 16px 0;border:2.5px dashed #D9CDB8;border-radius:20px;padding:11px 14px;display:flex;align-items:center;gap:12px;color:#9A8B78;background:rgba(255,255,255,.55)}
.soon .ic{width:38px;height:38px;border-radius:13px;background:#D9CDB8;color:#fff;font:400 22px/38px WenKai;text-align:center}.soon b{font-size:15px;display:block}.soon span{font-size:11.5px}'''
    cards=[('填','逐句填空','闯关 · 遮字补全','#FF8A3D','v1 主玩法','c-v1'),('接','看上句接下句','选出正确的下句','#4DA3FF','后续','c-next'),('排','诗句排序','拖回正确顺序','#8E7CFF','后续','c-next'),('连','诗题作者连线','诗题·诗人·朝代','#FF6B8B','后续','c-next'),('释','字词释义选择','读懂字词与诗意','#3FBF7F','后续','c-next'),('听','听读跟背','跟着范读背一背','#FFB020','后续','c-next')]
    b=statusbar()+'<div class="hd"><div class="back">‹</div><div><div style="font-size:12px;color:var(--sub)">首页 › <b style="color:var(--orange)">古诗词</b></div><div style="font-size:22px;font-weight:800">古诗词 · 选练习项</div></div><div class="streak">今日<b>1/3</b>关</div></div>'
    b+='<div class="today"><div class="t">今日古诗词闯关<span>已完成 1 / 3 关</span></div><div class="bar"><i></i></div><div class="btn">继续闯关 · 《示儿》第 2 关</div></div>'
    b+='<div class="st"><b>选一个练习项</b><span>选好后再选年级、选诗</span></div><div class="grid">'
    for ic,n,d,col,t2,tc in cards:
        b+=f'<div class="card p"><div class="ic" style="background:{col}">{ic}</div><span class="chip {tc}">{t2}</span><div class="n">{n}</div><div class="d">{d}</div></div>'
    b+='</div><div style="text-align:center;font-size:12px;color:var(--sub);margin-top:12px">其余四类练习(听写、阅读、成语、文学常识)在首页</div>'
    b+=tabbar(0)+tag_demo()
    return page('01 古诗词练习项入口',b,css)

def grade_bar(sel, small=None):
    prog={'一':'3/3','二':'2/8','三':'2/6','四':'1/6','五':'1/6'}
    s='<div class="grades">'
    for g in '一二三四五':
        c,c2=GR[g]; on=g==sel
        s+=f'<div class="gk{" on" if on else ""}"><b style="background:{c if on else c2};color:{"#fff" if on else c}">{g}</b><span>{prog[g]}</span></div>'
    return s+'</div>'

GCSS='''.hd{padding:0 16px;display:flex;align-items:center;gap:12px}.hd .bc{font-size:12px;color:var(--sub)}.hd .bc b{color:var(--orange)}.hd h1{font-size:22px;font-weight:800}
.grades{display:flex;justify-content:space-between;padding:12px 16px 4px}.gk{width:62px;text-align:center}.gk b{display:flex;width:52px;height:52px;margin:0 auto;border-radius:19px;align-items:center;justify-content:center;font:400 27px WenKai}
.gk.on b{box-shadow:0 5px 0 rgba(0,0,0,.16);transform:translateY(-3px);width:56px;height:56px;margin-top:-2px}.gk span{display:block;font-size:11.5px;color:var(--sub);margin-top:6px;font-weight:700}.gk.on span{color:var(--ink)}
.cap{padding:0 20px;font-size:12px;color:var(--sub);margin-top:2px}
.seg{margin:8px 16px 10px;display:flex;background:var(--gray2);border-radius:16px;padding:4px}.seg div{flex:1;text-align:center;padding:8px 0;font-weight:800;font-size:14px;border-radius:12px;color:var(--sub)}.seg .on{background:#fff;color:var(--ink);box-shadow:0 2px 0 rgba(0,0,0,.08)}
.seg small{font-size:10.5px;font-weight:700;margin-left:4px;padding:1px 6px;border-radius:9px;background:#FFE1E8;color:#E0456B}
.row{margin:0 16px 8px;display:flex;align-items:center;gap:12px;padding:0 12px;}
.row .no{width:40px;height:40px;border-radius:50%;color:#fff;font:400 20px/40px WenKai;text-align:center;flex:none}
.row .tt{flex:1;min-width:0}.row .tt b{font-size:17.5px;display:block;font-weight:800;white-space:nowrap}.row .tt span{font-size:12px;color:var(--sub)}
.row .rt{text-align:right;flex:none}.row .rt .chip{font-size:11.5px}.row .rt div{margin-top:3px;line-height:0}
.warn{margin:0 16px 8px;padding:9px 12px;border-radius:16px;background:#FFF0F3;border:2px dashed #FF9DB0;color:#C03A5C;font-size:12.5px;font-weight:700;line-height:1.4}'''

def row(i,t,sub,stage,stars_n=None,h=64):
    cl,col=STAGE[stage]
    st=stars(stars_n,3,15) if stars_n is not None else ''
    return f'<div class="card row" style="height:{h}px"><div class="no" style="background:{col}">{i}</div><div class="tt"><b>{t}</b><span>{sub}</span></div><div class="rt"><span class="chip {cl}">{stage}</span><div>{st}</div></div></div>'

def s02():
    b=statusbar()+'<div class="hd"><div class="back">‹</div><div><div class="bc">练习项 › <b>逐句填空</b></div><h1>选择年级和诗</h1></div></div>'
    b+=grade_bar('五')+'<div class="cap" style="text-align:center;margin-bottom:2px">已掌握 / 本年级诗数(示例数据)</div>'
    b+='<div class="seg"><div class="on">上册 · 2026 新版</div><div>下册 <small>待新版</small></div></div>'
    rows=[('示儿','陆游〔宋〕 · 4 句 · 4 关','在学',None),('题临安邸','林升〔宋〕 · 4 句 · 4 关','会了',2),('己亥杂诗','龚自珍〔清〕 · 4 句 · 4 关','已掌握',3),('山居秋暝','王维〔唐〕 · 8 句 · 8 关','在学',None),('枫桥夜泊','张继〔唐〕 · 4 句 · 4 关','在学',None),('早春呈水部张十八员外','韩愈〔唐〕 · 4 句 · 4 关','不会',None)]
    for i,(t,s,st,sn) in enumerate(rows,1): b+=row(i,t,s,st,sn,66)
    b+=tabbar(0)+tag_demo()
    return page('02 年级选择与诗目列表 五年级',b,GCSS)

def s03():
    b=statusbar()+'<div class="hd"><div class="back">‹</div><div><div class="bc">练习项 › <b>逐句填空</b></div><h1>选择年级和诗</h1></div></div>'
    b+=grade_bar('三')+'<div class="cap" style="text-align:center;margin-bottom:2px">已掌握 / 本年级诗数(示例数据)</div>'
    b+='<div class="seg"><div>上册 <small>未核实</small></div><div class="on">下册 · 2025 春</div></div>'
    b+='<div class="warn" style="margin-bottom:8px">三年级上册“古诗三首”(第4课、第20课)教材篇目<b>未核实</b>,核实前不上架、不出题。</div>'
    rows=[('绝句','杜甫〔唐〕 · 4 句 · 4 关','已掌握',3),('惠崇春江晚景','苏轼〔宋〕 · 4 句 · 4 关','会了',2),('三衢道中','曾几〔宋〕 · 4 句 · 4 关','在学',None),('元日','王安石〔宋〕 · 4 句 · 4 关','不会',None),('清明','杜牧〔唐〕 · 4 句 · 4 关','不会',None),('九月九日忆山东兄弟','王维〔唐〕 · 4 句 · 4 关','已掌握',3)]
    for i,(t,s,st,sn) in enumerate(rows,1): b+=row(i,t,s,st,sn,60)
    b+=tabbar(0)+tag_demo()
    return page('03 年级选择与诗目列表 三年级(含未核实)',b,GCSS)
