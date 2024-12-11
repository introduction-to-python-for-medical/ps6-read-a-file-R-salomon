def create_codon_dict(file_path):
    rows = []
    file = open(path, "r")
    rows = file.readlines()
    file.close()
  
    Codon_to_Amino_Acid = {}
    for row in rows:
      row_cells = row.strip().split('\t')
      codon = row_cells[0]
      amino_acid = row_cells[2]
      Codon_to_Amino_Acid[codon] = amino_acid
    return Codon_to_Amino_Acid

