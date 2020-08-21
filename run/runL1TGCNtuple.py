
# number of events to be processed, -1 for all
events = -1 
#events = 100

# inputs path/name, ['file1', 'file2',..] 
inputs = ['/home/shiomi/ATLAS/L1residualforRun-3/residualforRun-2/L1TGCNtupleforRun3/data/user.shiomi/user.shiomi.20925697.EXT0._000010.ESD.pool.root']


#output path/name
output = 'L1TGCNtuple.pool.root'

#-------------------------------------------------------------
# misc.
#-------------------------------------------------------------

from AthenaCommon.AthenaCommonFlags import jobproperties as jp
jp.AthenaCommonFlags.EvtMax = tkEvtMax if 'tkEvtMax' in locals() else events

#import glob
#directory = "/home/tomoe/maxi183/SingleMuon/20.1.3.3/ESD/"
#inputs = glob.glob(directory + "*")
jp.AthenaCommonFlags.FilesInput = tkInput if 'tkInput' in locals() else inputs

from AthenaCommon.AppMgr import ServiceMgr
from GaudiSvc.GaudiSvcConf import THistSvc
ServiceMgr += THistSvc()
OutputName = tkOutput if 'tkOutput' in locals() else output
ServiceMgr.THistSvc.Output = ["L1TGCNtuple DATAFILE='%s' OPT='RECREATE'" % OutputName]


from RecExConfig.RecFlags import rec
rec.OutputLevel = INFO

from AnalysisExamples.AnalysisFlags import AnalysisFlags

if AnalysisFlags.DoNavigation:
  include("RecExCommon/AllDet_detDescr.py")
  ServiceMgr.EventSelector.BackNavigation = True

#rec.doTrigger.set_Value_and_Lock(False)
from TriggerJobOpts.TriggerFlags import TriggerFlags
TriggerFlags.doTriggerConfigOnly.set_Value_and_Lock(True)

rec.doAOD.set_Value_and_Lock(False)
rec.doCBNT.set_Value_and_Lock(False)
rec.doWriteESD.set_Value_and_Lock(False)
rec.doWriteAOD.set_Value_and_Lock(False)
rec.doWriteTAG.set_Value_and_Lock(False)
rec.doHist.set_Value_and_Lock(False)

#rec.doPerfMon = False
rec.doPerfMon.set_Value_and_Lock(False)
rec.doDetailedPerfMon.set_Value_and_Lock(False)
rec.doSemiDetailedPerfMon.set_Value_and_Lock(False)
from PerfMonComps.PerfMonFlags import jobproperties
jobproperties.PerfMonFlags.doMonitoring.set_Value_and_Lock(False)

#from InDetRecExample.InDetJobProperties import InDetFlags # for x311 
#InDetFlags.useDCS.set_Value_and_Lock(False)

#-------------------------------------------------------------
# user algorithm
#-------------------------------------------------------------
rec.UserAlgs = ["L1TGCNtuple/L1TGCNtuple_options.py"]

include("RecExCommon/RecExCommon_topOptions.py")
