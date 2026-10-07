// 五档量表版验证：从 index.html 抽真实逻辑，按轴卷积统计分布
const fs = require('fs');
const R = '/Users/ivy/WorkBuddy/2026-08-15-15-14-02/echoes-of-you/';
eval(fs.readFileSync(R + 'data.js', 'utf8').replace('window.DATA=', 'var DATA='));
const html = fs.readFileSync(R + 'index.html', 'utf8');

['function calc(', 'function sign(', 'function code(', 'function rare(', 'function resolve(', 'function isLazy(']
  .forEach(s => { if (html.indexOf(s) < 0) { console.error('页面缺函数: ' + s); process.exit(1); } });

const Q = DATA.questions, SC = DATA.scale.map(s => s.v);

// 复刻页面逻辑
function signOf(vals, qs) {
  let total = 0;
  for (let i = 0; i < qs.length; i++) total += vals[i] * qs[i].dir * qs[i].w;
  if (total !== 0) return [total > 0 ? 1 : -1, total];
  const mx = Math.max(...qs.map(q => q.w));
  let tie = 0;
  for (let j = 0; j < qs.length; j++) if (qs[j].w === mx) tie += vals[j] * qs[j].dir;
  if (tie !== 0) return [tie > 0 ? 1 : -1, total];
  let t1 = 0;
  for (let k = 0; k < qs.length; k++) if (qs[k].w < mx) t1 += vals[k] * qs[k].dir;
  return [t1 >= 0 ? 1 : -1, total];
}

// 每轴枚举 5^(该轴题数) 种（24 题版 = 5^6 = 15625），聚合成 (符号, 得分) -> 计数
const AXES = ['R','E','S','T'];
const axisStates = {};
AXES.forEach(ax => {
  const qs = Q.filter(q => q.axis === ax);
  const m = new Map();
  // 该轴题数可能不是 3，用递归枚举所有档位组合
  (function walk(vals){
    if (vals.length === qs.length) {
      const [sg, tot] = signOf(vals, qs);
      const key = sg + '|' + tot;
      m.set(key, (m.get(key) || 0) + 1);
      return;
    }
    for (const v of SC) walk(vals.concat(v));
  })([]);
  axisStates[ax] = [...m.entries()].map(([k,n]) => {
    const [sg,tot] = k.split('|').map(Number);
    return {sg, tot, n};
  });
  const t = axisStates[ax].reduce((s,x)=>s+x.n,0);
  const posP = axisStates[ax].filter(x=>x.sg>0).reduce((s,x)=>s+x.n,0)/t;
  const tieP = axisStates[ax].filter(x=>x.tot===0).reduce((s,x)=>s+x.n,0)/t;
  console.log(`${ax} 轴: 正极 ${(posP*100).toFixed(1)}%  需打破平局 ${(tieP*100).toFixed(1)}%`);
});
console.log();

function rare(s){
  const K=AXES;
  const strong=K.filter(k=>Math.abs(s[k])>=6).length;
  const weak=K.filter(k=>Math.abs(s[k])<=3).length;
  const pos=K.filter(k=>s[k]>0).length;
  if(weak===4&&pos===2)return 'ocarina';
  if(s.S<=-6&&strong>=3)return 'siku';
  if(s.R<=-6&&s.S>=6)return 'jawharp';
  if(s.R>=6&&s.E<=-6)return 'glassharp';
  if(s.E<=-6&&s.T<=-6)return 'hangdrum_bass';
  return null;
}

const grid = {}, rareHit = {};
let total = 0, mainN = 0;
for (const r of axisStates.R) for (const e of axisStates.E)
for (const sx of axisStates.S) for (const t of axisStates.T) {
  const w = r.n * e.n * sx.n * t.n;
  total += w;
  const sc = {R:r.tot, E:e.tot, S:sx.tot, T:t.tot};
  const rr = rare(sc);
  if (rr) { rareHit[rr] = (rareHit[rr]||0) + w; }
  else {
    const c = (r.sg>0?'L':'C')+(e.sg>0?'O':'I')+(sx.sg>0?'S':'W')+(t.sg>0?'B':'D');
    grid[c] = (grid[c]||0) + w; mainN += w;
  }
}

