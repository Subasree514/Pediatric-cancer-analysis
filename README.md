## 1. Addition of RS and basal essential media to pediatric cancer GEMs
 https://github.com/Subasree514/Pediatric-cancer-analysis/tree/main/GEM-modification-RS-integration

01_grrules_create.m\
02_mem_constraint.m\
03_mem_sink.m\
04_rs_merge.m\
05_loop_check.m

### Additional files:
-loopcheck.m - to check the presence of thermodynamically infeasible cycles\
-memhuman.m - details about uptake rates of nutrients from basal essential media\
-RS_demands.py - to add compartmental and total demand reactions to the reactive species\

### Basic human tasks performed by GEMs:
10a_Cobra_humantasks.m\
10b_humantask_statistic.m

## 2.  Generation of parsimonious flux data and generation of machine learning features from flux data
https://github.com/Subasree514/Pediatric-cancer-analysis/tree/main/Flux-analysis\
06_pfba.ipynb\
07_feature_generation.ipynb

### Systems-level analysis of SHAP important metabolic pathways 
09_systems_analysis.ipynb\

## 3. Machine learning and feature interpretation using SHAP 
08_ML_analysis.ipynb
