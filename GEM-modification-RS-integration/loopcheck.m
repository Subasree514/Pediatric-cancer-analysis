%% remove TICs
[rxnInLoopfinal, Nfinal, loopInfofinal] = findMinNull(modelnew);
find(rxnInLoopfinal(:,1)==1);
backward_loops=modelnew.rxns(ans);
find(rxnInLoopfinal(:,2)==1);
forward_loops=modelnew.rxns(ans);
both_loops=intersect(forward_loops,backward_loops);
both_loop_rs=intersect(both_loops,model.rxns);
printRxnFormula(modelnew,both_loop_rs)
%%
both_loop_id=findRxnIDs(modelnew,both_loop_rs);
modelnew.lb(both_loop_id)=0;
modelnew.ub(both_loop_id)=0;
%%
[rxnInLoopfinal, Nfinal, loopInfofinal] = findMinNull(modelnew);
find(rxnInLoopfinal(:,1)==1);
backward_loop_2=modelnew.rxns(ans);
find(rxnInLoopfinal(:,2)==1);
forward_loop_2=modelnew.rxns(ans);
both_loops_2=intersect(forward_loop_2,backward_loop_2);
both_loop_rs_2=intersect(both_loops_2,model.rxns);
for_rs_2=intersect(forward_loop_2,model.rxns);
back_rs_2=intersect(backward_loop_2,model.rxns);
printRxnFormula(modelnew,both_loop_rs_2)
printRxnFormula(modelnew,for_rs_2)
printRxnFormula(modelnew,back_rs_2)
%%
back_loop_id_2=findRxnIDs(modelnew,back_rs_2);
modelnew.lb(back_loop_id_2)=0;
%%
[rxnInLoopfinal, Nfinal, loopInfofinal] = findMinNull(modelnew);
find(rxnInLoopfinal(:,1)==1);
backward_loop_3=modelnew.rxns(ans);
find(rxnInLoopfinal(:,2)==1);
forward_loop_3=modelnew.rxns(ans);
both_loops_3=intersect(forward_loop_3,backward_loop_3);
both_loop_rs_3=intersect(both_loops_3,model.rxns);
for_rs_3=intersect(forward_loop_3, model.rxns);
back_rs_3=intersect(backward_loop_3,model.rxns);
printRxnFormula(modelnew,both_loop_rs_3)
printRxnFormula(modelnew,for_rs_3)
printRxnFormula(modelnew,back_rs_3)
%%
for_loop_id_3=findRxnIDs(modelnew,{'RS_3','RS_27'});
modelnew.ub(for_loop_id_3)=0;
%%
%%
[rxnInLoopfinal, Nfinal, loopInfofinal] = findMinNull(modelnew);
find(rxnInLoopfinal(:,1)==1);
backward_loop_4=modelnew.rxns(ans);
find(rxnInLoopfinal(:,2)==1);
forward_loop_4=modelnew.rxns(ans);
both_loops_4=intersect(forward_loop_4,backward_loop_4);
both_loop_rs_4=intersect(both_loops_4,model.rxns);
for_rs_4=intersect(forward_loop_4, model.rxns);
back_rs_4=intersect(backward_loop_4,model.rxns);
printRxnFormula(modelnew,both_loop_rs_4)
printRxnFormula(modelnew,for_rs_4)
printRxnFormula(modelnew,back_rs_4)
%%