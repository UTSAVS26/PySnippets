import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pysnippets.maths import polar_rectangular_conversion as prc


r = 5
theta = 1.57  
rect_coords = prc.polar_to_rectangular(r, theta)
print(f"Polar to Rectangular (Radians): {rect_coords}")

rect_coords_degrees = prc.polar_to_rectangular(r, 90, degrees=True)
print(f"Polar to Rectangular (Degrees): {rect_coords_degrees}")

x, y = 3, 4
polar_coords = prc.rectangular_to_polar(x, y)
print(f"Rectangular to Polar: {polar_coords}")

polar_list = [(5, 0.5), (3, 1), (2, 1.5)]
bulk_rect = prc.bulk_polar_to_rectangular(polar_list)
print(f"Bulk Polar to Rectangular: {bulk_rect}")

r, theta, z = 3, 1.57, 7
cylindrical_to_rect = prc.cylindrical_to_rectangular(r, theta, z)
print(f"Cylindrical to Rectangular: {cylindrical_to_rect}")

complex_number = prc.polar_to_complex(5, 45, degrees=True)
print(f"Polar to Complex: {complex_number}")

complex_to_polar_coords = prc.complex_to_polar(complex(3, 4))
print(f"Complex to Polar: {complex_to_polar_coords}")
