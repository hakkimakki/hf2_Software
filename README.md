# hf2_Software

## Instalation

### Linux
#### Ubuntu / Debian
`sudo apt install -y build-essential cmake libusb-1.0-0-dev pkg-config libfftw3-dev htop curl wget git zsh python-pip virtualenv libtool autoconf pkg-config libxml2-dev vim ncdu libfftw3-dev swig`<br>
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

**PRBS Source for BER Testing**<br>
`git clone https://github.com/gr-vt/gr-mapper`<br>
Go to file: `gr-mapper/python/prbs_sink_b.py` and edit the following lines:<br>
line 25 `if self.nbits > 200000:`<br>
add lines after line 27 <br>
`self.nerrs = 0`<br>
`self.nbits = 0`<br>
save the file and continue<br>
`cd gr-mapper`<br>
`cmake ./`<br>
`make`<br>
`sudo make install`<br>
`sudo ldconfig`<br>
<br><br>

 
