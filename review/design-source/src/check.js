()=>{const ph=document.querySelector('.phone');const pr=ph.getBoundingClientRect();const out=[];
const els=[...ph.querySelectorAll('*')].filter(e=>[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim()));
const R=els.map(e=>{const r=document.createRange();r.selectNodeContents(e);return [e,r.getBoundingClientRect(),[...r.getClientRects()]]});
for(const [e,r] of R){ if(r.right>pr.right+1||r.left<pr.left-1||r.bottom>pr.bottom+1) out.push('OUT '+e.textContent.trim().slice(0,12)+' '+Math.round(r.right));
 const par=e.closest('.card,.chip,.op,.btn,.tx,.bub,.tag,.cta,.bx,.mo,.ch>div,.opt>div,.rw,.tg>div');
 if(par&&par!==e){const q=par.getBoundingClientRect(); if(r.right>q.right+1||r.left<q.left-1||r.bottom>q.bottom+1||r.top<q.top-1) out.push('SPILL '+e.textContent.trim().slice(0,14)+' in '+par.className)}}
for(let i=0;i<R.length;i++)for(let j=i+1;j<R.length;j++){const [a,,ca]=R[i],[b,,cb]=R[j]; if(a.contains(b)||b.contains(a))continue;
 let hit=null;for(const ra of ca)for(const rb of cb){const ox=Math.min(ra.right,rb.right)-Math.max(ra.left,rb.left),oy=Math.min(ra.bottom,rb.bottom)-Math.max(ra.top,rb.top);if(ox>3&&oy>4&&ra.width>0&&rb.width>0)hit=Math.round(ox)+'x'+Math.round(oy)}
 if(hit) out.push('OVERLAP "'+a.textContent.trim().slice(0,10)+'" & "'+b.textContent.trim().slice(0,10)+'" '+hit)}
return out}
