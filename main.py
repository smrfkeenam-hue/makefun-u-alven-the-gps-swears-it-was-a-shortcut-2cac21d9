import os

LINE = "The map said that lake was a road, and I stand by it; you got here early, you're just finishing the last hundred metres by swimming."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + "/entry.txt"
with open(out, "w", encoding="utf-8") as f:
    f.write(LINE)
