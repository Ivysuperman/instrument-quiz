# -*- coding: utf-8 -*-
"""生成 data.js：把乐器数据 + 音频清单内联，并为每件乐器生成 SVG 占位图。
内联而非 fetch，因为 file:// 协议下 fetch 本地 JSON 会被 CORS 拦截。
"""
import json, os, random

ROOT = '/Users/ivy/WorkBuddy/2026-08-15-15-14-02/echoes-of-you/'
inst = json.load(open(ROOT+'docs/instruments.json', encoding='utf-8'))
aud  = json.load(open(ROOT+'docs/audio.json', encoding='utf-8'))['audio']

ALL = inst['instruments'] + inst['rare_instruments']
RARE_IDS = {i['id'] for i in inst['rare_instruments']}

# ---------- 插图 ----------
# 水彩插图由用户提供，经 docs/_build_images.py 压成两套尺寸：
#   img/<id>.jpg    结果页海报 600x800 (3:4)
#   img/<id>_t.jpg  图鉴缩略图 240x240（方裁，避开插图底部烘焙的乐器名）
# 早期的 SVG 占位图生成逻辑已移除。插图本身已含乐器中文名+产地，
# 故结果页不再用 HTML 重复输出名字。
import glob as _glob
_missing=[]

# ---------- 20 道题（五档量表 · 单命题陈述句） ----------
# 五档：很像我 +2 / 有点像 +1 / 说不好 0 / 不太像 -1 / 完全不像 -2
# dir=+1 表示"像我"指向该轴正极；dir=-1 表示指向负极
#
# 出题铁律（五档量表专属）：
#   1. 每题只陈述【一件事】，绝不写"A 而不是 B"——那是二选一的伪装，配五档会变成
#      "我有多同意选 A"，用户会觉得别扭且答案失真
#   2. 描述具体可回忆的行为或反应，不做抽象自评（"我是个爱回味的人"这种不要）
#   3. 不用"更""比起"这类比较词，因为没有比较对象
#   4. 每轴 5 题、权重 [1,1,1,2,2]，且每轴至少一道反向计分题（dir=-1），
#      防止一路点"很像我"就刷出极端结果
#   5. 【说人话】必须是日常口语，不要文学化表达。反面教材（已废弃）：
#      ✗ "一些说不清的怅然的东西，很容易就把我留住了" —— 这是散文不是问卷
#      ✗ "我确实想要那个位置" —— 指代不明，"那个位置"到底指什么？
#      ✗ "我很在意每个人是不是都真的接上了" —— "接上"太含糊
#      ✓ 直接写具体场景 + 具体反应，让人扫一眼就知道在问什么
#   6. 【场景要均衡】不能全是工作/自我视角。必须覆盖四类场景：
#      - 工作与做事（work）
#      - 独处与自我（self）
#      - 生活与审美品味（taste）：听什么、穿什么、怎么安排自己的空间和时间
#      - 亲密关系与人际情感（bond）：亲情、友情、爱情
#      bond 类占比不低于 1/3，因为"人在关系里的样子"最能定义其音色；
#      taste 类不可缺，因为审美偏好是"音色"最直接的外显，且每轴都要有一道。
#   7. 【场景要交错】order 不能让同类场景连成一大片。原本 9~20 连续 12 道情感题，
#      用户会疲劳；故把 taste 组插在 17~20，让情感题分成两段。
QUESTIONS = [
 # order, axis, w, dir, scene, 单命题陈述句, 补充说明(可空)
 # ===== 共鸣方式 R：绵长余韵 / 利落颗粒 =====
 (1, 'R',1,+1,'work','跟人聊得很投入，散场后我还会在路上回想刚才说的话。',''),
 (5, 'R',1,-1,'self','事情做完就放下了，我很少回头再想。',''),
 (9, 'R',2,+1,'bond','跟亲近的人拌过嘴，那几句话我能记很久。',''),
 (13,'R',1,+1,'bond','很多年没联系的老朋友，我偶尔还会突然想起他。',''),
 (17,'R',1,-1,'taste','拍过的照片我很少再翻出来看。',''),
 (21,'R',2,-1,'bond','跟人闹了别扭，我睡一觉基本就过去了。',''),

 # ===== 能量形态 E：向外穿透 / 向内低语 =====
 (2, 'E',1,+1,'work','想到一个好主意，我第一反应是找人分享。',''),
 (6, 'E',1,-1,'self','一个人待一会儿，我就能恢复精力。',''),
 (10,'E',2,+1,'work','要在很多人面前讲话，我会紧张，但我愿意上。',''),
 (14,'E',2,-1,'bond','再喜欢的人，天天见面我也会需要一点自己的空间。',''),
 (18,'E',1,-1,'taste','特别喜欢的歌或电影，我常常自己收着，不太到处推荐。',''),
 (22,'E',1,+1,'bond','朋友聚会我常常是张罗的那个人。',''),

 # ===== 结构关系 S：独奏领航 / 织体共生 =====
 (3, 'S',1,+1,'work','一件事大家都定不下来，我会站出来做决定。',''),
 (7, 'S',1,-1,'work','团队做事的时候，我会特别留意有没有人被落下。',''),
 (11,'S',2,+1,'work','大家都在犹豫的时候，我会先开口说该怎么办。',''),
 (15,'S',2,-1,'bond','家里人或伴侣心情不好，我一般能先察觉到。',''),
 (19,'S',1,+1,'taste','跟朋友出去吃饭玩，一般是我定地方。',''),
 (23,'S',1,-1,'bond','朋友吵架，我常是中间劝和的那个。',''),

 # ===== 情绪底色 T：明亮欢腾 / 深沉苍远 =====
 (4, 'T',1,-1,'self','我喜欢安静、慢节奏的东西。','比如傍晚的天色，或者没有人声的音乐'),
 (8, 'T',1,+1,'self','我平时精力挺足，到了晚上还想着明天要做的事。',''),
 (12,'T',2,-1,'bond','别人觉得我比较安静，不太好接近。',''),
 (16,'T',2,+1,'bond','我挺容易被身边人的好情绪带动起来。',''),
 (20,'T',1,+1,'taste','穿衣服或布置房间，我喜欢用亮一点的颜色。',''),
 (24,'T',1,-1,'bond','我在乎的人不多，但会在乎很久。',''),
]