console.log('=== 主结果 ===');
console.log(`占比 ${(mainN/total*100).toFixed(1)}%   覆盖 ${Object.keys(grid).length}/16`);
const miss = Object.keys(DATA.map).filter(c => !grid[c]);
console.log('未覆盖: ' + (miss.length ? miss.join(',') : '无 ✓'));
const vs = Object.values(grid);
console.log(`单格 ${(Math.min(...vs)/total*100).toFixed(2)}% ~ ${(Math.max(...vs)/total*100).toFixed(2)}%  (差 ${(Math.max(...vs)/Math.min(...vs)).toFixed(1)}x)`);

console.log('\n=== 稀有款 ===');
Object.keys(rareHit).sort((a,b)=>rareHit[b]-rareHit[a]).forEach(k =>
  console.log(`  ${k.padEnd(16)}${(rareHit[k]/total*100).toFixed(2)}%`));
const unreach = Object.keys(DATA.inst).filter(k=>DATA.inst[k].rare && !rareHit[k]);
console.log('不可达: ' + (unreach.length ? unreach.join(',') : '无 ✓'));
console.log(`\n总作答组合 ${total.toLocaleString()} (5^${Q.length})`);

// 场景分布
const scn={};
Q.forEach(q=>{ scn[q.scene]=(scn[q.scene]||0)+1 });
console.log('\n=== 场景分布 ===');
const SN={work:'工作做事',self:'独处自我',taste:'生活品味',bond:'人际情感'};
Object.keys(scn).forEach(k=>console.log(`  ${SN[k]||k} ${scn[k]} 题 ${(scn[k]/Q.length*100).toFixed(0)}%`));
const noBond=['R','E','S','T'].filter(ax=>!Q.some(q=>q.axis===ax&&q.scene==='bond'));
const noTaste=['R','E','S','T'].filter(ax=>!Q.some(q=>q.axis===ax&&q.scene==='taste'));
console.log('缺情感题的轴: ' + (noBond.length?noBond.join(','):'无 ✓'));
console.log('缺品味题的轴: ' + (noTaste.length?noTaste.join(','):'无 ✓'));
// 场景交错：连续同类场景过多会让用户疲劳
let run=1,mxRun=1;
const seq=Q.slice().sort((a,b)=>a.order-b.order).map(q=>q.scene);
for(let i=1;i<seq.length;i++){ run = seq[i]===seq[i-1] ? run+1 : 1; mxRun=Math.max(mxRun,run); }
console.log('最长同场景连续: ' + mxRun + ' 道 ' + (mxRun<=2?'✓':'← 应 ≤2'));

// 全选"很像我"和全选"完全不像"的极端情况
console.log('\n=== 极端作答检查 ===');
[[2,'全选 很像我'],[-2,'全选 完全不像'],[0,'全选 说不好']].forEach(([v,label])=>{
  const s={R:0,E:0,S:0,T:0};
  Q.forEach(q=>{ s[q.axis]+=v*q.dir*q.w });
  const ans=Q.map(()=>v);
  const lazy=ans.every(x=>x===ans[0]);
  const rr=lazy?null:rare(s);
  const sg={};
  AXES.forEach(ax=>{ const qs=Q.filter(q=>q.axis===ax);
    sg[ax]=signOf(qs.map(()=>v),qs)[0]; });
  const c=(sg.R>0?'L':'C')+(sg.E>0?'O':'I')+(sg.S>0?'S':'W')+(sg.T>0?'B':'D');
  const id=rr||DATA.map[c];
  console.log(`  ${label}: 分数 R${s.R} E${s.E} S${s.S} T${s.T} -> ${DATA.inst[id].name_zh}${rr?' (稀有)':''}`);
});
