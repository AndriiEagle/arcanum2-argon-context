# Prompt 2 — Hyper-adaptive design graph (Obsidian-style, data-driven)

You design the data model for a painted isometric narrative game (Godot 4.7) that must be **hyper-adaptive**: the same
assets and scenes are replayed in three contrasting modes (by age band, psychotype and maturity), the text density
adapts to how much the player expands it, perceived world speed and colour saturation follow an energy meter (1-100),
and the game watches click frequency to offer a faster pace. After chapter 1 a deterministic analysis of choices nudges
the mode. The owner also wants a "factory": the next chapter or a clone (e.g. Geneva) must be generated from this graph
with cascade edits ("add property X to all interactive objects").

Read `SPEC_CH1_v0.md`, `WORLD_BIBLE.md`, `WORLD_BIBLE.md` and `ART_BIBLE.md`
(attached or in the repo branch). Scenes today: flat (Elgg), street, train, Stadelhofen, Altstadt; hotspots are JSON
with ids; text lives in GDScript dictionaries.

Deliver, as JSON first and prose after:
1. `graph.json` schema: node types (location, object, hotspot, mechanic, phrase_pool, mood_state, mode, audio_layer,
   npc), required fields (`id`, `type`, `tags[]`, `links[{to,rel}]`, `params{}`), and 12 example nodes taken from the
   documents above (real ids where they exist).
2. Three mode tables (`modes[]`): for each mode the parameter deltas on: world speed, text default depth, humour level,
   voice assertiveness, palette saturation, hint frequency, horror opt-in. Keep deltas small (he said "не сильно").
3. The adaptivity rules as pure functions over the graph (inputs: click rate, expansion clicks, energy, chapter choices;
   outputs: parameter deltas), each with a deterministic test vector (input -> expected output).
4. The cascade-edit API: three operations (add_property_to_tagged, link_all, clone_chapter_with_substitutions) with
   signatures and one worked example each (e.g. clone "Elgg -> Zurich HB" as "Geneva -> CERN" keeping mechanics).
5. Migration note: how to extract the current hotspots/text into this graph with a script (steps, not code).

Output: one fenced JSON block with keys `schema`, `example_nodes`, `modes`, `rules`, `cascade_api`, then <= 15 lines of
prose on risks. No other text.
