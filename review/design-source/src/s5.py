# -*- coding: utf-8 -*-
from lib import *

CAT={'poem':('诗','#FF8A3D','古诗词'),'dict':('写','#4DA3FF','生字词听写'),'read':('读','#3FBF7F','阅读理解找证据'),'idiom':('语','#8E7CFF','成语与近义词'),'lit':('识','#FF6B8B','文学常识速问')}
BASE='''.top{display:flex;align-items:center;gap:10px;padding:0 16px;height:36px}
.top .x{width:34px;height:34px;border-radius:12px;background:#fff;color:var(--sub);display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700;flex:none}
.top .pb{flex:1;height:14px;background:var(--gray2);border-radius:9px;overflow:hidden}.top .pb i{display:block;height:100%;background:var(--green);border-radius:9px}
.top .rt{font-size:13px;font-weight:800;color:var(--sub);flex:none}
.ttl{padding:8px 20px 0;display:flex;justify-content:space-between;align-items:baseline;gap:8px}.ttl b{font-size:20px;font-weight:800;white-space:nowrap}.ttl span{font-size:12.5px;color:var(--sub)}
.btn{height:52px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:800;color:#fff}
.cta{position:absolute;left:16px;right:16px;bottom:22px;height:56px;border-radius:20px;color:#fff;font-size:20px;font-weight:800;display:flex;align-items:center;justify-content:center;z-index:7}
.or{background:var(--orange);box-shadow:0 5px 0 #E2622A}.gn{background:var(--green);box-shadow:0 5px 0 #2A9A63}.bl{background:var(--blue);box-shadow:0 5px 0 #2F82E0}.pk{background:var(--pink);box-shadow:0 5px 0 #D63A5F}.pu{background:var(--purple);box-shadow:0 5px 0 #6A57E0}.gy{background:#D8D1C6;box-shadow:0 5px 0 #BDB5A8}
.wh{background:#fff;color:var(--orange);box-shadow:0 4px 0 #EADFCB}
.say{display:flex;align-items:center;gap:10px}.say .bub{background:#fff;border-radius:18px;padding:8px 13px;font-size:13.5px;font-weight:700;position:relative;flex:1;line-height:1.45}
.say .bub:before{content:'';position:absolute;left:-7px;top:16px;border:8px solid transparent;border-left:0;border-right-color:#fff}
.ic{width:40px;height:40px;border-radius:14px;color:#fff;font:400 23px/40px WenKai;text-align:center;flex:none}
'''

def tianzi(s=96,ch='',col='#3B2F2F',fs=None):
    fs=fs or int(s*0.7)
    return f'<div style="width:{s}px;height:{s}px;border:3px solid #E8927C;border-radius:6px;background:#fff;position:relative;flex:none;background-image:repeating-linear-gradient(to bottom,#F3C1B4 0 6px,transparent 6px 12px),repeating-linear-gradient(to right,#F3C1B4 0 6px,transparent 6px 12px);background-size:2px 100%,100% 2px;background-position:center,center;background-repeat:no-repeat;display:flex;align-items:center;justify-content:center;font:400 {fs}px WenKai;color:{col}">{ch}</div>'

SPK='<svg width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M4 9v6h4l5 4V5L8 9H4z" fill="#fff"/><path d="M16 8.5a5 5 0 010 7M18.5 6a8.5 8.5 0 010 12" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'
def spk(s=64): return SPK.format(s=s)

def hdr_home(land=False):
    return f'<div style="display:flex;align-items:center;gap:12px;padding:{"0" if land else "6px 20px 0"}">{mascot(48 if land else 52)}<div><div style="font-size:{20 if land else 22}px;font-weight:800">你好,同学!</div><div style="font-size:12.5px;color:var(--sub);margin-top:2px">每天 15 分钟,一点点变厉害</div></div><div style="margin-left:auto;background:#fff;border-radius:14px;padding:6px 10px;font-size:12px;font-weight:700;color:#B26A1A;text-align:center;line-height:1.3;white-space:nowrap">连续打卡<b style="display:block;font-size:20px;color:var(--orange)">5 天</b></div></div>'

