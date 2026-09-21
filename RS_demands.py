# Code to add compartmental and overall demad reactions to the RS model
## import libraries
import cobra
from cobra import Reaction, Metabolite
from cobra.io import save_matlab_model, read_sbml_model, write_sbml_model, load_matlab_model
## import RS model
rs_model = load_matlab_model('/Users/subasrees/Desktop/Reactive-species-reactions-module-RSRM-/RSmodel_Recon3D1_2024_withGPRs_updated.mat')

# Details of the model
print(len(rs_model.groups))
print(len(rs_model.reactions))
print(len(rs_model.metabolites))

## Initialize demand metabolites for all important RS in the model
rs_model.add_metabolites([
    Metabolite(
    'h2s[total]',
    name='Hydrogen Sulfide',
    compartment='total',
    formula='H2S',
    charge=0
    ),
    Metabolite(
    'HC00250[total]',
    name='Hydrogen Sulfide',
    compartment='total',
    formula='HS',
    charge=-1
    ),
    Metabolite(
    'no[total]',
    name='Nitric oxide',
    compartment='total',
    formula='NO',
    charge=0
    ),
    Metabolite(
    'h2o2[total]',
    name='Hydrogen peroxide',
    compartment='total',
    formula='H2O2',
    charge=0
    ),
    Metabolite(
    'oh_rad[total]',
    name='Hydroxyl radical',
    compartment='total',
    formula='OH',
    charge=0
    ),
    Metabolite(
    'o2s[total]',
    name='Super oxide anion',
    compartment='total',
    formula='O2',
    charge=-1
    ),
    Metabolite(
    'CE5643[total]',
    name='Peroxynitrite',
    compartment='total',
    formula='NO3',
    charge=-1
    ),
    Metabolite(
    'CE4633[total]',
    name='Hypochlorous acid',
    compartment='total',
    formula='ClHO',
    charge=0
    ),
    Metabolite(
    'no2_rad[total]',
    name='Nitrite radical',
    compartment='total',
    formula='NO2',
    charge=0
    ),
    Metabolite(
    'ho2_rad[total]',
    name='Hydroperoxy radical',
    compartment='total',
    formula='HO2',
    charge=0
    ),
])
rs_model.add_metabolites([
    Metabolite(
    'no[e]',
    name='Nitric oxide',
    compartment='e',
    formula='NO',
    charge=0
    ),
    Metabolite(
    'h2o2[n]',
    name='Hydrogen peroxide',
    compartment='n',
    formula='H2O2',
    charge=0
    ),  
    Metabolite(
    'h2o2[m]',
    name='Hydrogen peroxide',
    compartment='m',
    formula='H2O2',
    charge=0
    ), 
    Metabolite(
    'h2o2[x]',
    name='Hydrogen peroxide',
    compartment='x',
    formula='H2O2',
    charge=0
    ),
    Metabolite(
    'h2o2[r]',
    name='Hydrogen peroxide',
    compartment='r',
    formula='H2O2',
    charge=0
    ),
    Metabolite(
    'h2o2[l]',
    name='Hydrogen peroxide',
    compartment='l',
    formula='H2O2',
    charge=0
    ),
    Metabolite(
    'o2s[m]',
    name='Superoxide anion',
    compartment='m',
    formula='O2',
    charge=-1
    ),
    Metabolite(
    'o2s[e]',
    name='Superoxide anion',
    compartment='e',
    formula='O2',
    charge=-1
    )
])
## 1. NO demand
rs_model.add_boundary(rs_model.metabolites.get_by_id("no[total]"), type="demand")
## 2. H2S demand
rs_model.add_boundary(rs_model.metabolites.get_by_id("h2s[total]"), type="demand")
## 3. SUPER OXIDE DEMAND
rs_model.add_boundary(rs_model.metabolites.get_by_id("o2s[total]"), type="demand")
## 4. HS ion
rs_model.add_boundary(rs_model.metabolites.get_by_id("HC00250[total]"), type="demand")
## 5. PEROXYNITRITE
rs_model.add_boundary(rs_model.metabolites.get_by_id("CE5643[total]"), type="demand")
## 6. Hydroxyl radical demand
rs_model.add_boundary(rs_model.metabolites.get_by_id("oh_rad[total]"), type="demand")
## 7. H2O2 demand
rs_model.add_boundary(rs_model.metabolites.get_by_id("h2o2[total]"), type="demand")
## 8. no2_rad demand
rs_model.add_boundary(rs_model.metabolites.get_by_id("no2_rad[total]"), type="demand")
## 9 Hypochlorous acid 
rs_model.add_boundary(rs_model.metabolites.get_by_id("CE4633[total]"), type="demand")
## 10 hydroperoxyl radical
rs_model.add_boundary(rs_model.metabolites.get_by_id("ho2_rad[total]"), type="demand")

