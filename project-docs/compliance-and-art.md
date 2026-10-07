# 声之肖像 · 文化合规清单与生图规范

---

## 第一部分：文化合规

### 1.1 筛选原则

你提出的要求是"不要有对现代主流文化有冲突的文化意味"。我把这条拆成四个可操作的排除标准：

| # | 标准 | 说明 |
|---|---|---|
| **A** | **无性别禁忌** | 存在"女性不可演奏/触碰"传统的乐器一律排除。测试面向所有人，不能给任何用户一个"你不该拥有这件乐器"的结果 |
| **B** | **非宗教/召灵圣器** | 核心功能是通灵、召唤祖灵、萨满仪式的乐器排除。把圣器做成"性格测试奖品"是轻慢 |
| **C** | **无种姓/世袭门槛** | 演奏权限被世袭阶层垄断的乐器排除，或需谨慎处理 |
| **D** | **无政治/族群敏感归属** | 存在主权争议、族群归属争议的乐器排除，避免产地标注引发争端 |

### 1.2 已排除的乐器及依据

这些都是"看起来很适合、但实际有雷"的候选，我逐一核查后剔除：

| 乐器 | 排除依据 | 触发标准 |
|---|---|---|
| **迪吉里杜管**<br>Didgeridoo | 澳大利亚部分原住民社区（尤其东南部）明确禁止女性及非原住民演奏甚至触碰，视为"文化盗窃"。2008 年 HarperCollins 因在《The Daring Book for Girls》中鼓励女孩演奏而公开道歉，原住民学者 Mark Rose 称之为"极端的文化不敏感" | **A + B** |
| **姆比拉**<br>Mbira dzavadzimu | 名字直译即"祖灵之琴"。核心用途是 bira 通宵召灵仪式，音乐用于帮助灵媒进入出神状态与逝去祖先沟通，被视为"灵性技术"而非乐器 | **B** |
| **科拉琴**<br>Kora | ⚠️ **有条件保留**（见 1.3） | **C** |
| **祖尔纳**<br>Zurna | 音量极大、强节庆属性，且在多国存在名称与归属的族群争议 | **D** |
| 各类**萨满鼓** | 功能定位为萨满仪式法器 | **B** |
| **卡林巴（传统姆比拉族）** | ⚠️ **仅采用现代全音阶款**（见 1.3） | **B** |

### 1.3 有条件保留的两件，及处理方式

这两件我没有一刀切排除，而是通过**文案措辞**规避风险 —— 这是更专业的做法，因为它们本身极具魅力，直接砍掉可惜。

**① 科拉琴 Kora**

- **风险**：传统上属于曼德族世袭音乐家阶层 jali（griot）的家族技艺，在 jaliya 传统内由男性演奏。
- **处理**：`learn` 字段**只描述器物构造与演奏手法**（葫芦共鸣箱、21 弦、双手四指），**不写"你天生属于某个世袭传统"**这类把用户代入世袭身份的话。`title` 用「记忆的编织者」呼应其口述史功能，但落点在"编织记忆"这一普遍人性，而非"你是 griot"。
- **补充事实**：该传统已在开放，Sona Jobarteh 是首位知名女性科拉琴演奏家，部分 jali 父亲也开始教女儿演奏。

**② 卡林巴 Kalimba**

- **风险**：与神圣的姆比拉同属非洲拉梅拉琴大家族，容易被混为一谈。
- **处理**：数据中 id 明确写作 `kalimba_diatonic`，`origin` 字段如实标注**"现代全音阶款由 Hugh Tracey 于 1950 年代基于非洲拉梅拉琴族改制"**。这是诚实的溯源 —— 既不假装它是古老圣器，也不掩盖它的非洲根源。
- **底线**：绝不把它描述成"非洲祖灵乐器"。它是一件面向大众的现代改制乐器，如实说就好。

### 1.4 入选的 21 件乐器 · 合规状态

**16 件主乐器**