HCSS='''.today{margin:12px 16px 0;padding:12px 16px 14px;background:linear-gradient(135deg,#FF9A4D,#FF7A3D);color:#fff;border-radius:24px;box-shadow:0 5px 0 #E2622A}
.today .t{display:flex;justify-content:space-between;font-weight:800;font-size:16px}.today .t span{font-size:13px;font-weight:600}
.pbar{height:10px;border-radius:9px;background:rgba(255,255,255,.35);margin:8px 0 2px;overflow:hidden}.pbar i{display:block;height:100%;width:20%;background:#fff;border-radius:9px}
.stp{display:flex;margin-top:10px}.stp>div{flex:1;text-align:center;font-size:12px;font-weight:700;position:relative;line-height:1.35}
.stp b{display:flex;width:28px;height:28px;margin:0 auto 3px;border-radius:50%;background:rgba(255,255,255,.3);align-items:center;justify-content:center;font-size:14px}
.stp>div:not(:last-child):after{content:'';position:absolute;top:13px;left:calc(50% + 20px);right:calc(-50% + 20px);height:2px;background:rgba(255,255,255,.5)}
.stp .done b{background:#fff}.stp .cur b{background:#fff;color:#E2622A;box-shadow:0 0 0 4px rgba(255,255,255,.45)}.stp small{display:block;font-size:11px;font-weight:600;opacity:.92}
.go{margin-top:10px;background:#fff;color:#E2622A;border-radius:16px;text-align:center;padding:10px;font-weight:800;font-size:16px}
.st{display:flex;justify-content:space-between;align-items:baseline;padding:12px 20px 6px}.st b{font-size:17px}.st span{font-size:12px;color:var(--sub)}
.cat{margin:0 16px 8px;padding:8px 12px;display:flex;align-items:center;gap:12px;height:58px}
.cat .n{font-size:16px;font-weight:800}.cat .d{font-size:11.5px;color:var(--sub);margin-top:1px}
.soon{margin:0 16px;border:2.5px dashed #D9CDB8;border-radius:20px;padding:8px 12px;display:flex;align-items:center;gap:12px;color:#9A8B78;background:rgba(255,255,255,.55);height:58px}
.soon b{font-size:15px;display:block}.soon span.d{font-size:11.5px}'''
STEPS=[('done','','错题重考','3 分'),('cur','2','古诗词','5 分'),('','3','阅读理解','5 分'),('','4','快问快答','2 分')]
CATROWS=[('poem','填空闯关 · 一~五年级','今日主练','c-v1'),('dict','听读音 · 纸上写 · 自核','重考 2 词','c-learn'),('read','读短文 · 划出依据句才得分','今日主练','c-v1'),('idiom','接龙 + 选/说出意思','','' ),('lit','5 题 · 快问快答','今日加餐','c-got')]

def s_home():
    b=statusbar()+hdr_home()
    b+='<div class="today"><div class="t">今日 15 分钟计划<span>已完成 3 / 15 分钟</span></div><div class="pbar"><i></i></div><div class="stp">'
    for c,n,l,m in STEPS:
        b+=f'<div class="{c}"><b>{ck(16,"#FF8A3D") if c=="done" else n}</b>{l}<small>{m}</small></div>'
    b+='</div><div class="go">继续 · 古诗词《示儿》第 2 关</div></div>'
    b+='<div class="st"><b>五类练习</b><span>想多练哪个,就点哪个</span></div>'
    for k,d,chip,cc in CATROWS:
        g,col,n=CAT[k]
        b+=f'<div class="card cat"><div class="ic" style="background:{col}">{g}</div><div style="flex:1;min-width:0"><div class="n">{n}</div><div class="d">{d}</div></div>'+(f'<span class="chip {cc}">{chip}</span>' if chip else '<span style="color:var(--gray);font-size:22px">›</span>')+'</div>'
    b+='<div class="soon"><div class="ic" style="background:#D9CDB8">作</div><div style="flex:1;min-width:0"><b>表达习作素材积累</b><span class="d">好词好句、素材卡片</span></div><span class="chip c-next">即将上线</span></div>'
    b+=tabbar(0)+tag_demo()
    return page('01 新版首页',b,BASE+HCSS)

# ---------------- 听写 ----------------
def s_dict1():
    css=BASE+'''.hero{margin:12px 16px 0;padding:14px 16px 14px;text-align:center}
.spk{margin:10px auto 8px;width:124px;height:124px;border-radius:50%;background:linear-gradient(145deg,#6DB8FF,#4DA3FF);box-shadow:0 8px 0 #2F82E0,0 0 0 12px rgba(77,163,255,.16);display:flex;align-items:center;justify-content:center}
.two{display:flex;gap:10px;justify-content:center;margin-top:10px}.two div{height:42px;border-radius:15px;padding:0 16px;display:flex;align-items:center;font-size:14.5px;font-weight:800;background:#fff;color:#1E78D8;box-shadow:inset 0 0 0 2.5px #BFDDFF}
.paper{margin:12px 16px 0;padding:12px 16px 14px;background:#FFFDF6;border:2px dashed #E7D9BC;border-radius:22px}
.paper .l{display:flex;justify-content:space-between;font-size:13px;font-weight:800;margin-bottom:10px}.paper .l span{color:var(--sub);font-weight:600}
.sq{display:flex;gap:14px;justify-content:center}'''
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i style="width:50%"></i></div><div class="rt">3 / 6</div></div>'
    b+='<div class="ttl"><b>生字词听写</b><span>示例词语 · 非教材原表</span></div>'
    b+=f'<div class="card hero"><span class="chip c-und" style="background:#DCEEFF;color:#1E78D8">听读音 · 第 3 个词</span><div class="spk">{spk(64)}</div><div style="font-size:15px;font-weight:800">点一下,听这个词怎么读</div><div class="two"><div>再听一遍</div><div>慢速听</div></div><div style="font-size:12px;color:var(--sub);margin-top:9px">已听 1 次 · 读音来自手机系统语音</div></div>'
    b+=f'<div class="paper"><div class="l">写在你的本子上<span>(不用在屏幕上写)</span></div><div class="sq">{tianzi(92)}{tianzi(92)}</div><div style="text-align:center;font-size:12px;color:var(--sub);margin-top:8px">这个词一共 2 个字</div></div>'
    b+=f'<div class="say" style="margin:12px 16px 0">{mascot(48)}<div class="bub">听清楚,一笔一画写。<br>写好了再点下面的按钮。</div></div>'
    b+='<div class="cta or">我写好了 ›</div>'+tag_demo()
    return page('12 听写作答页',b,css)

