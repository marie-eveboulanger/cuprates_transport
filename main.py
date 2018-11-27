import time

from band import BandStructure
from admr import ADMR
from chambers import Conductivity
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

bandObject = BandStructure(mu = -0.825)
# bandObject.figMultipleFS2D()


start_total_time = time.time()
ADMRObject = ADMR(bandObject, Bamp=45, gamma_0=15, gamma_k=65, power=12, a0=0)
ADMRObject.runADMR()
print("ADMR time : %.6s seconds" % (time.time() - start_total_time))

ADMRObject.fileADMR()
ADMRObject.figADMR()



# mu_a = np.arange(0.81, 0.835, 0.001)
# for mu in mu_a:
#     mu = mu * t
#     print("mu = " + r"{0:.4f}".format(mu) + " * t" )
#     band_parameters = np.array([a, b, c, mu, t, tp, tpp, tz, tz2], dtype = np.float64)
#     admrFunc(band_parameters, mesh_parameters, tau_parameters, B_amp, B_phi_a, B_theta_a, fig_show = False)

# gamma_k_a = np.arange(0, 120, 20)
# gamma_0_a = np.arange(50, 170, 20)
# for gamma_0 in gamma_0_a:
#     for gamma_k in gamma_k_a:
#         print("gamma_0 = " + r"{0:.1f}".format(gamma_0) + " THz")
#         print("gamma_k = " + r"{0:.1f}".format(gamma_k) + " THz")
#         tau_parameters = np.array([gamma_0, gamma_k, power], dtype = np.float64)
#         admrFunc(band_parameters, mesh_parameters, tau_parameters, B_amp, B_phi_a, B_theta_a, fig_show = False)









