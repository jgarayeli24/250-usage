# Script usado para armar el piloto de Tranqui. Ajusta las rutas S, P, A y W, la lista de escenas y los tiempos para cada vídeo nuevo.
import subprocess, json, os
S='/tmp/claude-0/-home-user-250-usage/9b0e3052-9d6c-5ef8-aec1-12ec09faba9f/scratchpad'
P=f'{S}/piloto'; A='/home/user/250-usage/canal-tranqui/assets'; W=f'{S}/montaje'; os.makedirs(W,exist_ok=True)
pick=json.load(open(f'{P}/picks.json'))['pick']
def img(k): return f'{P}/{k}_{pick[k]}.png'
def clip(k): return f'{P}/{k}_0.mp4'
FPS=25; GAP=0.4
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
voices=[f'{A}/voz-apertura-piloto-toma1.mp3']+[f'{P}/v{i}_0.mp3' for i in range(3,8)]
D=[dur(v) for v in voices]
# visual plan per block: list of (type, source, end_time_within_block or None=fill)
plan=[
 [('img',img('s1a'),4.5),('clip',clip('c1b'),9.5),('img',img('s1b'),19.8),('clip',clip('c2'),24.8),('img',img('s2'),None)],
 [('img',img('s3a'),28.9),('clip',clip('c3b'),33.9),('img',img('s3b'),35.2),('img',img('s2'),45.8),('img',img('s3c'),None)],
 [('clip',clip('c4a'),5.0),('img',img('s4b'),13.8),('img',img('s4c'),31.5),('clip',clip('c4d'),36.5),('img',img('s4d'),43.8),('img',img('s4e'),None)],
 [('img',img('s2'),7.8),('img',img('s3a'),18.8),('img',img('s5a'),31.9),('img',img('s5b'),36.7),('img',img('s5c'),63.0),('clip',clip('c5d'),68.0),('img',img('s5d'),None)],
 [('img',img('s6b'),19.2),('clip',clip('c6a'),24.2),('img',img('s6a'),33.1),('img',img('s6b'),None)],
 [('img',img('s4a'),10.35),('clip',f'{A}/clip-cierre-piloto.mp4',15.35),('img',f'{A}/fotograma-cierre-piloto.png',None)],
]
segs=[]; n=0
for b,(items,d) in enumerate(zip(plan,D)):
    total=d+(GAP if b<len(D)-1 else 1.5)
    t=0
    for typ,src,end in items:
        e=total if end is None else end
        ln=round(e-t,3); t=e
        out=f'{W}/seg{n:03d}.mp4'; n+=1
        fr=int(round(ln*FPS))
        if typ=='img':
            zin = n%2==0
            z = "min(zoom+0.0007,1.15)" if zin else "if(eq(on,0),1.15,max(zoom-0.0007,1.0))"
            vf=f"scale=2560:-2,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1280x720:fps={FPS},format=yuv420p"
            cmd=['ffmpeg','-v','error','-y','-loop','1','-i',src,'-vf',vf,'-frames:v',str(fr),'-c:v','libx264','-preset','veryfast','-crf','20',out]
        else:
            vf=f"scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps={FPS},tpad=stop_mode=clone:stop_duration=30,format=yuv420p"
            cmd=['ffmpeg','-v','error','-y','-i',src,'-vf',vf,'-an','-frames:v',str(fr),'-c:v','libx264','-preset','veryfast','-crf','20',out]
        subprocess.run(cmd,check=True); segs.append(out)
with open(f'{W}/list.txt','w') as f:
    for s in segs: f.write(f"file '{s}'\n")
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{W}/list.txt','-c','copy',f'{W}/video.mp4'],check=True)
# block start times
starts=[]; t=0
for b,d in enumerate(D): starts.append(t); t+=d+GAP
end=t-GAP+1.5
json.dump({'starts':starts,'D':D,'end':end},open(f'{W}/timing.json','w'))
print('blocks',[round(s,2) for s in starts],'end',round(end,2),'segs',len(segs))