def s_dict2():
    css=BASE+'''.info{padding:4px 20px 0;font-size:12.5px;color:var(--sub);line-height:1.5}
.r{margin:0 16px 8px;height:62px;padding:0 12px;display:flex;align-items:center;gap:10px}
.r .no{width:28px;height:28px;border-radius:50%;background:var(--gray2);color:var(--sub);font-weight:800;font-size:13px;display:flex;align-items:center;justify-content:center;flex:none}
.r .w{flex:1;min-width:0;display:flex;align-items:center;gap:8px}.r .w .p{font-size:11.5px;color:var(--sub);line-height:1.2}.r .w .k{font:400 28px/1.15 WenKai;letter-spacing:2px}
.tg{display:flex;gap:6px;flex:none}.tg div{width:44px;height:40px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:var(--gray2)}
.tg .g{background:var(--green);box-shadow:0 3px 0 #2A9A63}.tg .p{background:var(--pink);box-shadow:0 3px 0 #D63A5F}
.sum{position:absolute;left:16px;right:16px;bottom:92px;display:flex;gap:10px}.sum div{flex:1;text-align:center;height:38px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:800}'''
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i style="width:100%"></i></div><div class="rt">6 / 6</div></div>'
    b+='<div class="ttl"><b>自核:对照答案判分</b><span>示例词语</span></div>'
    b+='<div class="info" style="margin-bottom:8px">先看答案,再对照本子上写的:每个字都对才算“对”;写错了,点出错的字。</div>'
    W=[('珍惜','zhēn xī',1,''),('勇敢','yǒng gǎn',1,''),('灿烂','càn làn',0,'灿'),('观察','guān chá',1,''),('秘密','mì mì',0,'秘'),('温暖','wēn nuǎn',1,'')]
    for i,(w,p,ok,bad) in enumerate(W,1):
        chip=f'<span class="chip" style="background:var(--pink2);color:#D63A5F;flex:none">错字:{bad}</span>' if bad else ''
        b+=f'<div class="card r"><div class="no">{i}</div><div class="w"><div><div class="p">{p}</div><div class="k">{w}</div></div>{chip}</div><div class="tg"><div class="{"g" if ok else ""}">{ck(22,"#fff" if ok else "#B9B0A3")}</div><div class="{"" if ok else "p"}">{cr(20,"#B9B0A3" if ok else "#fff")}</div></div></div>'
    b+='<div class="sum"><div style="background:var(--green2);color:#1F9A5E">写对 4 个</div><div style="background:var(--pink2);color:#D63A5F">写错 2 个</div></div>'
    b+='<div class="cta or">完成自核 · 2 个错词进错题本</div>'+tag_demo()
    return page('13 听写自核页',b,css)

