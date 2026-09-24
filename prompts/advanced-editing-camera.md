# Advanced Editing, Camera, and Visual Transformation: 9 Original Prompts

[← Previous: Multimodal control, editing, and extension](control-editing-extension.md) · [English home](../README.md) · [中文主页](../README_ZH.md) · Next: [Storyboards, text, and evaluation →](storyboard-text-evaluation.md)

> Source: adapted from [Flaq AI](https://github.com/flaqai/awesome-gemini-omni-flash), under MIT. Prompts are practice briefs, not SeaImagine-verified results. Advanced controls depend on the selected interface.

These recipes focus on controlled changes to an existing generation or an uploaded, authorized clip. For an edit, make the requested change measurable and name the elements that must remain invariant. Camera-angle changes generate a new interpretation of the scene; they do not recover hidden pixels or establish forensic truth.

## 01 | Replace one prop without changing the performance

**Mode:** Edit · **Input:** An authorized clip containing one plain paper kite · **Goal:** Object replacement with contact continuity

Send this as the next turn after generating or uploading the source video:

```text
Replace only the white paper kite with a small mechanical manta-shaped glider made from matte blue fabric, thin bamboo ribs, and one brass tail weight.

The new glider must occupy the kite's original position and scale in every frame. Preserve the existing string attachment, the child's two-hand grip, string tension, wind response, shadows, camera path, timing, background, clothing, face, dialogue, ambience, and music exactly. The glider may flex in the same wind but must not flap like an animal.

No extra prop, glowing parts, text, logo, watermark, or changes to anything else.
```

**Acceptance check:** Compare the hand position, string path, and background landmarks before checking material detail. If the performance drifts, shorten the instruction to the replacement sentence plus the preserve sentence.

## 02 | Remove a foreground obstruction and reconstruct the scene

**Mode:** Edit · **Input:** A source clip with an unwanted freestanding sign · **Goal:** Removal and natural reconstruction

```text
Remove only the freestanding yellow sign in the lower-left foreground for the entire clip. Reconstruct the previously hidden pavement, curb edge, rain reflections, and passing shadows so they remain spatially and temporally consistent with the surrounding scene.

Preserve every person, vehicle, walking path, reflection outside the removed area, camera movement, focus pull, exposure, timing, dialogue, foley, ambience, and music exactly. Do not crop, reframe, blur, cover, or replace the sign with another object. Keep everything else the same.
```

**Repair turn if a visible patch remains:**

```text
Repair only the former sign area so the pavement texture and moving reflections continue naturally through it. Keep everything else the same.
```

## 03 | Move an existing scene into a reference environment

**Mode:** Stateful edit + image reference · **Inputs:** Previous video and an owned environment image · **Goal:** World replacement without identity drift

```text
[# References <IMAGE_REF_0>@Image1]
Change only the environment of the existing video to the glass-roofed winter garden shown in Image1. Use Image1 for architecture, materials, plant density, daylight direction, and color palette; do not use it as a literal first frame.

Keep the original adult subject, face, hair, clothing, body proportions, walking performance, screen position, timing, lens, camera path, and audio unchanged. Rebuild floor contact, occlusion, reflections, shadows, and room reverberation so the subject belongs naturally in the winter garden. Preserve the source clip's duration and edit rhythm.

Do not import people, signs, furniture, text, brands, or audio from Image1. No doorway morphing, floating feet, extra plants crossing the face, logo, or watermark.
```

**Tip:** Use an environment image with a camera height and perspective close to the source clip. Large perspective conflicts are more likely to change the performance.

## 04 | Isolate the subject while the world becomes animated line art

**Mode:** Edit · **Goal:** Selective style transformation

```text
Transform only the environment into hand-drawn charcoal line animation on warm off-white paper. Keep the cyclist and bicycle fully photorealistic and unchanged.

The line-art road, buildings, trees, shadows, and clouds must retain the original geometry, perspective, motion, occlusion order, and camera parallax. Use confident charcoal contours, sparse cross-hatching, and subtle paper grain; animated lines may breathe slightly but must not crawl across the cyclist. Preserve the original rider identity, clothing, bicycle construction, pedaling, wheel contact, camera path, timing, and all source audio.

No color in the line-art environment except the existing photorealistic subject. No sketch labels, page borders, added objects, text, logo, or watermark. Keep everything else the same.
```

**Acceptance check:** Inspect subject edges frame by frame around spokes, hair, and hands. A good result preserves occlusion rather than drawing the background over the subject.

## 05 | Re-camera as an over-the-shoulder shot

**Mode:** Edit / camera reinterpretation · **Input:** One source clip, 10 seconds or shorter · **Goal:** New viewpoint with the same event

```text
Recreate the same event as one continuous over-the-shoulder shot from behind the ceramic artist's right shoulder, at seated eye level, using a natural 50 mm lens perspective.

Keep the same adult artist, blue apron, clay bowl, wheel speed, exact hand sequence, studio layout, daylight, duration, dialogue, wheel sound, and room tone. The near shoulder may softly frame the lower-right edge but must never block the hands or bowl. Begin on both hands centering the clay, make a slow 20-centimeter push forward, and finish with the bowl centered and the artist's profile visible.

Do not invent objects that were not supported by the source scene. No cutaways, reverse shot, camera shake, altered action order, extra hands, text, logo, or watermark.
```

> This is a generated alternate view, not a recovered recording of an unseen camera. Use it for creative continuity, not evidence, measurement, or incident reconstruction.

## 06 | Close-up, tilt, and reveal in one controlled move

**Mode:** Text-to-video or image-to-video · **Goal:** Multi-stage camera direction

```text
Create a 10-second, 9:16 footwear film in one unbroken shot. An adult runner stands at the edge of an empty rain-darkened track before sunrise, wearing original unbranded slate-gray trail shoes and a saffron windbreaker.

[0-3s] Begin 20 centimeters above the ground in a tight three-quarter close-up of the left shoe. The runner tightens the laces once; droplets roll from the textured upper.
[3-7s] Tilt upward at a constant slow speed from shoe to knee to a waist-up profile while the runner rises. Keep vertical lines stable and maintain focus through the move.
[7-10s] Widen smoothly to a medium-full shot as the runner takes exactly two warm-up steps toward lane one, then stops in a ready stance.

Audio: lace friction, damp sole contact, distant city hum, one restrained original pulse beginning at 6s. No dialogue.
Preserve shoe construction, clothing, body proportions, track geometry, and left/right orientation. No cuts, speed ramp, brand marks, text, crowd, duplicate limbs, or watermark.
```

## 07 | Dive through an original poster into its world

**Mode:** Image-to-video · **Input:** An original poster or illustration · **Goal:** Continuous omnizoom-style transition

```text
[# Sources <FIRST_FRAME>@Image1]
Use Image1 as the exact first frame. Create a 10-second continuous forward camera journey into the original illustrated poster, with no cuts or dissolves.

[0-2s] Hold long enough to read the composition, then push toward the tiny painted greenhouse window near the poster center.
[2-6s] Pass through that window as flat ink and paper fibers gain depth continuously: brush marks become garden paths, painted leaves become dimensional foliage, and the printed moon becomes a real moonlit sky. Preserve the poster's teal, cream, and copper palette.
[6-10s] Continue along the same axis into the greenhouse, skim above wet leaves, and settle on a small glass terrarium containing one newly sprouted seed.

Audio begins as close paper texture and pencil movement, then opens into glass-room rain, leaves, and a soft original three-note motif. No dialogue.
No tunnel warp, sudden scene cut, copied franchise imagery, new text, logo, or watermark.
```

## 08 | Add a readable fictional AR maintenance overlay

**Mode:** Edit · **Goal:** Screen graphics anchored to moving machinery

```text
Add one fictional augmented-reality maintenance overlay around the existing water pump only. Use thin cyan vector lines with three stable callouts anchored to the correct moving parts.

Exact on-screen text, and no other text:
"FLOW 18 L/MIN"
"TEMP 42°C"
"STATUS STABLE"

The labels appear at 2s, remain fully readable inside the 10% safe area, track the pump without jitter, and fade out at 9s. The overlay must pass behind the technician's hands when they cross in front of the pump. Preserve the source pump, technician, tools, actions, camera, timing, lighting, dialogue, machinery sound, and room tone exactly.

No brand interface, warning alarm, changing numbers, extra diagram, face tracking, subtitles, logo, or watermark. Keep everything else the same.
```

**Localization variant:** Replace only the three quoted strings in a separate edit turn. Keep line lengths short and approve each language independently.

## 09 | Add motion-reactive light trails without changing physics

**Mode:** Edit · **Input:** An authorized roller-skating clip · **Goal:** Controlled motion effect

```text
Add one narrow amber light trail behind each roller skate for the entire clip. Each trail must originate at the rear wheel axle, follow the actual wheel path with a 0.35-second decay, respect floor perspective and occlusion, and become brighter only during faster movement.

Preserve the skater's identity, clothing, body motion, wheel contact, speed, floor reflections, camera movement, timing, and original audio exactly. The effect is emissive light only: it must not push the skater, change the trajectory, create sparks, illuminate the face, or leave permanent marks on the floor.

No trails from hands or body, no particles, flame, smoke, brand marks, text, logo, watermark, or changes to anything else.
```

**Why it works:** The effect has a precise origin, decay time, occlusion rule, and non-effect list. Those are easier to verify than a broad request such as “make it more futuristic.”

## Editing checklist

- Use one source video per edit decision; the API does not support cross-video reasoning.
- Treat a changed camera angle as a creative regeneration, not hidden-scene recovery.
- Make one primary change per turn and name only the invariants that matter.
- For reference images, assign one explicit role and exclude unwanted people, text, and brands.
- Verify contact, occlusion, reflections, shadows, and audio continuity before surface style.
- Keep uploaded edit clips within the current API limits documented in the [official Gemini Omni guide](https://ai.google.dev/gemini-api/docs/omni).
