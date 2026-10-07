# 找到你的灵魂乐器

一个移动端优先的单页测试：24 道题，从全世界 21 件乐器里找到那件「替你说话」的。
附水彩插画、真实演奏音频与可分享的结果卡。

## 本地预览

纯静态，**没有任何构建步骤，也不依赖后端**。两种方式都能跑：

```bash
# 方式一：直接双击 index.html 用浏览器打开（可以，页面不使用 fetch）
# 方式二：起个本地服务（推荐，和线上行为一致）
python3 -m http.server 8000
# 然后打开 http://localhost:8000
```

## 部署到 GitHub Pages

1. 新建一个仓库（**Public**，否则 Pages 需要付费方案）。
2. 把本目录**全部内容**（包括隐藏文件 `.nojekyll`）推上去，放在仓库根目录。
3. 仓库 → **Settings** → **Pages**：
   - Source 选 **Deploy from a branch**
   - Branch 选 **main**，目录选 **`/ (root)`** ← **不要选 `/docs`**
4. 等 1–2 分钟，站点地址是 `https://<用户名>.github.io/<仓库名>`

### 部署后补一步：让分享有预览图

`index.html` 里的分享预览图地址用了占位符，因为它必须是绝对 URL。
替换成你的实际地址（在仓库目录执行）：

```bash
# macOS
sed -i '' 's|__SITE_URL__|https://你的用户名.github.io/仓库名|g' index.html
# Linux
sed -i    's|__SITE_URL__|https://你的用户名.github.io/仓库名|g' index.html
```

然后重新提交。这样在微信/微博里转发时会显示标题、简介和那张分享卡图。

## 目录结构

```
index.html          全部结构 + 样式 + 逻辑（单文件，24 KB）
data.js             21 件乐器数据 + 24 道题 + 音频清单（40 KB）
img/
  <id>.jpg          结果页海报 600x800
  <id>_t.jpg        图鉴缩略图 240x240
audio/
  <id>.m4a          AAC，iOS 优先
  <id>.mp3          兜底格式
assets/
  bg-instruments.jpg  首页线描底图
  share-card.jpg      社交分享预览图 1200x630
.nojekyll           告诉 GitHub Pages 不要跑 Jekyll
CREDITS.md          素材来源与授权（CC BY 要求署名，请勿删除）
project-docs/       设计文档与构建脚本（不参与页面运行）
```

## 体积

| 项 | 大小 |
|---|---|
| 首屏（index.html + data.js + 首页底图） | **229 KB** |
| 进结果页再加载 1 张海报 | +24 KB |
| 点播放再加载 1 条音频 | +83 KB |
| 进图鉴再加载 21 张缩略图 | +104 KB |
| 仓库总计 | 约 4.4 MB |

音频用 `preload="none"`，不点播放不会下载。

## 兼容性

- 移动端优先，iOS Safari / Android Chrome / 微信内置浏览器实测可用
- 音频按 `canPlayType` 能力检测在 m4a / mp3 间自动选择，不做 UA 嗅探
- 浏览器拦截自动播放时只停止播放、保留按钮，不会让按钮消失

## 授权

素材授权见 [CREDITS.md](CREDITS.md)。**音频多数为 CC BY / CC BY-SA，署名不可移除。**