def s_dict3():
    css=BASE+'''.hero{margin:10px 16px 0;padding:12px 16px;display:flex;align-items:center;gap:14px}
.sec{margin:10px 16px 0;padding:10px 14px 12px}.sec h3{font-size:15px;font-weight:800;display:flex;justify-content:space-between;align-items:baseline}.sec h3 small{font-size:11.5px;color:var(--sub);font-weight:600}
.wr{display:flex;align-items:center;gap:10px;margin-top:8px;background:#FFF6E0;border-radius:14px;padding:6px 10px}.wr .k{font:400 26px WenKai;letter-spacing:2px}.wr .p{font-size:12px;color:var(--sub);flex:1}
.tl{display:flex;margin-top:12px}.tl>div{flex:1;text-align:center;font-size:12px;font-weight:700;position:relative;line-height:1.4}
.tl b{display:flex;width:30px;height:30px;margin:0 auto 4px;border-radius:50%;background:var(--gray2);color:var(--sub);align-items:center;justify-content:center;font-size:13px}
.tl small{display:block;font-size:10.5px;font-weight:600;color:var(--sub)}
.tl>div:not(:last-child):after{content:'';position:absolute;top:14px;left:calc(50% + 20px);right:calc(-50% + 20px);height:2px;background:var(--gray2)}
.tl .dn b{background:var(--green);color:#fff}.tl .nx b{background:var(--orange);color:#fff;box-shadow:0 0 0 4px rgba(255,138,61,.28)}.tl .nx{color:var(--orange)}
.ban{margin-top:8px;border:2.5px solid var(--orange);border-radius:18px;background:#fff;padding:9px 12px;display:flex;align-items:center;gap:10px}
.ban .ic{width:34px;height:34px;border-radius:11px;line-height:34px;font-size:19px;background:var(--orange)}.ban .go{margin-left:auto;background:var(--orange);color:#fff;font-size:12.5px;font-weight:800;border-radius:99px;padding:5px 11px;white-space:nowrap}'''
    b=statusbar()+'<div class="top"><div class="back">‹</div><div style="font-size:20px;font-weight:800">听写完成</div></div>'
    b+=f'<div class="card hero">{ring(67,74,"#4DA3FF",label="4 / 6",sw=9)}<div><div style="font-size:18px;font-weight:800">写对 4 个词,真棒!</div><div style="font-size:12.5px;color:var(--sub);margin-top:4px;line-height:1.5">错的 2 个词不用担心,<br>隔天再写一次,就记牢啦。</div></div></div>'
    b+='<div class="card sec"><h3>已自动加入错题本<small>2 个词</small></h3>'
    b+='<div class="wr"><span class="k">灿烂</span><span class="p">càn làn</span><span class="chip" style="background:var(--pink2);color:#D63A5F">错字:灿</span></div>'
    b+='<div class="wr"><span class="k">秘密</span><span class="p">mì mì</span><span class="chip" style="background:var(--pink2);color:#D63A5F">错字:秘</span></div></div>'
    b+='<div class="card sec"><h3>重考安排<small>示例日期</small></h3><div class="tl"><div class="dn"><b>'+ck(16)+'</b>今天听写<small>10月1日 周四</small></div><div class="nx"><b>1</b>隔天重考<small>明天 10月2日</small></div><div><b>2</b>3 天后<small>10月4日 周日</small></div><div><b>3</b>7 天后<small>10月8日 周四</small></div></div><div style="font-size:11.5px;color:var(--sub);margin-top:8px;text-align:center">连续 3 次都写对,就从错题本“毕业”</div></div>'
    b+='<div class="card sec"><h3>明天打开会这样提醒你<small>首页顶部</small></h3><div class="ban"><div class="ic">错</div><div style="font-size:13px;font-weight:800;line-height:1.4">今天有 2 个词要重考<br><span style="font-weight:500;color:var(--sub);font-size:11.5px">隔天重考 · 约 1 分钟</span></div><div class="go">去重考</div></div>'
    b+='<div style="font-size:11.5px;color:var(--sub);margin-top:8px;line-height:1.5">网页版不能像原生 App 那样在后台弹通知,所以提醒放在首页;也可以下载日历提醒(.ics)。</div></div>'
    b+='<div style="position:absolute;left:16px;right:16px;bottom:90px;display:flex;gap:10px"><div class="btn wh" style="flex:1;height:46px;font-size:15px;box-shadow:inset 0 0 0 2.5px var(--orange2)">下载日历提醒</div></div>'
    b+='<div class="cta or">回到首页</div>'+tag_demo()
    return page('14 听写错题隔天重考提醒页',b,css)

