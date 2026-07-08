from __future__ import annotations

from common import inventory, status_mark, write_output


def main() -> None:
    data = inventory()
    lines = ["# Input Inventory", "", "## Topic Builder Outputs"]
    for name, ok in data["topic_outputs"].items():
        lines.append(f"- {status_mark(ok)} `{name}`")
    lines += ["", "## Model Builder Outputs"]
    for name, ok in data["model_outputs"].items():
        lines.append(f"- {status_mark(ok)} `{name}`")
    lines += ["", "## Story Builder Inputs"]
    for name, ok in data["inputs"].items():
        lines.append(f"- {status_mark(ok)} `{name}`")
    lines += ["", "## Blocking Missing Inputs"]
    if data["critical_missing"]:
        lines += [f"- {path}" for path in data["critical_missing"]]
    else:
        lines.append("- None")
    write_output("input_inventory.md", "\n".join(lines))


if __name__ == "__main__":
    main()