| 乐器 | 产地 | 合规备注 |
|---|---|---|
| 杜杜克管 Duduk | 亚美尼亚 | UNESCO 名录，用于婚礼与葬礼等世俗场合，无演奏者身份限制 |
| 键控提琴 Nyckelharpa | 瑞典 | 民间舞曲乐器，1970 年代由 Eric Sahlström 推动复兴，完全开放 |
| 古筝 Guzheng | 中国 | 主流民族乐器，无限制 |
| 科拉琴 Kora | 西非曼德地区 | ⚠️ 按 1.3 处理，只谈器物不谈世袭身份 |
| 葫芦丝 Hulusi | 中国云南 | 民间抒情乐器，无限制 |
| 康特勒琴 Kantele | 芬兰 | 民族象征乐器，史诗背景为文学而非宗教仪轨 |
| 手碟 Handpan | 瑞士（2000 年） | 当代发明，零传统包袱。注意：创制者反对"hang drum"叫法，勿称"手碟鼓" |
| 桑图尔 Santur | 伊朗 | 古典艺术音乐乐器，世俗语境 |
| 卡瓦尔笛 Kaval | 巴尔干 | 牧人乐器，世俗 |
| 钢鼓 Steelpan | 特立尼达和多巴哥 | 20 世纪诞生，狂欢节乐器，全民参与 |
| 卡宏鼓 Cajón | 秘鲁 | 世俗节奏乐器，全球流行 |
| 马林巴 Marimba | 中美洲与非洲 | 已高度国际化，音乐学院标准乐器 |
| 锡哨笛 Tin whistle | 爱尔兰 | 大众普及，无限制 |
| 卡林巴 Kalimba | 现代改制款 | ⚠️ 按 1.3 处理，如实标注改制来源 |
| 恰朗戈 Charango | 安第斯高地 | 世俗民间乐器 |
| 马头琴 Morin khuur | 蒙古国 | UNESCO 名录，日常与庆典乐器，无演奏限制 |

**5 件稀有款**

| 乐器 | 产地 | 合规备注 |
|---|---|---|
| 西库 Siku | 安第斯高地 | 世俗合奏乐器。**注意**：其 ira/arka 双排在传统宇宙观中有阴阳互补（yanantin）的象征，文案只取"两人交替才成曲"的协作意象，**不引申性别对应** |
| 玻璃竖琴 Glass harp | 欧洲 | 18 世纪沙龙乐器，无包袱 |
| 低音陶钵鼓 Udu | 尼日利亚伊博地区 | 世俗节奏乐器 |
| 口簧琴 Jaw harp | 欧亚广泛分布 | **注意**：图瓦、萨哈等地的 khomus 有萨满关联，故 `origin` 写"欧亚大陆广泛分布"，`learn` 只讲发声原理（口腔作共鸣箱、泛音选择），不涉萨满语境 |
| ~~水管风琴 Hydraulophone~~ | 加拿大 | **已剔除** —— 2005 年当代发明，全球仅极少数装置，无合规音源，用户现实中几乎不可能见到或听到。换为陶笛 |

### 1.5 文案红线

写任何新文案时必须遵守：

**禁止**
- ❌ 把乐器与**特定民族的性格**绑定："马头琴人都很豪迈"→ 这是刻板印象
- ❌ 使用**灵性/通灵**措辞："这件乐器能连接你的灵魂频率"
- ❌ 编造伪科学："对应 528Hz 治愈频率""激活你的松果体"
- ❌ 声称某乐器"最古老/最原始"——"原始"一词带殖民视角，且此类论断通常无法证实
- ❌ 把民族服饰、宗教符号画进插画（见第二部分）
- ❌ 提及现存的政治争议、领土归属

**必须**
- ✅ `learn` 字段的每句话都要**可核实**。本项目的 UNESCO 名录年份、弦数、材质、构造原理均经查证
- ✅ 产地标注到**文化区域**而非强行归入单一现代国家（如"巴尔干地区""安第斯高地""西非曼德地区"）
- ✅ 当代发明的乐器**如实写明创制年代与发明者**（手碟、卡林巴现代款）
- ✅ 描写落点始终在**普遍人性**，而非"你属于某个族群"