# ---------------- 阅读理解 ----------------
SENT=['清晨,小林走到楼下,发现花坛里的牵牛花开了。','昨天傍晚,它还只是紧紧闭着的花苞。','他蹲下来仔细看,花瓣上挂着亮晶晶的露珠。','奶奶说,牵牛花大多在清晨开放,太阳升高以后就慢慢合拢了。','小林想把花开的样子画下来,决定明天再早一点起床。']
def s_read1():
    css=BASE+'''.pass{margin:8px 16px 0;padding:12px 14px 12px;position:relative}
.pass h2{font:400 21px WenKai;text-align:center}.pass .sub{text-align:center;font-size:11.5px;color:var(--sub);margin:2px 0 8px}
.pass p{font:400 18px/34px WenKai;text-align:justify}
.sn{border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone;padding:2px 1px}
.no{display:inline-block;width:16px;height:16px;border-radius:50%;background:var(--gray2);color:var(--sub);font:700 10px/16px 'Noto Sans CJK SC';text-align:center;vertical-align:3px;margin-right:2px;font-style:normal}
.sn.sel{background:#FFE477;box-shadow:0 2px 0 #F0B62A}.sn.sel .no{background:var(--orange);color:#fff}
.q{margin:10px 16px 0;padding:11px 14px 12px}.q .h{font-size:15px;font-weight:800;line-height:1.45}
.q .o{display:flex;gap:8px;margin-top:9px}.q .o div{flex:1;height:38px;border-radius:13px;background:var(--gray2);display:flex;align-items:center;justify-content:center;font-size:14.5px;font-weight:800;color:var(--sub)}
.q .o .on{background:var(--blue2);color:#1E78D8;box-shadow:inset 0 0 0 2.5px var(--blue)}
.rule{margin:10px 16px 0;padding:8px 12px;border-radius:16px;background:var(--yellow2);color:#8A6200;font-size:12.5px;font-weight:700;line-height:1.45;display:flex;gap:10px;align-items:center}
.two{position:absolute;left:16px;right:16px;bottom:22px;display:flex;gap:10px}.two .btn{height:56px;font-size:19px}'''
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i style="width:25%"></i></div><div class="rt">第 1 / 2 题</div></div>'
    b+='<div class="ttl"><b>阅读 · 找依据</b><span class="chip c-und" style="background:#FFF1C4;color:#B98100">示例文本 · 原创</span></div>'
    p=''
    for i,s in enumerate(SENT,1):
        p+=f'<span class="sn{" sel" if i in (1,4) else ""}"><i class="no">{i}</i>{s}</span>'
    b+=f'<div class="card pass"><h2>清晨的牵牛花</h2><div class="sub">原创示例短文 · 点一句就划上,再点取消</div><p>{p}</p></div>'
    b+='<div class="card q"><div class="h">问题:牵牛花一般在什么时候开放?</div><div class="o"><div class="on">A 清晨</div><div>B 中午</div><div>C 傍晚</div></div></div>'
    b+='<div class="rule">'+lk(20,'#B98100')+'<span>先划出依据句,再提交,才能得分。已划 2 句(第 1、4 句)</span></div>'
    b+='<div class="two"><div class="btn wh" style="width:112px;box-shadow:inset 0 0 0 2.5px var(--orange2)">清除</div><div class="btn gn" style="flex:1">提交答案</div></div>'+tag_demo()
    return page('15 阅读理解划句作答页',b,css)

def s_read2():
    css=BASE+'''.sc{margin:8px 16px 0;padding:10px 16px;display:flex;align-items:center;gap:14px}
.rw{margin:8px 0 0;padding:7px 10px;border-radius:14px;font:400 15px/25px WenKai;display:flex;gap:8px;align-items:flex-start;background:#F7F3EA;color:#8C7B6B}
.rw .no{width:18px;height:18px;border-radius:50%;background:#fff;font:700 11px/18px 'Noto Sans CJK SC';text-align:center;flex:none;margin-top:3px;color:var(--sub)}
.rw .tg{display:block;font:700 11.5px 'Noto Sans CJK SC';margin-top:2px}
.rw.ok{background:var(--green2);color:#256B47;box-shadow:inset 0 0 0 2.5px var(--green)}.rw.ok .no{background:var(--green);color:#fff}
.rw.bad{background:var(--pink2);color:#8E2C46;box-shadow:inset 0 0 0 2.5px var(--pink)}.rw.bad .no{background:var(--pink);color:#fff}
.bk{margin:8px 16px 0;padding:9px 14px}.bk h3{font-size:14px;font-weight:800;margin-bottom:5px}
.li{display:flex;justify-content:space-between;font-size:13px;padding:3px 0;align-items:center}.li b{font-weight:800}
.ex{margin:8px 16px 0;padding:9px 12px;border-radius:16px;background:#fff;font-size:12.5px;line-height:1.55;color:#5B4A3A;box-shadow:inset 0 0 0 2px #EADFCB}
.two{position:absolute;left:16px;right:16px;bottom:22px;display:flex;gap:10px}.two .btn{height:54px;font-size:18px}'''
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i style="width:50%"></i></div><div class="rt">第 1 / 2 题</div></div>'
    b+=f'<div class="card sc">{ring(67,70,"#3FBF7F",label="2/3",sw=9)}<div><div style="font-size:18px;font-weight:800">找到了依据,还多划了一句</div><div style="margin-top:5px">{stars(2,3,22)}</div></div></div>'
    rows=[('bad','多划了','这句只说了“今天”花开了,不能说明“一般”什么时候开'),('','',''),('','',''),('ok','标准依据句 · 你划到了',''),('','','')]
    b+='<div class="card" style="margin:8px 16px 0;padding:8px 12px 10px"><div style="font-size:13px;font-weight:800">原文(标出了标准依据)<span style="font-weight:600;color:var(--sub);font-size:11.5px">　示例文本 · 原创</span></div>'
    for i,s in enumerate(SENT,1):
        cls,tg,_=rows[i-1]
        tgh=f'<span class="tg" style="color:{"#1F9A5E" if cls=="ok" else "#D63A5F"}">{tg}</span>' if tg else ''
        b+=f'<div class="rw {cls}"><i class="no">{i}</i><div>{s}{tgh}</div></div>'
    b+='</div>'
    b+='<div class="card bk"><h3>得分明细(满分 3 分)</h3><div class="li"><span>选对答案:A 清晨</span><b style="color:#1F9A5E">+1</b></div><div class="li"><span>划到标准依据句(第 4 句)</span><b style="color:#1F9A5E">+1</b></div><div class="li"><span>没有多划无关句(多划了第 1 句)</span><b style="color:#D63A5F">+0</b></div></div>'
    b+='<div class="ex"><b>为什么是第 4 句?</b>它直接写了牵牛花“大多在清晨开放”;第 1 句只是今天清晨花开了。未满分已进错题本,明天再练。</div>'
    b+='<div class="two"><div class="btn wh" style="flex:1;color:var(--pink);box-shadow:inset 0 0 0 2.5px #F5C2CD">看错题本</div><div class="btn gn" style="flex:1">下一题 ›</div></div>'+tag_demo()
    return page('16 阅读理解得分反馈页',b,css)

