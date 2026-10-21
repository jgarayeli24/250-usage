# Script usado para armar el piloto de Tranqui. Ajusta las rutas S, P, A y W, la lista de escenas y los tiempos para cada vídeo nuevo.
import subprocess, json, os
S='/tmp/claude-0/-home-user-250-usage/9b0e3052-9d6c-5ef8-aec1-12ec09faba9f/scratchpad'
P=f'{S}/piloto'; A='/home/user/250-usage/canal-tranqui/assets'; W=f'{S}/montaje'
T=json.load(open(f'{W}/timing.json')); st=T['starts']; END=T['end']
voices=[f'{A}/voz-apertura-piloto-toma1.mp3']+[f'{P}/v{i}_0.mp3' for i in range(3,8)]
music=f'{A}/tema-musical-opcion1.mp3'
fx={'brake':f'{P}/fxbrake_1.mp3','plop':f'{P}/fxplop_0.mp3','whoosh':f'{P}/fxwhoosh_0.mp3'}
cues=[('brake',4.3),('whoosh',5.0),('plop',6.8),('brake',st[2]+0.3),('whoosh',st[2]+5.2),('plop',st[2]+33.5),('plop',st[3]+64.5)]
falls=[6.8,st[2]+33.5,st[3]+64.5]
# ---- audio
inp=[]; fl=[]; idx=0
for i,v in enumerate(voices):
    inp+=['-i',v]; ms=int(st[i]*1000); fl.append(f'[{idx}:a]adelay={ms}|{ms},aformat=channel_layouts=stereo[v{i}]'); idx+=1
inp+=['-stream_loop','-1','-i',music]; fl.append(f'[{idx}:a]volume=0.13,atrim=0:{END},afade=t=in:d=1.5,afade=t=out:st={END-3}:d=3,aformat=channel_layouts=stereo[mus]'); idx+=1
for j,(k,t) in enumerate(cues):
    inp+=['-i',fx[k]]; ms=int(t*1000); vol=0.55 if k!='plop' else 0.8
    fl.append(f'[{idx}:a]volume={vol},adelay={ms}|{ms},aformat=channel_layouts=stereo[f{j}]'); idx+=1
mixin=''.join(f'[v{i}]' for i in range(len(voices)))+'[mus]'+''.join(f'[f{j}]' for j in range(len(cues)))
n=len(voices)+1+len(cues)
fl.append(f'{mixin}amix=inputs={n}:normalize=0:duration=longest,atrim=0:{END},loudnorm=I=-14:TP=-1.5:LRA=11[aout]')
subprocess.run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(fl),'-map','[aout]','-c:a','aac','-b:a','192k',f'{W}/audio.m4a'],check=True)
# ---- text overlays
TX=f'{W}/txt'; os.makedirs(TX,exist_ok=True)
BOLD='/usr/share/fonts/opentype/inter/Inter-Bold.otf'; BLACK='/usr/share/fonts/opentype/inter/Inter-Black.otf'
labels=[ # (text, start, end, kind)
 ('¿QUÉ PASARÍA SI LA TIERRA DEJARA DE GIRAR?',25.2,31.5,'title'),
 ('Ecuador: 1.670 km/h',st[1]+7.7,st[1]+10.8,'lab'),
 ('Bogotá: ~1.660 km/h',st[1]+10.8,st[1]+16.5,'lab'),
 ('Ciudad de México: ~1.575 km/h',st[1]+16.5,st[1]+21.7,'lab'),
 ('Buenos Aires: ~1.375 km/h',st[1]+21.7,st[1]+25.5,'lab'),
 ('Madrid: ~1.270 km/h',st[1]+25.5,st[1]+28.9,'lab'),
 ('Avión comercial: ~900 km/h',st[1]+28.9,st[1]+33.9,'lab'),
 ('Tornado récord: ~480 km/h',st[2]+17.3,st[2]+24.5,'lab'),
 ('Viento en el ecuador: +1.600 km/h',st[2]+24.5,st[2]+31.5,'lab'),
 ('6 meses de día · 6 meses de noche',st[3]+18.8,st[3]+31.9,'lab'),
 ('Ecuador: ~21 km más ancho que los polos',st[3]+40.5,st[3]+51.0,'lab'),
 ('Hace 70 millones de años: día de ~23,5 h',st[4]+19.2,st[4]+29.4,'lab'),
 ('La Luna se aleja ~3,8 cm por año',st[4]+33.1,st[4]+40.0,'lab'),
 ('PRÓXIMO: ¿Y si la Luna desapareciera?',st[5]+17.0,END,'title2'),
]
for i,c in enumerate(['1','2','3']):
    labels.append((f'Clementinas caídas: {c}',falls[i],falls[i+1] if i<2 else END,'count'))
vf=[]
for i,(txt,a,b,kind) in enumerate(labels):
    f=f'{TX}/t{i}.txt'; open(f,'w').write(txt)
    if kind=='title': s=f"fontfile={BLACK}:fontsize=42:fontcolor=white:borderw=6:bordercolor=0x4A2C17:line_spacing=8:x=(w-text_w)/2:y=h-text_h-50"
    elif kind=='title2': s=f"fontfile={BLACK}:fontsize=46:fontcolor=white:borderw=6:bordercolor=0x4A2C17:x=(w-text_w)/2:y=h-text_h-50"
    elif kind=='count': s=f"fontfile={BOLD}:fontsize=30:fontcolor=white:box=1:boxcolor=0xF28C28@0.92:boxborderw=14:x=w-text_w-40:y=36"
    else: s=f"fontfile={BOLD}:fontsize=44:fontcolor=white:box=1:boxcolor=0x4A2C17@0.85:boxborderw=20:x=(w-text_w)/2:y=h-text_h-70"
    vf.append(f"drawtext=textfile={f}:{s}:enable='between(t,{a:.2f},{b:.2f})'")
out='/home/user/250-usage/canal-tranqui/piloto/piloto-tierra-deja-de-girar.mp4'; os.makedirs(os.path.dirname(out),exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/video.mp4','-i',f'{W}/audio.m4a','-vf',','.join(vf),'-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-crf','21','-c:a','copy','-shortest','-movflags','+faststart',out],check=True)
print('done',out)
