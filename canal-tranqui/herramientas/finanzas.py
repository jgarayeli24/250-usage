# Modelo financiero canal Tranqui, 24 meses
GOOGLE=25.0      # Google AI Pro 19.99 + IVA 21% aprox
def costo(m):
    if m<=3: return GOOGLE+6            # 2 videos/mes, ElevenLabs Starter
    return GOOGLE+22+10                 # 4 videos/mes, ElevenLabs Creator + colchon creditos Flow
# vistas largas por mes (meses 1-12), luego crecimiento mensual
esc={
 'Pesimista':dict(v=[300,600,1000,1500,2000,2500,3000,3500,4000,5000,6000,7000],g=1.05,rpm=1.0,spon=0,spon_desde=99),
 'Base':     dict(v=[1000,2000,4000,7000,12000,18000,25000,35000,50000,70000,90000,120000],g=1.06,rpm=2.0,spon=150,spon_desde=11),
 'Optimista':dict(v=[2000,5000,15000,40000,80000,120000,180000,250000,300000,400000,500000,600000],g=1.03,rpm=3.5,spon=500,spon_desde=7),
}
VPH=15  # vistas por hora de visualizacion: 4 min promedio por vista
SUBS_POR_VISTA=1/150
for n,e in esc.items():
    v=e['v'][:]
    while len(v)<24: v.append(int(v[-1]*e['g']))
    cum=0; ypp=None; c1=c2=i1=i2=0; rows=[]
    for m in range(1,25):
        cum+=v[m-1]
        horas=sum(v[max(0,m-12):m])/VPH; subs=cum*SUBS_POR_VISTA
        if ypp is None and horas>=4000 and subs>=1000: ypp=m+1   # aprobacion al mes siguiente
        ads = v[m-1]*e['rpm']/1000 if ypp and m>=ypp else 0
        sp = e['spon'] if m>=e['spon_desde'] else 0
        ing=ads+sp; c=costo(m)
        if m<=12: c1+=c; i1+=ing
        else: c2+=c; i2+=ing
        rows.append((m,v[m-1],round(subs),round(ing),round(c)))
    print(f"\n{n}: monetiza mes {ypp}  | Año1 costo {c1:.0f} ingreso {i1:.0f} neto {i1-c1:.0f} | Año2 costo {c2:.0f} ingreso {i2:.0f} neto {i2-c2:.0f}")
    print("  mes12:",rows[11],"mes24:",rows[23])