### 1.6 事实核查记录

`learn` 与 `trivia` 字段中的关键事实来源：

| 事实 | 来源 |
|---|---|
| 杜杜克管 2005 年入选、dam duduk 循环呼吸持续低音、杏木+芦苇双簧 | UNESCO ICH 名录 00092 |
| 键控提琴 16 弦（3 旋律 + 1 持续低音 + 12 共鸣）、音枕截弦 | Smithsonian NMAH 藏品记录、organology.net |
| 科拉琴 21 弦分 11/10、葫芦+牛皮、kumbengo / birimintingo | 大都会艺术博物馆藏品 501115、worldinstruments.org |
| 手碟 2000 年 PANArt 创制、Ding/Gu、亥姆霍兹共振、氮化钢 | PANArt 官方史料、Wikipedia Hang 条目 |
| 康特勒琴《卡莱瓦拉》狗鱼颚骨、后改桦木 | 芬兰史诗《卡莱瓦拉》、美国国会图书馆民俗中心 |
| 马头琴 2003 年入选、马尾弦与弓、tatlaga 驯畜调 | UNESCO ICH 名录 00068、中国人大网译介 |
| 西库 13 管分 ira 6 / arka 7、双人 hocket 交替 | worldinstruments.org、Wikipedia Siku 条目 |
| 卡林巴 Hugh Tracey 1950 年代全音阶改制 | 多方史料一致 |
| 迪吉里杜管性别禁忌与 2008 年 HarperCollins 道歉事件 | Wikipedia Didgeridoo 条目（引 Mark Rose、Linda Barwick） |
| 姆比拉 bira 召灵仪式、"祖灵之琴"词义 | LibreTexts 民族音乐学教材、etymology.life |

### 1.7 文化故事（story 字段）的额外红线

`story` 字段讲人与命运，比器物科普更容易越界，故追加三条：

1. **涉及殖民、奴隶制的故事，落点必须在创造力与韧性，不渲染压迫细节。**
   钢鼓与卡宏鼓的故事都涉及禁令与奴役背景。写法是把重心放在"他们如何绕过限制造出新东西"，而非描述受压迫的惨状。钢鼓故事的收尾是「你越禁，它越长得出来」——这是对创造力的致敬，不是对苦难的消费。

2. **传说与史实必须分清。**
   康特勒琴的鱼骨琴故事明确写"芬兰史诗《卡莱瓦拉》里"，不写成"历史上第一把康特勒琴是鱼骨做的"；恰朗戈起源写"传说它的形制是……"。凡无法确证的，一律用"传说""据说""史诗里"标明。

3. **不神化、不猎奇。**
   杜杜克管的故事写"亚美尼亚人说它是唯一能哭的乐器"——归因于当地人的说法，而非由我们断言。口簧琴的故事只讲"头骨作共鸣箱"的声学事实与分布之广，完全不涉萨满语境。

### 1.8 故事部分的事实核查记录

| 故事要点 | 来源 |
|---|---|
| 钢鼓：1880 年代皮鼓被禁 → 改用竹子（tamboo bamboo）→ 竹子也被禁 → 1930 年代饼干罐/垃圾桶盖/废油桶 → 1992 年定为国家乐器 | Wikipedia Steelpan、特立尼达和多巴哥奥委会 ttoc.org、worldinstruments.org |
| 卡宏鼓：殖民禁鼓、取用港口水果木箱、可伪装成凳子；1977 年 Paco de Lucía 在利马听到后带回西班牙 | Wikipedia Cajón、cajon.world、peru.info |
| 键控提琴：1940 年代仅十余名演奏者，1960 年代末只剩个位数；Eric Sahlström（1912–1986）改良并开班教学，今瑞典约一万人演奏 | nordstjernan.com、Wikipedia Eric Sahlström |
| 手碟：需手写信说明动机、被选中才出售、须签不得转卖获利条款、2013 年停产 | PANArt 官方史料、instruments-du-monde.com |
| 康特勒琴：狗鱼颚骨造琴、沉海后以桦木重做、离去时留下此琴 | 芬兰史诗《卡莱瓦拉》 |
| 西库：整套含四种尺寸，最大低音管可达约 1.5 米 | worldinstruments.org |
| 科拉琴：jali 兼任家谱专家、调解人、口述史保存者 | thekoracafe.com、worldinstruments.org |

