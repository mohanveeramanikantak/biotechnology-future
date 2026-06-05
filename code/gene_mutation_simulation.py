# Gene Mutation Simulation

import random

dna_sequence = "ATGCGTACGTA"

print("Original DNA Sequence:", dna_sequence)

# Convert string to list for mutation
dna_list = list(dna_sequence)

# Random mutation position
position = random.randint(0, len(dna_list) - 1)

# DNA bases
bases = ["A", "T", "G", "C"]

# Replace with a different base
old_base = dna_list[position]
new_base = random.choice([base for base in bases if base != old_base])

dna_list[position] = new_base

mutated_sequence = "".join(dna_list)

print("Mutation Position:", position)
print("Old Base:", old_base)
print("New Base:", new_base)
print("Mutated DNA Sequence:", mutated_sequence)
