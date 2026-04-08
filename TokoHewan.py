import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 1. Variabel

terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'Barang Terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'Permintaan')
harga = ctrl.Antecedent(np.arange(0, 100001, 1), 'Harga per Item')
profit = ctrl.Antecedent(np.arange(0, 4000001, 1), 'Profit')
stok = ctrl.Consequent(np.arange(0, 1001, 1), 'Stok Makanan')

# 2. Membership Function

terjual['rendah'] = fuzz.trimf(terjual.universe, [0, 0, 40])
terjual['sedang'] = fuzz.trimf(terjual.universe, [30, 50, 70])
terjual['tinggi'] = fuzz.trimf(terjual.universe, [60, 100, 100])

permintaan['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])

harga['murah'] = fuzz.trimf(harga.universe, [0, 0, 40000])
harga['sedang'] = fuzz.trimf(harga.universe, [30000, 50000, 80000])
harga['mahal'] = fuzz.trimf(harga.universe, [60000, 100000, 100000])

profit['rendah'] = fuzz.trimf(profit.universe, [0, 0, 1500000])
profit['sedang'] = fuzz.trimf(profit.universe, [1000000, 2000000, 2500000])
profit['tinggi'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000])

stok['sedang'] = fuzz.trimf(stok.universe, [100, 500, 900])
stok['banyak'] = fuzz.trimf(stok.universe, [600, 1000, 1000])

# 3. Visualisasi (FIX)

def tampilkan(var, judul):
# .view() otomatis membuat figure baru, tidak perlu ditimpa subplots() yang kosong
    var.view()
    plt.title(judul)

tampilkan(terjual, "Barang Terjual")
tampilkan(permintaan, "Permintaan")
tampilkan(harga, "Harga per Item")
tampilkan(profit, "Profit")
tampilkan(stok, "Stok Makanan")

# 4. Rules

rule1 = ctrl.Rule(terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
rule2 = ctrl.Rule(terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule3 = ctrl.Rule(terjual['tinggi'] & permintaan['sedang'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule4 = ctrl.Rule(terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule5 = ctrl.Rule(terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
rule6 = ctrl.Rule(terjual['rendah'] & permintaan['rendah'] & harga['sedang'] & profit['sedang'], stok['sedang'])

# 5. Sistem

stok_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
simulasi = ctrl.ControlSystemSimulation(stok_ctrl)

# 6. Input

simulasi.input['Barang Terjual'] = 80
simulasi.input['Permintaan'] = 255
simulasi.input['Harga per Item'] = 25000
simulasi.input['Profit'] = 3500000

# 7. Proses

simulasi.compute()

# 8. Output

hasil = simulasi.output['Stok Makanan']
print("Jumlah stok optimal:", hasil)

plt.show()