---

## 第二部分：生图规范

### 2.1 统一风格定义

**目标**：21 张图放在一起必须像**同一位画家、同一本图鉴里的插页**。风格一致性比单张的精美度重要得多 —— 单张再好看，21 张风格不统一，产品就垮了。

**核心风格描述（所有 prompt 共用）**

```
minimalist watercolor illustration, single musical instrument, 
centered composition, isolated on warm off-white paper background,
soft wet-on-wet washes with visible pigment granulation,
delicate dry-brush texture at edges, 
restrained palette of 2-3 muted earth tones plus one accent,
loose confident brushwork, generous negative space,
subtle graphite underdrawing showing through in places,
no background scenery, no human figures, no hands, no text, no labels,
museum field-guide aesthetic, elegant and understated,
soft natural lighting from upper left, gentle cast shadow
```

**负向提示（所有图共用）**

```
photorealistic, 3d render, digital painting, heavy outlines, cartoon, 
anime, cel shading, neon colors, oversaturated, glossy, plastic, 
cluttered background, multiple instruments, people, hands, faces, 
text, watermark, signature, logo, ethnic costume, religious symbols, 
flags, maps, tribal patterns, gradient mesh, lens flare, bokeh
```

> **为什么明确排除 `ethnic costume / religious symbols / flags / tribal patterns`**：
> 这直接对应 1.5 的文案红线。生图模型在画"民族乐器"时极易自动加上民族服饰、宗教符号、部落纹样作为"氛围点缀" —— 而这恰恰是最容易造成文化冒犯的元素。**必须在负向提示里显式禁止**，不能指望模型自觉。

### 2.2 技术参数

| 项 | 建议值 | 理由 |
|---|---|---|
| 比例 | **1:1** | 结果卡与图鉴网格都用方图，一套图两处复用 |
| 分辨率 | ≥ 1024×1024 | 结果卡截图 `scale:2` 时不发虚 |
| 背景 | **暖白纸色**（非纯白、非透明） | 纯白在深色卡片上会像贴纸；暖白有纸感，和水彩调性一致 |
| 输出格式 | PNG | 保留边缘柔和过渡 |
| 命名 | `img/<id>.png` | 与 `instruments.json` 的 id 严格对应，如 `img/duduk.png` |

### 2.3 单件乐器 Prompt

每条 = **统一风格描述 + 下方主体描述 + 该件配色**。配色取自 `instruments.json` 的 `palette` 字段。

> 使用方式：把「主体描述」插入统一风格描述的 `single musical instrument` 之后，并把 `restrained palette of...` 一句替换为该件的具体配色。

#### 主乐器 16 件

