# Storyboards, Split Screens, Text, and Evaluation: 9 Original Prompts

<!-- catalog:hero:start -->
[![故事板、文字与评测 / Storyboards, text and evaluation](../assets/category-storyboard-v2.png)](../assets/category-storyboard-v2.png)

*分类题材示意 / Category illustration*
<!-- catalog:hero:end -->

[← Previous: Advanced editing, camera, and visual transformation](advanced-editing-camera.md) · [English home](../README.md) · [中文主页](../README_ZH.md)

> Source: adapted from [Flaq AI](https://github.com/flaqai/awesome-gemini-omni-flash), under MIT. Prompts are practice briefs, not SeaImagine-verified results. Advanced controls depend on the selected interface.

This collection turns planning boards, diagrams, source clips, and exact copy into structured video. It also includes a repeatable evaluation recipe. A storyboard is a shot plan, not nine independent first frames; exact text should be short, quoted, timed, and tested at draft resolution before delivery.

<a id="case-index"></a>

<!-- catalog:toc:start -->
**本页案例 / Cases** · [全部 76 例 / All 76 cases](../docs/prompt-index.md)

- [01 · Convert a 3×3 storyboard into one ordered micro-story](#case-01) · [TXT](copy/storyboard-text-evaluation-01.txt)
- [02 · Nine-window split screen with synchronized detail actions](#case-02) · [TXT](copy/storyboard-text-evaluation-02.txt)
- [03 · Single-source action replay from two generated viewpoints](#case-03) · [TXT](copy/storyboard-text-evaluation-03.txt)
- [04 · Turn a static process diagram into motion](#case-04) · [TXT](copy/storyboard-text-evaluation-04.txt)
- [05 · Use one image as an instruction board and another as identity](#case-05) · [TXT](copy/storyboard-text-evaluation-05.txt)
- [06 · Word-by-word kinetic typography synchronized to speech](#case-06) · [TXT](copy/storyboard-text-evaluation-06.txt)
- [07 · One title sequence, four language-safe variants](#case-07) · [TXT](copy/storyboard-text-evaluation-07.txt)
- [08 · Clay-table explainer: why tectonic plates move](#case-08) · [TXT](copy/storyboard-text-evaluation-08.txt)
- [09 · Controlled A/B/C prompt evaluation](#case-09) · [TXT](copy/storyboard-text-evaluation-09.txt)
<!-- catalog:toc:end -->

<a id="case-01"></a>

## 01 | Convert a 3×3 storyboard into one ordered micro-story

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-01.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Image reference to video · **Input:** One original 3×3 storyboard sheet · **Goal:** Preserve panel order and narrative logic

```text
[# References <IMAGE_REF_0>@Image1]
Use Image1 only as a nine-panel storyboard and art-direction reference. Read panels left to right, top to bottom. Create a coherent 10-second animated short based on that exact order; do not show the grid, panel borders, arrows, notes, or captions in the final video.

Story: a tiny solar-powered delivery rover notices a fallen seedling, stops, extends one padded tool, returns the seedling upright, presses soil around it, then resumes its route as the seedling's leaves turn toward the sun.

[0-3s] Combine panels 1-3 into the setup and discovery.
[3-7s] Combine panels 4-7 into one continuous repair action with clear tool-to-soil contact.
[7-10s] Use panels 8-9 for the payoff and a steady final composition.

Preserve the rover design, seedling pot, left-to-right geography, warm miniature-set lighting, and scale across every shot. Use motivated cuts only where the board changes shot size.
Audio: small electric motor, soft soil contact, leaves, one original hopeful three-note cue. No dialogue.
No extra character, rescue montage, printed notes, brand, text, logo, or watermark.
```

**Board preparation:** Number panels outside the artwork, keep one dominant action per panel, and use the same identity anchors in all nine drawings.

<a id="case-02"></a>

## 02 | Nine-window split screen with synchronized detail actions

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-02.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Text-to-video · **Goal:** Stable 3×3 layout and simultaneous motion

```text
Create a 10-second 16:9 video divided into an exact 3×3 grid with nine equal windows and thin warm-gray dividers. The grid remains locked for the entire clip.

Each window shows a different close detail from the same fictional neighborhood bakery at 5:30 a.m.:
top row: flour landing on a table; dough folded once; an oven thermometer rising.
middle row: a whisk turning; steam leaving a kettle; a hand opening plain paper bags.
bottom row: a bicycle wheel stopping outside; a lamp switching on; one round loaf placed on a cooling rack.

[0-6s] All nine actions unfold at natural, different speeds.
[6-8s] Actions settle one by one from top-left to bottom-right.
[8-10s] Every window holds a calm finished state.

Audio: one coherent bakery soundscape mixed across the grid—soft dough contact, whisk, kettle, oven tick, bicycle freewheel—with an original low marimba pulse. No dialogue.
Maintain nine windows only, consistent warm palette, plausible hands, and unique content per window. No merged cells, moving dividers, labels, brands, logos, subtitles, or watermark.
```

<a id="case-03"></a>

## 03 | Single-source action replay from two generated viewpoints

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-03.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Edit / reinterpret source event · **Input:** One authorized action clip · **Goal:** Creative replay, not forensic reconstruction

```text
Re-edit the same single-source event as a 10-second action replay with exactly three shots. Preserve the same adult skateboarder, plain clothing, board design, trick order, landing direction, location, weather, and original ambient sound.

[0-3s] Use the source viewpoint at normal speed to establish the approach.
[3-7s] Generate a low side view of the same jump at 50% speed, keeping board-to-foot contact and believable gravity.
[7-10s] Generate a high rear three-quarter view at normal speed for the landing and roll-away.

Use two clean cuts at exactly 3s and 7s. Match the skater's position and motion phase across each cut. Carry wheel sound continuously; lower it naturally during slow motion and add no new music.

No impossible rotation, duplicate skater, crowd reaction, score graphics, brand marks, text, logo, or watermark.
```

> Alternate views are model-generated interpretations. Label them as reenactment or visualization if viewers might mistake them for recorded evidence.

<a id="case-04"></a>

## 04 | Turn a static process diagram into motion

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-04.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Image reference to video · **Input:** An original, rights-cleared diagram · **Goal:** Animate structure without inventing facts

```text
[# References <IMAGE_REF_0>@Image1]
Create a 10-second classroom motion graphic from Image1. Use Image1 as the exact information hierarchy, color key, and layout reference; do not treat it as a literal first frame. Topic: how rainwater moves through a simple urban bioswale.

[0-3s] Build the clean cross-section in layers: road, curb opening, planted soil, gravel, drain. Keep all component positions aligned to Image1.
[3-7s] Animate blue rainwater entering through the curb, slowing among plant stems, filtering downward, and reaching the underdrain. Flow direction must follow the diagram's arrows.
[7-10s] Hold the complete cross-section and reveal only these exact labels: "RUNOFF", "FILTER SOIL", "UNDERDRAIN".

Style: clear 2.5D educational graphic, restrained palette, large readable type, no decorative data.
Audio: rainfall, soft granular filtering texture, neutral original pulse. English narration spoken once: "A bioswale slows runoff and filters water through planted soil."
Do not add claims, percentages, extra labels, people, brand, logo, or watermark.
```

**Fact check:** Review domain-specific labels and causal claims with a qualified source before publishing.

<a id="case-05"></a>

## 05 | Use one image as an instruction board and another as identity

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-05.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Multiple image references · **Inputs:** Image1 = original four-step action board, Image2 = original robot reference · **Goal:** Separate action and identity roles

```text
[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]
Create a 10-second workshop demonstration. Use Image1 only for the four-step action order. Use Image2 only for the small repair robot's exact identity, materials, proportions, and tool-arm design. Neither image is a literal first frame.

The robot performs the four actions from Image1 in order: inspect a loose wooden drawer handle, stabilize the drawer, tighten exactly two screws, then test the handle once. Show continuous tool contact and believable resistance. One fixed waist-height camera with a gentle 10-degree arc; keep the whole drawer and both tool arms visible.

Audio: tiny motor movement, two distinct screwdriver bursts, wood creak, one quiet confirmation chime. No dialogue or music.
Preserve the robot from Image2 and the order from Image1. Do not copy notes, arrows, background, people, or text from either reference. No new tool, extra arm, brand, logo, or watermark.
```

<a id="case-06"></a>

## 06 | Word-by-word kinetic typography synchronized to speech

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-06.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Text-to-video · **Goal:** Exact short text and speech timing

```text
Create a 9:16, 10-second kinetic-type video on a deep navy background. Use one bold geometric sans-serif typeface, cream letters, and a single coral accent. Keep all text inside a 10% mobile safe area.

An adult narrator speaks this exact English sentence once: "Small steps make distant places reachable."

Reveal exactly one word per beat, synchronized to the spoken word:
[0.5s] "SMALL"
[1.7s] "STEPS"
[3.0s] "MAKE"
[4.0s] "DISTANT"
[5.6s] "PLACES"
[7.0s] "REACHABLE"

Each word enters through a simple physical motion related to meaning: SMALL scales from 90% to 100%; STEPS moves in two short increments; DISTANT begins farther back; REACHABLE joins the full sentence. From 8-10s, hold the exact complete sentence in title case: "Small steps make distant places reachable."

Audio: clear neutral English voice, one soft original percussive beat per word, no music bed.
No misspelling, repeated word, extra punctuation, subtitle track, icon, logo, or watermark.
```

<a id="case-07"></a>

## 07 | One title sequence, four language-safe variants

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-07.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Text-to-video master + one edit per locale · **Goal:** Multilingual exact-copy workflow

First create a text-free master:

```text
Create a 10-second 16:9 opening title background for a calm night-train travel series. View through a carriage window as soft rain trails diagonally across the glass and distant town lights pass from right to left. Keep the center-left area dark, stable, and uncluttered from 5s to 10s for later typography.

Audio: train rhythm, soft rain, one original warm synth chord. No speech, melody, text, signage, brand, logo, or watermark.
```

Then make one separate edit per language:

```text
Add only this exact English title from 5s to 10s: "WINDOWS AFTER MIDNIGHT". Center it in the reserved area, large, cream, fully readable. Keep everything else the same.
```

```text
Add only this exact Simplified Chinese title from 5s to 10s: "午夜之后的车窗". Preserve every character exactly. Center it in the reserved area, large, cream, fully readable. Keep everything else the same.
```

```text
Add only this exact Japanese title from 5s to 10s: "真夜中の車窓". Preserve every character exactly. Center it in the reserved area, large, cream, fully readable. Keep everything else the same.
```

```text
Add only this exact Arabic title from 5s to 10s, right-to-left: "نوافذ بعد منتصف الليل". Preserve joining, order, and punctuation exactly. Center it in the reserved area, large, cream, fully readable. Keep everything else the same.
```

**Review:** Approve spelling, glyph joining, safe area, reading time, and unintended background text with a native reader.

<a id="case-08"></a>

## 08 | Clay-table explainer: why tectonic plates move

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-08.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Text-to-video · **Goal:** Material science explainer with an accuracy boundary

```text
Create a 10-second handcrafted clay-table explainer showing a simplified cross-section of two tectonic plates above the upper mantle. Clearly present it as a conceptual model, not literal scale, speed, or material.

[0-3s] A cutaway globe segment opens onto two differently colored rigid clay plates. Exact small label: "TECTONIC PLATES".
[3-7s] Slow arrows in the softer layer below indicate broad mantle circulation while the plates move a few millimeters in the model. One plate meets the other and begins to descend at a subduction boundary. Exact label replaces the first: "SUBDUCTION ZONE".
[7-10s] Pull back to show a raised volcanic arc above the descending plate. Final exact note: "SIMPLIFIED MODEL — NOT TO SCALE".

Style: tactile stop motion, visible fingerprints, restrained earth colors, consistent cross-section geometry.
Audio: clay contact, low granular movement, original two-note educational cue. Calm narration spoken once: "Earth's rigid plates move slowly above a warmer, deformable mantle."
No fast catastrophic collision, city destruction, inaccurate hollow Earth, extra labels, logo, or watermark.
```

<a id="case-09"></a>

## 09 | Controlled A/B/C prompt evaluation

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/storyboard-text-evaluation-09.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**Mode:** Text-to-video benchmark · **Goal:** Compare prompt variables fairly

Use the same base prompt for three runs:

```text
Benchmark scene, 10 seconds, 16:9. One adult craftsperson wearing a plain olive apron places exactly three blue ceramic tiles onto a pale worktable from left to right, then aligns them with a wooden ruler and removes both hands from frame. Fixed camera at chest height, medium shot, soft daylight from frame left, plain gray wall.

Audio: three distinct ceramic contacts, ruler sliding on wood, quiet room tone. No speech or music.
Preserve one person, two hands, three tiles, tile color, action order, camera, table, lighting, and duration. No cuts, extra objects, text, brands, logo, or watermark.
```

Change only one line per variant:

```text
Variant A — Camera: completely locked tripod shot.
Variant B — Camera: 15-centimeter slow push-in from 2s to 8s.
Variant C — Camera: 20-degree slow arc from front-left to front-right from 2s to 8s.
```

Score each output from 0-2 on these six checks:

| Check | 0 | 1 | 2 |
|---|---|---|---|
| Object count | Not three | Temporarily wrong | Exactly three throughout |
| Action order | Wrong | Ambiguous | Correct and clear |
| Hands and contact | Broken | Minor artifact | Plausible throughout |
| Camera compliance | Wrong move | Approximate | Matches variant |
| Audio sync | Missing/wrong | Partial | Three contacts align |
| Exclusions | Major violation | Minor issue | None visible/audible |

Record model name, date, resolution, seed if exposed, prompt text, inputs, score, and observed failure. A single attractive output is not evidence that one variant is generally better.

## Planning and evaluation checklist

- Give a storyboard one reading order and one action per panel.
- Use only one source video for replay or alternate-view experiments.
- Keep split-screen cell count, borders, and settling order explicit.
- Quote every required word; forbid all other text.
- Create a text-free master before localizing, then edit one language per turn.
- Label generated alternate views and scientific simplifications honestly.
- Compare variants at the same aspect ratio, duration, resolution, and source inputs.
