from dna_toolkit import transcribe

def test_basic_transcription():
    assert transcribe("ATGC") == "AUGC"
    print("✓ Basic transcription passed")

def test_lowercase_input():
    assert transcribe("atgc") == "AUGC"
    print("✓ Lowercase input passed")

def test_no_thymine():
    assert transcribe("AAGC") == "AAGC"
    print("✓ No T sequence passed")

def test_invalid_base():
    try:
        transcribe("ATGX")
        print("✗ Should have raised an error")
    except ValueError:
        print("✓ Invalid base correctly caught")

if __name__ == "__main__":
    test_basic_transcription()
    test_lowercase_input()
    test_no_thymine()
    test_invalid_base()
    print("\nAll tests passed! 🎉")
