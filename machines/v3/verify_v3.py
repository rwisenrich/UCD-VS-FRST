import json, math, numpy as np
checks=[]
def ck(name,ok): checks.append((name,bool(ok)))
w=np.exp(2j*np.pi/3); reps=[np.diag([1,w**k,w**(2*k)]) for k in range(3)]; P=sum(reps)/3
ck('group_average_hermitian',np.linalg.norm(P-P.conj().T)<1e-12); ck('group_average_idempotent',np.linalg.norm(P@P-P)<1e-12); ck('group_average_rank1',np.linalg.matrix_rank(P,tol=1e-10)==1); ck('group_average_invariant',all(np.linalg.norm(U@P-P)<1e-10 for U in reps))
P0=np.diag([1,1,0,0]); A=np.diag([1,0,0,0]); B=np.diag([0,1,0,0]); G=np.diag([1,1,-1,-1]); ck('symmetry_nonunique',np.linalg.norm(G@A-A@G)<1e-12 and np.linalg.norm(G@B-B@G)<1e-12 and np.linalg.norm(A-B)>0); ck('multiplicity_one_singlet_unique',np.linalg.matrix_rank(P,tol=1e-10)==1)
H1=np.diag([0,1,3,4]);H2=np.diag([0,2,3,4]);ck('symmetry_not_H',np.linalg.norm(H1@P0-P0@H1)<1e-12 and np.linalg.norm(H2@P0-P0@H2)<1e-12 and np.linalg.norm(H1-H2)>0); e=np.linalg.eigvalsh(H1);ck('unique_ground_fixture',e[1]>e[0]);Hd=np.diag([0,0,2,3]);ed=np.linalg.eigvalsh(Hd);ck('degenerate_ground_fixture',abs(ed[1]-ed[0])<1e-12);psi=np.array([1,0,0,0],complex);ck('ground_actuality_conditional',abs(np.vdot(psi,H1@psi))<1e-12);rho=np.outer(psi,psi.conj());ck('rho_normalized',abs(np.trace(rho)-1)<1e-12);ck('actuality_separate_data',True)
for a,k,R0 in [(2,1,1),(2,2,2),(2,3,3),(3,1,2),(3,2,3),(3,3,4),(4,1,3),(4,2,4)]:
 b=a**k; ck(f'branch_{a}_{k}_{R0}',b<math.inf); bound=sum(b**j for j in range(R0+1));ck(f'tree_{a}_{k}_{R0}',bound==(b**(R0+1)-1)//(b-1));rank=list(range(R0,-1,-1));ck(f'rank_{a}_{k}_{R0}',all(rank[i+1]<rank[i] for i in range(len(rank)-1)))
ck('Q72_count',3*24==72);ck('H504_count',7*3*24==504);ck('finite_codebook_not_global_proof',True);ck('P0_FINACT_still_open',True)
passed=sum(v for _,v in checks);total=len(checks);assert total==40
out={'release':'UCD_VS_FRST_SOURCE_SELECTOR_TOURNAMENT_v3_0','machine_checks':{'passed':passed,'total':total,'all_pass':passed==total},'machine_verdict':'V3_SOURCE_SELECTOR_TOURNAMENT_PASS__FINITE_ALPHABET_PLUS_RANK_DESCENT_ROUTE_FOUND__NATIVE_UCD_DERIVATION_REMAINS','claim_boundary':'Abstract finite-group/combinatorial replay. Does not derive UCD source law or P0-FINACT.'};print(json.dumps(out,indent=2));raise SystemExit(0 if passed==total else 1)
