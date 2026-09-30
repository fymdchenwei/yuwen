# -*- coding: utf-8 -*-
import sys,os,asyncio
sys.path.insert(0,os.path.dirname(__file__))
import s1,s2,s3,s4,s5,s6,s7
OUT='/workspace/mockup-full'
# (分组, 文件名, 生成函数)
P=[('通用','H1-新版首页',s5.s_home),('通用','H2-错题本',s6.s_mist),('通用','H3-总进度与徽章总览',s6.s_prog),('通用','H4-添加到主屏幕引导',s6.s_a2hs),
('古诗词','P00-练习项分类总览',s1.s00),('古诗词','P01-古诗词练习项入口',s1.s01),('古诗词','P02-年级与诗目-五年级',s1.s02),('古诗词','P03-年级与诗目-三年级含未核实',s1.s03),('古诗词','P04-闯关关卡路径',s2.s04),('古诗词','P05-填空作答中',s2.s05),('古诗词','P06-答对反馈',s2.s06),('古诗词','P07-答错反馈-加入错题本',s2.s07),('古诗词','P08-通关徽章弹窗',s3.s08),('古诗词','P09-徽章墙',s3.s09),('古诗词','P10-进度可视化',s4.s10),
('生字词听写','D1-听写作答页',s5.s_dict1),('生字词听写','D2-自核页',s5.s_dict2),('生字词听写','D3-错题隔天重考提醒页',s5.s_dict3),
('阅读理解找证据','R1-划句作答页',s5.s_read1),('阅读理解找证据','R2-得分反馈页',s5.s_read2),
('成语与近义词','I1-接龙作答页',s5.s_idiom1),('成语与近义词','I2-释义反馈页',s5.s_idiom2),
('文学常识速问','L1-答题页',s5.s_lit1),('文学常识速问','L2-结果页',s5.s_lit2)]
L=[('横版','LS1-首页',s7.l_home),('横版','LS2-古诗词填空作答页',s7.l_fill),('横版','LS3-闯关路径页',s7.l_path),('横版','LS4-阅读理解划句页',s7.l_read),('横版','LS5-进度与徽章页',s7.l_prog)]
def run():
    JS=open(os.path.join(os.path.dirname(__file__),'check.js')).read()
    for g,n,f in P+L: open(f'{OUT}/html/{n}.html','w',encoding='utf-8').write(f())
    import subprocess
    subprocess.check_call(['/workspace/venv-pw/bin/python',os.path.join(os.path.dirname(__file__),'subset.py')])
    from playwright.async_api import async_playwright
    async def main():
        async with async_playwright() as p:
            br=await p.chromium.launch()
            for lst,sub,vw,vh in [(P,'portrait',390,844),(L,'landscape',844,390)]:
                pg=await br.new_page(viewport={'width':vw,'height':vh},device_scale_factor=2)
                for g,n,_ in lst:
                    await pg.goto(f'file://{OUT}/html/{n}.html'); await pg.wait_for_timeout(300)
                    await pg.locator('.phone').screenshot(path=f'{OUT}/png/{sub}/{n}.png')
                    r=await pg.evaluate(JS)
                    print(n,r if r else 'OK')
            await br.close()
    asyncio.run(main())

if __name__=='__main__': run()
