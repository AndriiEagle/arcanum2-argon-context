# Prompt 3 — One mechanic, drop-in GDScript with a headless test

Target: Godot 4.7.1, 2D painted isometric scene. The hero is a `Sprite2D`/`AnimatedSprite2D` child of a `Node2D`
"actors" layer; props and hotspots are `Sprite2D` nodes with `Area2D` pick shapes; everything is y-sorted in a
`Node2D` with `y_sort_enabled = true`. We cannot show you the project; write a self-contained module that only needs
the node paths it is given.

Mechanic: **occlusion x-ray halo** (Arcanum/Fallout style). When any prop sprite with a higher draw order overlaps the
hero's bounding box by more than 20% of the hero's area, draw a soft circular field (radius = 1.2 x hero height,
feathered edge, 35% opacity, warm tint from the scene's light colour) that reveals the hero through the prop. The field
fades in over 0.15 s and out over 0.25 s; it never shows when nothing occludes; it must cost < 0.2 ms per frame with 40
props (no per-frame allocation, no per-pixel work on the CPU — use a shader on a `CanvasItem` mask or `CanvasGroup`).

Deliver:
1. `xray_halo.gd` (a `Node2D` you add under the actors layer; exports: `hero_path`, `props_root_path`, `radius_mul`,
   `opacity`, `tint`), plus `xray_halo.gdshader`.
2. `tests/test_xray_halo.gd`: runs with `godot --headless -s tests/test_xray_halo.gd`, builds a tiny scene in code
   (hero rect, two props), asserts: (a) no halo when no overlap, (b) halo active at 25% overlap, (c) inactive at 10%,
   (d) fade timings within one frame of spec, (e) prints `OK 5/5` or the failing assert. No external test framework.
3. A 10-line integration note: where to add the node, which y-sort pitfall to check, and what to tune if the scene uses
   `CanvasLayer` for UI.

Output: three fenced code blocks (`gd`, `gdshader`, `gd`) with the file names as the first comment line, then the note.
No other prose.
