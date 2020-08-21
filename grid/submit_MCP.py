import os

user    = 'user.shiomi'
version = '2016-01-00-01'
athena  = '21.3.15'
retry   = '3'

listfile = open('/gpfs/fs7001/shiomi/ATLAS/L1TGCNtuple/l1tgcntuple/grid/MCP.list')
ESDs = listfile.readlines() 
listfile.close()

for ESD in ESDs:
    ESD = ESD.rstrip()
    command =  'pathena /gpfs/fs7001/shiomi/ATLAS/L1TGCNtuple/l1tgcntuple/grid/runL1TGCNtuple.py'
    #command += ' --athenaTag=%s' % athena
    #command += ' --split=999'
    #command += ' --nFilesPerJob=1'
    command += ' --forceStaged'
    command += ' --inDS=%s' % ESD
    
    output = ESD.replace('DESDM_MCP', 'NTUP_MCP.' + retry)
    output = output.replace('DESDM_ZMUMU', 'NTUP_ZMUMU.' + retry)
    output = output.replace('DESDM_TILEMU', 'NTUP_TILEMU.' + retry)
    output = output.replace('ESD', 'NTUP.' + retry)
    output = output.replace('/','')
    output = output.replace('_EXT0','')
    #output = output.replace('Pythia8BPhotospp_A14_CTEQ6L1_','')
    
    command += ' --outDS=%s' % (output)


    #if 'group.det-muon' in user:
        #command += ' --official --voms atlas:/atlas/det-muon/Role=production'
        #command += ' --destSE TOKYO-LCG2_DET-MUON'
        #command += ' --destSE CERN-PROD_DET-MUON'
    
    print command
    os.system(command)