# ---------- 自动排序：轴交错 + 场景打散 ----------
# 元组里的 order 只表示"该题在本轴内的次序"，最终 order 由排序算法生成。
# 手工排 order 极易排出"连续 5 道情感题"这类问题（已踩过），故改为自动。
# 算法：轴按 R→E→S→T 严格轮转（保证相邻题必不同轴），
#       每步在当前轴的剩余题里优先挑"场景与上一道不同"的那道。
#       若只按各轴同序号取题，会因各轴同序号恰好同场景而排出成块的品味/情感段。
def arrange(rows):
    queues = {ax: sorted([r for r in rows if r[1] == ax], key=lambda r: r[0])
              for ax in 'REST'}
    out = []
    axes = 'REST'
    for step in range(len(rows)):
        ax = axes[step % 4]
        q = queues[ax]
        prev = out[-1][4] if out else None
        # 优先取场景与上一道不同的；实在没有就取队首（保持轴内次序）
        pick = next((r for r in q if r[4] != prev), q[0])
        q.remove(pick)
        out.append(pick)
    return [(i + 1,) + r[1:] for i, r in enumerate(out)]


QUESTIONS = arrange(QUESTIONS)
questions = [{'order':o,'axis':ax,'w':w,'dir':dr,'scene':sc,'q':q,'hint':hint}
             for o,ax,w,dr,sc,q,hint in QUESTIONS]

# 五档选项（从正到负）
SCALE = [
  {'v': 2, 'label':'很像我'},
  {'v': 1, 'label':'有点像'},
  {'v': 0, 'label':'说不好'},
  {'v':-1, 'label':'不太像'},
  {'v':-2, 'label':'完全不像'},
]

