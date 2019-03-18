def idf_bundler(ems_file, occupation_file, construction_file, output, seed_file = 'seed.idf'):
    
    seed = open(seed_file, 'rb')
    ems = open(ems_file, 'rb')
    occupation = open(occupation_file, 'rb')
    construction = open(construction_file, 'rb')
    
    with open(output, 'wb') as model:
        
        for line in seed:
            model.write(line)
            
        model.write('\n')
        
        for line in ems:
            model.write(line)
            
        model.write('\n')
        
        for line in occupation:
            model.write(line)
            
        model.write('\n')
        
        for line in construction:
            model.write(line)
            
        model.write('\n')

idf_bundler(ems_file='ems1.idf', occupation_file='occupation2.idf', construction_file='construction3.idf', output='modelo_teste.idf', seed_file = 'seed.idf')