# ---------------- 成语 ----------------
def idiom_boxes(txt,cls='',fs=28,w=40):
    return ''.join(f'<span class="bx {cls}" style="width:{w}px;height:{w+6}px;font-size:{fs}px">{c}</span>' for c in txt)
IDCSS=BASE+'''.seg{margin:8px 16px 0;display:flex;background:var(--gray2);border-radius:16px;padding:4px}.seg div{flex:1;text-align:center;padding:7px 0;font-weight:800;font-size:14px;border-radius:12px;color:var(--sub)}.seg .on{background:#fff;color:var(--ink);box-shadow:0 2px 0 rgba(0,0,0,.08)}
.bx{display:inline-flex;align-items:center;justify-content:center;border-radius:11px;background:#fff;font-family:WenKai;box-shadow:0 3px 0 #E6DDCC;margin-right:5px}
.bx.hl{background:var(--purple2);color:#6A57E0;box-shadow:0 3px 0 #C9C1FF}.bx.em{background:var(--yellow2);border:3px dashed var(--orange);box-shadow:none}
.bx.gg{background:var(--green2);color:#1F9A5E;box-shadow:0 3px 0 #BDEBD0}.bx.rr{background:var(--pink2);color:#D63A5F;box-shadow:0 3px 0 #F5C2CD}
.lk{margin:8px 16px 0;padding:8px 12px;display:flex;align-items:center;gap:10px}.lk .m{font-size:12px;color:var(--sub);line-height:1.4;flex:1}
.lk .n{width:24px;height:24px;border-radius:50%;background:var(--green);display:flex;align-items:center;justify-content:center;flex:none}
.arw{text-align:center;color:var(--purple);font-size:12px;font-weight:800;margin-top:4px}
.sc{margin:8px 16px 0;padding:10px 12px 12px}.sc h3{font-size:14.5px;font-weight:800;display:flex;align-items:center;gap:8px}.sc h3 i{font-style:normal;width:22px;height:22px;border-radius:50%;background:var(--purple);color:#fff;font-size:12px;display:flex;align-items:center;justify-content:center}
.ch{display:flex;gap:8px;margin-top:9px}.ch div{flex:1;height:42px;border-radius:14px;background:var(--gray2);display:flex;align-items:center;justify-content:center;font:400 17px WenKai;color:var(--ink)}
.ch .on{background:var(--green2);box-shadow:inset 0 0 0 2.5px var(--green);color:#1F9A5E}
.mo{margin-top:7px;min-height:42px;border-radius:14px;background:var(--gray2);padding:6px 12px;display:flex;gap:9px;align-items:center;font-size:13px;font-weight:700;line-height:1.35}.mo b{width:22px;height:22px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;flex:none;color:var(--sub)}
.mo.gg{background:var(--green2);box-shadow:inset 0 0 0 2.5px var(--green);color:#1F6B47}.mo.gg b{background:var(--green);color:#fff}.mo.rr{background:var(--pink2);box-shadow:inset 0 0 0 2.5px var(--pink);color:#8E2C46}.mo.rr b{background:var(--pink);color:#fff}
'''
MEAN=[('A','下定决心,努力谋求强盛'),('B','遇到困难就马上放弃'),('C','心里很生气,大声发脾气')]
def s_idiom1():
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i style="width:40%;background:var(--purple)"></i></div><div class="rt">已接 2 个</div></div>'
    b+='<div class="ttl"><b>成语接龙</b><span>示例题</span></div><div class="seg"><div class="on">接龙 + 释义</div><div>近义词</div></div>'
    b+=f'<div class="card lk"><div class="n">{ck(14)}</div><div>{idiom_boxes("一心一意","",22,32)}</div><div class="m">心思专一,没有别的想法</div></div>'
    b+='<div class="arw">最后一个字“意”接下一个的第一个字 ↓</div>'
    b+=f'<div class="card lk" style="margin-top:4px"><div class="n">{ck(14)}</div><div>{idiom_boxes("意气风发","",22,32)}</div><div class="m">精神振奋,气概昂扬</div></div>'
    b+=f'<div class="card sc"><h3><i>1</i>接词:选一个以“发”开头的成语</h3><div style="margin-top:8px">{idiom_boxes("发","hl",26,40)}<span class="bx em" style="width:40px;height:46px"></span><span class="bx em" style="width:40px;height:46px"></span><span class="bx em" style="width:40px;height:46px"></span></div><div class="ch"><div style="font-size:15px" class="on">发愤图强</div><div style="font-size:15px">发人深省</div><div style="font-size:15px">发扬光大</div></div></div>'
    b+='<div class="card sc" style="opacity:.98"><h3><i>2</i>选意思:“发愤图强”是什么意思?</h3>'
    for k,t in MEAN: b+=f'<div class="mo"><b>{k}</b>{t}</div>'
    b+='<div style="margin-top:8px;text-align:center;font-size:13px;font-weight:800;color:var(--purple)">想自己说?点这里说给家长听 › 家长点“对/不对”</div></div>'
    b+='<div class="cta gy">确 定</div>'+tag_demo()
    return page('17 成语接龙作答页',b,IDCSS)

