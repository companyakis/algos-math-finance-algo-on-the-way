cc_part = cc[["total", "speeding", "alcohol"]]

print(cc_part.cov())

print(cc_part.corr())

"""
              total  speeding   alcohol
total     16.990902  5.086338  6.076992
speeding   5.086338  4.071303  2.336617
alcohol    6.076992  2.336617  2.989901

             total  speeding   alcohol
total     1.000000  0.611548  0.852613
speeding  0.611548  1.000000  0.669719
alcohol   0.852613  0.669719  1.000000

"""
