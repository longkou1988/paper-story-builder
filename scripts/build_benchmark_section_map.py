from __future__ import annotations

from common import OUTPUT_DIR, read_text, save_json


def main() -> None:
    analysis = read_text(OUTPUT_DIR / "benchmark_structure_analysis.md")
    sections = []
    for line in analysis.splitlines():
        if line.startswith("- ") and not line.startswith("- Use") and not line.startswith("- Do not"):
            sections.append({"label": line[2:].strip(), "rhetorical_function": "to be interpreted from benchmark structure only"})
    save_json("benchmark_section_map.json", {
        "source": "benchmark_structure_analysis.md",
        "use_policy": "structure-only; no copying or importing substantive claims",
        "sections": sections,
    })


if __name__ == "__main__":
    main()
