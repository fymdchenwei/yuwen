# -*- coding: utf-8 -*-
from lib import *
from s5 import BASE,CAT,tianzi
from s3 import medal

def s_mist():
    css=BASE+'''.hd{padding:0 20px;display:flex;align-items:center;gap:12px}.hd h1{font-size:24px;font-weight:800}
.sum{margin:8px 16px 0;padding:10px 14px;display:flex;align-items:center;gap:12px}
.sum .c{flex:1;text-align:center}.sum .c b{display:block;font-size:24px;line-height:1.1}.sum .c span{font-size:11.5px;color:var(--sub);font-weight:700}
.tabs{display:flex;gap:6px;padding:10px 16px 4px;overflow:hidden}.tabs div{padding:5px 11px;border-radius:99px;background:#fff;font-weight:800;font-size:12.5px;color:var(--sub);white-space:nowrap}.tabs .on{background:var(--ink);color:#fff}
.gt{padding:6px 20px 4px;font-size:13px;font-weight:800;color:var(--orange)}
.it{margin:0 16px 7px;padding:8px 12px;display:flex;align-items:center;gap:10px;height:58px}
.it .ic{width:34px;height:34px;border-radius:12px;line-height:34px;font-size:19px}
.it .m{flex:1;min-width:0}.it .m b{font-size:15px;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.it .m span{font-size:11.5px;color:var(--sub)}
.it .rt{text-align:right;flex:none;font-size:11.5px;color:var(--sub)}.it .rt .chip{font-size:11.5px;margin-bottom:2px}
.tip{margin:4px 16px 0;padding:0 4px;font-size:11.5px;color:var(--sub);line-height:1.5;text-align:center}'''
    b=statusbar()+'<div class="hd"><h1>错题本</h1><span style="margin-left:auto;font-size:12px;color:var(--sub)">五类练习共用一本</span></div>'
    b+='<div class="card sum"><div class="c"><b style="color:var(--pink)">4</b><span>今天要复习</span></div><div class="c"><b style="color:var(--orange)">12</b><span>待复习</span></div><div class="c"><b style="color:var(--green)">7</b><span>已毕业</span></div><div style="background:var(--orange);color:#fff;border-radius:16px;padding:10px 14px;font-weight:800;font-size:14px;box-shadow:0 4px 0 #E2622A;white-space:nowrap">复习 4 题</div></div>'
    b+='<div class="tabs"><div class="on">全部 12</div><div>古诗词</div><div>听写</div><div>阅读</div><div>成语</div><div>常识</div></div>'
    b+='<div class="gt">今天要复习</div>'
    rows=[('dict','灿烂','听写 · 错字:灿','今天','第 1 次复习'),('dict','秘密','听写 · 错字:秘','今天','第 1 次复习'),('poem','但悲不见九州同','古诗词 · 《示儿》第 2 关','今天','第 1 次复习'),('read','《清晨的牵牛花》第 1 题','阅读 · 依据句划错','今天','第 2 次复习')]
    for k,t2,s2,d,r in rows:
        g,col,n=CAT[k]
        b+=f'<div class="card it"><div class="ic" style="background:{col}">{g}</div><div class="m"><b>{t2}</b><span>{s2}</span></div><div class="rt"><span class="chip" style="background:var(--pink2);color:#D63A5F">重考 · {d}</span><br>{r}</div></div>'
    b+='<div class="gt" style="color:var(--sub)">接下来</div>'
    rows2=[('idiom','发愤图强','成语 · 释义选错','明天','第 1 次复习'),('lit','《朝花夕拾》的作者','文学常识 · 答错','明天','第 1 次复习')]
    for k,t,s,d,r in rows2:
        g,col,n=CAT[k]
        b+=f'<div class="card it"><div class="ic" style="background:{col}">{g}</div><div class="m"><b>{t}</b><span>{s}</span></div><div class="rt"><span class="chip c-next">{d}</span><br>{r}</div></div>'
    b+='<div class="tip">连续 3 次答对就“毕业”;答错会回到第 1 次(明天→3 天后→7 天后)</div>'
    b+=tabbar(2)+tag_demo()
    return page('21 错题本',b,css)

