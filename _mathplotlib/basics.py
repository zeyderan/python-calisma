import matplotlib.pyplot as plt
import numpy as np
# x = [1,2,3,4]
# y = [1,4,9,16]

# plt.plot(x,y,'o--r')
# plt.axis([0,6,0,20])
# plt.title('grafik başlığı')
# plt.xlabel('x exseni')
# plt.ylabel('y ekseni')
# plt.show()

# x = [1,2,3,4]
# y = [1,4,9,16]
# plt.plot(x,y,'o--g') # docs üzerinden özelleştirme seçeneklerine bakılabilir
# # o - marker
# # -- çizgi tipi
# # g - green 

# plt.axis([0,6,0,20])

x = np.linspace(0,2,100)

# plt.plot(x,x,'r',label='doğrusa')
# plt.plot(x,x**2,'b',label='kares')
# plt.plot(x,x**3,'--',label='kübü')
# plt.plot(x,x**4,'.',label='4.kuvvaeti')
# plt.legend()
# plt.show()

fig, axs = plt.subplots(2)

axs[0] = plt.plot(x,x,"r")
axs[1] = plt.plot(x,x**2,"b")

plt.show()
