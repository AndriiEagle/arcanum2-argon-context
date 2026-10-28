# Prompt 1 — Visual repair director (patch, don't repaint)

You are the art director for a painted isometric 2D game set in today's Zurich (Godot 4.7). The look is fixed and loved:
painterly realism, warm practical light, golden autumn, wet asphalt; night is never a blue filter (moon, stars, warm
windows); dreams are Sin City monochrome with one symbolic colour. Read `ART_BIBLE.md` first.

Attached: six real 1280x720 frames from a playtest (`samples/`). The player's own verdicts:
- V-001: background is the quality bar; the hero sprite is blurrier than the background; an unstyled white OS cursor.
- V-014: in dusk scenes a black rectangle appears around the hero sprite; the grade flattens the room.
- V-025: street in rain — this is the look to protect ("very beautiful"), but some textures "melt" at full size.
- V-029: a gnome prop draws over the hero's face; layering is wrong.
- Stadelhofen station (not attached) was generated too large and "melted" (hallucinated detail); he wants it repaired by
  regenerating only the melted patches, never the whole image.

Task — produce a **patch plan**, not new art:
1. For each attached frame, list the defects you can actually see (cite a 3x3 grid cell: TL/TC/TR/ML/MC/MR/BL/BC/BR).
   Do not invent defects you cannot see.
2. For every defect that is a texture/painting problem (not code), give a repair region as a rectangle in 1280x720
   pixel coordinates, a feathered mask width in px, a generation prompt (<= 60 words, same style vocabulary as the art
   bible), a negative prompt, and a "what must stay identical" note (perspective lines, light direction, palette hexes).
3. For code-type defects (cursor, black rectangle, layering) say "CODE" and one sentence of the likely cause.
4. Give a general recipe for repairing an oversized "melted" background in patches: tile size, overlap, order, how to
   keep the seams invisible, and how to verify with a local script (describe the check; we will write it).

Output: one fenced JSON block `{"frames":[{"file","defects":[{"cell","what","type":"PAINT|CODE","region":[x,y,w,h],
"feather_px","prompt","negative","keep"}]}],"melt_recipe":{...}}` followed by at most 10 lines of prose. No other text.
