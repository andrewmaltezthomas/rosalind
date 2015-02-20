homozygous_dominant = raw_input("Enter number of homozygous dominant organisms:")
homozygous_dominant = float(homozygous_dominant)
heterozygous = raw_input("Enter number of heterozygous organisms:")
heterozygous = float(heterozygous)
homozygous_recessive = raw_input("Enter number of homozygous recessive organisms:")
homozygous_recessive = float(homozygous_recessive)
total = homozygous_recessive + homozygous_dominant + heterozygous

# There are fewer ways to get two recessive alleles, 
# So calculate that instead and then subtract the result from one to get the probability of a dominant allele 

# Probability of two recessive parents mating:
prob_homozygous_recessive = (homozygous_recessive / total) * ((homozygous_recessive - 1) / (total - 1))
# Probability of two heterozygous parents mating:
prob_heterozygous = (heterozygous / total) * ((heterozygous - 1) / (total - 1))

# Punnet square for heterozygous mating:
# |   | Y  | y  |
# |---+----+----|
# | Y | YY | Yy |
# | y | Yy | yy |
# Only 1/4 of those will be recessive so we take the probability of two heterozygous mating and multiply it by 1/4.

# Probability of a heterozygous and a recessive parent mating:
prob_heterozygous_homozgous_recessive = (heterozygous / total) * (homozygous_recessive / (total - 1)) + (homozygous_recessive / total) * (heterozygous / (total - 1))

# Punnet square for heterozygous & recessive mating:
# |   | Y  | y  |
# |---+----+----|
# | y | Yy | yy |
# | y | Yy | yy |
# In this case half the offspring have two recessive alleles so multiply the probability by 1/2.

# Total probability of a recessive allele:
prob_recessive = prob_homozygous_recessive + prob_heterozygous * 1/4 + prob_heterozygous_homozgous_recessive * 1/2
# Probability of a dominant allele:
prob_dominant = 1 - prob_recessive
print prob_dominant