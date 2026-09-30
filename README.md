# 每日 15 分钟 · 语文学习

站点首页就是学习应用（古诗词闯关、错题本、徽章、离线）。效果图评审页移到了 `review/`。

- 学习应用：<https://fymdchenwei.github.io/yuwen/>
- 效果图评审：<https://fymdchenwei.github.io/yuwen/review/>
- 旧地址 <https://fymdchenwei.github.io/yuwen/app/> 会跳回首页

应用里的连续天数、进度和得分只来自这台设备上的真实练习，新用户从 0 开始。效果图里的数字仍是示例。

## 目录

- `index.html`、`js/`、`css/`、`data/`、`icons/`、`manifest.webmanifest`、`sw.js`：学习应用
- `app/`：旧地址跳转页，以及给已安装旧版的更新用 Service Worker
- `review/`：效果图、设计说明和生成效果图时用的源文件

`review/design-source/fonts/wenkai-subset.ttf` 是霞鹜文楷（LXGW WenKai）按效果图用字裁出的子集，字体许可为 OFL。学习应用本身不加载这个字体，离线时用系统中文字体。
