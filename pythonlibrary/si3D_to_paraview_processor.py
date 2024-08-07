import os
from si3D_to_paraview import *

root = 'S:/si3D/02_ClearLake/00_HgTests/'
# root = '/home/savalma/si3D/'
fileSims = ['013_HgTest']
concTracer = ['SS1', 'Hg0', 'HgII', 'MeHg']
# concTracer = ['DO', 'PON', 'DON', 'NH4', 'NO3', 'POP', 'DOP', 'PO4', 'POC', 'DOC', 'ALG1']

# Code section
for i in fileSims:
    filesim = i
    pathfile = root + i
    pathsave = root + i + '/paraview'

    # To obtain simulation information
    os.chdir(pathfile)

    fid = open('si3d_inp.txt', 'r')
    lines = fid.readlines()
    year = lines[5]
    month = lines[6]
    day = lines[7]
    hour = lines[8]
    year = str(year.split()[2])
    month = str(month.split()[2])
    day = str(day.split()[2])
    hour = str(hour.split()[2])
    minute = str(hour[2:4])
    hour = str(hour[0:2])
    startDate = year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':00'

    # To obtain dx
    dx = lines[16]
    dx = str(dx)
    dx = float(dx[14:34])

    # To obtain dz
    dz = lines[18]
    dz = str(dz)
    dz = float(dz[14:34])

    # To obtain dt
    dt = lines[22]
    dt = str(dt)
    dt = float(dt[14:34])

    # To obtain idz
    idz = lines[23]
    idz = str(idz)
    idz = int(idz[14:34])
    if idz == 0:
        deltaZ = 'constant'
    elif idz == -1:
        deltaZ = 'variable'
    # To obtain iTurb
    iTurb = lines[76]
    iTurb = str(iTurb)
    iTurb = int(iTurb[14:34])
    # To obtain output settings
    itspf = lines[75]
    itspf = str(itspf)
    itspf = int(itspf[14:34])
    itspfh = lines[64]
    itspfh = str(itspfh)
    itspfh = int(itspfh[14:34])
    itspftr = lines[105]
    itspftr = str(itspftr)
    itspftr = int(itspftr[14:34])

    nTracer = lines[102]
    nTracer = str(nTracer)
    nTracer = int(nTracer[14:34])

    if (itspf != itspfh) or (itspf != itspftr) or (itspfh != itspftr):
        raise ValueError('Error the variables itspf and itspfh must be the same. If tracers are modeled, itspftr, itspf, and itspfh must be the same')
    if nTracer > 0:
        if nTracer != len(concTracer):
            raise ValueError('Number of tracers modeled different from number of units provided as input')

    if os.path.isfile('si3d_3D'):
        n_frames = si3D_to_paraview(pathfile, pathsave, startDate, deltaZ, dx, dz, dt, iTurb, itspf, nTracer, concTracer)
    else:
        raise ValueError('3D File not Found')
