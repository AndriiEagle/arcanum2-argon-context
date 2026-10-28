# World bible — working title "Arcanum 2" (painted narrative game, Zurich, today + 5 years)

This file is the condensed canon for an external art/design model. Everything here is decided; do not re-invent it.

## One paragraph
A migrant hero in his thirties lives in a rented flat in Elgg, a small town east of Zurich, and commutes by SBB train to
Zurich Stadelhofen and the Altstadt. By day: a real, beautiful Switzerland — craft, money worries, burnout, a phone with
an AI assistant, a neighbour who plays the violin. By night: dreams in cinematic monochrome with one symbolic colour.
Combat, when it comes, is harsh (Fear & Hunger register), but chapter 1 is about one year of life: it ends when the hero
ships the game of his dreams. The hero is the author's alter ego under another name; real people appear under other
names. Languages: 5; the "migrant language" mechanic shows German lines with blurred words and the hero's translated
thought underneath.

## Genre and camera
Painted isometric 2D (Godot 4.7), fixed camera per location, click-to-move, hotspots, dialogue boxes with portrait,
thought bubbles. References the owner names: Arcanum, Fallout 1-2, Heroes of Might and Magic III (isometry and
readability), visual novels for portrait emotion, Steins;Gate for the phone-in-hand moment, Sherlock (BBC) for the
"deduction overlay" when the hero reasons.

## Visual law (sealed)
1. World: painted, crisp, realism + a pinch of magic + technology five years ahead. Not pixel art. Two accepted idioms:
   oil/gouache painting (A) and parchment schematic (D) for maps/diaries.
2. Night is never a blue filter: moon, stars, a moon path on water, warm windows.
3. Dreams: Sin City monochrome, cinematic, one symbolic colour per dream on about 20% of the frame, always meaningful
   (green snake eyes, red heat). Near-future noir layer: 70-80% monochrome, at most 30% accent.
4. Light and palette per location are in `ART_BIBLE.md` (temperatures, the "living window" F5 rule: one lit window
   shows where the person and the story are).
5. Autumn is the season: golden leaves, wet asphalt with reflections, rain and umbrellas, church bells; a sunny version
   and a grey rainy version of the same morning must both exist and change how people move and how many are outside.
6. Hero style "3 — crisp": clean silhouette, readable at 1280x720, no blur; morning scenes in a bathrobe, laptop asleep
   on the windowsill; later the grey jacket and an electro-acoustic guitar with steel strings.
7. UI: painted kit, monochrome phone UI with a ChatGPT-like assistant restyled to the game, icons that can replace
   words (traffic-sign clarity), one highlighted word per sentence at most in one sentence of three.

## Route of chapter 1 (opening)
Dream montage (fast monochrome cuts, horror undertone) -> black -> church bells -> wake up in the Elgg flat (coffee on
the windowsill, diary, phone) -> street in Elgg (fountain with a child-angel statue, church, benches, a modest pizzeria,
a burnt shed, the neighbour's house with the violin room under a sloped roof and a skylight) -> SBB train (Winterthur in
the window) -> Zurich Stadelhofen (wet yellow leaves, the "Velora" kiosk, a bench with one dry seat) -> Altstadt.

## Mechanics the art must serve
- Energy 1-100 drives saturation, detail, focus and perceived world speed (100 = full colour; low = pale, slow, blurred).
- Choices change the portrait and body language with non-linear easing (draining = fast in/slow out; energising =
  slow in/fast out).
- Thought bubble vs. spoken line are visually different; while thinking, the surroundings desaturate and freeze in a
  radius; the most important object keeps its colour (deduction mode).
- First-person "glasses" mask for close looks: elliptical vision, faint nose, centre 30% sharp, edges softer.
- Occlusion x-ray halo around the hero behind props (Arcanum/Fallout style).
- Passers-by as translucent "ghosts" on looping paths; sit on a bench and listen to Swiss-German murmur.
- Three contrasting modes (age band x psychotype x maturity) with small parameter deltas, chosen to make the player
  replay the other two.

## Hard no
No pixel art, no blue-filter night, no flat grey dreams, no generic fantasy, no stock-photo faces, no text walls.
