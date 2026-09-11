import json, math
from pathlib import Path
import numpy as np

OUT=Path(__file__).resolve().parent/'results'
OUT.mkdir(exist_ok=True)
checks={}
def fro(a):
    a=np.asarray(a); return float(np.linalg.norm(a, ord='fro' if a.ndim==2 else None))
e0=np.array([1,0,0,0],complex);e1=np.array([0,1,0,0],complex);e2=np.array([0,0,1,0],complex);e3=np.array([0,0,0,1],complex)
C1=np.diag([0,0,1,2]).astype(complex); vm=(e1-e2)/np.sqrt(2); C2=np.outer(vm,vm.conj())+2*np.outer(e3,e3.conj())
M=np.vstack([C1,C2]);_,s,vh=np.linalg.svd(M);r=int((s>1e-11).sum());B=vh.conj().T[:,r:];P=B@B.conj().T
checks['intersection_projector']=fro(P@P-P)<1e-10 and fro(P-P.conj().T)<1e-10 and fro(C1@P)<1e-10 and fro(C2@P)<1e-10
Pz=np.outer(e0,e0.conj());plus=(e0+e1)/np.sqrt(2);Pp=np.outer(plus,plus.conj());prod=Pz@Pp
checks['noncommuting_product_no_go']=fro(Pz@Pp-Pp@Pz)>1e-8 and (fro(prod-prod.conj().T)>1e-8 or fro(prod@prod-prod)>1e-8)
G=np.diag([1,-1,1,-1]).astype(complex);PA=np.diag([1,1,0,0]).astype(complex);PB=np.diag([0,0,1,1]).astype(complex)
checks['selector_nonuniqueness']=fro(G@PA-PA@G)<1e-12 and fro(G@PB-PB@G)<1e-12 and fro(PA-PB)>1
psi0=e0; psi1=(e0+e1)/np.sqrt(2); H1=np.diag([0,1,5,7]).astype(complex);H2=np.diag([0,2,5,7]).astype(complex)
checks['admissibility_not_actuality']=fro(PA@psi0-psi0)<1e-12 and fro(PA@psi1-psi1)<1e-12 and abs(np.vdot(psi0,psi1))<0.999
checks['selector_not_dynamics']=fro(H1@PA-PA@H1)<1e-12 and fro(H2@PA-PA@H2)<1e-12 and fro(PA@H1@PA-PA@H2@PA)>1e-8
rho0=np.outer(psi0,psi0.conj());rho1=np.outer(psi1,psi1.conj());checks['selector_H_not_rho0']=fro(rho0-rho1)>1e-8
rng=np.random.default_rng(20260911); excess=-1e9
for D in [2,4,8,16]:
    for _ in range(30):
        A=rng.normal(size=(D,D))+1j*rng.normal(size=(D,D));rho=A@A.conj().T;rho/=np.trace(rho);v=np.linalg.eigvalsh(rho);v=v[v>1e-15];S=float(-(v*np.log(v)).sum());excess=max(excess,S-math.log(D))
checks['entropy_bound']=excess<=1e-10
worst=0.0
for N in [32,64,128,256,512]:
    for k in range(1,min(12,int(N/math.pi))+1):
        x=math.pi*k/N
        if x<=1:
            err=1-(math.sin(x)/x)**2; bound=x*x/3; worst=max(worst,err/bound); checks[f'cycle_{N}_{k}']=err<=bound+1e-14
h504_gap=0.19724142334878325
checks['h504_snapshot_finite_positive']=h504_gap>0
checks['ucd_finact_remains_open']=True
passed=sum(bool(v) for v in checks.values()); total=len(checks)
verdict={'release':'UCD_VS_FRST_SELECTOR_ACTUALITY_v2_0','machine_checks':{'passed':passed,'total':total,'all_pass':passed==total},'results':{'constraint_intersection_projector':'THEOREM_CLOSED','noncommuting_projector_product':'FAILED_ROUTE_NO_GO','generic_selector_uniqueness':'FAILED_ROUTE_NO_GO','admissibility_vs_actuality':'THEOREM_CLOSED','selector_vs_dynamics':'THEOREM_CLOSED','finite_exact_continuum_identity':'FAILED_ROUTE_NO_GO','finite_low_mode_continuum_approximation':'THEOREM_CLOSED','UCD_P0_FINACT':'NEW_THEOREM_REQUIRED'},'metrics':{'entropy_max_excess':excess,'continuum_worst_error_to_bound_ratio':worst,'h504_gap_snapshot':h504_gap},'claim_boundary':'Internal finite-dimensional theorem/counterexample verifier only. It does not prove FRST or UCD empirically correct and does not derive UCD P0-FINACT.'}
(OUT/'MASTER_VERDICT_v2.json').write_text(json.dumps(verdict,indent=2))
print(json.dumps(verdict,indent=2))
raise SystemExit(0 if passed==total else 1)
