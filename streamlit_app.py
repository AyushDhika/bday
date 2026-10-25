import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday, Nandini 🌸",
    page_icon="🌸",
    layout="centered",
)

# Minimal Streamlit CSS reset
st.markdown(
    """
    <style>
      .stApp { margin: 0 !important; padding: 0 !important; overflow: hidden !important; }
      .main .block-container { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

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
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;800&family=Cinzel+Decorative:wght@700;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Great+Vibes&family=Italiana&display=swap" rel="stylesheet">
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    :root{
      --gold:#d4af37; --gold-lt:#f7e7a1; --gold-dk:#a87b18;
      --wine:#6b1428; --wine-dk:#3d0b1c; --plum:#4a0d2e;
      --blush:#ffd1e1; --champ:#f5e6c8;
      --ink:#f8dfe8;
    }
    html{min-height:100%;background:#0c0208; overflow-y:auto; -webkit-overflow-scrolling:touch;}
    body{
      font-family:'Cormorant Garamond',Georgia,serif;
      min-height:100vh;color:var(--ink);
      background:
        radial-gradient(circle at 50% 30%, rgba(107,20,40,.55) 0%, transparent 55%),
        radial-gradient(circle at 15% 85%, rgba(212,175,55,.10), transparent 40%),
        radial-gradient(circle at 85% 15%, rgba(255,122,168,.10), transparent 40%),
        radial-gradient(ellipse at 50% 0%, #3d0b26 0%, #1c0412 50%, #0c0208 100%);
      background-attachment:fixed;
      padding:46px 16px 70px;
      overflow-x:hidden; overflow-y:auto; position:relative;
      touch-action:pan-y; -webkit-tap-highlight-color:transparent; user-select:none;
    }
    body::after{
      content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
      background-image:
        radial-gradient(rgba(255,255,255,.025) 1px, transparent 1px),
        radial-gradient(rgba(0,0,0,.05) 1px, transparent 1px);
      background-size:3px 3px, 7px 7px;
      background-position:0 0, 2px 3px;
      mix-blend-mode:overlay;opacity:.5;
    }
    body::before{
      content:"";position:fixed;inset:14px;pointer-events:none;z-index:3;
      border:1px solid rgba(212,175,55,.42);
      box-shadow:inset 0 0 0 4px rgba(0,0,0,.18), inset 0 0 0 5px rgba(212,175,55,.14);
    }
    .frame-inner{
      position:fixed;inset:22px;pointer-events:none;z-index:3;
      border:1px solid rgba(212,175,55,.16);
    }
    @media (max-width:520px){ body::before{inset:8px} .frame-inner{inset:14px} }

    .corner{
      position:fixed;width:94px;height:94px;z-index:4;pointer-events:none;
      opacity:.85;
    }
    .corner--tl{top:18px;left:18px}
    .corner--tr{top:18px;right:18px;transform:scaleX(-1)}
    .corner--bl{bottom:18px;left:18px;transform:scaleY(-1)}
    .corner--br{bottom:18px;right:18px;transform:scale(-1)}
    @media (max-width:520px){
      .corner{width:66px;height:66px}
      .corner--tl{top:11px;left:11px}
      .corner--tr{top:11px;right:11px}
      .corner--bl{bottom:11px;left:11px}
      .corner--br{bottom:11px;right:11px}
    }

    .gold{
      background:linear-gradient(100deg,#8a6516 0%,#f7e7a1 18%,#d4af37 34%,#fff4cf 50%,#c9971f 64%,#f3d57a 82%,#8a6516 100%);
      background-size:220% 100%;
      -webkit-background-clip:text;background-clip:text;color:transparent;
      animation:shimmer 6s linear infinite;
      filter:drop-shadow(0 1px 0 rgba(0,0,0,.4));
    }
    @keyframes shimmer{from{background-position:0% 50%}to{background-position:-220% 50%}}

    .halo{
      position:absolute;width:420px;height:420px;border-radius:50%;
      background:radial-gradient(circle, rgba(255,183,208,.28) 0%, rgba(212,175,55,.16) 30%, transparent 65%);
      filter:blur(18px);animation:halo 4s ease-in-out infinite;pointer-events:none;
    }
    @keyframes halo{0%,100%{transform:scale(1);opacity:.85}50%{transform:scale(1.09);opacity:1}}

    #fx{position:fixed;inset:0;width:100%;height:100%;z-index:50;pointer-events:none}

    #intro{
      position:fixed;inset:0;z-index:999999;cursor:pointer;overflow:hidden;
      display:flex;flex-direction:column;align-items:center;justify-content:center;
      text-align:center;padding:24px 24px 30vh;
      background:
        radial-gradient(circle at 50% 42%, rgba(255,122,168,.20), transparent 42%),
        radial-gradient(circle at 50% 50%, rgba(212,175,55,.10), transparent 55%),
        radial-gradient(ellipse at 50% 40%, #3d0b26 0%, #1c0512 62%, #0a0206 100%);
      transition:opacity 1.1s ease, transform 1.3s ease, visibility 1.1s;
      touch-action:manipulation; -webkit-tap-highlight-color:transparent; user-select:none;
    }
    #intro.hide{opacity:0;visibility:hidden;pointer-events:none;transform:scale(1.14)}
    #intro:focus-visible{outline:none}
    #intro:focus-visible .seal{box-shadow:0 0 0 3px #fff4cf, 0 0 80px rgba(212,175,55,.8)}

    .seal-wrap{position:relative;display:grid;place-items:center}
    .seal{
      width:168px;height:168px;border-radius:50%;position:relative;
      display:grid;place-items:center;z-index:2;
      background:
        radial-gradient(circle at 34% 28%, #fff8dc 0%, #f7e7a1 16%, #f3d57a 34%, #d4af37 58%, #a87b18 82%, #6b4a0a 100%);
      box-shadow:
        0 0 0 8px rgba(212,175,55,.16),
        0 22px 55px rgba(0,0,0,.6),
        0 0 90px rgba(212,175,55,.4),
        inset 0 -8px 22px rgba(107,74,10,.5),
        inset 0 6px 12px rgba(255,248,220,.55);
      animation:sealPulse 3s ease-in-out infinite;
    }
    .seal::before{
      content:"";position:absolute;inset:11px;border-radius:50%;
      border:2px dashed rgba(90,40,5,.5);
    }
    .seal::after{
      content:"";position:absolute;inset:-8px;border-radius:50%;
      border:1px solid rgba(247,231,161,.65);
      animation:ripple 3s ease-out infinite;
    }
    .seal span{
      font-family:'Great Vibes',cursive;font-size:5.2rem;color:#4a0d1c;line-height:1;
      transform:translateY(5px);
      text-shadow:0 1px 0 rgba(255,244,207,.7), 0 -1px 0 rgba(60,20,0,.5);
    }
    @keyframes sealPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.055)}}
    @keyframes ripple{from{transform:scale(1);opacity:.95}to{transform:scale(1.75);opacity:0}}

    .intro-for{
      margin-top:38px;font-family:'Cinzel',serif;font-size:.7rem;
      letter-spacing:.55em;text-transform:uppercase;color:#e8c26a;
      text-shadow:0 0 12px rgba(212,175,55,.5);
    }
    .intro-name{
      font-family:'Cinzel Decorative',serif;font-weight:700;
      font-size:clamp(2.6rem,12vw,4.2rem);line-height:1.1;
      margin-top:10px;letter-spacing:.06em;
    }
    .intro-rule{
      display:flex;align-items:center;gap:12px;margin-top:16px;
    }
    .intro-rule i{display:block;width:60px;height:1px;
      background:linear-gradient(90deg,transparent,var(--gold))}
    .intro-rule i:last-child{background:linear-gradient(270deg,transparent,var(--gold))}
    .intro-rule svg{width:16px;height:16px;fill:var(--gold)}
    .intro-tap{
      margin-top:20px;font-style:italic;font-size:1.05rem;color:#f2b8cc;
      animation:breathe 2.4s ease-in-out infinite;letter-spacing:.02em;
    }
    @keyframes breathe{0%,100%{opacity:.55}50%{opacity:1}}

    main{position:relative;z-index:2;max-width:660px;margin:0 auto;text-align:center}

    .rv{opacity:0}
    body.started .rv{animation:reveal 1.3s cubic-bezier(.2,.7,.2,1) var(--d,0s) forwards}
    @keyframes reveal{
      from{opacity:0;transform:translateY(24px);filter:blur(7px)}
      to  {opacity:1;transform:none;filter:blur(0)}
    }

    .eyebrow{
      font-family:'Cinzel',serif;font-size:.7rem;letter-spacing:.55em;
      text-transform:uppercase;color:#e8c26a;
      text-shadow:0 0 14px rgba(212,175,55,.4);
    }
    h1{font-weight:400;margin-top:14px}
    h1 .script{
      display:block;font-family:'Great Vibes',cursive;
      font-size:clamp(2.5rem,10vw,4.4rem);line-height:1.05;color:var(--blush);
      text-shadow:0 0 30px rgba(255,122,168,.6), 0 2px 12px rgba(0,0,0,.5);
    }
    h1 .name{
      display:block;font-family:'Cinzel Decorative',serif;font-weight:900;
      font-size:clamp(2.3rem,12vw,4.8rem);letter-spacing:.12em;line-height:1.15;
      margin-top:6px;padding-left:.12em;
      filter:drop-shadow(0 0 18px rgba(212,175,55,.5)) drop-shadow(0 6px 14px rgba(0,0,0,.55));
    }
    .ltr{display:inline-block;opacity:0}
    body.started .ltr{
      animation:letterIn 1.2s cubic-bezier(.2,1.4,.4,1) var(--d) both,
                shimmer 6s linear infinite;
    }
    @keyframes letterIn{
      from{opacity:0;transform:translateY(50px) scale(.35) rotate(-14deg);filter:blur(12px)}
      to  {opacity:1;transform:none;filter:blur(0)}
    }
    .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

    .bouquet-wrap{
      width:min(94vw,560px);margin:20px auto 0;cursor:pointer;position:relative;
      filter:
        drop-shadow(0 36px 55px rgba(0,0,0,.65))
        drop-shadow(0 0 55px rgba(255,122,168,.18));
      -webkit-tap-highlight-color:transparent;
    }
    #bouquet{width:100%;height:auto;display:block;overflow:visible}
    body.started .bouquet-wrap{animation:floaty 7s ease-in-out 3s infinite}
    @keyframes floaty{
      0%,100%{transform:translateY(0) rotate(0)}
      50%{transform:translateY(-14px) rotate(.5deg)}
    }

    .bloom{opacity:0;transform:scale(0);transform-box:fill-box;transform-origin:50% 50%}
    body.started .bloom{animation:bloom 1.1s cubic-bezier(.2,1.5,.4,1) var(--d,0s) forwards}
    @keyframes bloom{
      0%  {opacity:0;transform:scale(.05) rotate(-150deg)}
      60% {opacity:1;transform:scale(1.14) rotate(8deg)}
      100%{opacity:1;transform:scale(1) rotate(0)}
    }
    .stems,.leaves,.greenery,.wrapArt,.bowGroup,.tailGroup{
      opacity:0;transition:opacity 1.1s ease var(--wd, .2s);
    }
    body.started .stems{opacity:.85;transition-delay:.15s}
    body.started .leaves{opacity:1;transition-delay:.25s}
    body.started .greenery{opacity:1;transition-delay:.3s}
    body.started .wrapArt{opacity:1;transition-delay:1.4s}
    body.started .bowGroup{opacity:1;transition-delay:1.85s}
    body.started .tailGroup{opacity:1;transition-delay:2.05s}

    .glint{transform-box:fill-box;transform-origin:50% 50%;opacity:0}
    body.started .glint{animation:twinkle 3s ease-in-out var(--d) infinite}
    @keyframes twinkle{
      0%,100%{opacity:0;transform:scale(.2) rotate(0)}
      50%{opacity:1;transform:scale(1.4) rotate(45deg)}
    }

    .letter{max-width:35rem;margin:10px auto 0;padding:0 8px}
    .divider{display:flex;align-items:center;justify-content:center;gap:16px;margin:10px 0 26px}
    .divider i{display:block;height:1px;width:min(24vw,110px);
      background:linear-gradient(90deg,transparent,var(--gold))}
    .divider i:last-child{background:linear-gradient(270deg,transparent,var(--gold))}
    .divider svg{width:22px;height:22px;fill:var(--gold);
      filter:drop-shadow(0 0 8px rgba(212,175,55,.7))}
    .line{
      font-style:italic;font-size:clamp(1.15rem,4.4vw,1.42rem);line-height:1.62;
      color:var(--ink);margin:0 auto 1.2rem;text-wrap:balance;
    }
    .line em{font-style:italic;font-weight:500}
    .sign{
      font-family:'Great Vibes',cursive;
      font-size:clamp(2rem,8vw,2.8rem);margin-top:12px;line-height:1.2;
    }

    #more{
      margin-top:34px;cursor:pointer;
      font-family:'Cinzel',serif;font-size:.72rem;letter-spacing:.32em;text-transform:uppercase;
      color:var(--gold-lt);
      background:linear-gradient(135deg, rgba(212,175,55,.14), rgba(107,20,40,.28));
      border:1px solid rgba(212,175,55,.7);border-radius:999px;padding:17px 34px;
      box-shadow:
        inset 0 0 22px rgba(212,175,55,.16),
        0 0 28px rgba(212,175,55,.18),
        0 8px 22px rgba(0,0,0,.4);
      transition:background .3s, box-shadow .3s, transform .3s;
    }
    #more:hover{
      background:linear-gradient(135deg, rgba(212,175,55,.26), rgba(107,20,40,.4));
      box-shadow:inset 0 0 22px rgba(212,175,55,.28), 0 0 42px rgba(212,175,55,.42), 0 8px 22px rgba(0,0,0,.5);
      transform:translateY(-2px);
    }
    #more:active{transform:scale(.97)}
    #more:focus-visible{outline:2px solid var(--gold-lt);outline-offset:5px}

    @media (prefers-reduced-motion: reduce){
      #fx{display:none}
      .gold,body.started .ltr,.halo,.seal{animation:none}
      .rv,.ltr,.bloom,.stems,.leaves,.greenery,.wrapArt,.bowGroup,.tailGroup{
        opacity:1;transform:none;filter:none;transition:none;
      }
      body.started .rv,body.started .bloom,body.started .bouquet-wrap{animation:none}
      .glint,body.started .glint{animation:none;opacity:.85}
      .seal::after,.intro-tap{animation:none}
    }
  </style>
</head>
<body>

<!-- gold filigree corners (repeated 4×) -->
<svg class="corner corner--tl" viewBox="0 0 100 100" aria-hidden="true">
  <path d="M4,4 L40,4 Q62,4 62,26 L62,40" fill="none" stroke="#d4af37" stroke-width="1.3" opacity=".75"/>
  <path d="M4,4 L4,40 Q4,62 26,62 L40,62" fill="none" stroke="#d4af37" stroke-width="1.3" opacity=".75"/>
  <path d="M18,18 Q30,8 42,18 Q32,32 18,18 Z" fill="none" stroke="#d4af37" stroke-width=".8" opacity=".7"/>
  <path d="M18,18 L18,40 M18,18 L40,18" fill="none" stroke="#d4af37" stroke-width=".5" opacity=".5"/>
  <path d="M42,18 Q56,10 62,26" fill="none" stroke="#d4af37" stroke-width=".6" opacity=".5"/>
  <path d="M18,42 Q10,56 26,62" fill="none" stroke="#d4af37" stroke-width=".6" opacity=".5"/>
  <circle cx="18" cy="18" r="2" fill="#d4af37" opacity=".85"/>
  <circle cx="62" cy="4" r="1.6" fill="#d4af37" opacity=".65"/>
  <circle cx="4" cy="62" r="1.6" fill="#d4af37" opacity=".65"/>
  <circle cx="50" cy="50" r="1" fill="#f7e7a1" opacity=".7"/>
</svg>
<svg class="corner corner--tr" viewBox="0 0 100 100" aria-hidden="true">
  <use href="#cornerPath"/>
</svg>
<svg class="corner corner--bl" viewBox="0 0 100 100" aria-hidden="true">
  <use href="#cornerPath"/>
</svg>
<svg class="corner corner--br" viewBox="0 0 100 100" aria-hidden="true">
  <use href="#cornerPath"/>
</svg>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <g id="cornerPath">
      <path d="M4,4 L40,4 Q62,4 62,26 L62,40" fill="none" stroke="#d4af37" stroke-width="1.3" opacity=".75"/>
      <path d="M4,4 L4,40 Q4,62 26,62 L40,62" fill="none" stroke="#d4af37" stroke-width="1.3" opacity=".75"/>
      <path d="M18,18 Q30,8 42,18 Q32,32 18,18 Z" fill="none" stroke="#d4af37" stroke-width=".8" opacity=".7"/>
      <path d="M18,18 L18,40 M18,18 L40,18" fill="none" stroke="#d4af37" stroke-width=".5" opacity=".5"/>
      <path d="M42,18 Q56,10 62,26" fill="none" stroke="#d4af37" stroke-width=".6" opacity=".5"/>
      <path d="M18,42 Q10,56 26,62" fill="none" stroke="#d4af37" stroke-width=".6" opacity=".5"/>
      <circle cx="18" cy="18" r="2" fill="#d4af37" opacity=".85"/>
      <circle cx="62" cy="4" r="1.6" fill="#d4af37" opacity=".65"/>
      <circle cx="4" cy="62" r="1.6" fill="#d4af37" opacity=".65"/>
      <circle cx="50" cy="50" r="1" fill="#f7e7a1" opacity=".7"/>
    </g>
  </defs>
</svg>
<div class="frame-inner"></div>

<canvas id="fx" aria-hidden="true"></canvas>

<!-- ===== TAP TO OPEN ===== -->
<div id="intro" role="button" tabindex="0" onclick="openGift(event)" ontouchstart="openGift(event)" onmousedown="openGift(event)" aria-label="Open your birthday surprise">
  <div class="seal-wrap">
    <div class="halo"></div>
    <div class="seal" aria-hidden="true"><span>N</span></div>
  </div>
  <p class="intro-for">For the one &amp; only</p>
  <p class="intro-name gold">Nandini</p>
  <div class="intro-rule" aria-hidden="true">
    <i></i>
    <svg viewBox="0 0 24 24"><path d="M12 2l2.4 6.6 6.6.5-5 4.2 1.6 6.5L12 16.4 6.4 19.8l1.6-6.5-5-4.2 6.6-.5z"/></svg>
    <i></i>
  </div>
  <p class="intro-tap">tap to unveil your surprise</p>
</div>

<main>
  <header>
    <p class="eyebrow rv" style="--d:.2s">✦ Today the world celebrates ✦</p>
    <h1>
      <span class="script rv" style="--d:.45s">Happy Birthday</span>
      <span class="name" id="name">NANDINI</span>
    </h1>
  </header>

  <div class="bouquet-wrap" id="bouquetWrap">
    <svg id="bouquet" viewBox="0 0 640 960" xmlns="http://www.w3.org/2000/svg" role="img"
         aria-label="An exotic luxury bouquet of peonies, orchids, proteas, anthuriums and calla lilies in wine, blush and champagne, wrapped in ivory silk with a burgundy sash and gold bow"></svg>
  </div>

  <section class="letter">
    <div class="divider rv" style="--d:2.2s" aria-hidden="true">
      <i></i>
      <svg viewBox="0 0 24 24"><path d="M12 21s-7.5-4.6-10-9.2C.3 8.5 2.2 4 6.3 4c2.4 0 4 1.3 5.7 3.4C13.7 5.3 15.3 4 17.7 4c4.1 0 6 4.5 4.3 7.8C19.5 16.4 12 21 12 21z"/></svg>
      <i></i>
    </div>

    <p class="line rv" style="--d:2.5s">On the day you arrived, the world quietly bloomed into
      something softer, wilder, more beautiful — and it has been <em class="gold">flowering</em> ever since.</p>
    <p class="line rv" style="--d:3.1s">You turn ordinary afternoons into something worth remembering,
      and you make everyone lucky enough to be near you feel a little more at home in themselves.</p>
    <p class="line rv" style="--d:3.7s">May this year wrap you in velvet mornings, endless laughter,
      and a love so steady you never once have to wonder if you're enough —
      because you <em class="gold">always, always are.</em></p>
    <p class="line rv" style="--d:4.3s">Every flower in this bouquet is a wish for you — every petal,
      every gilded stem, every promise of softness yet to come.</p>

    <p class="sign gold rv" style="--d:5.0s">Happy birthday, beautiful soul ♥</p>

    <button type="button" id="more" class="rv" style="--d:5.5s">🌸 Shower her with flowers</button>
  </section>
</main>

<script>
/* =========================================================
   PARENT DOM HACK (Fixes Streamlit Tap Blocking Issues)
   This forces the Streamlit iframe to break out and become
   a true full-screen native app, guaranteeing clicks work.
   ========================================================= */
(function hackStreamlitParent() {
  try {
    const parentDoc = window.parent.document;
    
    // 1. Inject CSS into parent to hide Streamlit UI
    const css = `
      header, footer, #MainMenu, .stAppHeader, .stDeployButton, 
      [data-testid="stHeader"], [data-testid="collapsedControl"],
      .stAppDeployButton, .st-emotion-cache-16idsys {
        display: none !important;
        visibility: hidden !important;
      }
      .stApp {
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
      }
      .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
        margin: 0 !important;
      }
    `;
    const style = parentDoc.createElement('style');
    style.innerHTML = css;
    parentDoc.head.appendChild(style);

    // 2. Fix the iframe element itself to be full screen
    const iframe = window.frameElement;
    if (iframe) {
      iframe.style.cssText = `
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 9999999 !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
      `;
      
      // Remove any max-height or height constraints from parent wrappers
      let parent = iframe.parentElement;
      while(parent && parent !== parentDoc.body) {
        parent.style.overflow = 'visible';
        parent.style.maxHeight = 'none';
        parent.style.height = 'auto';
        parent = parent.parentElement;
      }
    }
  } catch(e) {
    console.log("Parent hack failed", e);
  }
})();

/* =========================================================
   PALETTE
   ========================================================= */
const C = {
  wine:    { main:'#8b1e3f', dark:'#4a0d1c', light:'#d64568', glow:'#ff4d6d' },
  plum:    { main:'#6b2c4a', dark:'#3d0b26', light:'#a05878', glow:'#d84a84' },
  rose:    { main:'#e63950', dark:'#a4161a', light:'#ffb7c0', glow:'#ff8fa3' },
  blush:   { main:'#f4c6d4', dark:'#e89ab0', light:'#fff0f4', glow:'#ffffff' },
  champ:   { main:'#f5e6c8', dark:'#e0c896', light:'#fffaf0', glow:'#ffffff' },
  gold:    { main:'#d4af37', dark:'#a87b18', light:'#f7e7a1', glow:'#fff4cf' },
  emerald: { main:'#2d6a4f', dark:'#1b4332', light:'#7fc99a', glow:'#74c69d' },
  sage:    { main:'#8fa88a', dark:'#5c7356', light:'#c2d4bb', glow:'#d8f3dc' },
  blackBac:{ main:'#4a0414', dark:'#1a0005', light:'#800b28', glow:'#b31236' }
};
const n1 = v => v.toFixed(1);
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* =========================================================
   EXOTIC FLOWER SHAPES (centred on 0,0)
   ========================================================= */
function peony(r, c) {
  let s = '';
  for (let i = 0; i < 10; i++) {
    const a = i * 36;
    s += `<path d="M0,${n1(-r*0.15)}
              C${n1(-r*0.45)},${n1(-r*0.35)} ${n1(-r*0.58)},${n1(-r*0.75)} ${n1(-r*0.25)},${n1(-r*0.98)}
              C${n1(-r*0.05)},${n1(-r*1.08)} ${n1(r*0.2)},${n1(-r*1.02)} ${n1(r*0.35)},${n1(-r*0.78)}
              C${n1(r*0.5)},${n1(-r*0.55)} ${n1(r*0.4)},${n1(-r*0.3)} 0,${n1(-r*0.45)} Z"
          fill="${c.main}" opacity="0.97" transform="rotate(${a})"/>`;
  }
  for (let i = 0; i < 10; i++) {
    const a = i * 36 + 18;
    s += `<ellipse cy="${n1(-r*0.85)}" rx="${n1(r*0.22)}" ry="${n1(r*0.09)}"
             fill="${c.light}" opacity="0.55" transform="rotate(${a})"/>`;
  }
  for (let i = 0; i < 7; i++) {
    const a = i * 360/7 + 20;
    s += `<path d="M0,${n1(-r*0.15)}
              C${n1(-r*0.3)},${n1(-r*0.3)} ${n1(-r*0.4)},${n1(-r*0.6)} ${n1(-r*0.15)},${n1(-r*0.75)}
              C${n1(r*0.05)},${n1(-r*0.85)} ${n1(r*0.3)},${n1(-r*0.6)} 0,${n1(-r*0.4)} Z"
          fill="${c.dark}" transform="rotate(${a})"/>`;
  }
  for (let i = 0; i < 5; i++) {
    const a = i * 72 + 30;
    s += `<ellipse cy="${n1(-r*0.3)}" rx="${n1(r*0.17)}" ry="${n1(r*0.3)}"
             fill="${c.light}" transform="rotate(${a})"/>`;
  }
  s += `<circle r="${n1(r*0.12)}" fill="${c.dark}"/>`;
  s += `<circle r="${n1(r*0.06)}" fill="${c.light}"/>`;
  for (let i = 0; i < 5; i++) {
    const a = i * 72 + 15, rad = a * Math.PI / 180;
    s += `<circle cx="${n1(Math.cos(rad)*r*0.1)}" cy="${n1(Math.sin(rad)*r*0.1)}"
             r="${n1(r*0.025)}" fill="#f7e7a1" opacity="0.85"/>`;
  }
  return s;
}

function rose(r, c) {
  let s = '';
  for (let i = 0; i < 6; i++)
    s += `<ellipse cy="${n1(-r*0.55)}" rx="${n1(r*0.4)}" ry="${n1(r*0.55)}"
             fill="${c.main}" transform="rotate(${i*60})"/>`;
  for (let i = 0; i < 6; i++)
    s += `<ellipse cy="${n1(-r*0.32)}" rx="${n1(r*0.27)}" ry="${n1(r*0.36)}"
             fill="${c.dark}" opacity="0.9" transform="rotate(${i*60+30})"/>`;
  for (let i = 0; i < 5; i++)
    s += `<ellipse cy="${n1(-r*0.15)}" rx="${n1(r*0.15)}" ry="${n1(r*0.2)}"
             fill="${c.light}" transform="rotate(${i*72+20})"/>`;
  s += `<circle r="${n1(r*0.08)}" fill="${c.dark}"/>`;
  return s;
}

function ranunculus(r, c) {
  let s = '';
  for (let i = 5; i >= 1; i--)
    s += `<circle r="${n1(r*i/5)}" fill="${i % 2 ? c.main : c.dark}"/>`;
  for (let i = 0; i < 12; i++) {
    const a = i * 30;
    s += `<ellipse cy="${n1(-r*0.88)}" rx="${n1(r*0.1)}" ry="${n1(r*0.18)}"
             fill="${c.light}" opacity="0.9" transform="rotate(${a})"/>`;
  }
  s += `<circle r="${n1(r*0.12)}" fill="${c.dark}"/>`;
  s += `<circle r="${n1(r*0.05)}" fill="#f7e7a1"/>`;
  return s;
}

function orchid(r, c) {
  let s = '';
  for (let i = 0; i < 3; i++) {
    const a = i * 120;
    s += `<ellipse cy="${n1(-r*0.47)}" rx="${n1(r*0.18)}" ry="${n1(r*0.55)}"
             fill="${c.dark}" transform="rotate(${a})"/>`;
  }
  s += `<ellipse cx="${n1(-r*0.45)}" cy="${n1(-r*0.08)}" rx="${n1(r*0.48)}" ry="${n1(r*0.15)}"
           fill="${c.main}" transform="rotate(-25)"/>`;
  s += `<ellipse cx="${n1(r*0.45)}" cy="${n1(-r*0.08)}" rx="${n1(r*0.48)}" ry="${n1(r*0.15)}"
           fill="${c.main}" transform="rotate(25)"/>`;
  s += `<path d="M0,${n1(-r*0.08)}
           C${n1(-r*0.35)},${n1(r*0.15)} ${n1(-r*0.4)},${n1(r*0.55)} ${n1(-r*0.1)},${n1(r*0.62)}
           C${n1(-r*0.02)},${n1(r*0.64)} ${n1(r*0.02)},${n1(r*0.64)} ${n1(r*0.1)},${n1(r*0.62)}
           C${n1(r*0.4)},${n1(r*0.55)} ${n1(r*0.35)},${n1(r*0.15)} 0,${n1(-r*0.08)} Z"
        fill="${c.light}" stroke="${c.main}" stroke-width="1"/>`;
  s += `<circle r="${n1(r*0.14)}" cy="${n1(-r*0.02)}" fill="${c.main}"/>`;
  s += `<circle r="${n1(r*0.06)}" cy="${n1(-r*0.08)}" fill="#f7e7a1"/>`;
  s += `<path d="M0,${n1(r*0.05)} L${n1(-r*0.1)},${n1(r*0.45)} M0,${n1(r*0.05)} L${n1(r*0.1)},${n1(r*0.45)}"
           stroke="${c.dark}" stroke-width="0.8" opacity="0.6"/>`;
  return s;
}

function anthurium(r, c) {
  let s = '';
  s += `<path d="M0,${n1(-r*0.15)}
           C${n1(-r*0.55)},${n1(-r*0.75)} ${n1(-r*1.05)},${n1(-r*0.35)} ${n1(-r*0.7)},${n1(r*0.35)}
           C${n1(-r*0.4)},${n1(r*0.85)} 0,${n1(r*0.55)} 0,${n1(r*0.15)}
           C0,${n1(r*0.55)} ${n1(r*0.4)},${n1(r*0.85)} ${n1(r*0.7)},${n1(r*0.35)}
           C${n1(r*1.05)},${n1(-r*0.35)} ${n1(r*0.55)},${n1(-r*0.75)} 0,${n1(-r*0.15)} Z"
        fill="${c.main}" stroke="${c.dark}" stroke-width="1.2"/>`;
  s += `<path d="M0,0 Q${n1(r*0.08)},${n1(-r*0.5)} 0,${n1(-r*0.85)}"
           stroke="${c.light}" stroke-width="${n1(r*0.11)}" fill="none" stroke-linecap="round"/>`;
  return s;
}

function protea(r, c) {
  let s = '';
  for (let i = 0; i < 18; i++) {
    const a = i * 20;
    s += `<path d="M0,${n1(-r*0.15)} L${n1(-r*0.08)},${n1(-r*0.85)} L0,${n1(-r*1.12)} L${n1(r*0.08)},${n1(-r*0.85)} Z"
           fill="${i % 2 ? c.main : c.dark}" transform="rotate(${a})"/>`;
  }
  for (let i = 0; i < 12; i++) {
    const a = i * 30 + 15;
    s += `<path d="M0,${n1(-r*0.1)} L${n1(-r*0.05)},${n1(-r*0.55)} L0,${n1(-r*0.72)} L${n1(r*0.05)},${n1(-r*0.55)} Z"
           fill="${c.light}" transform="rotate(${a})"/>`;
  }
  s += `<circle r="${n1(r*0.3)}" fill="${c.dark}"/>`;
  s += `<circle r="${n1(r*0.18)}" fill="${c.main}"/>`;
  s += `<circle r="${n1(r*0.08)}" fill="#f7e7a1"/>`;
  return s;
}

function calla(r, c) {
  let s = '';
  s += `<path d="M0,${n1(-r*0.85)}
           C${n1(-r*0.4)},${n1(-r*0.55)} ${n1(-r*0.5)},${n1(r*0.25)} 0,${n1(r*0.7)}
           C${n1(r*0.5)},${n1(r*0.25)} ${n1(r*0.4)},${n1(-r*0.55)} 0,${n1(-r*0.85)} Z"
        fill="${c.main}" stroke="${c.dark}" stroke-width="1"/>`;
  s += `<path d="M0,${n1(-r*0.65)} C${n1(-r*0.2)},${n1(-r*0.15)} ${n1(-r*0.15)},${n1(r*0.3)} 0,${n1(r*0.55)}"
           stroke="${c.dark}" fill="none" stroke-width="1.5" opacity="0.5"/>`;
  s += `<path d="M0,${n1(r*0.55)} L0,${n1(-r*0.35)}"
           stroke="#f7e7a1" stroke-width="${n1(r*0.09)}" stroke-linecap="round"/>`;
  s += `<circle cy="${n1(-r*0.4)}" r="${n1(r*0.08)}" fill="#e8d5a3"/>`;
  return s;
}

function eucalyptus(len, c, dir = -90) {
  let s = `<g transform="rotate(${dir})">`;
  s += `<path d="M0,0 Q${n1(len*0.15)},${n1(-len*0.5)} ${n1(len*0.2)},${n1(-len)}"
           stroke="${c.dark}" stroke-width="1.8" fill="none"/>`;
  for (let i = 1; i <= 6; i++) {
    const t = i / 6, y = -len * t, x = len * 0.18 * t;
    const rr = len * (0.14 - t * 0.05);
    s += `<ellipse cx="${n1(x - len*0.11)}" cy="${n1(y)}" rx="${n1(rr)}" ry="${n1(rr*1.3)}"
             fill="${c.main}" opacity="0.92" transform="rotate(-20, ${n1(x)}, ${n1(y)})"/>`;
    s += `<ellipse cx="${n1(x + len*0.11)}" cy="${n1(y)}" rx="${n1(rr)}" ry="${n1(rr*1.3)}"
             fill="${c.main}" opacity="0.92" transform="rotate(20, ${n1(x)}, ${n1(y)})"/>`;
  }
  s += `</g>`;
  return s;
}

function fern(len, c, dir = -90) {
  let s = `<g transform="rotate(${dir})">`;
  s += `<path d="M0,0 L0,${n1(-len)}" stroke="${c.dark}" stroke-width="1.8"/>`;
  for (let i = 1; i <= 10; i++) {
    const t = i / 11, y = -len * t, ll = len * 0.3 * (1 - t * 0.55);
    s += `<path d="M0,${n1(y)} Q${n1(-ll*0.5)},${n1(y-ll*0.3)} ${n1(-ll)},${n1(y-ll*0.7)}"
             fill="none" stroke="${c.main}" stroke-width="1.5" stroke-linecap="round"/>`;
    s += `<path d="M0,${n1(y)} Q${n1(ll*0.5)},${n1(y-ll*0.3)} ${n1(ll)},${n1(y-ll*0.7)}"
             fill="none" stroke="${c.main}" stroke-width="1.5" stroke-linecap="round"/>`;
  }
  s += `</g>`;
  return s;
}

function leafShape(len, c) {
  return `<path d="M0,0 Q${n1(len*.5)},${n1(-len*.44)} ${len},0 Q${n1(len*.5)},${n1(len*.44)} 0,0 Z" fill="${c}"/>
          <path d="M0,0 Q${n1(len*.5)},0 ${n1(len*.92)},0" stroke="${c === '#1b4332' ? '#0a2a18' : '#1b5e20'}"
                stroke-width="1.2" fill="none" opacity="0.35"/>`;
}

const heroes = [
  { t:'orchid',     x:320, y:92,  r:40, c:C.champ,  rot:  0, d:0.30 },
  { t:'peony',      x:210, y:142, r:46, c:C.blush,  rot: 20, d:0.35 },
  { t:'peony',      x:430, y:142, r:46, c:C.rose,   rot:-20, d:0.38 },
  { t:'protea',     x:530, y:250, r:38, c:C.wine,   rot:  0, d:0.42 },
  { t:'protea',     x:110, y:250, r:38, c:C.rose,   rot:  0, d:0.45 },
  { t:'anthurium',  x:490, y:340, r:34, c:C.wine,   rot: 25, d:0.50 },
  { t:'anthurium',  x:150, y:340, r:34, c:C.rose,   rot:-25, d:0.53 },
  { t:'peony',      x:320, y:172, r:52, c:C.blush,  rot:  0, d:0.56 },
  { t:'rose',       x:250, y:232, r:32, c:C.wine,   rot: 10, d:0.60 },
  { t:'rose',       x:390, y:232, r:32, c:C.rose,   rot:-10, d:0.63 },
  { t:'orchid',     x:460, y:200, r:30, c:C.plum,   rot: 30, d:0.66 },
  { t:'orchid',     x:180, y:200, r:30, c:C.wine,   rot:-30, d:0.69 },
  { t:'rose',       x:320, y:200, r:42, c:C.blackBac, rot: 0, d:0.55 },
  { t:'peony',      x:320, y:292, r:66, c:C.wine,   rot:  0, d:0.15 },
  { t:'calla',      x:240, y:322, r:36, c:C.champ,  rot:-20, d:0.72 },
  { t:'calla',      x:400, y:322, r:36, c:C.blush,  rot: 20, d:0.75 },
  { t:'rose',       x:320, y:382, r:38, c:C.rose,   rot:  0, d:0.78 },
  { t:'ranunculus', x:220, y:402, r:26, c:C.champ,  rot:  0, d:0.80 },
  { t:'ranunculus', x:420, y:402, r:26, c:C.blush,  rot:  0, d:0.82 },
  { t:'orchid',     x:490, y:442, r:30, c:C.plum,   rot: 40, d:0.84 },
  { t:'orchid',     x:150, y:442, r:30, c:C.wine,   rot:-40, d:0.86 },
  { t:'rose',       x:280, y:452, r:28, c:C.wine,   rot: 15, d:0.88 },
  { t:'rose',       x:360, y:452, r:28, c:C.rose,   rot:-15, d:0.90 }
];

const filler = [
  { t:'ranunculus', x:270, y:160, r:22, c:C.rose,   rot:  0, d:0.92 },
  { t:'ranunculus', x:370, y:160, r:22, c:C.wine,   rot:  0, d:0.94 },
  { t:'rose',       x:150, y:300, r:24, c:C.champ,  rot: 20, d:0.96 },
  { t:'rose',       x:490, y:300, r:24, c:C.blush,  rot:-20, d:0.98 },
  { t:'ranunculus', x:200, y:360, r:22, c:C.plum,   rot:  0, d:1.00 },
  { t:'ranunculus', x:440, y:360, r:22, c:C.wine,   rot:  0, d:1.02 },
  { t:'orchid',     x:320, y:250, r:22, c:C.champ,  rot: 15, d:1.04 },
  { t:'rose',       x:390, y:292, r:22, c:C.plum,   rot: 30, d:1.06 },
  { t:'rose',       x:250, y:292, r:22, c:C.wine,   rot:-30, d:1.08 },
  { t:'ranunculus', x:320, y:455, r:22, c:C.rose,   rot:  0, d:1.10 },
  { t:'rose',       x:390, y:410, r:20, c:C.wine,   rot: 45, d:1.12 },
  { t:'rose',       x:250, y:410, r:20, c:C.rose,   rot:-45, d:1.14 }
];

const greenery = [
  { t:'eucalyptus', x:80,  y:250, len:150, dir:-170, d:0.20 },
  { t:'eucalyptus', x:560, y:250, len:150, dir:-10,  d:0.22 },
  { t:'fern',       x:60,  y:400, len:170, dir:-155, d:0.24 },
  { t:'fern',       x:580, y:400, len:170, dir:-25,  d:0.26 },
  { t:'eucalyptus', x:120, y:440, len:130, dir:-140, d:0.28 },
  { t:'eucalyptus', x:520, y:440, len:130, dir:-40,  d:0.30 },
  { t:'fern',       x:320, y:60,  len:110, dir:-90,  d:0.18 }
];

const leaves = [
  { x:80,  y:340, len:72, a:-160, c:'#2d6a4f' },
  { x:560, y:340, len:72, a:-20,  c:'#2d6a4f' },
  { x:110, y:500, len:66, a:-150, c:'#1b4332' },
  { x:530, y:500, len:66, a:-30,  c:'#1b4332' },
  { x:200, y:100, len:52, a:-135, c:'#2d6a4f' },
  { x:440, y:100, len:52, a:-45,  c:'#2d6a4f' }
];

const draw = (f) => {
  if (f.t === 'peony')      return peony(f.r, f.c);
  if (f.t === 'rose')       return rose(f.r, f.c);
  if (f.t === 'ranunculus') return ranunculus(f.r, f.c);
  if (f.t === 'orchid')     return orchid(f.r, f.c);
  if (f.t === 'anthurium')  return anthurium(f.r, f.c);
  if (f.t === 'protea')     return protea(f.r, f.c);
  if (f.t === 'calla')      return calla(f.r, f.c);
  return '';
};

let roses = [];

function buildBouquet() {
  const out = [];
  out.push(`<defs>
    <linearGradient id="wrapGrad" x1="0.15" y1="0" x2="0.85" y2="1">
      <stop offset="0%"   stop-color="#fffaf0"/>
      <stop offset="30%"  stop-color="#f5e6c8"/>
      <stop offset="70%"  stop-color="#e0c896"/>
      <stop offset="100%" stop-color="#b08e56"/>
    </linearGradient>
    <linearGradient id="wrapGradDark" x1="0.2" y1="0" x2="0.8" y2="1">
      <stop offset="0%"   stop-color="#f5e6c8"/>
      <stop offset="55%"  stop-color="#d9be87"/>
      <stop offset="100%" stop-color="#a07a44"/>
    </linearGradient>
    <linearGradient id="sashGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#a42a4f"/>
      <stop offset="45%"  stop-color="#6b1428"/>
      <stop offset="100%" stop-color="#3d0b1c"/>
    </linearGradient>
    <linearGradient id="bowGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#fff4cf"/>
      <stop offset="35%"  stop-color="#f3d57a"/>
      <stop offset="70%"  stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#a87b18"/>
    </linearGradient>
    <linearGradient id="bowShadow" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#c9971f"/>
      <stop offset="100%" stop-color="#7d5a0f"/>
    </linearGradient>
    <linearGradient id="stemGrad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%"   stop-color="#1b4332"/>
      <stop offset="100%" stop-color="#3f7d4a"/>
    </linearGradient>
    <radialGradient id="glowGrad">
      <stop offset="0%"   stop-color="#f4c6d4" stop-opacity="0.28"/>
      <stop offset="55%"  stop-color="#d4af37" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="#d4af37" stop-opacity="0"/>
    </radialGradient>
    <filter id="petalShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="3" stdDeviation="2.5" flood-color="#1a050b" flood-opacity="0.6"/>
    </filter>
    <filter id="goldGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="1.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>`);
  out.push(`<ellipse cx="320" cy="300" rx="310" ry="290" fill="url(#glowGrad)"/>`);
  out.push('<g class="greenery">');
  greenery.forEach(g => {
    out.push(`<g transform="translate(${g.x},${g.y})">
      <g class="bloom" style="--d:${g.d}s">${g.t === 'fern' ? fern(g.len, C.sage, g.dir) : eucalyptus(g.len, C.sage, g.dir)}</g>
    </g>`);
  });
  out.push('</g>');
  out.push(`<g class="wrapArt">
    <path d="M 80 220 Q 40 420 120 620 L 520 620 Q 600 420 560 220 Q 440 150 320 150 Q 200 150 80 220 Z"
          fill="url(#wrapGrad)" stroke="#a87b18" stroke-width="1.4" stroke-opacity="0.65"/>
    <path d="M 120 220 Q 220 170 320 168 Q 420 170 520 220"
          fill="none" stroke="#d4af37" stroke-width="0.8" opacity="0.55"/>
    <path d="M 140 260 Q 230 210 320 208 Q 410 210 500 260"
          fill="none" stroke="#d4af37" stroke-width="0.6" opacity="0.35"/>
  </g>`);
  out.push('<g class="stems">');
  for (let i = 0; i < 40; i++) {
    const a = (i / 40) * Math.PI * 2;
    const x = 320 + Math.cos(a) * 200;
    const y = 290 + Math.sin(a) * 200;
    out.push(`<path d="M 320 640 Q ${n1(320 + (x - 320) * 0.6)} 460 ${n1(x)} ${n1(y)}"
             fill="none" stroke="url(#stemGrad)" stroke-width="3.4" stroke-linecap="round"/>`);
  }
  out.push('</g>');
  out.push('<g class="leaves">');
  leaves.forEach(l =>
    out.push(`<g transform="translate(${l.x},${l.y}) rotate(${l.a})">${leafShape(l.len, l.c)}</g>`)
  );
  out.push('</g>');
  roses = heroes.concat(filler).sort((a, b) => a.y - b.y);
  roses.forEach(f => {
    out.push(`<g transform="translate(${n1(f.x)},${n1(f.y)}) rotate(${n1(f.rot)})" filter="url(#petalShadow)">
      <g class="bloom" style="--d:${f.d.toFixed(2)}s">${draw(f)}</g>
    </g>`);
  });
  out.push(`<g class="wrapArt">
    <path d="M 130 420 Q 140 540 200 640 L 440 640 Q 500 540 510 420 Q 420 500 320 500 Q 220 500 130 420 Z"
          fill="url(#wrapGradDark)" stroke="#a87b18" stroke-width="1.2" stroke-opacity="0.55"/>
    <path d="M 200 640 Q 230 560 320 540 Q 410 560 440 640"
          fill="none" stroke="#fff4cf" stroke-width="1" opacity="0.55"/>
    <path d="M 240 460 Q 260 540 260 630"
          fill="none" stroke="#a87b18" stroke-width="0.9" opacity="0.35"/>
    <path d="M 400 460 Q 380 540 380 630"
          fill="none" stroke="#a87b18" stroke-width="0.9" opacity="0.35"/>
    <path d="M 320 500 L 320 640"
          fill="none" stroke="#a87b18" stroke-width="0.7" opacity="0.25"/>
  </g>`);
  out.push(`<g class="wrapArt" style="transition-delay:1.55s">
    <rect x="176" y="616" width="288" height="52" rx="4" fill="url(#sashGrad)"/>
    <rect x="176" y="618" width="288" height="2" fill="#f7e7a1" opacity="0.7"/>
    <rect x="176" y="664" width="288" height="2" fill="#f7e7a1" opacity="0.55"/>
    <rect x="176" y="616" width="288" height="52" rx="4" fill="none" stroke="#d4af37" stroke-width="0.8" opacity="0.65"/>
    <path d="M 180 642 L 460 642" stroke="#d4af37" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.8"/>
  </g>`);
  out.push(`<g class="wrapArt" style="transition-delay:1.7s">
    <path d="M 200 668 L 440 668 L 495 900 Q 320 945 145 900 Z"
          fill="url(#wrapGrad)" stroke="#a87b18" stroke-width="1.4" stroke-opacity="0.6"/>
    <path d="M 220 668 Q 260 810 235 900"
          fill="none" stroke="#a87b18" stroke-width="1" opacity="0.35"/>
    <path d="M 420 668 Q 380 810 405 900"
          fill="none" stroke="#a87b18" stroke-width="1" opacity="0.35"/>
    <path d="M 300 668 Q 305 820 300 925"
          fill="none" stroke="#fff4cf" stroke-width="1" opacity="0.5"/>
    <path d="M 340 668 Q 335 820 340 925"
          fill="none" stroke="#a87b18" stroke-width="0.8" opacity="0.25"/>
    <path d="M 175 880 Q 320 925 465 880"
          fill="none" stroke="#fff4cf" stroke-width="1" opacity="0.55"/>
  </g>`);
  out.push(`<g class="bowGroup">
    <path d="M 320 642 C 232 590 178 626 200 682 C 216 722 282 700 320 642 Z"
          fill="url(#bowGrad)" stroke="#7d5a0f" stroke-width="1.4"/>
    <path d="M 320 642 C 408 590 462 626 440 682 C 424 722 358 700 320 642 Z"
          fill="url(#bowGrad)" stroke="#7d5a0f" stroke-width="1.4"/>
    <path d="M 320 642 C 260 604 220 620 218 656"
          fill="none" stroke="#fff4cf" stroke-width="1.2" opacity="0.7"/>
    <path d="M 320 642 C 380 604 420 620 422 656"
          fill="none" stroke="#fff4cf" stroke-width="1.2" opacity="0.7"/>
    <ellipse cx="320" cy="644" rx="26" ry="20" fill="url(#bowShadow)" stroke="#7d5a0f" stroke-width="1.2"/>
    <ellipse cx="316" cy="638" rx="10" ry="7" fill="#f7e7a1" opacity="0.75"/>
  </g>`);
  out.push(`<g class="tailGroup">
    <path d="M 300 654 C 270 760 240 880 220 940 L 260 918 L 290 962 L 296 900 C 306 800 312 720 312 654 Z"
          fill="url(#bowGrad)" stroke="#7d5a0f" stroke-width="1.3"/>
    <path d="M 340 654 C 370 760 400 880 420 940 L 380 918 L 350 962 L 344 900 C 334 800 328 720 328 654 Z"
          fill="url(#bowGrad)" stroke="#7d5a0f" stroke-width="1.3"/>
    <path d="M 306 660 C 300 760 292 860 282 916"
          fill="none" stroke="#fff4cf" stroke-width="1" opacity="0.65"/>
    <path d="M 334 660 C 340 760 348 860 358 916"
          fill="none" stroke="#fff4cf" stroke-width="1" opacity="0.65"/>
    <path d="M 290 962 L 285 985 M 290 962 L 295 985 M 290 962 L 300 983"
          stroke="#d4af37" stroke-width="1.3"/>
    <path d="M 350 962 L 345 985 M 350 962 L 355 985 M 350 962 L 360 983"
          stroke="#d4af37" stroke-width="1.3"/>
  </g>`);
  out.push(`<g class="wrapArt" style="transition-delay:2.1s">
    <path d="M 372 668 Q 400 720 412 760" stroke="#d4af37" stroke-width="1.2" fill="none"/>
    <g transform="translate(414, 760) rotate(8)">
      <rect x="-26" y="-38" width="52" height="66" rx="4" fill="#fffaf0" stroke="#d4af37" stroke-width="1.3"/>
      <rect x="-22" y="-34" width="44" height="58" rx="2" fill="none" stroke="#d4af37" stroke-width="0.5" opacity="0.55"/>
      <text x="0" y="-12" font-family="'Great Vibes', cursive" font-size="14" fill="#6b1428" text-anchor="middle">Happy</text>
      <text x="0" y="4"  font-family="'Great Vibes', cursive" font-size="14" fill="#6b1428" text-anchor="middle">Birthday</text>
      <path d="M 0,12 L 3,17 L 8,17 L 4,21 L 6,26 L 0,23 L -6,26 L -4,21 L -8,17 L -3,17 Z" fill="#d4af37"/>
    </g>
  </g>`);
  [[100,240,0],[540,250,.8],[70,420,1.6],[570,430,.4],[320,60,1.2],[210,500,2],[430,510,.6],[590,340,1.9],[50,340,1.1],[320,700,1.4]]
    .forEach(g => out.push(`<g transform="translate(${g[0]},${g[1]})">
      <path class="glint" style="--d:${g[2]}s" d="M0,-10 Q1.5,-1.5 10,0 Q1.5,1.5 0,10 Q-1.5,1.5 -10,0 Q-1.5,-1.5 0,-10Z"
            fill="#fff4cf" filter="url(#goldGlow)"/></g>`));
  document.getElementById('bouquet').innerHTML = out.join('');
}
buildBouquet();

(function splitName(){
  const el = document.getElementById('name');
  const txt = el.textContent.trim();
  el.innerHTML = `<span class="sr">${txt}</span>` + [...txt].map((ch,i)=>
    `<span class="ltr gold" aria-hidden="true" style="--d:${(0.75 + i*0.12).toFixed(2)}s">${ch === ' ' ? '&nbsp;' : ch}</span>`
  ).join('');
})();

const cvs = document.getElementById('fx');
const ctx = cvs.getContext('2d');
let W = 0, H = 0, DPR = 1;
function resize(){
  DPR = Math.min(window.devicePixelRatio || 1, 2);
  W = innerWidth; H = innerHeight;
  cvs.width = W * DPR; cvs.height = H * DPR;
}
resize();
addEventListener('resize', resize);

const rand = (a,b) => a + Math.random() * (b - a);
const pick = a => a[Math.random() * a.length | 0];
const TAU = Math.PI * 2;

function mk(draw){
  const s = document.createElement('canvas');
  s.width = s.height = 96;
  const c = s.getContext('2d');
  c.translate(48,48); c.scale(1.5,1.5);
  draw(c);
  return s;
}
function sakura(col, core){ return mk(c=>{
  for (let i = 0; i < 5; i++){
    c.save(); c.rotate(i * TAU / 5);
    const g = c.createLinearGradient(0,0,0,-28);
    g.addColorStop(0,'#ffffff'); g.addColorStop(.4,col); g.addColorStop(1,col);
    c.beginPath(); c.moveTo(0,0);
    c.bezierCurveTo(-13,-7,-14,-24,-4,-28); c.lineTo(0,-24); c.lineTo(4,-28);
    c.bezierCurveTo(14,-24,13,-7,0,0);
    c.fillStyle = g; c.fill(); c.restore();
  }
  c.beginPath(); c.arc(0,0,4.5,0,TAU); c.fillStyle = core; c.fill();
  for (let i = 0; i < 5; i++){
    const a = i * TAU / 5 + .63;
    c.beginPath(); c.arc(Math.sin(a)*8.5,-Math.cos(a)*8.5,1.7,0,TAU); c.fillStyle = '#f7d774'; c.fill();
  }
});}
function rose(col, dark){ return mk(c=>{
  for (let i = 0; i < 6; i++){
    c.save(); c.rotate(i * TAU / 6);
    c.beginPath(); c.ellipse(0,-14,12,14,0,0,TAU); c.fillStyle = col; c.fill(); c.restore();
  }
  const g = c.createRadialGradient(-4,-4,2,0,0,16);
  g.addColorStop(0,col); g.addColorStop(1,dark);
  c.beginPath(); c.arc(0,0,15,0,TAU); c.fillStyle = g; c.fill();
  c.strokeStyle = dark; c.lineWidth = 2.2; c.lineCap = 'round';
  [12,8.5,5.5,2.8].forEach((r,k)=>{ c.beginPath(); c.arc(k%2 ? 1.2 : -1.2, k%2 ? -1 : 1, r, k*1.4, k*1.4 + 4.4); c.stroke(); });
});}
function orchidSprite(col, dark){ return mk(c=>{
  for (let i = 0; i < 3; i++){
    c.save(); c.rotate(i * TAU / 3);
    c.beginPath(); c.ellipse(0,-19,6.5,17,0,0,TAU); c.fillStyle = dark; c.fill(); c.restore();
  }
  c.save(); c.rotate(-.4); c.beginPath(); c.ellipse(-15,-4,16,5,0,0,TAU); c.fillStyle = col; c.fill(); c.restore();
  c.save(); c.rotate(.4);  c.beginPath(); c.ellipse( 15,-4,16,5,0,0,TAU); c.fillStyle = col; c.fill(); c.restore();
  const g = c.createRadialGradient(0,0,1,0,0,14);
  g.addColorStop(0, '#fff4cf'); g.addColorStop(1, col);
  c.beginPath(); c.ellipse(0,6,9,12,0,0,TAU); c.fillStyle = g; c.fill();
  c.beginPath(); c.arc(0,0,4,0,TAU); c.fillStyle = '#f7e7a1'; c.fill();
});}
function petal(col){ return mk(c=>{
  const g = c.createRadialGradient(-3,-8,1,0,0,22);
  g.addColorStop(0,'#ffffff'); g.addColorStop(.35,col); g.addColorStop(1,col);
  c.beginPath(); c.moveTo(0,22);
  c.bezierCurveTo(-16,10,-14,-14,-4,-22); c.lineTo(0,-17); c.lineTo(4,-22);
  c.bezierCurveTo(14,-14,16,10,0,22);
  c.fillStyle = g; c.fill();
});}
function leaf(col){ return mk(c=>{
  c.beginPath(); c.moveTo(0,28); c.quadraticCurveTo(-17,0,0,-28); c.quadraticCurveTo(17,0,0,28);
  c.fillStyle = col; c.fill();
  c.strokeStyle = 'rgba(0,40,0,.3)'; c.lineWidth = 1.4; c.beginPath(); c.moveTo(0,26); c.lineTo(0,-24); c.stroke();
});}
function heart(col){ return mk(c=>{
  const g = c.createRadialGradient(-8,-10,2,0,0,28);
  g.addColorStop(0,'#ffffff'); g.addColorStop(.3,col); g.addColorStop(1,col);
  c.beginPath(); c.moveTo(0,22);
  c.bezierCurveTo(-32,2,-22,-26,0,-10); c.bezierCurveTo(22,-26,32,2,0,22);
  c.fillStyle = g; c.fill();
});}
function goldDust(){ return mk(c=>{
  const g = c.createRadialGradient(0,0,0,0,0,22);
  g.addColorStop(0, 'rgba(255,244,207,1)');
  g.addColorStop(.35,'rgba(247,215,116,.7)');
  g.addColorStop(1,  'rgba(212,175,55,0)');
  c.fillStyle = g; c.beginPath(); c.arc(0,0,22,0,TAU); c.fill();
  c.fillStyle = '#fff8dc'; c.beginPath();
  c.moveTo(0,-15); c.quadraticCurveTo(1.5,-1.5,15,0); c.quadraticCurveTo(1.5,1.5,0,15);
  c.quadraticCurveTo(-1.5,1.5,-15,0); c.quadraticCurveTo(-1.5,-1.5,0,-15); c.fill();
});}
function goldLeaf(col){ return mk(c=>{
  const g = c.createLinearGradient(-10,-10,10,10);
  g.addColorStop(0,'#fff4cf'); g.addColorStop(.5,col); g.addColorStop(1,'#8a6516');
  c.beginPath();
  c.moveTo(0,-15); c.bezierCurveTo(12,-5,15,10,0,15); c.bezierCurveTo(-15,10,-12,-5,0,-15);
  c.fillStyle = g; c.fill();
  c.strokeStyle = '#fff4cf'; c.lineWidth = 0.5; c.stroke();
});}
function pearl(){ return mk(c=>{
  const g = c.createRadialGradient(-3,-3,1,0,0,10);
  g.addColorStop(0,'#ffffff'); g.addColorStop(.4,'#fdfbf7'); g.addColorStop(1,'#bba99a');
  c.beginPath(); c.arc(0,0,10,0,TAU); c.fillStyle = g; c.fill();
  c.beginPath(); c.arc(-3,-3,3,0,TAU); c.fillStyle = 'rgba(255,255,255,0.8)'; c.fill();
});}
function silkRibbon(col){ return mk(c=>{
  const g = c.createLinearGradient(-10,0,10,0);
  g.addColorStop(0,col); g.addColorStop(.5,'rgba(255,255,255,0.4)'); g.addColorStop(1,col);
  c.beginPath();
  c.moveTo(-8,-20); c.bezierCurveTo(10,-10,-10,10,8,20); c.lineTo(4,20);
  c.bezierCurveTo(-14,10,6,-10,-12,-20);
  c.fillStyle = g; c.fill();
});}

const SPR = {
  flower:[ sakura('#ffb7d0','#e63950'), sakura('#f4c6d4','#a4161a'), sakura('#f5e6c8','#d4af37'),
           rose('#8b1e3f','#3d0b1c'), rose('#e63950','#6b1428'), rose('#f4c6d4','#a4161a'),
           orchidSprite('#f5e6c8','#a87b18'), orchidSprite('#f4c6d4','#8b1e3f'),
           orchidSprite('#6b2c4a','#3d0b26') ],
  petal: [ petal('#f4c6d4'), petal('#8b1e3f'), petal('#e63950'), petal('#f5e6c8'), petal('#6b2c4a') ],
  leaf:  [ leaf('#2d6a4f'), leaf('#1b4332') ],
  heart: [ heart('#e63950'), heart('#f4c6d4'), heart('#d4af37') ],
  gold:  [ goldDust(), goldLeaf('#d4af37') ],
  pearl: [ pearl() ],
  ribbon:[ silkRibbon('#f4c6d4'), silkRibbon('#8b1e3f') ]
};

function kind(){
  const r = Math.random();
  if (r < .40) return 'flower';
  if (r < .65) return 'petal';
  if (r < .75) return 'heart';
  if (r < .82) return 'leaf';
  if (r < .90) return 'gold';
  if (r < .96) return 'pearl';
  return 'ribbon';
}

const P = [];
const MAX = 700;
let ambient = 0;

function add(o){
  if (reduce || P.length >= MAX) return;
  P.push(Object.assign({
    rot:rand(0,TAU), vr:rand(-.08,.08), flip:rand(0,TAU), vf:rand(.02,.07),
    sway:0, swayP:rand(0,TAU), age:0, drag:.98, g:.08, term:4.5, life:200, op:1, fi:6, type:'petal'
  }, o));
}
function sparks(x, y, n, power){
  for (let i = 0; i < n; i++){
    const a = Math.random() * TAU, sp = power * rand(.3,1.4);
    add({ spr:SPR.gold[0], x, y, vx:Math.cos(a)*sp, vy:Math.sin(a)*sp, size:rand(8,20),
          g:.02, drag:.94, life:rand(50,100), twinkle:true, vr:0, type:'gold' });
  }
}
function burst(x, y, n = 40, power = 8, ring = false){
  for (let i = 0; i < n; i++){
    const a = ring ? i / n * TAU : Math.random() * TAU;
    const sp = power * (ring ? rand(.85,1.05) : rand(.25,1));
    const k = kind();
    add({ spr:pick(SPR[k]), x, y, vx:Math.cos(a)*sp, vy:Math.sin(a)*sp - power*.25,
          size:k === 'flower' ? rand(22,40) : rand(12,24), g:rand(.06,.1), drag:rand(.965,.98),
          life:rand(170,260), sway:rand(.2,.8), type:k });
  }
  sparks(x, y, Math.round(n * .6), power);
}
function cannon(x, y, dir, n, power){
  for (let i = 0; i < n; i++){
    const a = dir + rand(-.3,.3), sp = power * rand(.6,1.15), k = kind();
    add({ spr:pick(SPR[k]), x, y, vx:Math.cos(a)*sp, vy:Math.sin(a)*sp,
          size:k === 'flower' ? rand(20,34) : rand(12,22), g:.13, drag:.988, term:3.6,
          life:rand(260,340), sway:rand(.3,1), type:k });
  }
  sparks(x, y, n / 2, power * .7);
}
function miniBurst(x, y){
  for (let i = 0; i < 10; i++){
    const a = Math.random() * TAU, sp = rand(2,4.8);
    add({ spr:pick(SPR.petal), x, y, vx:Math.cos(a)*sp, vy:Math.sin(a)*sp - 1.5,
          size:rand(9,16), g:.06, drag:.97, life:rand(90,150), sway:rand(.2,.6), type:'petal' });
  }
  sparks(x, y, 8, 4);
}
function rain(n){
  for (let i = 0; i < n; i++){
    const k = kind();
    add({ spr:pick(SPR[k]), x:rand(0,W), y:rand(-H*.7,-20), vx:rand(-.5,.5), vy:rand(1.4,3),
          g:.004, drag:1, term:4, life:1e9, size:k === 'flower' ? rand(20,34) : rand(12,22), sway:rand(.4,1.2), type:k });
  }
}
function spawnAmbient(){
  const r = Math.random(), k = r < .5 ? 'petal' : r < .88 ? 'flower' : 'gold';
  ambient++;
  add({ spr:pick(SPR[k]), x:rand(0,W), y:-30, vx:rand(-.3,.3), vy:rand(.6,1.3), g:0, drag:1, term:9,
        life:1e9, size:k === 'flower' ? rand(14,24) : rand(10,18), sway:rand(.3,1), op:rand(.5,.85), amb:true, type:k });
}
function spawnDust(){
  add({ spr:SPR.gold[0], x:rand(0,W), y:rand(0,H), vx:rand(-.1,.1), vy:rand(-.35,-.1), g:0, drag:1,
        life:rand(80,140), size:rand(5,11), twinkle:true, vr:0, op:.85, fi:25, type:'gold' });
}

let started = false, last = performance.now();
function tick(now){
  const dt = Math.min(3, (now - last) / 16.667); last = now;
  ctx.setTransform(1,0,0,1,0,0);
  ctx.clearRect(0,0,cvs.width,cvs.height);

  if (started){
    if (ambient < 30 && Math.random() < .1 * dt) spawnAmbient();
    if (Math.random() < .18 * dt) spawnDust();
  }

  for (let i = P.length - 1; i >= 0; i--){
    const p = P[i];
    p.age += dt;
    const left = p.life - p.age;
    if (left <= 0 || p.y > H + 60 || p.x < -90 || p.x > W + 90){
      if (p.amb) ambient--;
      P.splice(i,1); continue;
    }
    if (p.type === 'ribbon') {
      p.vy = Math.min(p.vy + 0.01, 2.5);
      p.sway += 0.002;
    } else if (p.type === 'gold') {
      p.vr *= 1.02;
    } else if (p.type === 'pearl') {
      p.vy = Math.min(p.vy + 0.05, 5);
    }

    const dk = Math.pow(p.drag, dt);
    p.vx *= dk;
    p.vy = p.vy * dk + p.g * dt;
    if (p.vy > p.term) p.vy = p.term;
    p.x += (p.vx + Math.sin(p.age * .03 + p.swayP) * p.sway) * dt;
    p.y += p.vy * dt;
    p.rot += p.vr * dt; p.flip += p.vf * dt;

    let a = p.op;
    if (left < 40) a *= left / 40;
    if (p.age < p.fi) a *= p.age / p.fi;
    if (p.twinkle) a *= .55 + .45 * Math.sin(p.age * .35 + p.swayP);
    ctx.globalAlpha = Math.max(0, a);

    const sx = p.twinkle ? 1 : Math.cos(p.flip);
    const cr = Math.cos(p.rot), sr = Math.sin(p.rot), s = p.size;
    ctx.setTransform(DPR*cr*sx, DPR*sr*sx, -DPR*sr, DPR*cr, DPR*p.x, DPR*p.y);
    ctx.drawImage(p.spr, -s/2, -s/2, s, s);
  }
  ctx.globalAlpha = 1;
  requestAnimationFrame(tick);
}
if (!reduce) requestAnimationFrame(tick);

function cannons(){
  const power = Math.sqrt(H) * .56;
  cannon(-10, H + 10, -Math.PI / 3, 60, power);
  cannon(W + 10, H + 10, -Math.PI * 2 / 3, 60, power);
}
function bloomBlasts(){
  const svg = document.getElementById('bouquet');
  roses.forEach(f => setTimeout(() => {
    const r = svg.getBoundingClientRect();
    const x = r.left + f.x / 640 * r.width;
    const y = r.top + f.y / 960 * r.height;
    if (y > -40 && y < H + 40) miniBurst(x, y);
  }, (f.d + .4) * 1000));
}
function grandOpening(){
  burst(W/2, H*.42, 70, 10, true);
  burst(W/2, H*.42, 50, 7);
  [[.18,.28],[.82,.26],[.5,.15],[.25,.56],[.75,.58]].forEach((p,i) =>
    setTimeout(() => burst(W*p[0], H*p[1], 40, 7), 450 + i*330));
  setTimeout(cannons, 1900);
  setTimeout(() => rain(46), 2700);
  bloomBlasts();
  setInterval(() => {
    if (!document.hidden) burst(rand(W*.15, W*.85), rand(H*.12, H*.45), 26, 6);
  }, 5400);
}

const intro = document.getElementById('intro');
function openGift(e){
  if (started) return;
  started = true;
  if (e) {
    e.preventDefault();
    e.stopPropagation();
  }
  intro.classList.add('hide');
  document.body.classList.add('started');
  grandOpening();
}
intro.addEventListener('click', openGift);
intro.addEventListener('touchstart', function(e) {
  e.preventDefault();
  openGift(e);
}, {passive: false});
intro.addEventListener('mousedown', openGift);
intro.addEventListener('keydown', e => {
  if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); openGift(e); }
});
intro.focus();

document.addEventListener('click', e => {
  if (!started || e.target.closest('#more')) return;
  burst(e.clientX, e.clientY, 26, 6);
});

document.getElementById('more').addEventListener('click', () => {
  burst(W/2, H*.4, 60, 10, true);
  cannons();
  rain(60);
});
</script>
</body>
</html>
"""

components.html(BIRTHDAY_HTML, height=2000, scrolling=True)
