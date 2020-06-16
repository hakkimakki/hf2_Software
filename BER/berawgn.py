#!/usr/bin/env python
#
# Copyright 2012,2013 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
#

"""
BER simulation for QPSK signals, compare to theoretical values.
Change the N_BITS value to simulate more bits per Eb/N0 value,
thus allowing to check for lower BER values.

Lower values will work faster, higher values will use a lot of RAM.
Also, this app isn't highly optimized--the flow graph is completely
reinstantiated for every Eb/N0 value.
Of course, expect the maximum value for BER to be one order of
magnitude below what you chose for N_BITS.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals


import math
import numpy
from gnuradio import gr, digital
from gnuradio import analog
from gnuradio import blocks
import sys

try:
    from scipy.special import erfc
except ImportError:
    print("Error: could not import scipy (http://www.scipy.org/)")
    sys.exit(1)

try:
    from matplotlib import pyplot
except ImportError:
    print("Error: could not from matplotlib import pyplot (http://matplotlib.sourceforge.net/)")
    sys.exit(1)

# Best to choose powers of 10
N_BITS = 1e7
RAND_SEED = 42

    # Indexing for different Meassurment Methodes
    # 0 BPSK
    # 1 QPSK
    # 2 8PSK
    # 3 16-QAM
# 4 64-QAM
# 5 256-QAM
modulations = ["BPSK","QPSK","8PSK","16-QAM","64-QAM","256-QAM"]



def berawgn(EbN0):
    """ Calculates theoretical bit error rate in AWGN (for BPSK and given Eb/N0) """
    return 0.5 * erfc(math.sqrt(10**(float(EbN0) / 10)))

class BitErrors(gr.hier_block2):
    """ Two inputs: true and received bits. We compare them and
    add up the number of incorrect bits. Because integrate_ff()
    can only add up a certain number of values, the output is
    not a scalar, but a sequence of values, the sum of which is
    the BER. """
    def __init__(self, bits_per_byte):
        gr.hier_block2.__init__(self, str("BitErrors"),
                gr.io_signature(2, 2, gr.sizeof_char),
                gr.io_signature(1, 1, gr.sizeof_int))

        # Bit comparison
        comp = blocks.xor_bb()
        intdump_decim = 100000
        if N_BITS < intdump_decim:
            intdump_decim = int(N_BITS)
        self.connect(self,
                     comp,
                     blocks.unpack_k_bits_bb(bits_per_byte),
                     blocks.uchar_to_float(),
                     blocks.integrate_ff(intdump_decim),
                     blocks.multiply_const_ff(1.0 / N_BITS),
                     self)
        self.connect((self, 1), (comp, 1))

class BERAWGNSimu(gr.top_block):
    " This contains the simulation flow graph "
    def __init__(self, EbN0,modulation):
        gr.top_block.__init__(self)
        if modulation == "BPSK":
            self.const = digital.constellation_bpsk()
        elif modulation == "QPSK":
            self.const = digital.constellation_qpsk()
        elif modulation == "8PSK":
            self.const = digital.constellation_8psk()
        elif modulation == "16-QAM":
            self.const = digital.qam_constellation(constellation_points=16, differential=True, mod_code='none', large_ampls_to_corners=False)
        elif modulation == "64-QAM":
            self.const = digital.qam_constellation(constellation_points=64, differential=True, mod_code='none', large_ampls_to_corners=False)
        elif modulation == "256-QAM":
            self.const = digital.qam_constellation(constellation_points=256, differential=True, mod_code='none', large_ampls_to_corners=False)
        #self.const = digital.qam_constellation(constellation_points=4, differential=True, mod_code='none', large_ampls_to_corners=False)
        #print(self.const.bits_per_symbol())
        #print(self.const.arity())
        #print(self.const.points())
        #print(self.const.base())
        # Source is N_BITS bits, non-repeated
        b = int(N_BITS / self.const.bits_per_symbol())
        a = map(int, numpy.random.randint(0, self.const.arity(), b))
        data = list(a)
        src   = blocks.vector_source_b(data, False)
        mod   = digital.chunks_to_symbols_bc((self.const.points()), 1)
        add   = blocks.add_vcc()
        noise = analog.noise_source_c(analog.GR_GAUSSIAN,
                                      self.EbN0_to_noise_voltage(EbN0),
                                      RAND_SEED)
        demod = digital.constellation_decoder_cb(self.const.base())
        ber   = BitErrors(self.const.bits_per_symbol())
        self.sink  = blocks.vector_sink_f()
        self.connect(src, mod, add, demod, ber, self.sink)
        self.connect(noise, (add, 1))
        self.connect(src, (ber, 1))

    def EbN0_to_noise_voltage(self, EbN0):
        """ Converts Eb/N0 to a complex noise voltage (assuming unit symbol power) """
        a = 10**(float(EbN0) / 10)
        b = 1.0 / math.sqrt(self.const.bits_per_symbol()*a)
        #print(b)
        return b


def simulate_ber(EbN0,modulation):
    """ All the work's done here: create flow graph, run, read out BER """
    print("Eb/N0 = %d dB" % EbN0)
    fg = BERAWGNSimu(EbN0,modulation)
    fg.run()
    return numpy.sum(fg.sink.data())

if __name__ == "__main__":
    EbN0_min = 0
    EbN0_max = 16
    EbN0_range = list(range(EbN0_min, EbN0_max+1))
    #ber_theory = [berawgn(x)      for x in EbN0_range]
    print("Init plots...")
    # Init the Plots
    f = pyplot.figure()
    s = f.add_subplot(1,1,1)
    s.set_title('BER Simulation')
    s.set_xlabel('Eb/N0 (dB)')
    s.set_ylabel('BER')
    s.set_ylim([10e-8,0.1])
    s.grid()
    #Start Simulation
    print("Simulating...")
    for modulation in modulations:
        print(modulation)
        ber_simu = [simulate_ber(x,modulation) for x in EbN0_range]
        s.semilogy(EbN0_range, ber_simu, marker='o', label=modulation) 
    #Show Plots
    s.legend()
    pyplot.show()