def s_idiom2():
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i style="width:60%;background:var(--purple)"></i></div><div class="rt">已接 3 个</div></div>'
    b+='<div class="ttl"><b>释义反馈</b><span>示例题</span></div>'
    b+='<div style="display:flex;gap:10px;margin:10px 16px 0"><div class="card" style="flex:1;padding:9px 10px;display:flex;gap:8px;align-items:center;font-size:13px;font-weight:800;color:#1F9A5E"><span style="width:26px;height:26px;border-radius:50%;background:var(--green);display:flex;align-items:center;justify-content:center;flex:none">'+ck(15)+'</span>接词对了</div><div class="card" style="flex:1;padding:9px 10px;display:flex;gap:8px;align-items:center;font-size:13px;font-weight:800;color:#D63A5F"><span style="width:26px;height:26px;border-radius:50%;background:var(--pink);display:flex;align-items:center;justify-content:center;flex:none">'+cr(14)+'</span>意思差一点</div></div>'
    b+=f'<div class="card sc" style="margin-top:10px"><h3>你选的意思</h3><div class="mo rr"><b>C</b>心里很生气,大声发脾气</div><div style="font-size:12px;color:var(--sub);margin-top:6px">这里的“发”不是“发脾气”,是“奋起、努力”的意思。</div></div>'
    b+=f'<div class="card sc" style="background:#fff"><div style="text-align:center">{idiom_boxes("发愤图强","gg",30,46)}</div><div class="mo gg" style="margin-top:10px"><b>A</b>正确意思:下定决心,努力谋求强盛</div><div style="margin-top:9px;font-size:13px;line-height:1.6"><b style="color:#6A57E0">例句(原创)</b>:他发愤图强,每天坚持练习,终于跟上了大家。</div><div style="margin-top:6px;font-size:13px"><b style="color:#6A57E0">近义成语</b>:奋发图强</div></div>'
    b+='<div class="card" style="margin:8px 16px 0;padding:9px 12px;display:flex;align-items:center;gap:10px;font-size:13.5px;font-weight:700"><span style="width:28px;height:28px;border-radius:9px;background:var(--orange);color:#fff;font:400 16px/28px WenKai;text-align:center;flex:none">错</span><span style="flex:1">“发愤图强”的意思已加入错题本<br><small style="font-weight:500;color:var(--sub)">明天、3 天后、7 天后再考</small></span></div>'
    b+='<div class="cta pu">接下一个:以“强”开头 ›</div>'+tag_demo()
    return page('18 成语释义反馈页',b,IDCSS)

