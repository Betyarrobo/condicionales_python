battery_level = 10
battery_low = False
low_power_mode = False
wifi_disconnect = False
lock_screen = False
if battery_level < 15:
    battery_low = True
if (wifi_disconnect == True) and (lock_screen == False):
    print("El dispositivo se ha desconectado de la red")
if ((battery_low == True) or (low_power_mode == True)) and (lock_screen == False):

    print("El sistema disminuirá el brillo de la pantalla para ahorrar energia")