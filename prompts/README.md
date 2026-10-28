# Three isolated evaluation prompts (prepared 2026-10-28)

Goal: see what an external web model can do for this game in three separate lanes: **visual repair director**,
**hyper-adaptive design graph**, **mechanic code with a headless test**. Run each prompt in its own chat; never merge
the three. Ask the model to read `WORLD_BIBLE.md`, `ART_BIBLE.md`, `SPEC_CH1_v0.md` and look at `samples/` first.

## Samples
| file | what it shows | why it is here |
|---|---|---|
| `samples/V-001_00-00-33.png` | flat, hero at the window, OS cursor visible | reference background quality; cursor defect |
| `samples/V-007_00-06-43.png` | flat, dialogue box with portrait | text/UI layout, portrait style |
| `samples/V-014_00-12-12.png` | flat, dusk grade | black-rectangle / grade issue |
| `samples/V-025_00-20-07.png` | Elgg street, rain, umbrella | the look to protect |
| `samples/V-029_00-23-21.png` | street, gnome prop over the hero | layering defect |
| `samples/V-043_00-36-41.png` | phone / UI moment | phone interface direction |
| `samples/V-0xx_*.jpg` (8 more) | later street, train, Stadelhofen moments | breadth of locations and light |

## Acceptance (done locally by us, no model needed)
- Prompt 1 -> a JSON plan: regions inside 1280x720, each with prompt, mask spec, blend width; no "regenerate the
  whole image".
- Prompt 2 -> JSON with schema, example nodes, modes, rules with test vectors, cascade API; no prose outside the block.
- Prompt 3 -> the GDScript module + headless test must pass unchanged in Godot 4.7.1.