## Add individual demand reactions for the RS in organelles
## H2S
reaction = Reaction('H2S_c_demand')
reaction.name = 'Hydrogen sulfide cytosolic demand'
reaction.group = 'RSS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2s[c]'): -1.0,rs_model.metabolites.get_by_id('h2s[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('H2S_e_demand')
reaction.name = 'Hydrogen sulfide extracellular demand'
reaction.subsystem = 'RSS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2s[e]'): -1.0,rs_model.metabolites.get_by_id('h2s[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('H2S_l_demand')
reaction.name = 'Hydrogen sulfide lysosome demand'
reaction.subsystem = 'RSS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2s[l]'): -1.0,rs_model.metabolites.get_by_id('h2s[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('H2S_m_demand')
reaction.name = 'Hydrogen sulfide mitochondrial demand'
reaction.subsystem = 'RSS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2s[m]'): -1.0,rs_model.metabolites.get_by_id('h2s[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 

## NO
reaction = Reaction('NITRIC-OXIDE_c_demand')
reaction.name = 'Nitric oxide cytosolic demand'
reaction.subsystem = 'RNS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('no[c]'): -1.0,rs_model.metabolites.get_by_id('no[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('NITRIC-OXIDE_e_demand')
reaction.name = 'Nitric oxide extracellular demand'
reaction.subsystem = 'RNS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('no[e]'): -1.0,rs_model.metabolites.get_by_id('no[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('NITRIC-OXIDE_n_demand')
reaction.name = 'Nitric oxide nucleus demand'
reaction.subsystem = 'RNS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('no[n]'): -1.0,rs_model.metabolites.get_by_id('no[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 

## NO2_rad
reaction = Reaction('no2_rad_g_demand')
reaction.name = 'Nitrogen dioxide radical golgi demand'
reaction.subsystem = 'RNS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('no2_rad[g]'): -1.0,rs_model.metabolites.get_by_id('no2_rad[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('no2_rad_c_demand')
reaction.name = 'Nitrogen dioxide radical cytosolic demand'
reaction.subsystem = 'RNS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('no2_rad[c]'): -1.0,rs_model.metabolites.get_by_id('no2_rad[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])

## H2O2
reaction = Reaction('H2O2_c_demand')
reaction.name = 'HYDROGEN PEROXIDE cytosol demand'
reaction.groups = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2o2[c]'): -1.0,rs_model.metabolites.get_by_id('h2o2[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('H2O2_n_demand')
reaction.name = 'HYDROGEN PEROXIDE nucleus demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2o2[n]'): -1.0,rs_model.metabolites.get_by_id('h2o2[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('H2O2_m_demand')
reaction.name = 'HYDROGEN PEROXIDE mitochondrial demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2o2[m]'): -1.0,rs_model.metabolites.get_by_id('h2o2[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('H2O2_x_demand')
reaction.name = 'HYDROGEN PEROXIDE peroxisomal demand'
reaction.groups = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2o2[x]'): -1.0,rs_model.metabolites.get_by_id('h2o2[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('H2O2_e_demand')
reaction.name = 'HYDROGEN PEROXIDE extracellular demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id ('h2o2[e]'): -1.0,rs_model.metabolites.get_by_id('h2o2[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('H2O2_r_demand')
reaction.name = 'HYDROGEN PEROXIDE endoplasmic reticuluar transport'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id ('h2o2[r]'): -1.0,rs_model.metabolites.get_by_id('h2o2[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('H2O2_l_demand')
reaction.name = 'HYDROGEN PEROXIDE lysosome demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('h2o2[l]'): -1.0,rs_model.metabolites.get_by_id('h2o2[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])

## Hydroxyl radical
reaction = Reaction('oh_rad_c_demand')
reaction.name = 'HYDROXYL radical cytosolic demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('oh_rad[c]'): -1.0,rs_model.metabolites.get_by_id('oh_rad[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('oh_rad_e_demand')
reaction.name = 'HYDROXYL radical extracellular demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('oh_rad[e]'): -1.0,rs_model.metabolites.get_by_id('oh_rad[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('oh_rad_n_demand')
reaction.name = 'HYDROXYL radical nucleus demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('oh_rad[n]'): -1.0,rs_model.metabolites.get_by_id('oh_rad[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('oh_rad_x_demand')
reaction.name = 'HYDROXYL radical peroxisomal demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('oh_rad[x]'): -1.0,rs_model.metabolites.get_by_id('oh_rad[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])

## SUPER OXIDE 
reaction = Reaction('Super_oxide_c_demand')
reaction.name = 'Superoxide cytosol demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('o2s[c]'): -1.0,rs_model.metabolites.get_by_id('o2s[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('Super_oxide_n_demand')
reaction.name = 'Super oxide nucleus demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('o2s[n]'): -1.0,rs_model.metabolites.get_by_id('o2s[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('Super_oxide_m_demand')
reaction.name = 'Superoxide mitochondrial demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('o2s[m]'): -1.0,rs_model.metabolites.get_by_id('o2s[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('Super_oxide_x_demand')
reaction.name = 'Super oxide peroxisome demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('o2s[x]'): -1.0,rs_model.metabolites.get_by_id('o2s[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('Super_oxide_e_demand')
reaction.name = 'Super oxide extracellular demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('o2s[e]'): -1.0,rs_model.metabolites.get_by_id('o2s[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])

## Hydrogen sulfide ion
reaction = Reaction('HS_m_demand')
reaction.name = 'Hydrosulfide ion mitochondrial demand'
reaction.subsystem = 'RSS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('HC00250[m]'): -1.0,rs_model.metabolites.get_by_id('HC00250[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('HS_c_demand')
reaction.name = 'Hydrogen sulfide cytosolic demand'
reaction.group = 'RSS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('HC00250[c]'): -1.0,rs_model.metabolites.get_by_id('HC00250[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('HS_e_demand')
reaction.name = 'Hydrogen sulfide extracellular demand'
reaction.subsystem = 'RSS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('HC00250[e]'): -1.0,rs_model.metabolites.get_by_id('HC00250[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 
##
reaction = Reaction('HS_l_demand')
reaction.name = 'Hydrogen sulfide lysosome demand'
reaction.subsystem = 'RSS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('HC00250[l]'): -1.0,rs_model.metabolites.get_by_id('HC00250[total]'): 1.0})
rs_model.add_reactions([reaction])
print(reaction.reaction) 

## Peroxynitrite 
reaction = Reaction('Peroxynitrite_c_demand')
reaction.name = 'Peroxynitrite cytosolic demand'
reaction.subsystem = 'RNS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('CE5643[c]'): -1.0,rs_model.metabolites.get_by_id('CE5643[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('Peroxynitrite_e_demand')
reaction.name = 'Peroxynitrite extracellular demand'
reaction.subsystem = 'RNS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('CE5643[e]'): -1.0,rs_model.metabolites.get_by_id('CE5643[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('Peroxynitrite_n_demand')
reaction.name = 'Peroxynitrite nuclear demand'
reaction.subsystem = 'RNS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('CE5643[n]'): -1.0,rs_model.metabolites.get_by_id('CE5643[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])

## Hydroperoxyl radical
reaction = Reaction('ho2_rad_c_demand')
reaction.name = 'Peroxide radical cytosolic demand'
reaction.subsystem = 'ROS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('ho2_rad[c]'): -1.0,rs_model.metabolites.get_by_id('ho2_rad[total]'): 1.0})
rs_model.add_reactions([reaction])

## Hypochlorous acid 
reaction = Reaction('Hypochlorous_c_demand')
reaction.name = 'Hypochlorous acid cytosolic demand'
reaction.subsystem = 'RCS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('CE4633[c]'): -1.0,rs_model.metabolites.get_by_id('CE4633[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
##
reaction = Reaction('Hypochlorous_e_demand')
reaction.name = 'Hypochlorous acid extracellular demand'
reaction.subsystem = 'RCS demand'
reaction.lower_bound =0.  # This is the default
reaction.upper_bound = 1000.  # This is the default
reaction.add_metabolites({rs_model.metabolites.get_by_id('CE4633[e]'): -1.0,rs_model.metabolites.get_by_id('CE4633[total]'): 1.0})
print(reaction.reaction) 
rs_model.add_reactions([reaction])
#save_matlab_model(rs_model, "/Users/subasrees/Downloads/Frontiers/Frontier_ccle/RSmodel_DM.mat")

## check mass and charge balances of all reactions
for i in rs_model.reactions:
    balance_check = rs_model.reactions.get_by_id(i.id).check_mass_balance()
    for j in balance_check:
        if True:
            print(i,j)
# Details of the model
print(len(rs_model.groups))
print(len(rs_model.reactions))
print(len(rs_model.metabolites))
