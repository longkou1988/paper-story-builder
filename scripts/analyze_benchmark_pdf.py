from __future__ import annotations

import re
from pathlib import Path

from common import INPUT_DIR, write_output


def extract_pdf_text(path: Path) -> str:
    for module_name in ("pypdf", "PyPDF2"):
        try:
            module = __import__(module_name)
            reader = module.PdfReader(str(path))
            return "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception:
            continue
    return ""


def guess_sections(text: str) -> list[str]:
    headings = []
    for line in text.splitlines():
        clean = line.strip()
        if 3 <= len(clean) <= 90 and re.match(r"^(abstract|introduction|theory|literature|hypoth|method|results|discussion|conclusion|contribution)", clean, re.I):
            headings.append(clean)
    return headings[:40]


def main() -> None:
    pdf = INPUT_DIR / "benchmark_article.pdf"
    if not pdf.exists():
        write_output("benchmark_structure_analysis.md", "# Benchmark Structure Analysis\n\nBLOCKED: `input/benchmark_article.pdf` is missing. Upload a benchmark article before formal story-chain drafting.")
        return
    text = extract_pdf_text(pdf)
    if not text.strip():
        write_output("benchmark_structure_analysis.md", "# Benchmark Structure Analysis\n\nLOW CONFIDENCE: PDF text could not be extracted. Use manual notes in `input/manual_story_notes.md` or provide a readable PDF.")
        return
    headings = guess_sections(text)
    excerpt = text[:1800].replace("\n", " ")
    lines = ["# Benchmark Structure Analysis", "", "## Extracted Section Signals"]
    lines += [f"- {h}" for h in headings] or ["- Insufficient section signals detected"]
    lines += ["", "## Safe Structural Notes", "- Use only section order, rhetorical function, and paragraph-level logic as reference.", "- Do not copy, translate, or paraphrase benchmark wording.", "", "## Extraction Preview", excerpt]
    write_output("benchmark_structure_analysis.md", "\n".join(lines))


if __name__ == "__main__":
    main()
