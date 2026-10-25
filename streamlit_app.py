# app.py — Streamlit luxury birthday bouquet (optimised)
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Birthday, Nandini 🌸", page_icon="🌸", layout="centered")

st.markdown("""
<style>
  #MainMenu, footer {visibility:hidden;}
  header[data-testid="stHeader"] {background:transparent;height:0;}
  .block-container {padding:0 !important; max-width:100% !important;}
  iframe {border:none; display:block; width:100%;}
</style>
""", unsafe_allow_html=True)

BIRTHDAY_HTML = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Happy Birthday, Nandini 🌸</title>
<meta name="theme-color" content="#12030b">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Cinzel+Decorative:wght@700&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Great+Vibes&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  :root{
    --gold:#d4af37; --gold-lt:#f7e7a1;
    --blush:#ffd1e1; --ink:#f8dfe8;
  }
  html{background:#0c0208}
  body{
    font-family:'Cormorant Garamond',Georgia,serif;
    color:var(--ink);position:relative;overflow-x:hidden;
    background:
      radial-gradient(circle at 50% 20%, #4a0d2e 0%, #1c0412 55%, #0c0208 100%);
  }
  /* gold frame — fixed, cheap (no shadows) */
  body::before{
    content:"";position:fixed;inset:12px;pointer-events:none;z-index:3;
    border:1px solid rgba(212,175,55,.4);
  }
  .frame-inner{position:fixed;inset:19px;pointer-events:none;z-index:3;border:1px solid rgba(212,175,55,.15)}
  @media (max-width:520px){ body::before{inset:7px} .frame-inner{inset:13px} }

  .corner{position:absolute;width:78px;height:78px;z-index:4;pointer-events:none;opacity:.8}
  .corner--tl{top:12px;left:12px}
  .corner--tr{top:12px;right:12px;transform:scaleX(-1)}
  .corner--bl{bottom:12px;left:12px;transform:scaleY(-1)}
  .corner--br{bottom:12px;right:12px;transform:scale(-1)}
  @media (max-width:520px){
    .corner{width:54px;height:54px}
    .corner--tl,.corner--tr{top:8px}
    .corner--bl,.corner--br{bottom:8px}
    .corner--tl,.corner--bl{left:8px}
    .corner--tr,.corner--br{right:8px}
  }

  /* static gold gradient (no animation → no repaint) */
  .gold{
    background:linear-gradient(100deg,#a87b18 0%,#f7e7a1 22%,#d4af37 45%,#fff4cf 55%,#d4af37 70%,#a87b18 100%);
    -webkit-background-clip:text;background-clip:text;color:transparent;
  }

  #fx{position:fixed;inset:0;width:100%;height:100%;z-index:50;pointer-events:none}

  /* ================= INTRO (in normal flow) ================= */
  #intro{
    position:relative;z-index:100;
    min-height:min(100svh, 760px);
    display:flex;flex-direction:column;align-items:center;justify-content:center;
    text-align:center;padding:48px 24px 38px;
    cursor:pointer;touch-action:manipulation;
    -webkit-tap-highlight-color:transparent;
    background:
      radial-gradient(circle at 50% 45%, rgba(255,122,168,.20), transparent 45%),
      radial-gradient(ellipse at 50% 40%, #3d0b26 0%, #1c0512 62%, #0a0206 100%);
    transition:opacity .7s ease, transform .7s ease;
  }
  #intro.hide{opacity:0;transform:scale(1.08);pointer-events:none}
  #intro.gone{display:none}

  .seal-wrap{position:relative;display:grid;place-items:center}
  .halo{
    position:absolute;width:min(84vw,380px);height:min(84vw,380px);border-radius:50%;
    background:radial-gradient(circle, rgba(255,183,208,.26) 0%, rgba(212,175,55,.14) 32%, transparent 66%);
    pointer-events:none;
  }
  .seal{
    width:126px;height:126px;border-radius:50%;position:relative;z-index:2;
    display:grid;place-items:center;
    background:radial-gradient(circle at 34% 28%, #fff8dc 0%, #f7e7a1 18%, #f3d57a 36%, #d4af37 60%, #a87b18 84%, #6b4a0a 100%);
    box-shadow:
      0 0 0 5px rgba(212,175,55,.16),
      0 18px 40px rgba(0,0,0,.55),
      0 0 60px rgba(212,175,55,.35);
  }
  .seal::before{content:"";position:absolute;inset:10px;border-radius:50%;border:1.5px dashed rgba(90,40,5,.4)}
  .seal span{font-family:'Great Vibes',cursive;font-size:4rem;color:#4a0d1c;line-height:1;transform:translateY(4px)}

  .intro-for{margin-top:30px;font-family:'Cinzel',serif;font-size:.66rem;letter-spacing:.5em;text-transform:uppercase;color:#e8c26a}
  .intro-name{font-family:'Cinzel Decorative',serif;font-weight:700;font-size:clamp(2.3rem,10vw,3.7rem);line-height:1.1;margin-top:8px;letter-spacing:.05em}
  .intro-rule{display:flex;align-items:center;gap:12px;margin-top:14px}
  .intro-rule i{display:block;width:52px;height:1px;background:linear-gradient(90deg,transparent,var(--gold))}
  .intro-rule i:last-child{background:linear-gradient(270deg,transparent,var(--gold))}
  .intro-rule svg{width:15px;height:15px;fill:var(--gold)}
  .intro-tap{margin-top:16px;font-style:italic;font-size:1rem;color:#f2b8cc;animation:fade 2.6s ease-in-out infinite}
  @keyframes fade{0%,100%{opacity:.6}50%{opacity:1}}

  #openBtn{
    margin-top:24px;cursor:pointer;position:relative;z-index:5;
    font-family:'Cinzel',serif;font-size:.7rem;letter-spacing:.3em;text-transform:uppercase;
    color:var(--gold-lt);
    background:linear-gradient(135deg, rgba(212,175,55,.18), rgba(107,20,40,.35));
    border:1px solid rgba(212,175,55,.75);border-radius:999px;padding:15px 30px;
    transition:transform .2s;
    touch-action:manipulation;-webkit-tap-highlight-color:transparent;
  }
  #openBtn:active{transform:scale(.96)}
  #openBtn:focus-visible{outline:2px solid var(--gold-lt);outline-offset:5px}

  /* ================= MAIN ================= */
  main{position:relative;z-index:2;max-width:640px;margin:0 auto;text-align:center;padding:12px 16px 64px}

  .rv{opacity:0}
  body.started .rv{animation:reveal .9s ease var(--d,0s) forwards}
  @keyframes reveal{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}

  .eyebrow{font-family:'Cinzel',serif;font-size:.66rem;letter-spacing:.5em;text-transform:uppercase;color:#e8c26a}
  h1{font-weight:400;margin-top:12px}
  h1 .script{display:block;font-family:'Great Vibes',cursive;font-size:clamp(2.3rem,9.5vw,4rem);line-height:1.05;color:var(--blush)}
  h1 .name{display:block;font-family:'Cinzel Decorative',serif;font-weight:700;font-size:clamp(2rem,10.5vw,4.2rem);letter-spacing:.12em;line-height:1.15;margin-top:6px;padding-left:.12em}
  .ltr{display:inline-block;opacity:0}
  body.started .ltr{animation:letterIn .9s cubic-bezier(.2,1.4,.4,1) var(--d) forwards}
  @keyframes letterIn{from{opacity:0;transform:translateY(34px) scale(.5)}to{opacity:1;transform:none}}
  .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

  .bouquet-wrap{width:min(92vw,520px);margin:14px auto 0;cursor:pointer;position:relative;-webkit-tap-highlight-color:transparent}
  #bouquet{width:100%;height:auto;display:block;overflow:visible}

  .bloom{opacity:0;transform:scale(0);transform-box:fill-box;transform-origin:50% 50%}
  body.started .bloom{animation:bloom .85s cubic-bezier(.2,1.5,.4,1) var(--d,0s) forwards}
  @keyframes bloom{0%{opacity:0;transform:scale(.1)}65%{opacity:1;transform:scale(1.1)}100%{opacity:1;transform:scale(1)}}

  .stems,.leaves,.greenery,.wrapArt,.bowGroup,.tailGroup{opacity:0;transition:opacity .8s ease}
  body.started .stems{opacity:.7;transition-delay:.1s}
  body.started .leaves{opacity:1;transition-delay:.18s}
  body.started .greenery{opacity:1;transition-delay:.22s}
  body.started .wrapArt{opacity:1;transition-delay:1.1s}
  body.started .bowGroup{opacity:1;transition-delay:1.45s}
  body.started .tailGroup{opacity:1;transition-delay:1.6s}

  .glint{transform-box:fill-box;transform-origin:50% 50%;opacity:0}
  body.started .glint{animation:twinkle 3.4s ease-in-out var(--d) infinite}
  @keyframes twinkle{0%,100%{opacity:0}50%{opacity:1}}

  .letter{max-width:34rem;margin:8px auto 0;padding:0 8px}
  .divider{display:flex;align-items:center;justify-content:center;gap:14px;margin:8px 0 22px}
  .divider i{display:block;height:1px;width:min(22vw,100px);background:linear-gradient(90deg,transparent,var(--gold))}
  .divider i:last-child{background:linear-gradient(270deg,transparent,var(--gold))}
  .divider svg{width:20px;height:20px;fill:var(--gold)}
  .line{font-style:italic;font-size:clamp(1.08rem,4.2vw,1.34rem);line-height:1.6;color:var(--ink);margin:0 auto 1.1rem;text-wrap:balance}
  .sign{font-family:'Great Vibes',cursive;font-size:clamp(1.8rem,7.5vw,2.5rem);margin-top:10px;line-height:1.2}

  #more{
    margin-top:28px;cursor:pointer;
    font-family:'Cinzel',serif;font-size:.68rem;letter-spacing:.28em;text-transform:uppercase;
    color:var(--gold-lt);
    background:linear-gradient(135deg, rgba(212,175,55,.14), rgba(107,20,40,.28));
    border:1px solid rgba(212,175,55,.7);border-radius:999px;padding:15px 30px;
    transition:transform .2s;
  }
  #more:active{transform:scale(.97)}
  #more:focus-visible{outline:2px solid var(--gold-lt);outline-offset:5px}

  @media (prefers-reduced-motion: reduce){
    #fx{display:none}
    .rv,.ltr,.bloom,.stems,.leaves,.greenery,.wrapArt,.bowGroup,.tailGroup{opacity:1;transform:none;transition:none;animation:none!important}
    .glint,body.started .glint{animation:none;opacity:.8}
    .intro-tap{animation:none}
  }
</style>
</head>
<body>

<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <g id="cornerPath">
    <path d="M4,4 L40,4 Q62,4 62,26 L62,40" fill="none" stroke="#d4af37" stroke-width="1.3" opacity=".75"/>
    <path d="M4,4 L4,40 Q4,62 26,62 L40,62" fill="none" stroke="#d4af37" stroke-width="1.3" opacity=".75"/>
    <path d="M18,18 Q30,8 42,18 Q32,32 18,18 Z" fill="none" stroke="#d4af37" stroke-width=".8" opacity=".7"/>
    <circle cx="18" cy="18" r="2" fill="#d4af37" opacity=".85"/>
    <circle cx="62" cy="4" r="1.6" fill="#d4af37" opacity=".6"/>
    <circle cx="4" cy="62" r="1.6" fill="#d4af37" opacity=".6"/>
  </g>
</defs></svg>
<svg class="corner corner--tl" viewBox="0 0 100 100" aria-hidden="true"><use href="#cornerPath"/></svg>
<svg class="corner corner--tr" viewBox="0 0 100 100" aria-hidden="true"><use href="#cornerPath"/></svg>
<svg class="corner corner--bl" viewBox="0 0 100 100" aria-hidden="true"><use href="#cornerPath"/></svg>
<svg class="corner corner--br" viewBox="0 0 100 100" aria-hidden="true"><use href="#cornerPath"/></svg>
<div class="frame-inner"></div>

<canvas id="fx" aria-hidden="true"></canvas>

<!-- ===== INTRO ===== -->
<div id="intro" role="button" tabindex="0" aria-label="Open your birthday surprise">
  <div class="seal-wrap">
    <div class="halo"></div>
    <div class="seal" aria-hidden="true"><span>N</span></div>
  </div>
  <p class="intro-for">For the one &amp; only</p>
  <!-- ✏️ EDIT NAME (intro) -->
  <p class="intro-name gold">Nandini</p>
  <div class="intro-rule" aria-hidden="true">
    <i></i>
    <svg viewBox="0 0 24 24"><path d="M12 2l2.4 6.6 6.6.5-5 4.2 1.6 6.5L12 16.4 6.4 19.8l1.6-6.5-5-4.2 6.6-.5z"/></svg>
    <i></i>
  </div>
  <p class="intro-tap">tap anywhere to unveil your surprise</p>
  <button id="openBtn" type="button">✦ Open your surprise ✦</button>
</div>

<main>
  <header>
    <p class="eyebrow rv" style="--d:.15s">✦ Today the world celebrates ✦</p>
    <h1>
      <span class="script rv" style="--d:.35s">Happy Birthday</span>
      <!-- ✏️ EDIT HER NAME HERE -->
      <span class="name" id="name">NANDINI</span>
    </h1>
  </header>

  <div class="bouquet-wrap" id="bouquetWrap">
    <svg id="bouquet" viewBox="0 0 640 960" xmlns="http://www.w3.org/2000/svg" role="img"
         aria-label="Luxury bouquet of peonies, orchids, protea, anthurium and calla lilies in wine, blush and champagne, wrapped in ivory silk with a burgundy sash and gold bow"></svg>
  </div>

  <section class="letter">
    <div class="divider rv" style="--d:1.8s" aria-hidden="true">
      <i></i>
      <svg viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-10-9.2C.3 8.5 2.2 4 6.3 4c2.4 0 4 1.3 5.7 3.4C13.7 5.3 15.3 4 17.7 4c4.1 0 6 4.5 4.3 7.8C19.5 16.4 12 21 12 21z"/></svg>
      <i></i>
    </div>

    <!-- ✏️ EDIT YOUR MESSAGE HERE -->
    <p class="line rv" style="--d:2.1s">On the day you arrived, the world quietly bloomed into
      something softer, wilder, more beautiful — and it has been <em class="gold">flowering</em> ever since.</p>
    <p class="line rv" style="--d:2.6s">You turn ordinary afternoons into something worth remembering,
      and you make everyone lucky enough to be near you feel a little more at home in themselves.</p>
    <p class="line rv" style="--d:3.1s">May this year wrap you in velvet mornings, endless laughter,
      and a love so steady you never once have to wonder if you're enough —
      because you <em class="gold">always, always are.</em></p>
    <p class="line rv" style="--d:3.6s">Every flower in this bouquet is a wish for you — every petal,
      every gilded stem, every promise of softness yet to come.</p>

    <p class="sign gold rv" style="--d:4.2s">Happy birthday, beautiful soul ♥</p>

    <button type="button" id="more" class="rv" style="--d:4.7s">🌸 Shower her with flowers</button>
  </section>
</main>

<script>
/* =========================================================
   0. OPEN LOGIC FIRST (taps can never be lost)
   ========================================================= */
let started = false;
const introEl = document.getElementById('intro');

function openGift(){
  if (started) return;
  started = true;
  introEl.classList.add('hide');
  document.body.classList.add('started');
  setTimeout(() => introEl.classList.add('gone'), 750);
  try { grandOpening(); } catch (e) { console.error(e); }
}
introEl.addEventListener('click', openGift);
document.getElementById('openBtn').addEventListener('click', e => { e.stopPropagation(); openGift(); });
document.addEventListener('pointerdown', openGift, { passive:true });
document.addEventListener('keydown', e => {
  if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openGift(); }
});
document.addEventListener('click', e => {
  if (!started || e.target.closest('#more') || e.target.closest('#openBtn')) return;
  try { burst(e.clientX, e.clientY, 14, 5); } catch (err) {}
});

/* =========================================================
   1. PALETTE
   ========================================================= */
const C = {
  wine:  { main:'#8b1e3f', dark:'#4a0d1c', light:'#c45a7a' },
  plum:  { main:'#6b2c4a', dark:'#3d0b26', light:'#a05878' },
  rose:  { main:'#e63950', dark:'#a4161a', light:'#ffb7c0' },
  blush: { main:'#f4c6d4', dark:'#e89ab0', light:'#fff0f4' },
  champ: { main:'#f5e6c8', dark:'#e0c896', light:'#fffaf0' },
  sage:  { main:'#8fa88a', dark:'#5c7356' }
};
const n1 = v => v.toFixed(1);
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* =========================================================
   2. FLOWER SHAPES — leaner node counts
   ========================================================= */
function rose(r, c){
  let s = '';
  for (let i = 0; i < 6; i++)
    s += `<ellipse cy="${n1(-r*.55)}" rx="${n1(r*.4)}" ry="${n1(r*.55)}" fill="${c.main}" transform="rotate(${i*60})"/>`;
  for (let i = 0; i < 5; i++)
    s += `<ellipse cy="${n1(-r*.3)}" rx="${n1(r*.26)}" ry="${n1(r*.35)}" fill="${c.dark}" opacity=".9" transform="rotate(${i*72+25})"/>`;
  s += `<circle r="${n1(r*.16)}" fill="${c.light}"/><circle r="${n1(r*.07)}" fill="${c.dark}"/>`;
  return s;
}
function peony(r, c){
  let s = '';
  for (let i = 0; i < 8; i++)
    s += `<path d="M0,${n1(-r*.15)} C${n1(-r*.45)},${n1(-r*.4)} ${n1(-r*.55)},${n1(-r*.8)} ${n1(-r*.2)},${n1(-r*.98)}
      C${n1(r*.15)},${n1(-r*1.05)} ${n1(r*.5)},${n1(-r*.7)} 0,${n1(-r*.45)} Z"
      fill="${c.main}" transform="rotate(${i*45})"/>`;
  for (let i = 0; i < 5; i++)
    s += `<ellipse cy="${n1(-r*.34)}" rx="${n1(r*.19)}" ry="${n1(r*.32)}" fill="${c.dark}" transform="rotate(${i*72+20})"/>`;
  s += `<circle r="${n1(r*.16)}" fill="${c.light}"/><circle r="${n1(r*.07)}" fill="${c.dark}"/>`;
  return s;
}
function orchid(r, c){
  let s = '';
  for (let i = 0; i < 3; i++)
    s += `<ellipse cy="${n1(-r*.47)}" rx="${n1(r*.18)}" ry="${n1(r*.55)}" fill="${c.dark}" transform="rotate(${i*120})"/>`;
  s += `<ellipse cx="${n1(-r*.45)}" cy="${n1(-r*.08)}" rx="${n1(r*.48)}" ry="${n1(r*.15)}" fill="${c.main}" transform="rotate(-25)"/>`;
  s += `<ellipse cx="${n1(r*.45)}" cy="${n1(-r*.08)}" rx="${n1(r*.48)}" ry="${n1(r*.15)}" fill="${c.main}" transform="rotate(25)"/>`;
  s += `<path d="M0,${n1(-r*.08)} C${n1(-r*.35)},${n1(r*.2)} ${n1(-r*.3)},${n1(r*.6)} 0,${n1(r*.62)}
    C${n1(r*.3)},${n1(r*.6)} ${n1(r*.35)},${n1(r*.2)} 0,${n1(-r*.08)} Z"
    fill="${c.light}" stroke="${c.main}" stroke-width="1"/>`;
  s += `<circle r="${n1(r*.06)}" cy="${n1(-r*.06)}" fill="#f7e7a1"/>`;
  return s;
}
function ranunculus(r, c){
  let s = '';
  for (let i = 4; i >= 1; i--)
    s += `<circle r="${n1(r*i/4)}" fill="${i%2 ? c.main : c.dark}"/>`;
  s += `<circle r="${n1(r*.14)}" fill="${c.light}"/>`;
  return s;
}
function anthurium(r, c){
  return `<path d="M0,${n1(-r*.15)} C${n1(-r*.55)},${n1(-r*.75)} ${n1(-r*1.05)},${n1(-r*.35)} ${n1(-r*.7)},${n1(r*.35)}
    C${n1(-r*.4)},${n1(r*.85)} 0,${n1(r*.55)} 0,${n1(r*.15)}
    C0,${n1(r*.55)} ${n1(r*.4)},${n1(r*.85)} ${n1(r*.7)},${n1(r*.35)}
    C${n1(r*1.05)},${n1(-r*.35)} ${n1(r*.55)},${n1(-r*.75)} 0,${n1(-r*.15)} Z"
    fill="${c.main}" stroke="${c.dark}" stroke-width="1.2"/>
    <path d="M0,0 Q${n1(r*.08)},${n1(-r*.5)} 0,${n1(-r*.85)}" stroke="${c.light}" stroke-width="${n1(r*.11)}" fill="none" stroke-linecap="round"/>`;
}
function protea(r, c){
  let s = '';
  for (let i = 0; i < 11; i++)
    s += `<path d="M0,${n1(-r*.15)} L${n1(-r*.09)},${n1(-r*.85)} L0,${n1(-r*1.1)} L${n1(r*.09)},${n1(-r*.85)} Z"
      fill="${i%2 ? c.main : c.dark}" transform="rotate(${i*32.7})"/>`;
  s += `<circle r="${n1(r*.26)}" fill="${c.dark}"/><circle r="${n1(r*.1)}" fill="#f7e7a1"/>`;
  return s;
}
function calla(r, c){
  return `<path d="M0,${n1(-r*.85)} C${n1(-r*.4)},${n1(-r*.55)} ${n1(-r*.5)},${n1(r*.25)} 0,${n1(r*.7)}
    C${n1(r*.5)},${n1(r*.25)} ${n1(r*.4)},${n1(-r*.55)} 0,${n1(-r*.85)} Z"
    fill="${c.main}" stroke="${c.dark}" stroke-width="1"/>
    <path d="M0,${n1(r*.55)} L0,${n1(-r*.35)}" stroke="#f7e7a1" stroke-width="${n1(r*.09)}" stroke-linecap="round"/>`;
}
function eucalyptus(len, c, dir){
  let s = `<g transform="rotate(${dir})">`;
  s += `<path d="M0,0 Q${n1(len*.15)},${n1(-len*.5)} ${n1(len*.2)},${n1(-len)}" stroke="${c.dark}" stroke-width="1.6" fill="none"/>`;
  for (let i = 1; i <= 5; i++){
    const t = i/6, y = -len*t, x = len*.18*t, rr = len*(.14 - t*.05);
    s += `<ellipse cx="${n1(x-len*.11)}" cy="${n1(y)}" rx="${n1(rr)}" ry="${n1(rr*1.3)}" fill="${c.main}" opacity=".92"/>`;
    s += `<ellipse cx="${n1(x+len*.11)}" cy="${n1(y)}" rx="${n1(rr)}" ry="${n1(rr*1.3)}" fill="${c.main}" opacity=".92"/>`;
  }
  return s + `</g>`;
}
function leafShape(len, c){
  return `<path d="M0,0 Q${n1(len*.5)},${n1(-len*.44)} ${len},0 Q${n1(len*.5)},${n1(len*.44)} 0,0 Z" fill="${c}"/>`;
}

/* =========================================================
   3. ARRANGEMENT — 16 flowers total
   ========================================================= */
const flowers = [
  { t:'orchid',     x:320, y:96,  r:36, c:C.champ, rot:  0, d:.30 },
  { t:'peony',      x:214, y:150, r:42, c:C.blush, rot: 18, d:.34 },
  { t:'peony',      x:426, y:150, r:42, c:C.rose,  rot:-18, d:.37 },
  { t:'protea',     x:520, y:256, r:34, c:C.wine,  rot:  0, d:.41 },
  { t:'anthurium',  x:150, y:330, r:32, c:C.rose,  rot:-22, d:.45 },
  { t:'anthurium',  x:490, y:330, r:32, c:C.wine,  rot: 22, d:.48 },
  { t:'peony',      x:320, y:286, r:60, c:C.wine,  rot:  0, d:.12 },
  { t:'calla',      x:250, y:330, r:32, c:C.champ, rot:-18, d:.55 },
  { t:'calla',      x:392, y:330, r:32, c:C.blush, rot: 18, d:.58 },
  { t:'rose',       x:320, y:378, r:34, c:C.rose,  rot:  0, d:.62 },
  { t:'orchid',     x:470, y:420, r:28, c:C.plum,  rot: 35, d:.66 },
  { t:'orchid',     x:170, y:420, r:28, c:C.wine,  rot:-35, d:.69 },
  { t:'ranunculus', x:240, y:410, r:24, c:C.champ, rot:  0, d:.73 },
  { t:'ranunculus', x:400, y:410, r:24, c:C.blush, rot:  0, d:.76 },
  { t:'rose',       x:286, y:446, r:26, c:C.wine,  rot: 12, d:.80 },
  { t:'rose',       x:354, y:446, r:26, c:C.rose,  rot:-12, d:.83 }
];
const greenery = [
  { x:86,  y:250, len:140, dir:-168, d:.20 },
  { x:554, y:250, len:140, dir:-12,  d:.22 },
  { x:70,  y:400, len:130, dir:-148, d:.25 },
  { x:570, y:400, len:130, dir:-32,  d:.27 },
  { x:320, y:70,  len:95,  dir:-90,  d:.16 }
];
const leaves = [
  { x:92,  y:340, len:66, a:-158, c:'#2d6a4f' },
  { x:548, y:340, len:66, a:-22,  c:'#2d6a4f' },
  { x:120, y:492, len:60, a:-148, c:'#1b4332' },
  { x:520, y:492, len:60, a:-32,  c:'#1b4332' }
];
const draw = f =>
  f.t==='peony' ? peony(f.r,f.c) :
  f.t==='rose' ? rose(f.r,f.c) :
  f.t==='ranunculus' ? ranunculus(f.r,f.c) :
  f.t==='orchid' ? orchid(f.r,f.c) :
  f.t==='anthurium' ? anthurium(f.r,f.c) :
  f.t==='protea' ? protea(f.r,f.c) :
  f.t==='calla' ? calla(f.r,f.c) : '';

/* =========================================================
   4. BUILD SVG
   ========================================================= */
let heroBlasts = [];
function buildBouquet(){
  const out = [];
  out.push(`<defs>
    <linearGradient id="wrapGrad" x1=".15" y1="0" x2=".85" y2="1">
      <stop offset="0%" stop-color="#fffaf0"/><stop offset="35%" stop-color="#f5e6c8"/>
      <stop offset="75%" stop-color="#e0c896"/><stop offset="100%" stop-color="#b08e56"/>
    </linearGradient>
    <linearGradient id="sashGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#a42a4f"/><stop offset="50%" stop-color="#6b1428"/><stop offset="100%" stop-color="#3d0b1c"/>
    </linearGradient>
    <linearGradient id="bowGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fff4cf"/><stop offset="40%" stop-color="#f3d57a"/>
      <stop offset="75%" stop-color="#d4af37"/><stop offset="100%" stop-color="#a87b18"/>
    </linearGradient>
    <linearGradient id="stemGrad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#1b4332"/><stop offset="100%" stop-color="#3f7d4a"/>
    </linearGradient>
  </defs>`);

  /* greenery */
  out.push('<g class="greenery">');
  greenery.forEach(g => out.push(`<g transform="translate(${g.x},${g.y})">
    <g class="bloom" style="--d:${g.d}s">${eucalyptus(g.len, C.sage, g.dir)}</g></g>`));
  out.push('</g>');

  /* back wrap */
  out.push(`<g class="wrapArt">
    <path d="M 80 220 Q 40 420 120 620 L 520 620 Q 600 420 560 220 Q 440 150 320 150 Q 200 150 80 220 Z"
      fill="url(#wrapGrad)" stroke="#a87b18" stroke-width="1.4" stroke-opacity=".6"/>
  </g>`);

  /* stems (12 only) */
  out.push('<g class="stems">');
  for (let i = 0; i < 12; i++){
    const a = (i/12)*Math.PI*2;
    const x = 320 + Math.cos(a)*180, y = 290 + Math.sin(a)*180;
    out.push(`<path d="M 320 630 Q ${n1(320+(x-320)*.6)} 460 ${n1(x)} ${n1(y)}"
      fill="none" stroke="url(#stemGrad)" stroke-width="3.5" stroke-linecap="round"/>`);
  }
  out.push('</g>');

  /* leaves */
  out.push('<g class="leaves">');
  leaves.forEach(l => out.push(`<g transform="translate(${l.x},${l.y}) rotate(${l.a})">${leafShape(l.len, l.c)}</g>`));
  out.push('</g>');

  /* flowers, back to front */
  const sorted = flowers.slice().sort((a,b) => a.y - b.y);
  sorted.forEach(f => out.push(`<g transform="translate(${n1(f.x)},${n1(f.y)}) rotate(${n1(f.rot)})">
    <g class="bloom" style="--d:${f.d.toFixed(2)}s">${draw(f)}</g></g>`));

  /* hero flowers that emit a small burst when they open */
  heroBlasts = [flowers[6], flowers[0], flowers[1], flowers[2], flowers[9], flowers[14]];

  /* front wrap */
  out.push(`<g class="wrapArt">
    <path d="M 130 420 Q 140 540 200 640 L 440 640 Q 500 540 510 420 Q 420 500 320 500 Q 220 500 130 420 Z"
      fill="url(#wrapGrad)" stroke="#a87b18" stroke-width="1.2" stroke-opacity=".5"/>
    <path d="M 200 640 Q 230 560 320 540 Q 410 560 440 640" fill="none" stroke="#fff4cf" stroke-width="1" opacity=".5"/>
  </g>`);

  /* sash */
  out.push(`<g class="wrapArt" style="transition-delay:1.2s">
    <rect x="176" y="616" width="288" height="50" rx="4" fill="url(#sashGrad)"/>
    <rect x="176" y="618" width="288" height="2" fill="#f7e7a1" opacity=".65"/>
    <rect x="176" y="662" width="288" height="2" fill="#f7e7a1" opacity=".5"/>
  </g>`);

  /* skirt */
  out.push(`<g class="wrapArt" style="transition-delay:1.35s">
    <path d="M 200 666 L 440 666 L 490 890 Q 320 935 150 890 Z"
      fill="url(#wrapGrad)" stroke="#a87b18" stroke-width="1.3" stroke-opacity=".55"/>
    <path d="M 300 666 Q 306 800 300 915" fill="none" stroke="#fff4cf" stroke-width="1" opacity=".45"/>
    <path d="M 180 872 Q 320 915 460 872" fill="none" stroke="#fff4cf" stroke-width="1" opacity=".5"/>
  </g>`);

  /* bow */
  out.push(`<g class="bowGroup">
    <path d="M 320 640 C 236 590 184 624 204 678 C 218 716 284 696 320 640 Z" fill="url(#bowGrad)" stroke="#7d5a0f" stroke-width="1.3"/>
    <path d="M 320 640 C 404 590 456 624 436 678 C 422 716 356 696 320 640 Z" fill="url(#bowGrad)" stroke="#7d5a0f" stroke-width="1.3"/>
    <ellipse cx="320" cy="642" rx="24" ry="18" fill="#c9971f" stroke="#7d5a0f" stroke-width="1.2"/>
    <ellipse cx="316" cy="636" rx="9" ry="6" fill="#f7e7a1" opacity=".8"/>
  </g>`);

  /* tails */
  out.push(`<g class="tailGroup">
    <path d="M 302 652 C 274 752 248 862 230 918 L 264 900 L 290 940 L 296 884 C 306 792 312 716 312 652 Z"
      fill="url(#bowGrad)" stroke="#7d5a0f" stroke-width="1.2"/>
    <path d="M 338 652 C 366 752 392 862 410 918 L 376 900 L 350 940 L 344 884 C 334 792 328 716 328 652 Z"
      fill="url(#bowGrad)" stroke="#7d5a0f" stroke-width="1.2"/>
  </g>`);

  /* tag */
  out.push(`<g class="wrapArt" style="transition-delay:1.7s">
    <path d="M 374 666 Q 398 712 410 750" stroke="#d4af37" stroke-width="1.2" fill="none"/>
    <g transform="translate(412, 752) rotate(8)">
      <rect x="-24" y="-34" width="48" height="60" rx="4" fill="#fffaf0" stroke="#d4af37" stroke-width="1.2"/>
      <text x="0" y="-10" font-family="'Great Vibes', cursive" font-size="13" fill="#6b1428" text-anchor="middle">Happy</text>
      <text x="0" y="6"  font-family="'Great Vibes', cursive" font-size="13" fill="#6b1428" text-anchor="middle">Birthday</text>
      <path d="M 0,13 L 3,18 L 8,18 L 4,22 L 6,27 L 0,24 L -6,27 L -4,22 L -8,18 L -3,18 Z" fill="#d4af37"/>
    </g>
  </g>`);

  /* 4 glints only */
  [[100,240,0],[540,250,1.2],[320,60,2.1],[560,420,1.6]].forEach(g =>
    out.push(`<g transform="translate(${g[0]},${g[1]})">
      <path class="glint" style="--d:${g[2]}s" d="M0,-10 Q1.5,-1.5 10,0 Q1.5,1.5 0,10 Q-1.5,1.5 -10,0 Q-1.5,-1.5 0,-10Z" fill="#fff4cf"/></g>`));

  document.getElementById('bouquet').innerHTML = out.join('');
}

function splitName(){
  const el = document.getElementById('name');
  const txt = el.textContent.trim();
  el.innerHTML = `<span class="sr">${txt}</span>` + [...txt].map((ch,i)=>
    `<span class="ltr gold" aria-hidden="true" style="--d:${(0.65 + i*0.1).toFixed(2)}s">${ch === ' ' ? '&nbsp;' : ch}</span>`
  ).join('');
}

/* =========================================================
   5. PARTICLE ENGINE — small & capped
   ========================================================= */
const cvs = document.getElementById('fx');
const ctx = cvs.getContext('2d', { alpha:true });
let W = 0, H = 0, DPR = 1;

function resize(){
  DPR = Math.min(window.devicePixelRatio || 1, 1.5);
  W = innerWidth; H = innerHeight;
  cvs.width  = Math.floor(W * DPR);
  cvs.height = Math.floor(H * DPR);
}
resize();
let resizeT;
addEventListener('resize', () => { clearTimeout(resizeT); resizeT = setTimeout(resize, 200); });

const rand = (a,b) => a + Math.random()*(b-a);
const pick = a => a[Math.random()*a.length|0];
const TAU = Math.PI*2;

function mk(fn){
  const s = document.createElement('canvas');
  s.width = s.height = 64;
  const c = s.getContext('2d');
  c.translate(32,32); c.scale(1.15,1.15);
  fn(c);
  return s;
}
function flowerSprite(col, dark){ return mk(c=>{
  for (let i = 0; i < 5; i++){
    c.save(); c.rotate(i*TAU/5);
    c.beginPath(); c.ellipse(0,-11,8,11,0,0,TAU);
    c.fillStyle = col; c.fill(); c.restore();
  }
  c.beginPath(); c.arc(0,0,4,0,TAU); c.fillStyle = dark; c.fill();
});}
function petalSprite(col){ return mk(c=>{
  c.beginPath(); c.moveTo(0,17);
  c.bezierCurveTo(-12,8,-11,-11,-3,-17); c.lineTo(0,-13); c.lineTo(3,-17);
  c.bezierCurveTo(11,-11,12,8,0,17);
  c.fillStyle = col; c.fill();
});}
function leafSprite(col){ return mk(c=>{
  c.beginPath(); c.moveTo(0,18); c.quadraticCurveTo(-11,0,0,-18); c.quadraticCurveTo(11,0,0,18);
  c.fillStyle = col; c.fill();
});}
function heartSprite(col){ return mk(c=>{
  c.beginPath(); c.moveTo(0,15);
  c.bezierCurveTo(-22,1,-15,-18,0,-7); c.bezierCurveTo(15,-18,22,1,0,15);
  c.fillStyle = col; c.fill();
});}
function goldSprite(){ return mk(c=>{
  c.fillStyle = '#fff4cf'; c.beginPath();
  c.moveTo(0,-11); c.quadraticCurveTo(1.2,-1.2,11,0); c.quadraticCurveTo(1.2,1.2,0,11);
  c.quadraticCurveTo(-1.2,1.2,-11,0); c.quadraticCurveTo(-1.2,-1.2,0,-11); c.fill();
});}

const SPR = {
  flower:[ flowerSprite('#e63950','#6b1428'), flowerSprite('#f4c6d4','#a4161a'),
           flowerSprite('#f5e6c8','#a87b18'), flowerSprite('#8b1e3f','#3d0b1c') ],
  petal: [ petalSprite('#f4c6d4'), petalSprite('#8b1e3f'), petalSprite('#e63950'), petalSprite('#f5e6c8') ],
  leaf:  [ leafSprite('#2d6a4f') ],
  heart: [ heartSprite('#e63950'), heartSprite('#f4c6d4') ],
  gold:  [ goldSprite() ]
};
function kind(){
  const r = Math.random();
  return r < .5 ? 'flower' : r < .8 ? 'petal' : r < .9 ? 'heart' : r < .96 ? 'leaf' : 'gold';
}

const P = [];
const MAX = 160;
let ambient = 0;

function add(o){
  if (reduce || P.length >= MAX) return;
  P.push(Object.assign({
    rot:rand(0,TAU), vr:rand(-.06,.06), flip:rand(0,TAU), vf:rand(.02,.05),
    sway:0, swayP:rand(0,TAU), age:0, drag:.98, g:.09, term:4.5, life:200, op:1, fi:6
  }, o));
}
function sparks(x,y,n,power){
  for (let i = 0; i < n; i++){
    const a = Math.random()*TAU, sp = power*rand(.3,1.3);
    add({ spr:SPR.gold[0], x, y, vx:Math.cos(a)*sp, vy:Math.sin(a)*sp, size:rand(7,16),
          g:.02, drag:.94, life:rand(45,90), twinkle:true, vr:0 });
  }
}
function burst(x,y,n=30,power=8,ring=false){
  for (let i = 0; i < n; i++){
    const a = ring ? i/n*TAU : Math.random()*TAU;
    const sp = power*(ring ? rand(.85,1.05) : rand(.25,1));
    const k = kind();
    add({ spr:pick(SPR[k]), x, y, vx:Math.cos(a)*sp, vy:Math.sin(a)*sp - power*.25,
          size:k==='flower'?rand(18,30):rand(10,18), g:rand(.06,.1), drag:rand(.965,.98),
          life:rand(150,230), sway:rand(.2,.7) });
  }
  if (n > 16) sparks(x, y, Math.round(n*.4), power);
}
function cannon(x,y,dir,n,power){
  for (let i = 0; i < n; i++){
    const a = dir + rand(-.3,.3), sp = power*rand(.6,1.15), k = kind();
    add({ spr:pick(SPR[k]), x, y, vx:Math.cos(a)*sp, vy:Math.sin(a)*sp,
          size:k==='flower'?rand(16,28):rand(10,18), g:.14, drag:.988, term:3.6,
          life:rand(240,320), sway:rand(.3,.9) });
  }
  sparks(x, y, n/2, power*.7);
}
function rain(n){
  for (let i = 0; i < n; i++){
    const k = kind();
    add({ spr:pick(SPR[k]), x:rand(0,W), y:rand(-H*.7,-20), vx:rand(-.5,.5), vy:rand(1.4,2.8),
          g:.004, drag:1, term:4, life:1e9, size:k==='flower'?rand(16,28):rand(10,18), sway:rand(.4,1) });
  }
}
function spawnAmbient(){
  ambient++;
  add({ spr:pick(SPR.petal), x:rand(0,W), y:-25, vx:rand(-.25,.25), vy:rand(.6,1.1),
        g:0, drag:1, term:9, life:1e9, size:rand(9,16), sway:rand(.3,.9),
        op:rand(.5,.8), amb:true });
}

let running = false, last = 0, acc = 0, ambientTimer = 0;

function tick(now){
  if (!running) return;
  const dt = Math.min(2.5, (now - last)/16.667); last = now;

  ctx.setTransform(1,0,0,1,0,0);
  ctx.clearRect(0,0,cvs.width,cvs.height);

  if (started){
    ambientTimer += dt;
    if (ambient < 10 && ambientTimer > 18){ ambientTimer = 0; spawnAmbient(); }
  }

  for (let i = P.length-1; i >= 0; i--){
    const p = P[i];
    p.age += dt;
    const left = p.life - p.age;
    if (left <= 0 || p.y > H+60 || p.x < -70 || p.x > W+70){
      if (p.amb) ambient--;
      P.splice(i,1); continue;
    }
    const dk = Math.pow(p.drag, dt);
    p.vx *= dk;
    p.vy = p.vy*dk + p.g*dt;
    if (p.vy > p.term) p.vy = p.term;
    p.x += (p.vx + Math.sin(p.age*.03 + p.swayP)*p.sway)*dt;
    p.y += p.vy*dt;
    p.rot += p.vr*dt; p.flip += p.vf*dt;

    let a = p.op;
    if (left < 30) a *= left/30;
    if (p.age < p.fi) a *= p.age/p.fi;
    if (p.twinkle) a *= .55 + .45*Math.sin(p.age*.35 + p.swayP);
    ctx.globalAlpha = Math.max(0, a);

    const sx = p.twinkle ? 1 : Math.cos(p.flip);
    const cr = Math.cos(p.rot), sr = Math.sin(p.rot), s = p.size;
    ctx.setTransform(DPR*cr*sx, DPR*sr*sx, -DPR*sr, DPR*cr, DPR*p.x, DPR*p.y);
    ctx.drawImage(p.spr, -s/2, -s/2, s, s);
  }
  ctx.globalAlpha = 1;
  ctx.setTransform(1,0,0,1,0,0);
  requestAnimationFrame(tick);
}

function startLoop(){
  if (reduce || running) return;
  running = true; last = performance.now();
  requestAnimationFrame(tick);
}
document.addEventListener('visibilitychange', () => {
  if (document.hidden){ running = false; }
  else if (started){ running = true; last = performance.now(); requestAnimationFrame(tick); }
});

/* =========================================================
   6. CHOREOGRAPHY — short, finite bursts
   ========================================================= */
function cannons(){
  const power = Math.sqrt(H)*.55;
  cannon(-10, H+10, -Math.PI/3, 34, power);
  cannon(W+10, H+10, -Math.PI*2/3, 34, power);
}
function bloomBlasts(){
  const svg = document.getElementById('bouquet');
  if (!svg) return;
  heroBlasts.forEach(f => setTimeout(() => {
    const r = svg.getBoundingClientRect();
    const x = r.left + f.x/640*r.width;
    const y = r.top + f.y/960*r.height;
    if (y > -40 && y < H+40) burst(x, y, 8, 3.4);
  }, (f.d + .35)*1000));
}
function grandOpening(){
  startLoop();
  burst(W/2, H*.42, 36, 9, true);
  burst(W/2, H*.42, 22, 6);
  [[.2,.3],[.8,.28],[.5,.16]].forEach((p,i) =>
    setTimeout(() => burst(W*p[0], H*p[1], 20, 6), 400 + i*320));
  setTimeout(cannons, 1500);
  setTimeout(() => rain(22), 2200);
  bloomBlasts();
}

/* =========================================================
   7. BOOT — listeners already attached above
   ========================================================= */
try { buildBouquet(); } catch(e){ console.error(e); }
try { splitName(); }    catch(e){ console.error(e); }

document.getElementById('more').addEventListener('click', () => {
  startLoop();
  burst(W/2, H*.4, 40, 9, true);
  cannons();
  rain(30);
});
</script>
</body>
</html>
"""

components.html(BIRTHDAY_HTML, height=1900, scrolling=True)
