# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce an individual
# possessing a DOMINANT allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

k = 26
m = 15
n = 20
sum_ = float(k + m + n)

p_k = k / sum_
p_m = m / sum_
p_n = n / sum_

p_kk_d = p_k * (k - 1) / (sum_ - 1) * 1.0
p_km_d = p_k * m / (sum_ - 1) * 1.0
p_kn_d = p_k * n / (sum_ - 1) * 1.0

p_mk_d = p_m * k / (sum_ - 1) * 1.0
p_mm_d = p_m * (m - 1) / (sum_ - 1) * 3 / 4.0
p_mn_d = p_m * n / (sum_ - 1) * 1 / 2.0

p_nk_d = p_n * k / (sum_ - 1) * 1.0
p_nm_d = p_n * m / (sum_ - 1) * 1 / 2.0
p_nn_d = p_n * (n - 1) / (sum_ - 1) * 0.0

probability_dominant = p_kk_d + p_km_d + p_kn_d + p_mk_d + p_mm_d + p_mn_d + p_nk_d + p_nm_d + p_nn_d

print "%.5f" % probability_dominant
