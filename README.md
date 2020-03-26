# hf2_Software

## Instalation

### Linux
#### Ubuntu / Debian
`sudo apt install -y build-essential cmake libusb-1.0-0-dev pkg-config libfftw3-dev htop curl wget git zsh python-pip virtualenv libtool autoconf pkg-config libxml2-dev vim ncdu libfftw3-dev`<br>
`sudo apt install gqrx-sdr`<br>
`sudo apt install hackrf`<br>
`sudo apt install gnuradio`<br>
Reboot Linux!

**Testing the HackRF**

1. Plug in the HackRF
2. run the hackrf_info command<br>
`$ hackrf_info`

If everything is OK, you should see something similar to the following:

> hackrf_info version: unknown<br>
> libhackrf version: unknown (0.5)<br>
> Found HackRF<br>
> Index: 0<br>
> Serial number: 0000000000000000################<br>
> Board ID Number: 2 (HackRF One)<br>
> Firmware Version: 2018.02.1 (API:1.02)<br>
> Part ID Number: 0x######## 0x########<br>

**FM Radio Example**

To test try the following Example to build an FM Receiver
* [HackRF One Receiving FM Radio Signals](https://www.youtube.com/watch?v=ye8wFVPF4wI)
<br><br>

**BLE Packet Dumper**
To test try the following Example to build an BLE Packet Dumper
* [ble_dump](https://github.com/drtyhlpr/ble_dump)
<br><br>

 
