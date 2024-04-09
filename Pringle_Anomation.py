import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from CONSTS import Dead, t_end, M, tau




A = np.loadtxt(f"A_{t_end}_{M}_{Dead}.txt")
D = np.loadtxt(f"D_{t_end}_{M}_{Dead}.txt")
X = np.loadtxt(f"X_{t_end}_{M}_{Dead}.txt")
DATA = np.loadtxt(f"DATA_{t_end}_{M}_{Dead}.txt")
B_z3 = np.loadtxt(f'B_z3_{t_end}_{M}_{Dead}.txt')
B_z2 = np.loadtxt(f'B_z2_{t_end}_{M}_{Dead}.txt')
B_z1 = np.loadtxt(f'B_z1_{t_end}_{M}_{Dead}.txt')
# V_r = np.loadtxt(f'V_r_{t_end}_{M}_{Dead}.txt')
New_V_r = np.loadtxt(f'New_V_r_{t_end}_{M}_{Dead}.txt')
M_dot = np.loadtxt(f'M_dot_{t_end}_{M}_{Dead}.txt')
B_z = B_z3

T = np.array([tau*i for i in range(M)])

# Время в миллионах лет
TAU = 1.39

D_0 = 1.8*10**(15)
V_0 = 1.2*100
M_0 = 1.8*10**(17)


# Function to update the plot for each frame
def update(frame):
    # Clear the previous frame
    ax_1.cla()
    ax_2.cla()
    # ax_3.cla()
    ax_4.cla()
    # ax_5.cla()
    # ax_6.cla()
    ax_7.cla()
    
    R_in = -2
    R_out = 3
    N = 101
    x_s = np.logspace(R_in, R_out, N+1)
    # x = np.logspace(R_in, R_out, N)
    x = np.array([(x_s[i+1]+x_s[i])/2 for i in range(N)])
    
    # Plot the data    
    
    ax_1.plot(x[1:], DATA[frame][1:], '--', color='r', label = f't={T[frame]:.2f}\nT={T[frame]*TAU:.2f} Myr')
    

    ax_1.set_ylim(10**(-5), 10**(6))
    ax_1.set_xlim(0.01, 1000)
    
    ax_1.set_xlabel('а.е.')
    ax_1.set_ylabel(r'$\Sigma,~{г}/{см}^2$ ')
    
    ax_1.set_yscale('log')
    ax_1.set_xscale('log')
    
    ax_1.set_title(fr'$\Sigma$ для различных $t$ с мертвой зоны')
    ax_1.legend(loc='best')

    ax_2.plot(x[1:], X[frame][1:], '--', color='r', label = f't={T[frame]:.2f}\nT={T[frame]*TAU:.2f} Myr')
    

   
    ax_2.set_ylim(10**(-19), 10**(0))
    ax_2.set_xlim(0.01, 1000)
    
    ax_2.axhline(y=10**(-12), color='k', linestyle='-')
    
    ax_2.set_xlabel('а.е.')
    ax_2.set_ylabel(r'x')
    
    ax_2.set_yscale('log')
    ax_2.set_xscale('log')
    
    ax_2.set_title(fr'Степень ионизации x')
    ax_2.legend(loc='best')


    # ax_3.plot(x[1:], D_0*D[frame][1:], '--', color='r', label = f't={T[frame]:.2f}\nT={T[frame]*TAU:.2f} Myr')
    # ax_3.set_ylim(10**(9), 10**(17))
    # ax_3.set_xlim(0.01, 1000)
    
    
    # ax_3.set_xlabel('а.е.')
    # ax_3.set_ylabel(r'$\nu,~{см}^2/{с}$')
    
    # ax_3.set_yscale('log')
    # ax_3.set_xscale('log')
    
    # ax_3.set_title(fr'Турбулентная вязкость $\nu$')
    # ax_3.legend(loc='best')


    ax_4.plot(x[1:], A[frame][1:], '--', color='r', label = f't={T[frame]:.2f}\nT={T[frame]*TAU:.2f} Myr')
    ax_4.set_ylim(0.5*10**(-4), 10**(-1))
    ax_4.set_xlim(0.01, 1000)


    ax_4.set_xlabel('а.е.')
    ax_4.set_ylabel(r'$\alpha$')

    ax_4.set_yscale('log')
    ax_4.set_xscale('log')

    ax_4.set_title(fr'Коэффициент $\alpha$')
    ax_4.legend(loc='best')
    
    
    # ax_5.plot(x[1:], 1*New_V_r[frame][1:], '--', color='r', label = f't={T[frame]:.2f}\nT={T[frame]*TAU:.2f} Myr')
    # ax_5.set_ylim(-6, 0.1)
    # ax_5.set_xlim(0.01, 1000)


    # ax_5.set_xlabel('а.е.')
    # ax_5.set_ylabel(r'$v_r,~{см}/{с}$')

    # # ax_5.set_yscale('log')
    # ax_5.set_xscale('log')

    # ax_5.set_title(fr'Радиальная скорость $v_r$')
    # ax_5.legend(loc='best')
    
    
    
    # ax_6.plot(x[1:], M_0*M_dot[frame][1:], '--', color='r', label = f't={T[frame]:.2f}\nT={T[frame]*TAU:.2f} Myr')
    # ax_6.set_yscale('log')

    # ax_6.set_ylim(10**(14), 10**(19))
    # ax_6.set_xlim(0.01, 1000)


    # ax_6.set_xlabel('а.е.')
    # ax_6.set_ylabel(r'$\dot{M},~{г}/{с}$')

    # # ax_6.set_yscale('log')
    # ax_6.set_xscale('log')

    # ax_6.set_title(r'Темп аккреции $\dot{M}$')
    # ax_6.legend(loc='best')
    
    ax_7.plot(x[1:], B_z[frame][1:], '-', color='r', label = f'min t={T[frame]*TAU:.2f} Myr')
    ax_7.plot(x[1:], B_z1[frame][1:], '--', color='y', label = f'Вмор t={T[frame]*TAU:.2f} Myr')
    ax_7.plot(x[1:], B_z2[frame][1:], '--', color='k', label = f'Дифф t={T[frame]*TAU:.2f} Myr')

    ax_7.set_ylim(10**(-6), 10**(5))
    ax_7.set_xlim(0.01, 1000)
  
    ax_7.axhline(y=10**(-12), color='k', linestyle='-')
   
    ax_7.set_xlabel('а.е.')
    ax_7.set_ylabel(r'$B_z$')
     
    ax_7.set_yscale('log')
    ax_7.set_xscale('log')
     
    ax_7.set_title(fr'Магнитное поле $B_z$')
    ax_7.legend(loc='upper right')
# Create a figure and axis
fig = plt.figure(figsize=(10, 10))
fig.subplots_adjust(hspace=0.6, wspace=0.4)

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
# ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 3)
# ax_5 = fig.add_subplot(2, 2, 3)
# ax_6 = fig.add_subplot(2, 2, 4)
ax_7 = fig.add_subplot(2, 2, 4)

# Create the animation
animation = FuncAnimation(fig, update, frames=range(0, M, 2), interval=200)

# Show the animated plot
# plt.show()

# animation.save(filename=f"Global_evolution_{Dead}_{t_end}.gif", writer="pillow")
animation.save(filename=f"10_Global_evolution_{Dead}_{t_end}.gif", writer="pillow")



