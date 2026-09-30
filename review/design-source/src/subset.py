# -*- coding: utf-8 -*-
# 从完整霞鹜文楷中按实际用字裁剪子集(OFL)。用法:先生成 html,再运行本脚本。
import glob,subprocess,sys
OUT='/workspace/mockup-full'
chars=set()
for f in glob.glob(OUT+'/html/*.html'): chars|=set(open(f,encoding='utf-8').read())
chars|=set('0123456789,.:;()[]<>/-~·、。,;:!?“”‘’《》〔〕 ')
open('/tmp/chars.txt','w',encoding='utf-8').write(''.join(sorted(chars)))
subprocess.check_call(['/workspace/venv-pw/bin/pyftsubset','/workspace/fonts/LXGWWenKai-Regular-v1.510.ttf','--text-file=/tmp/chars.txt','--output-file='+OUT+'/fonts/wenkai-subset.ttf','--layout-features=*'])
