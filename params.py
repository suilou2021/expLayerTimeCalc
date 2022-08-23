########################################################################
# params.py
#
# Created: Aug. 23, 2022
# Author: S. Huang
# This is the parameter file for calculating expected layer time for OEE
# based on GEN2.0 specifications
########################################################################

# gantry acceleration (mm/s^2)
a = 4900
# scan speed (mm/s)
v = 600
# ramp compensation factor
rampCompF = 1.3
# (empirical) time for indexing and offsetting per trajectory (s)
tIndexOffset = 0.18
# recoating and imaging time per layer considering double recoat factor (s)
tRecoatImg = 25.721
# gas head cleaning time (s)
tGasHeadCleaning = 14
# ramping distance
dx = (1/2)*v**2/a
# time for ramping
tRamping = v/a
# time for ramp compensation
tRampComp = tRamping + (rampCompF - 1)/v

