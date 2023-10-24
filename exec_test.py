import flopy
m = flopy.modflow.Modflow(modelname='model', exe_name='mf2005_test.exe')
m.dis()
m.bas()
m.lpf()
m.oc()
m.pcg()
m.write_inputs()
m.solve()
