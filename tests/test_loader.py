from src.pdf_loader import load_pdf

def test_loader():

    text = load_pdf("data/sample.pdf")

    assert len(text) > 0