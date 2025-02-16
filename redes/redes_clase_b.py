# -*- coding: utf-8 -*-
"""redes Clase B.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ydP-boZdZJitdbet_zx0OIj5E868O9Gs
"""

host = int(input(" ingrece la cantidad de host : "))
ip = str(input(" ingrece la direccion ip : "))
red=0
a = 0
b = 0
mask=0
contador = 0

# MASCARA 23
if host > 256 and host <= 512:
    host = 2
    mask = (2 ** 7) + (2 ** 6) + (2 ** 5) + (2 ** 4) + (2 ** 3) + (2 ** 2) + (2 ** 1)
    print(f"255.255.{mask}.0 /23")
    print(f"1.1.1.1.1.1.1.0")
    red = 2**7
    print("Cantidad de redes = ",red)
    print(f"cantidad de host {2}")
    while contador <= mask:
        print(f"{ip}.{a}.{b}     {ip}.{a}.{b + 1}      {ip}.{a + 1}.254    {ip}.{a + 1}.255")
        a = a + host
        contador = contador+2


# MASCARA 22
if host > 513 and host <= 1024:
    host = 4
    mask = (2 ** 7) + (2 ** 6) + (2 ** 5) + (2 ** 4) + (2 ** 3) + (2 ** 2)
    print(f"255.255.{mask}.0 /22")
    print(f"1.1.1.1.1.1.0.0")
    red = 2**6
    print("Cantidad de redes = ",red)
    print(f"cantidad de host {4}")
    while contador <= mask:
        print(f"{ip}.{a}.{b}     {ip}.{a}.{b + 1}      {ip}.{a + 3}.254    {ip}.{a + 3}.255")
        a = a + host
        contador = contador+4

# MASCARA 21
if host >= 1025 and host <= 2048:
    mask = (2 ** 7) + (2 ** 6) + (2 ** 5) + (2 ** 4) + (2 ** 3)
    host = 8
    print(f"255.255.{mask}.0 /21")
    print(f"1.1.1.1.1.0.0.0")
    red = 2 ** 5
    print("Cantidad de redes = ", red)
    print(f"cantidad de host {8}")
    while contador <= mask:
        print(f"{ip}.{a}.{b}     {ip}.{a}.{b + 1}      {ip}.{a + 7}.254    {ip}.{a + 7}.255")
        a = a + host
        contador = contador+8


# MASCARA 20
if host >= 2049 and host <= 4096:
    mask = (2 ** 7) + (2 ** 6) + (2 ** 5) + (2 ** 4)
    host = 16
    print(f"255.255.{mask}.0 /20")
    print(f"1.1.1.1.0.0.0.0")
    red = 2 ** 4
    print("Cantidad de redes = ", red)
    print(f"cantidad de host {16}")
    while contador <= mask:
        print(f"{ip}.{a}.{b}     {ip}.{a}.{b + 1}      {ip}.{a + 15}.254    {ip}.{a + 15}.255")
        a = a + host
        contador = contador+16


# MASCARA 19
if host >= 4097 and host <= 8192:
    mask = (2 ** 7) + (2 ** 6) + (2 ** 5)
    host = 32
    print(f"255.255.{mask}.0 /19")
    print(f"1.1.1.0.0.0.0.0")
    red = 2 ** 3
    print("Cantidad de redes = ", red)
    print(f"cantidad de host {32}")
    while contador <= mask:
        print(f"{ip}.{a}.{b}     {ip}.{a}.{b + 1}      {ip}.{a + 31}.254    {ip}.{a + 31}.255")
        a = a + host
        contador = contador+32


# MASCARA 18
if host >= 8193 and host <= 16384:
    mask = (2 ** 7) + (2 ** 6)
    host = 64
    print(f"255.255.{mask}.0 /18")
    print(f"1.1.0.0.0.0.0.0")
    red = 2 ** 2
    print("Cantidad de redes = ", red)
    print(f"cantidad de host {64}")
    while contador <= mask:
        print(f"{ip}.{a}.{b}     {ip}.{a}.{b + 1}      {ip}.{a + 63}.254    {ip}.{a + 63}.255")
        a = a + host
        contador = contador+64



# MASCARA 17
if host >= 16385 and host <= 32768:
    mask = (2 ** 7)
    host = 128
    print(f"255.255.{mask}.0 /17")
    print(f"1.0.0.0.0.0.0.0")
    red = 2 ** 1
    print("Cantidad de redes = ", red)
    print(f"cantidad de host {128}")
    while contador <= mask:
        print(f"{ip}.{a}.{b}     {ip}.{a}.{b + 1}      {ip}.{a + 127}.254    {ip}.{a + 127}.255")
        a = a + host
        contador = contador+128


# MASCARA 16
if host >= 32769 and host <= 65536:
    mask = 0
    host = 256
    print(f"255.255.{mask}.0 /16")
    print(f"0.0.0.0.0.0.0.0")
    red = 2 ** 0
    print("Cantidad de redes = ", red)
    print(f"cantidad de host {256}")
    while contador <= mask:
        print(f"{ip}.{a}.{b}     {ip}.{a}.{b + 1}      {ip}.{a + 255}.254    {ip}.{a + 255}.255")
        a = a + host
        contador = contador+256