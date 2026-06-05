# Protein Structure Analysis Simulation

protein_sequence = "MKTFFVAGIL"

print("Protein Sequence:", protein_sequence)

# Amino acid categories
hydrophobic = ["A", "V", "I", "L", "M", "F", "W", "Y"]
polar = ["S", "T", "N", "Q"]
charged = ["D", "E", "K", "R", "H"]

hydrophobic_count = 0
polar_count = 0
charged_count = 0

for amino_acid in protein_sequence:
    if amino_acid in hydrophobic:
        hydrophobic_count += 1
    elif amino_acid in polar:
        polar_count += 1
    elif amino_acid in charged:
        charged_count += 1

print("Hydrophobic Amino Acids:", hydrophobic_count)
print("Polar Amino Acids:", polar_count)
print("Charged Amino Acids:", charged_count)

if hydrophobic_count > polar_count:
    print("Analysis: Protein may have strong internal folding tendency")
else:
    print("Analysis: Protein may interact more with surrounding water")