| id | 主体描述（英文，直接可用） | 配色 |
|---|---|---|
| `duduk` | a slender cylindrical apricot-wood double-reed pipe lying diagonally, wide flat cane reed mouthpiece visible at top, nine finger holes, warm honey-brown wood grain | 蜜棕 `#8C6239` / 浅木 `#C89F6D` / 深褐 `#4A3B2A` |
| `nyckelharpa` | a Swedish keyed fiddle standing upright, violin-like body with a long row of small wooden keys along the neck, many fine strings, short arched bow resting beside it | 灰木 `#7A6A55` / 米白 `#D9C9A8` / 苔绿 `#3E4A3C` |
| `guzheng` | a long Chinese zither seen at a three-quarter angle, many parallel strings stretched over a row of small movable bridges, elongated wooden soundbox | 赭金 `#B5834C` / 米黄 `#E8D5B0` / 深栗 `#5C4530` |
| `kora` | a West African harp-lute, large round gourd body covered with pale hide, tall straight hardwood neck, twenty-one strings rising over a tall notched vertical bridge | 土金 `#A9803F` / 沙米 `#E3CBA0` / 深灰褐 `#43382C` |
| `hulusi` | a small Chinese gourd flute, round dried-gourd air chamber at the base with three bamboo pipes rising from it, one central longer pipe flanked by two shorter drone pipes | 竹青 `#9CAF88` / 浅青白 `#E4E9D4` / 深绿 `#5A6B4F` |
| `kantele` | a small Finnish box zither, simple trapezoidal wooden body carved from a single block, five to eleven strings, plain unadorned birch surface | 灰蓝 `#8FA3B0` / 冷白 `#DFE7EC` / 石青 `#42525C` |
| `handpan` | a convex steel handpan shaped like a smooth lens or flying saucer, central raised dome surrounded by seven gently hammered tone fields, brushed dark steel surface | 钢灰 `#7E8B92` / 银白 `#CFD8DC` / 墨灰 `#39434A` |
| `santur` | a Persian trapezoidal hammered dulcimer seen from above, dozens of parallel strings in groups over small bridges, a pair of very light slender wooden mallets resting on it | 木棕 `#9C7B5E` / 浅驼 `#E0CDB6` / 深褐 `#4B3A2C` |
| `kaval` | a long straight rim-blown wooden flute lying diagonally, plain cylindrical bore with no mouthpiece or fipple, eight finger holes, weathered pale wood | 麦褐 `#A3906F` / 亚麻 `#E5DBC4` / 橄榄 `#4E4736` |
| `steelpan` | a concave steel pan drum seen from slightly above, circular playing surface divided into hammered oval note sections, two rubber-tipped sticks resting on the rim | 金黄 `#C9A227` / 淡金 `#F2E3A0` / 橄榄绿 `#4A5A3A` |
| `cajon` | a simple rectangular wooden box drum, thin front playing panel with a round sound hole on the back side, clean plywood construction, seen at a three-quarter angle | 木棕 `#8B5E3C` / 浅木 `#DEC49E` / 深褐 `#3F3227` |
| `marimba` | a wooden keyboard percussion instrument, graduated rosewood bars in a row with tuned resonator tubes hanging beneath each bar, two pairs of yarn-wound mallets | 红木 `#A5714A` / 浅木 `#E8CFA9` / 深棕 `#4C3A2B` |
| `tinwhistle` | a simple six-holed tin whistle lying diagonally, narrow cylindrical metal tube with a small plastic fipple mouthpiece, matte brass finish | 苔绿 `#6E8B74` / 浅绿白 `#DCE8DA` / 深绿 `#3A4A3E` |
| `kalimba_diatonic` | a small thumb piano, rectangular wooden soundboard with a row of graduated metal tines arranged low in the center and rising alternately to both sides | 灰木 `#8A7B6B` / 浅米 `#E0D6C8` / 深褐 `#42392F` |
| `charango` | a small Andean lute with a compact rounded body and short neck, ten strings arranged in five closely paired courses, warm varnished wood | 陶橙 `#C08552` / 浅陶 `#F0DBB8` / 深棕 `#4F3E2E` |
| `morinkhuur` | a Mongolian two-stringed fiddle standing upright, trapezoidal soundbox, long fretless neck topped with a carved horse head, two tuning pegs jutting like ears, horsehair bow beside it | 灰褐 `#7C6A54` / 浅驼 `#D8CBB2` / 青灰 `#3B4340` |

#### 稀有款 5 件

