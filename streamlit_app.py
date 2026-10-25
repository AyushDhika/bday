


    
  
  if (reduce || running) return;
  running = true; last = performance.now();
  requestAnimationFrame(tick);
}
document.addEventListener('visibilitychange', () => {
  if (document.hidden){ running = false; }
  else if (started){ running = true; last = performance.now(); requestAnimationFrame(tick); }
});

/* =========================================================
   7. FLOODS
   ========================================================= */
function floodMedium(){
  MAX = MAX_SHOWER;
  const cx = W/2, cy = H*.42;
  const power = Math.sqrt(W*W + H*H) / 24;

  for (let i = 0; i < 60; i++){
    const a = i/60*TAU, k = kind();
    add({ spr:pick(SPR[k]), x:cx, y:cy,
          vx:Math.cos(a)*power*rand(.9,1.1), vy:Math.sin(a)*power*rand(.9,1.1) - 2,
          size:k==='flower'?rand(22,36):rand(12,20),
          g:.05, drag:.98, term:3, life:rand(200,280), sway:rand(.2,.6) });
  }
  rain(50, { speed:[1.6,3], size:[12,22], flowerSize:[20,32] });
  setTimeout(() => { MAX = MAX_NORMAL; }, 2800);
}

function flood(){
  MAX = MAX_SHOWER;
  const cx = W/2, cy = H*.40;
  const diag = Math.sqrt(W*W + H*H);
  const power = diag / 22;

  for (let i = 0; i < 100; i++){
    const a = i/100*TAU, k = kind();
    add({ spr:pick(SPR[k]), x:cx, y:cy,
          vx:Math.cos(a)*power*rand(.8,1.05),
          vy:Math.sin(a)*power*rand(.8,1.05) - 2,
          size:k==='flower'?rand(24,42):rand(14,24),
          g:.04, drag:.975, term:2.5, life:rand(260,360),
          sway:rand(.2,.7) });
  }
  for (let i = 0; i < 60; i++){
    const a = Math.random()*TAU, sp = power*rand(.1,.9), k = kind();
    add({ spr:pick(SPR[k]), x:cx, y:cy,
          vx:Math.cos(a)*sp, vy:Math.sin(a)*sp - 3,
          size:k==='flower'?rand(24,42):rand(14,24),
          g:.045, drag:.975, term:2.5, life:rand(260,360),
          sway:rand(.2,.7) });
  }
  rain(90, { speed:[1.6,3.6], size:[14,26], flowerSize:[22,38] });

  [[.14,.24],[.86,.24]].forEach(([fx,fy]) => {
    const px = W*fx, py = H*fy;
    for (let i = 0; i < 20; i++){
      const a = Math.random()*TAU, sp = rand(4,10), k = kind();
      add({ spr:pick(SPR[k]), x:px, y:py,
            vx:Math.cos(a)*sp, vy:Math.sin(a)*sp,
            size:k==='flower'?rand(20,34):rand(12,20),
            g:.07, drag:.975, term:3.4, life:rand(200,280),
            sway:rand(.2,.6) });
    }
  });
  cannon(-10, H*.55, 0, 36, power*.85);
  cannon(W+10, H*.55, Math.PI, 36, power*.85);
  sparks(cx, cy, 40, 8);

  setTimeout(() => {
    if (!started) return;
    MAX = MAX_SHOWER;
    for (let i = 0; i < 70; i++){
      const a = Math.random()*TAU, sp = power*rand(.4,1.1), k = kind();
      add({ spr:pick(SPR[k]), x:rand(0,W), y:rand(-40, H*.3),
            vx:Math.cos(a)*sp*.6, vy:Math.sin(a)*sp*.6 + 1,
            size:k==='flower'?rand(24,42):rand(14,24),
            g:.045, drag:.975, term:2.5, life:rand(260,360),
            sway:rand(.2,.7) });
    }
    rain(40, { speed:[1.6,3.4], size:[14,24], flowerSize:[22,36] });
    setTimeout(() => { MAX = MAX_NORMAL; }, 2600);
  }, 350);
}

/* =========================================================
   8. CHOREOGRAPHY
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
  floodMedium();
  burst(W/2, H*.42, 36, 9, true);
  [[.2,.3],[.8,.28],[.5,.16]].forEach((p,i) =>
    setTimeout(() => burst(W*p[0], H*p[1], 20, 6), 400 + i*320));
  setTimeout(cannons, 1500);
  setTimeout(() => rain(22), 2200);
  bloomBlasts();
}

/* =========================================================
   9. BOOT
   ========================================================= */
try { buildBouquet(); } catch(e){ console.error(e); }
try { splitName(); }    catch(e){ console.error(e); }

document.getElementById('more').addEventListener('click', () => {
  startLoop();
  flood();
});
</script>
</body>
</html>
"""

