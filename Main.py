import time
import IGP_DI
import IGPM_MFGV
import IPCA

while True:

    IGPM_MFGV.Main()
    IGP_DI.Main()
    IPCA.Main()
    print('funcionou')

    #30 minutos
    #time.sleep(1800)
    #6 dias
    time.sleep(691200)