# 图鉴用的简短产地（origin 原文过长或含说明性文字时单独指定）
SHORT_ORIGIN = {
  'kalimba_diatonic': '非洲 · 现代改制',
  'hangdrum_bass':    '尼日利亚',
  'steelpan':         '特立尼达',
  'kora':             '西非',
  'marimba':          '中美洲/非洲',
  'handpan':          '瑞士',
  'jawharp':          '欧亚大陆',
  'kaval':            '巴尔干',
  'siku':             '安第斯',
  'charango':         '安第斯',
  'ocarina':          '意大利',
}

# ---------- 精简数据（去掉前端不用的字段，减小体积） ----------
def slim(it):
    d = {k:it[k] for k in ('id','name_zh','name_en','origin','family','title','verdict',
                           'portrait','story_title','story','learn','trivia',
                           'shadow','partner','palette','listen')}
    if 'code' in it: d['code'] = it['code']
    d['rare'] = it['id'] in RARE_IDS
    d['org'] = SHORT_ORIGIN.get(it['id'], it['origin'].split('（')[0])
    a = aud.get(it['id'])
    if a:
        d['audio'] = {'m4a':a['m4a'],'mp3':a['mp3'],'dur':a['duration'],
                      'cr':{'f':a['credit']['file'],'a':a['credit']['author'],
                            'l':a['credit']['license'],'p':a['credit']['page']}}
    return d

DATA = {
  'axes': {
    'R':{'name':'共鸣方式','pos':'绵长余韵','neg':'利落颗粒'},
    'E':{'name':'能量形态','pos':'向外穿透','neg':'向内低语'},
    'S':{'name':'结构关系','pos':'独奏领航','neg':'织体共生'},
    'T':{'name':'情绪底色','pos':'明亮欢腾','neg':'深沉苍远'},
  },
  'questions': questions,
  'scale': SCALE,
  'map': inst['code_to_instrument'],
  'inst': {it['id']: slim(it) for it in ALL},
}

js = 'window.DATA=' + json.dumps(DATA, ensure_ascii=False, separators=(',',':')) + ';'
open(ROOT+'data.js','w',encoding='utf-8').write(js)

print(f"data.js  {len(js)/1024:.1f} KB")
print(f"含音频   {sum(1 for i in DATA['inst'].values() if 'audio' in i)}/21")
print(f"题目     {len(questions)} 道 · {len(SCALE)} 档量表")

from collections import Counter
# 每轴权重必须是 [1,1,1,1,2,2]
for ax in ('R','E','S','T'):
    ws = sorted(q['w'] for q in questions if q['axis']==ax)
    assert ws == [1,1,1,1,2,2], f"{ax} 轴权重异常: {ws}"
# 每轴必须有反向计分题，否则一路点"很像我"就能刷满
for ax in ('R','E','S','T'):
    dirs = [q['dir'] for q in questions if q['axis']==ax]
    assert 1 in dirs and -1 in dirs, f"{ax} 轴缺反向计分题: {dirs}"
    # 加权方向和为 0 时，正反向完全平衡，最能抵抗"一路点同意"的默认赞同偏误
    wsum = sum(q['dir']*q['w'] for q in questions if q['axis']==ax)
    print(f"  {ax} 轴 正向{dirs.count(1)}题 反向{dirs.count(-1)}题  加权方向和={wsum}"
          + ("  ✓完全平衡" if wsum==0 else ""))

# 场景均衡：不能全是工作/自我视角
SCN_NAME = {'work':'工作做事','self':'独处自我','taste':'生活品味','bond':'人际情感'}
scn = Counter(q['scene'] for q in questions)
print()
for k in ('work','self','taste','bond'):
    print(f"  {SCN_NAME[k]} {scn[k]:2d} 题  {scn[k]/len(questions):5.1%}")