def s_prog():
    css=BASE+'''.hd{padding:0 20px;display:flex;align-items:center;gap:12px}.hd h1{font-size:24px;font-weight:800}
.sec{margin:8px 16px 0;padding:10px 14px}.sec h3{font-size:15px;font-weight:800;display:flex;justify-content:space-between;align-items:baseline}.sec h3 small{font-size:11.5px;color:var(--sub);font-weight:600}
.top3{display:flex;gap:8px;margin-top:8px}.top3>div{flex:1;text-align:center;background:#FFF6E0;border-radius:16px;padding:7px 0;font-size:11.5px;color:var(--sub);font-weight:700}.top3 b{display:block;font-size:22px;color:var(--ink);line-height:1.15}
.cr{display:flex;align-items:center;gap:8px;margin-top:8px;font-size:13px;font-weight:800}.cr .g{width:26px;height:26px;border-radius:9px;color:#fff;font:400 15px/26px WenKai;text-align:center;flex:none}
.cr .nm{width:98px;flex:none;white-space:nowrap}.cr .b{flex:1;height:14px;border-radius:9px;background:var(--gray2);overflow:hidden}.cr .b i{display:block;height:100%;border-radius:9px}.cr em{font-style:normal;font-size:11.5px;color:var(--sub);width:36px;text-align:right}
.wk{display:flex;justify-content:space-between;margin-top:8px}.wk div{text-align:center;font-size:11px;color:var(--sub);font-weight:700}.wk i{display:flex;width:32px;height:32px;border-radius:50%;margin:0 auto 3px;align-items:center;justify-content:center;background:var(--gray2);font-style:normal}
.wk .d i{background:var(--green)}.wk .t i{background:#fff;box-shadow:0 0 0 3px var(--orange);color:var(--orange);font-weight:800;font-size:12px}
.bg{display:flex;gap:8px;margin-top:8px}.bg>div{flex:1;text-align:center;font-size:11.5px;font-weight:700;display:flex;flex-direction:column;align-items:center}'''
    b=statusbar()+'<div class="hd"><h1>总进度与徽章</h1><span style="margin-left:auto;font-size:12px;color:var(--sub)">本周</span></div>'
    b+='<div class="card sec"><h3>连续打卡<small>每天完成 15 分钟计划算 1 天</small></h3><div class="top3"><div><b style="color:var(--orange)">5 天</b>当前连续</div><div><b>12 天</b>最长纪录</div><div><b>3 分</b>今日已学 / 15</div></div>'
    b+='<div class="wk">'+''.join(f'<div class="{c}"><i>{ck(15) if c=="d" else ("今" if c=="t" else "")}</i>{n}</div>' for n,c in [('周日','d'),('周一','d'),('周二','d'),('周三','d'),('周四','t'),('周五',''),('周六','')])+'</div></div>'
    b+='<div class="card sec"><h3>五类练习进度<small>已掌握 / 总量 · 示例数据</small></h3>'
    for k,pct,t in [('poem',31,'9/29 首'),('dict',55,'44/80 词'),('read',20,'2/10 篇'),('idiom',42,'21/50 个'),('lit',36,'18/50 题')]:
        g,col,n=CAT[k]
        b+=f'<div class="cr"><div class="g" style="background:{col}">{g}</div><div class="nm">{n[:6]}</div><div class="b"><i style="width:{pct}%;background:{col}"></i></div><em>{t}</em></div>'
    b+='</div>'
    b+='<div class="card sec"><h3>成就徽章<small>已获得 8 / 20 枚 · 示例数据</small></h3><div class="bg">'
    for c1,c2,ch,n,lock in [('#FFD84D','#FF9F1C','连','连续 5 天',0),('#7FE0B0','#2FB57A','写','听写 10 词',0),('#8FCBFF','#3D8FEA','据','找到依据',0),('','','','连续 7 天',1),('','','','成语达人',1)]:
        b+=f'<div>{medal(c1,c2,ch,58,bool(lock))}<span style="margin-top:2px;{"color:#B9B0A3" if lock else ""}">{n}</span></div>'
    b+='</div><div style="margin-top:8px;font-size:12px;color:var(--sub);text-align:center">再连续 2 天,解锁「连续 7 天」徽章</div></div>'
    b+='<div style="margin:8px 16px 0;padding:10px 14px;border-radius:24px;background:linear-gradient(135deg,#FF8FA8,#FF6B8B);color:#fff;display:flex;align-items:center;gap:12px;box-shadow:0 5px 0 #D63A5F"><div style="width:40px;height:40px;border-radius:14px;background:#fff;color:var(--pink);font:400 23px/40px WenKai;text-align:center">错</div><div style="flex:1"><b style="font-size:16px;display:block">错题本</b><span style="font-size:12px">12 个待复习 · 已毕业 7 个</span></div><div style="background:#fff;color:var(--pink);font-weight:800;font-size:13px;border-radius:99px;padding:6px 12px">去复习 ›</div></div>'
    b+=tabbar(3)+tag_demo()
    return page('22 总进度与徽章总览',b,css)

