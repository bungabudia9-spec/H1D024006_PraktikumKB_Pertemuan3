import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# VARIABEL
kejelasan_informasi = ctrl.Antecedent(np.arange(0,101,1),'Kejelasan Informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0,101,1),'Kejelasan Persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0,101,1),'Kemampuan Petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0,101,1),'Ketersediaan Sarpras')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0,101,1),'Kepuasan Pelayanan')

# MEMBERSHIP FUNCTION
for variabel in [kejelasan_informasi, kejelasan_persyaratan, kemampuan_petugas, ketersediaan_sarpras]:

    variabel['Tidak Memuaskan'] = fuzz.trapmf(variabel.universe,[0,0,30,50])

    variabel['Cukup Memuaskan'] = fuzz.trapmf(variabel.universe,[30,45,65,80])

    variabel['Memuaskan'] = fuzz.trapmf(variabel.universe,[70,85,100,100])

#output variabel
kepuasan_pelayanan['Tidak Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe,[0,0,10,25])

kepuasan_pelayanan['Kurang Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe,[15,25,35,45])

kepuasan_pelayanan['Cukup Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe,[35,45,60,70])

kepuasan_pelayanan['Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe,[60,70,80,90])

kepuasan_pelayanan['Sangat Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe,[80,90,100,100])

# RULES 1 - 81 (EXCEL)
rule1 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
rule2 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule3 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

rule4 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule5 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule6 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

rule7 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule8 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule9 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule10 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule11 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule12 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

rule13 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule14 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule15 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule16 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule17 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule18 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule19 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule20 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule21 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule22 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule23 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule24 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule25 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule26 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule27 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule28 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule29 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule30 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

rule31 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])

rule32 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule33 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule34 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule35 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule36 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule37 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule38 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule39 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule40 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule41 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule42 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule43 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule44 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule45 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule46 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule47 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule48 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule49 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule50 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule51 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule52 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule53 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
rule54 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule55 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule56 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule57 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule58 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule59 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule60 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule61 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule62 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule63 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule64 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
rule65 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule66 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule67 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule68 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule69 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule70 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule71 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
rule72 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule73 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule74 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule75 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule76 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule77 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
rule78 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

rule79 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
rule80 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
rule81 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

# SISTEM FUZZY
sistem_kepuasan = ctrl.ControlSystem([
rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,
rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,
rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,
rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,
rule37,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,
rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,rule54,
rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63,
rule64,rule65,rule66,rule67,rule68,rule69,rule70,rule71,rule72,
rule73,rule74,rule75,rule76,rule77,rule78,rule79,rule80,rule81,

])

simulasi = ctrl.ControlSystemSimulation(sistem_kepuasan)

#input
simulasi.input['Kejelasan Informasi'] = 80
simulasi.input['Kejelasan Persyaratan'] = 75
simulasi.input['Kemampuan Petugas'] = 85
simulasi.input['Ketersediaan Sarpras'] = 90

#proses (compute)
simulasi.compute()

#output & visualisasi akhir
hasil = simulasi.output['Kepuasan Pelayanan']

print("Nilai Kepuasan Pelayanan:", hasil)

kepuasan_pelayanan.view(sim=simulasi)
plt.show()