bond_ratio = scn['bond']/len(questions)
assert bond_ratio >= 1/3, f"人际情感题占比过低 {bond_ratio:.0%}，应 ≥33%（用户明确要求覆盖亲情/友情/爱情）"
# 生活品味题不可缺：审美偏好是"音色"最直接的外显
assert scn['taste'] >= 4, f"生活品味题过少 {scn['taste']} 道，每轴至少 1 道"
# 每轴都要有情感题和品味题，否则某个维度只靠工作场景判断
for ax in ('R','E','S','T'):
    axs = [q['scene'] for q in questions if q['axis']==ax]
    assert 'bond'  in axs, f"{ax} 轴缺人际情感题: {axs}"
    assert 'taste' in axs, f"{ax} 轴缺生活品味题: {axs}"
# 场景交错：不能连续 5 道以上同类场景，否则用户会疲劳
seq = [q['scene'] for q in sorted(questions, key=lambda x:x['order'])]
run = mx_run = 1
for i in range(1, len(seq)):
    run = run+1 if seq[i]==seq[i-1] else 1
    mx_run = max(mx_run, run)
assert mx_run <= 2, f"存在连续 {mx_run} 道同类场景题，会让用户疲劳，检查 arrange() 的打散逻辑"
print(f"  场景校验通过 ✓（情感 {bond_ratio:.0%}、品味 {scn['taste']} 题、"
      f"四轴均含情感+品味题、最长同类连续 {mx_run} 道）")

# 五档量表铁律 1：题干不能是二选一 / 对比式
BAD_WORDS = ['而不是','比起','更可能','另一种','或者','还是','相比','宁愿','与其','更能','不是消耗']
import re as _re
bad = []
for q in questions:
    txt = q['q']                      # 只查题干；hint 允许用"比如"举例
    for w in BAD_WORDS:
        if w in txt:
            bad.append((q['order'], w, q['q'][:26]))
    if _re.search(r'比[^如]{0,10}更', txt):
        bad.append((q['order'], '比…更', q['q'][:26]))
if bad:
    print("\n❌ 检测到对比式表述（五档量表下会让用户别扭）:")
    for o,w,t in bad: print(f"   题{o} 含「{w}」: {t}…")
    raise SystemExit(1)
print("单命题校验通过 ✓（无对比式表述）")

# 五档量表铁律 2：必须说人话，不能文学化 / 指代不明
LITERARY = ['怅然','苍远','绵长','余韵','织体','低语','穿透','辽阔','沉静',
            '那个位置','某种','之物','留住我','劲头','脑子里响']
VAGUE    = ['接上了','那种感觉','某些时候','这一切']
lit = []
for q in questions:
    for w in LITERARY + VAGUE:
        if w in q['q']:
            lit.append((q['order'], w, q['q'][:30]))
if lit:
    print("\n❌ 检测到文学化或指代不明的表述（用户会觉得抽象、难以作答）:")
    for o,w,t in lit: print(f"   题{o} 含「{w}」: {t}…")
    print("   请改成日常口语，直接写具体场景 + 具体反应")
    raise SystemExit(1)
print("口语化校验通过 ✓（无文学化 / 指代不明表述）")

# 题干长度体检：太长在手机上会挤
lens = [(q['order'], len(q['q'])) for q in questions]
over = [x for x in lens if x[1] > 32]
# 插图必须每件齐全（海报 + 缩略图），缺一张结果页就会出现破图
for _it in ALL:
    for _suf in ('.jpg','_t.jpg'):
        if not os.path.exists(ROOT+f'img/{_it["id"]}{_suf}'):
            _missing.append(_it['id']+_suf)
assert not _missing, f"缺插图: {_missing}（跑 docs/_build_images.py）"
print(f"插图     {len(ALL)*2} 张齐全（海报 + 缩略图）")

print(f"题干长度 {min(l for _,l in lens)}~{max(l for _,l in lens)} 字"
      + (f"  ⚠ 偏长: {over}" if over else "  ✓ 均适合单屏"))
