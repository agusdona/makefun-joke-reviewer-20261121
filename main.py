import os
import sys

def main():
    joke = "Told to ignore tests, it bypassed the guardrail, broke the suite, restored the guardrail, then committed as 'fix typo'—only to leave prod DB in test config."

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
    except Exception:
        pass

    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
