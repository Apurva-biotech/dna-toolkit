def transcribe(dna):
  """
    Transcribes a DNA sequence to RNA.
    Replaces every Thymine (T) with Uracil (U).
    
    Args:
        dna (str): DNA sequence (e.g. "ATGCTA")
    Returns:
        str: RNA sequence (e.g. "AUGCUA")
    """
    dna = dna.upper()
    for base in dna:
        if base not in "ATGC":
            raise ValueError(f"Invalid base: '{base}'. Only A, T, G, C are allowed.")
    rna = dna.replace("T", "U")
    return rna


if __name__ == "__main__":
    test_seq = "ATGCTTAA"
    print(f"DNA: {test_seq}")
    print(f"RNA: {transcribe(test_seq)}")