| id | 主体描述 | 配色 |
|---|---|---|
| `siku` | Andean panpipes, two parallel rows of graduated bamboo tubes bound side by side with cord between two horizontal cane strips, forming a raft-like trapezoidal shape | 竹褐 `#B99A6B` / 浅竹 `#EBDCC0` / 深绿灰 `#46514A` |
| `glassharp` | an arrangement of several stemmed crystal glasses of graduated sizes on a plain surface, each filled to a different water level, transparent and luminous | 冰蓝 `#AFC4CE` / 近白 `#EEF4F6` / 石蓝 `#4A5A63` |
| `hangdrum_bass` | a rounded clay vessel drum with a narrow neck and a distinct round hole on its side wall, matte unglazed terracotta surface, organic hand-formed shape | 陶褐 `#8D6A4F` / 浅陶 `#DFC9AE` / 深褐 `#3E332A` |
| `jawharp` | a small metal jaw harp, horseshoe-shaped frame with a single thin flexible tongue extending through the center, polished steel, shown alone at slight angle | 铁灰 `#8E8577` / 浅灰 `#DDD6CA` / 深灰 `#414038` |
| `ocarina` | a small rounded clay vessel flute, egg/sweet-potato shape with a short side mouthpiece and a scattered row of round finger holes, matte glazed terracotta | 陶红 `#B5654A` / 浅陶 `#EFD5C6` / 深褐 `#54301F` |

### 2.4 生图执行建议

**先做基准图，再批量**

1. 先只生成 `duduk` 一张，反复调到满意 —— 这张是**风格基准**
2. 把满意的那张作为**风格参考图**（若工具支持 image reference / style reference）再生成其余 20 张
3. 若工具不支持参考图，则保持 prompt 的统一风格段**逐字不变**，只替换主体描述与配色，并固定 seed 或同一模型版本

**批次顺序建议**

按形制分批，同批风格更容易统一：

| 批次 | 乐器 | 共同点 |
|---|---|---|
| 1 · 管类 | duduk, kaval, tinwhistle, hulusi, siku | 细长、可斜置构图 |
| 2 · 弦类 | guzheng, kora, santur, kantele, nyckelharpa, charango, morinkhuur | 有琴弦，需注意弦的疏密表现 |
| 3 · 打击类 | handpan, steelpan, cajon, marimba, udu | 块面为主 |
| 4 · 特殊 | kalimba, glassharp, jawharp, ocarina | 小件或需特殊处理 |

**验收清单**

- [ ] 21 张并排放在一起，看起来像同一本图鉴（**这是最重要的一条**）
- [ ] 背景色一致（暖白纸色，非纯白）
- [ ] 无任何文字、水印、签名
- [ ] 无人物、无手、无民族服饰、无宗教符号、无旗帜纹样
- [ ] 乐器形制**正确**：马头琴顶端确实是马头；西库确实是两排管；卡林巴簧片确实是中间低两侧高；手碟确实是凸面而非凹面
- [ ] 缩略到 120×120px（图鉴网格尺寸）时仍能辨认是什么乐器
- [ ] 在深色卡片背景上不显脏、不像贴纸

> ⚠️ **形制正确性需要人工核对**。生图模型经常把马头琴画成普通小提琴、把西库画成单排排箫、把手碟画成凹面平底锅。**每一张都要对着 `learn` 字段的描述检查构造**，错的直接重生成 —— 一张形制错误的图会让整个"能学到东西"的产品承诺失效。

### 2.5 卡片整体视觉建议

图之外，结果卡本身的视觉调性：

| 元素 | 建议 |
|---|---|
| 卡片底色 | 深色系（`#1A1815` 左右的暖黑），让水彩图的暖白背景成为视觉焦点 |
| 判词字体 | 中文衬线（`Songti SC / STSong / serif`），20–24px，字重 400 |
| 正文字体 | 系统无衬线，15–16px，行高 1.7 |
| 主色调 | 取当件乐器 `palette` 的第一色作为该卡的强调色（分隔线、`trivia` 区块边框、四轴条形图） |
| `trivia` 区块 | 用该乐器强调色的低透明度填充 + 左侧 2px 竖线，这是最易被截图的单元，要在视觉上"可独立成立" |
| 留白 | 慷慨。区块间距 ≥ 24px。水彩风格需要呼吸感，挤在一起会显得廉价 |
| 稀有徽章 | 小尺寸、描边样式，放在标题上方，**不要**用金色渐变或发光效果 —— 与水彩的克制调性冲突 |

---

