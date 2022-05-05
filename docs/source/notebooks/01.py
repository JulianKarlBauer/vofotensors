# # Print available parameterizations of second-order fiber orientation tensors (FOT)

import vofotensors as vot

print("Available parameterizations of second order fiber orientation tensors:\n")
vot.utils.print_nested(vot.fabric_tensors.N2s_parametric)