# ---------------- 文学常识 ----------------
LCSS=BASE+'''.dots{display:flex;gap:6px;justify-content:center;margin-top:10px}.dots i{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--gray2);font-style:normal;font-size:12px;font-weight:800;color:var(--sub)}
.dots .g{background:var(--green)}.dots .p{background:var(--pink)}.dots .c{background:#fff;box-shadow:0 0 0 3px var(--orange);color:var(--orange)}
.qc{margin:14px 16px 0;padding:18px 16px 20px;text-align:center;background:linear-gradient(160deg,#FFEAF0,#fff 60%);position:relative}
.qc .k{font:400 30px/1.5 WenKai;margin-top:12px}
.opt{position:absolute;left:16px;right:16px;display:flex;flex-direction:column;gap:10px}
.opt div{height:56px;border-radius:18px;background:#fff;box-shadow:0 5px 0 #E6DDCC;display:flex;align-items:center;gap:12px;padding:0 16px;font:400 24px WenKai}
.opt div b{width:30px;height:30px;border-radius:50%;background:var(--gray2);color:var(--sub);font:800 14px 'Noto Sans CJK SC';display:flex;align-items:center;justify-content:center}
.opt .on{background:var(--pink2);box-shadow:inset 0 0 0 3px var(--pink),0 5px 0 #F5C2CD}.opt .on b{background:var(--pink);color:#fff}
.tm{display:flex;align-items:center;gap:6px;background:#fff;border-radius:99px;padding:4px 10px;font-size:13px;font-weight:800;color:var(--pink);flex:none}
'''
def s_lit1():
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i style="width:40%;background:var(--pink)"></i></div><div class="tm">5 秒</div></div>'
    b+='<div class="ttl"><b>快问快答</b><span>五年级水平 · 示例题</span></div>'
    b+='<div class="dots"><i class="g">'+ck(14)+'</i><i class="g">'+ck(14)+'</i><i class="c">3</i><i>4</i><i>5</i></div>'
    b+='<div class="card qc"><span class="chip" style="background:var(--pink2);color:#D63A5F">第 3 题 · 作者</span><div class="k">《西游记》的作者是谁?</div></div>'
    b+='<div class="opt" style="top:330px">'
    for k,t,on in [('A','施耐庵',0),('B','吴承恩',1),('C','罗贯中',0),('D','曹雪芹',0)]:
        b+=f'<div class="{"on" if on else ""}"><b>{k}</b>{t}</div>'
    b+='</div>'
    b+=f'<div class="say" style="position:absolute;left:16px;right:16px;bottom:74px">{mascot(46)}<div class="bub">点一下就提交,不用按确认。拿不准可以先跳过。</div></div>'
    b+='<div style="position:absolute;left:0;right:0;bottom:30px;text-align:center;font-size:14px;font-weight:800;color:var(--sub)">跳过,留到最后 ›</div>'+tag_demo()
    return page('19 文学常识答题页',b,LCSS)

def s_lit2():
    css=LCSS+'''.rr{margin:0 0 8px;padding:8px 12px;display:flex;align-items:center;gap:10px;min-height:52px}.rr .no{width:24px;height:24px;border-radius:50%;background:var(--gray2);font-size:12px;font-weight:800;color:var(--sub);display:flex;align-items:center;justify-content:center;flex:none}
.rr .t{flex:1;min-width:0;font-size:13.5px;font-weight:700;line-height:1.35}.rr .t small{display:block;font:400 15px WenKai;color:#1F9A5E;margin-top:1px}.rr .t small.b{color:#D63A5F}
.rr .m{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none}'''
    b=statusbar()+'<div class="top"><div class="x">×</div><div class="pb"><i style="width:100%;background:var(--pink)"></i></div><div class="rt">5 / 5</div></div>'
    b+=f'<div class="card" style="margin:10px 16px 0;padding:10px 16px;display:flex;align-items:center;gap:14px">{ring(80,74,"#FF6B8B",label="4 / 5",sw=9)}<div><div style="font-size:18px;font-weight:800">快问快答完成!</div><div style="margin-top:4px">{stars(2,3,22)}</div><div style="font-size:12px;color:var(--sub);margin-top:3px">用时 58 秒(示例)</div></div></div>'
    b+='<div style="margin:10px 16px 0">'
    R=[('“诗仙”指的是哪位诗人?','李白',1),('《论语》主要记录了谁和弟子的言行?','孔子',1),('《西游记》的作者是谁?','吴承恩',1),('《朝花夕拾》的作者是谁?','正确答案:鲁迅　你选了:巴金',0),('“诗圣”指的是哪位诗人?','杜甫',1)]
    for i,(q,a,ok) in enumerate(R,1):
        m=f'<div class="m" style="background:var(--green)">{ck(16)}</div>' if ok else f'<div class="m" style="background:var(--pink)">{cr(15)}</div>'
        b+=f'<div class="card rr"><div class="no">{i}</div><div class="t">{q}<small class="{"" if ok else "b"}">{a}</small></div>{m}</div>'
    b+='</div>'
    b+='<div class="card" style="margin:0 16px;padding:9px 14px;font-size:12.5px;line-height:1.55"><b style="color:#D63A5F">知识小卡</b>:《朝花夕拾》是鲁迅创作的回忆性散文集。答错的 1 题已加入错题本,明天再考。</div>'
    b+='<div style="position:absolute;left:16px;right:16px;bottom:22px;display:flex;gap:10px"><div class="btn wh" style="flex:1;height:56px;box-shadow:inset 0 0 0 2.5px var(--orange2);font-size:17px">再来一组</div><div class="btn pk" style="flex:1;height:56px;font-size:17px">回到首页</div></div>'+tag_demo()
    return page('20 文学常识结果页',b,css)