## 六、音频授权审查（上线前必做）

音频是整个项目**最容易出法律问题**的部分。素材清单自带的授权标注不能照信 —— 实测 21 条里
有 12 条没标授权，还有 2 条标了但不可用。全部逐条回源核实后的结论：

### 6.1 查实方法

| 来源 | 核实方式 |
|---|---|
| Wikimedia Commons | `action=query&prop=imageinfo&iiprop=extmetadata`，读 `LicenseShortName` |
| Freesound | 抓音频页 HTML，匹配 `creativecommons.org/licenses/...` 链接 |
| Internet Archive | `archive.org/metadata/<id>`，看有没有 `licenseurl` 字段 |

**没有 `licenseurl` 就是没有自由授权**，不要因为"能下载"就当成可用。

### 6.2 发现并处理的三个问题

1. **手碟 CC BY-NC-ND** —— `ND` 禁止改编，而"裁成 10 秒片段"本身就是改编，
   `NC` 还禁商用。**双重违规**。改用项目原有的 CC BY-SA 3.0 版本。
2. **康特勒琴 CC BY-NC** —— 禁商用。改用项目原有的 CC0 版本。
3. **卡瓦尔笛** —— 来源是 Internet Archive 的 `unlockedrecordings` /
   `vinyl_bostonpubliclibrary`（波士顿公共图书馆黑胶数字化），**无 `licenseurl`，
   属仍在版权期内的商业唱片**，IA 只按受控访问提供。维基上也确实没有任何卡瓦尔笛音频
   （英/德/西/俄/保加利亚语别名、分类树、intitle 都搜过）。**弃用，结果页自动隐藏播放键。**

科拉琴标注为"Free Art License，待审查"，回查 Commons 页面确认是干净的 **FAL** ——
这是 FSF 认可的自由 copyleft 许可，允许改编与商用，可用（需署名，且衍生品同样 FAL）。

### 6.3 最终授权清单

多数为 CC BY / CC BY-SA，**强制署名**。结果页的「音频来源与授权」可展开区逐条列出了
文件名、作者、许可证与原文件页链接。CC BY-SA 有传染性，若要商用建议优先替换为 CC0 素材。

| 乐器 | 许可证 | 作者 / 来源 |
|---|---|---|
| `duduk` | CC BY 4.0 | juskiddink / Freesound |
| `nyckelharpa` | CC0 | Statens musikverk / Wikimedia Commons |
| `guzheng` | CC BY 3.0 | Antti Luode / Wikimedia Commons |
| `kora` | Free Art License (FAL) | Cinus Laurent / Wikimedia Commons |
| `hulusi` | CC0 | iluppai / Wikimedia Commons |
| `kantele` | CC0 | Olli Niemitalo |
| `handpan` | CC BY-SA 3.0 | Michael Paschko (Ixkeys) www.hangblog.org |
| `santur` | CC BY-SA 4.0 | Mohammad R Azadehfar / Wikimedia Commons |
| `kaval` | — | **无音频（版权原因弃用）** |
| `steelpan` | CC BY 3.0 | Andy Clayton / Wikimedia Commons |
| `cajon` | CC BY 3.0 | Freesound sample 214524 |
| `marimba` | CC BY 3.0 | Kevin MacLeod / Wikimedia Commons |
| `tinwhistle` | CC BY 3.0 | luis_audp / Freesound |
| `kalimba_diatonic` | CC0 1.0 | A_Curious_coder / Freesound |
| `charango` | CC0 1.0 | Bmangelo / Freesound |
| `morinkhuur` | CC BY 4.0 | Qleq / Freesound |
| `siku` | CC BY 4.0 | CarlosCarty / Freesound |
| `glassharp` | CC BY-SA 2.5 | William Zeitler / Wikimedia Commons |
| `ocarina` | CC BY 3.0 | Ailes Grises at English Wikipedia |
| `hangdrum_bass` | CC BY 4.0 | ultradust / Freesound |
| `jawharp` | CC BY 4.0 | Atilio_Sanchez / Freesound |

