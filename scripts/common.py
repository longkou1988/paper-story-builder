from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT.parent
TOPIC_ROOT = SKILLS_ROOT / "paper-topic-builder"
MODEL_ROOT = SKILLS_ROOT / "paper-model-builder"
INPUT_DIR = ROOT / "input"
OUTPUT_DIR = ROOT / "output"

TOPIC_OUTPUTS = [
    "literature_matrix.xlsx",
    "variable_role_matrix.xlsx",
    "qualitative_mechanism_matrix.xlsx",
    "theory_gap_matrix.xlsx",
    "variable_network_summary.md",
    "topic_cards.md",
    "model_candidates.md",
    "final_research_story.md",
    "reviewer_evaluation.md",
]

MODEL_OUTPUTS = [
    "model_spec.json",
    "model_structure.md",
    "hypothesis_table.xlsx",
    "hypothesis_table.md",
    "model_diagram.mmd",
    "model_logic_check.md",
    "reviewer_model_evaluation.md",
    "model_story_for_paper.md",
]

CRITICAL_INPUTS = [
    MODEL_ROOT / "output" / "model_spec.json",
    MODEL_ROOT / "output" / "hypothesis_table.md",
    MODEL_ROOT / "output" / "model_story_for_paper.md",
    TOPIC_ROOT / "output" / "theory_gap_matrix.xlsx",
    TOPIC_ROOT / "output" / "final_research_story.md",
    INPUT_DIR / "benchmark_article.pdf",
]


def ensure_output_dir() -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR


def read_text(path: Path, default: str = "") -> str:
    if not path.exists():
        return default
    return path.read_text(encoding="utf-8", errors="replace")


def write_output(name: str, content: str) -> Path:
    ensure_output_dir()
    path = OUTPUT_DIR / name
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return path


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_json(name: str, data: dict) -> Path:
    ensure_output_dir()
    path = OUTPUT_DIR / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def inventory() -> dict:
    topic = {name: (TOPIC_ROOT / "output" / name).exists() for name in TOPIC_OUTPUTS}
    model = {name: (MODEL_ROOT / "output" / name).exists() for name in MODEL_OUTPUTS}
    inputs = {"benchmark_article.pdf": (INPUT_DIR / "benchmark_article.pdf").exists()}
    critical_missing = [str(path) for path in CRITICAL_INPUTS if not path.exists()]
    return {"topic_outputs": topic, "model_outputs": model, "inputs": inputs, "critical_missing": critical_missing}


def status_mark(ok: bool) -> str:
    return "OK" if ok else "MISSING"
