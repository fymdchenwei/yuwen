# -*- coding: utf-8 -*-
HEAD = '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t}</title><link rel="stylesheet" href="common.css"><style>{css}</style></head><body>'
def page(title, body, css='', land=False):
    return HEAD.format(t=title, css=css) + f'<div class="phone{" land" if land else ""}">{body}</div></body></html>'

def statusbar():
    return '<div class="sb"><span>9:41</span><span class="r"><span class="sig"><i style="height:4px"></i><i style="height:6px"></i><i style="height:8px"></i><i style="height:11px"></i></span><span class="bat"></span></span></div>'

def tabbar(on=0):
    items=[('首','首页'),('闯','闯关'),('错','错题本'),('我','我的')]
    s='<div class="tab">'
    for i,(g,n) in enumerate(items):
        cls=('on ' if i==on else '')+('dot' if i==2 else '')
        s+=f'<div class="{cls}"><b>{g}</b>{n}</div>'
    return s+'</div>'

CHECK='<svg width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="{c}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CROSS='<svg width="{s}" height="{s}" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="{c}" stroke-width="3.6" stroke-linecap="round"/></svg>'
LOCK='<svg width="{s}" height="{s}" viewBox="0 0 24 24"><rect x="5" y="10.5" width="14" height="10" rx="3" fill="{c}"/><path d="M8 10.5V8a4 4 0 018 0v2.5" fill="none" stroke="{c}" stroke-width="2.6" stroke-linecap="round"/></svg>'
def ck(s=20,c='#fff'): return CHECK.format(s=s,c=c)
def cr(s=20,c='#fff'): return CROSS.format(s=s,c=c)
def lk(s=20,c='#fff'): return LOCK.format(s=s,c=c)
def stars(n,total=3,sz=18):
    return ''.join(f'<i class="star{"" if i<n else " off"}" style="width:{sz}px;height:{sz}px"></i>' for i in range(total))

def mascot(size=64, mood='happy'):
    mouth = ('<i style="position:absolute;left:36%;top:60%;width:28%;height:14%;border-bottom:3px solid #7a4a2a;border-radius:0 0 20px 20px"></i>' if mood=='happy'
             else '<i style="position:absolute;left:40%;top:66%;width:20%;height:12%;border-top:3px solid #7a4a2a;border-radius:20px 20px 0 0"></i>')
    return f'''<div style="width:{size}px;height:{size}px;position:relative;flex:none">
<i style="position:absolute;left:8%;top:-4%;width:84%;height:22%;background:#3B2F2F;border-radius:6px"></i>
<i style="position:absolute;left:-2%;top:9%;width:104%;height:10%;background:#3B2F2F;border-radius:4px"></i>
<div style="position:absolute;left:4%;top:16%;width:92%;height:82%;background:linear-gradient(#FFD25E,#FFBE3D);border-radius:50%;box-shadow:0 3px 0 #E59A1D"></div>
<i style="position:absolute;left:28%;top:44%;width:9%;height:14%;background:#3B2F2F;border-radius:50%"></i>
<i style="position:absolute;left:63%;top:44%;width:9%;height:14%;background:#3B2F2F;border-radius:50%"></i>
<i style="position:absolute;left:16%;top:58%;width:15%;height:10%;background:#FF9DB0;border-radius:50%;opacity:.8"></i>
<i style="position:absolute;left:69%;top:58%;width:15%;height:10%;background:#FF9DB0;border-radius:50%;opacity:.8"></i>{mouth}</div>'''

def moon(size=90):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 100 100"><circle cx="50" cy="50" r="34" fill="#FFF3B0"/><circle cx="62" cy="42" r="30" fill="#FFCB47" opacity="0"/><path d="M62 20a32 32 0 1 0 14 52A26 26 0 0 1 62 20z" fill="#FFD84D"/><circle cx="44" cy="52" r="3" fill="#F0B62A"/><circle cx="52" cy="66" r="4.5" fill="#F0B62A"/></svg>'

def ring(pct, size=76, color='#3FBF7F', track='#EFEAE2', label='', sw=9):
    r=(size-sw)/2; c=2*3.14159*r
    return f'''<div style="position:relative;width:{size}px;height:{size}px"><svg width="{size}" height="{size}" style="transform:rotate(-90deg)"><circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{track}" stroke-width="{sw}"/><circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-dasharray="{c*pct/100} {c}"/></svg><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:{size*0.24}px;color:{color}">{label or str(pct)+'%'}</div></div>'''

def tag_demo(): return '<div class="note">示例数据 · 仅为设计示意</div>'


def rail(on=0):
    items=[('首','首页'),('闯','闯关'),('错','错题本'),('我','我的')]
    s='<div class="rail">'
    for i,(g,n) in enumerate(items):
        s+=f'<div class="{"on" if i==on else ""}"><b>{g}</b>{n}</div>'
    return s+'</div>'