def s_a2hs():
    css=BASE+'''.hd{padding:0 20px;display:flex;align-items:center;gap:12px}.hd h1{font-size:22px;font-weight:800}
.hero{margin:8px 16px 0;padding:12px 14px;display:flex;align-items:center;gap:12px}
.appicon{width:64px;height:64px;border-radius:16px;background:linear-gradient(145deg,#FFB14F,#FF7A3D);display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 4px 0 #E2622A;color:#fff;font:400 38px WenKai}
.seg{margin:10px 16px 0;display:flex;background:var(--gray2);border-radius:16px;padding:4px}.seg div{flex:1;text-align:center;padding:7px 0;font-weight:800;font-size:13.5px;border-radius:12px;color:var(--sub)}.seg .on{background:#fff;color:var(--ink);box-shadow:0 2px 0 rgba(0,0,0,.08)}
.step{margin:8px 16px 0;padding:8px 12px;display:flex;align-items:center;gap:12px}
.step .n{width:28px;height:28px;border-radius:50%;background:var(--orange);color:#fff;font-weight:800;font-size:14px;display:flex;align-items:center;justify-content:center;flex:none}
.step .t{font-size:14px;font-weight:800;line-height:1.35}.step .t small{display:block;font-size:11.5px;color:var(--sub);font-weight:600}
.ico{width:34px;height:34px;border-radius:10px;background:#F2F2F7;display:flex;align-items:center;justify-content:center;margin-left:auto;flex:none}
.url{margin:8px 16px 0;padding:9px 12px;border-radius:14px;background:#fff;font:600 12.5px 'Noto Sans CJK SC';color:#1E78D8;text-align:center;box-shadow:inset 0 0 0 2px #DCEEFF;word-break:break-all}
.off{margin:8px 16px 0;padding:9px 12px;display:flex;align-items:center;gap:10px;font-size:12.5px;line-height:1.5}
.off .i{width:32px;height:32px;border-radius:50%;background:var(--green2);display:flex;align-items:center;justify-content:center;flex:none}'''
    share='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1E78D8" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 15V3M8 7l4-4 4 4M6 11H5a1 1 0 00-1 1v8a1 1 0 001 1h14a1 1 0 001-1v-8a1 1 0 00-1-1h-1"/></svg>'
    plus='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#3B2F2F" stroke-width="2.2" stroke-linecap="round"><rect x="4" y="4" width="16" height="16" rx="4"/><path d="M12 8v8M8 12h8"/></svg>'
    b=statusbar()+'<div class="hd"><div class="back">‹</div><h1>添加到主屏幕</h1></div>'
    b+=f'<div class="card hero"><div class="appicon">学</div><div><div style="font-size:16px;font-weight:800">像 App 一样使用</div><div style="font-size:12.5px;color:var(--sub);margin-top:3px;line-height:1.5">一点就开,全屏显示,没网也能练</div></div></div>'
    b+='<div class="seg"><div class="on">iPhone / iPad(Safari)</div><div>安卓(Chrome)</div></div>'
    b+=f'<div class="card step"><div class="n">1</div><div class="t">点 Safari 底部的“分享”<small>方框加向上箭头的图标</small></div><div class="ico">{share}</div></div>'
    b+=f'<div class="card step"><div class="n">2</div><div class="t">向下滑,选“添加到主屏幕”<small>图标是方框里有个加号</small></div><div class="ico">{plus}</div></div>'
    b+='<div class="card step"><div class="n">3</div><div class="t">点右上角“添加”<small>回到桌面,找到“每日十五分钟”图标</small></div><div class="ico" style="width:auto;padding:0 10px;font-size:13px;font-weight:800;color:#1E78D8">添加</div></div>'
    b+='<div class="url"><span style="color:var(--sub);font-weight:600">网站地址:</span>https://fymdchenwei.github.io/yuwen/</div>'
    b+=f'<div class="card off"><div class="i">{ck(18,"#1F9A5E")}</div><div><b>离线也能用</b><br>第一次联网打开后,题目和字体会存在手机里,没网时也能练习、记进度。</div></div>'
    b+='<div class="card off" style="background:#FFF6E0;box-shadow:none"><div class="i" style="background:#FFE9D6;color:var(--orange);font-weight:800">!</div><div><b>小提醒</b><br>进度存在这台设备上,换手机或清除浏览器数据会丢失(可在“我的”里导出备份)。</div></div>'
    b+='<div class="cta or">我知道了,去添加</div>'+tag_demo()
    return page('23 添加到主屏幕引导页',b,css)
