# Arcanum 2 — context pack for external art/design models

Public, curated context so a web model (Gemini "Argon 4" or similar) can draw and design for this game in its exact
style. No game code, no private material — only canon, style, samples and three isolated evaluation prompts.

```
WORLD_BIBLE.md                 condensed world/genre/visual law (start here)
ART_BIBLE.md                   light, palettes, temperatures per location
SPEC_CH1_v0.md                 chapter-1 systems: day cycle, energy, habits, craft
prompts/PROMPT_1_visual_repair_director.md
prompts/PROMPT_2_hyperadaptive_graph.md
prompts/PROMPT_3_mechanic_code_with_tests.md
prompts/README.md              how we accept each answer locally
samples/                       real 1280x720 playtest frames (what the game looks like today)
```

How to use with a web model: open the repository link, ask the model to read `WORLD_BIBLE.md`, `ART_BIBLE.md` and the
sample frames first, then paste ONE prompt from `prompts/`. Each prompt is self-contained and ends with the output
format we parse.
