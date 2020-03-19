# hf2_Software

## Instalation

### Linux
#### Ubuntu / Debian
`sudo apt install -y build-essential cmake libusb-1.0-0-dev pkg-config libfftw3-dev htop curl wget git zsh python-pip virtualenv libtool autoconf pkg-config libxml2-dev vim ncdu libfftw3-dev`
`sudo apt install gqrx-sdr`
`sudo apt install gnuradio hackrf `

**Testing the HackRF**

1. Plug in the HackRF
2. run the hackrf_info command<br>
`$ hackrf_info`

If everything is OK, you should see something similar to the following:

> hackrf_info version: 2017.02.1<br>
> libhackrf version: 2017.02.1 (0.5)<br>
> Found HackRF<br>
> Index: 0<br>
> Serial number: 0000000000000000################<br>
> Board ID Number: 2 (HackRF One)<br>
> Firmware Version: 2017.02.1 (API:1.02)<br>
> Part ID Number: 0x######## 0x########<br>

**FM Radio Example**

This Example was derived from the following works:
* [RTL-SDR FM radio receiver with GNU Radio Companion](http://www.instructables.com/id/RTL-SDR-FM-radio-receiver-with-GNU-Radio-Companion/) 
* [How To Build an FM Receiver with the USRP in Less Than 10 Minutes](https://www.youtube.com/watch?v=KWeY2yqwVA0)
<br><br>

1. [Download the FM Radio Receiver python file here](https://raw.githubusercontent.com/rrobotics/hackrf-tests/master/fm_radio/fm_radio_rx.py)
2. Run the file <br>
`$ python ./fm_radio_rx.py`
3. [You can find the GNU Radio Companion source file here](https://raw.githubusercontent.com/rrobotics/hackrf-tests/master/fm_radio/fm_radio_rx.grc)

## [Getting Help](https://github.com/mossmann/hackrf/wiki/Getting-Help)
 
