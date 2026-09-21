filePath = '/Users/subasrees/Downloads/Frontiers/Frontier_ccle/Pediatric_tasks/Tasks_results.xlsx';
sheetList = sheetnames(filePath);
nModels = length(sheetList);

modelReactions = cell(nModels,1);
modelFluxes = cell(nModels,1);

for i = 1:nModels
    T = readtable(filePath, 'Sheet', sheetList{i});

    modelReactions{i} = string(T{:,1});
    modelFluxes{i} = T{:,2};
end

for i = 1:nModels
    
    T = readtable(filePath, 'Sheet', sheetList{i});
    
    modelReactions{i} = string(T{:,1});   % reaction names
    modelFluxes{i}   = T{:,2};            % flux values
    
end
allReactions = unique(vertcat(modelReactions{:}));
nReactions = length(allReactions);

presenceCount = zeros(nReactions,1);

for j = 1:nModels
    
    rxns = modelReactions{j};
    flux = modelFluxes{j};
    
    valid = ~isnan(flux);
    
    [tf, loc] = ismember(rxns, allReactions);
    
    presenceCount(loc(tf)) = presenceCount(loc(tf)) + valid(tf);
end

reactionFrequency = presenceCount / nModels;
sum(reactionFrequency >= 0.8)
display(ans)
fractionCore = ans /460 %(total human task count - 460)
display(ans)