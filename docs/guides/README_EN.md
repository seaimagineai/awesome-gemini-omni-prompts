# Gemini Omni — Further reading

[Index of all 60 prompts](../../README.md)

## Gemini Omni 1.1 Flash capability map

This section describes Google’s model/API documentation; confirm each feature in your selected interface before planning a production workflow.

Gemini Omni 1.1 Flash is a high-performance multimodal model for fast video generation, editing, and cinematic control. It can reason over text, image, and video context, generate video with audio, and use the Interactions API for conversational revisions and extensions.

| Capability | Best use cases | Prompt priority |
|---|---|---|
| Text → video with audio | Concepts, narrative, ads, social clips | Scene, action, camera, lighting, audio, timing |
| Image → video | Products, photos, illustrations | Declare first frame vs reference; separate subject, camera, and environment motion |
| First + last frame | Transitions, transformations, seasons, loops | Lock geometry, explain the continuous change, reserve a stable end frame |
| Multiple image references | Character, wardrobe, prop, and art-direction combinations | Give each `<IMAGE_REF_N>` exactly one responsibility |
| Video reference | Motion, subject, or camera-path guidance | Use `<VIDEO_REF_N>`; say it is not an edit source and ignore reference audio |
| Conversational editing | Lighting, object add/remove, style, text | Change one thing per turn; add `Keep everything else the same.` |
| Tail extension | Longer stories, character entrances, music sections | State continue vs cut and define both visual and audio continuity |
| Readable text | Signs, title cards, packaging, motion typography | Quote exact copy; specify language, placement, timing, and exclusivity |

The official API currently documents 360p, 720p (default), upscaled 1080p, and upscaled 4K output, with 16:9 and 9:16 aspect ratios. Generated video contains invisible SynthID. English is the only language reported as fully evaluated, so this project uses an English control layer plus exact target-language dialogue or text. Capabilities, regions, and parameters can change; verify them in the [Google AI Omni documentation](https://ai.google.dev/gemini-api/docs/omni) and the [Gemini Omni Flash model card](https://deepmind.google/models/model-cards/gemini-omni-flash/).

## A strong prompt reads like a directing brief

```text
[Mode] Text-to-video / Image-to-video / Reference-to-video / Edit / Extend
[Goal] Audience, emotion, use, duration, aspect ratio
[Reference roles] Image 1 is the first frame; Image 2 locks identity; Video 1 provides motion only
[Visual anchors] Subject, wardrobe, product geometry, set, time, palette
[Timeline] Setup → action → change → deliberate final frame
[Camera] Shot size, height, path, speed, focus, stopping point
[Performance and physics] Gaze, hands, weight, inertia, contact, cloth, water
[Audio] Dialogue, ambience, foley, original music, synchronization cues, silence
[Continuity] What must never change
[Avoid] Morphing, duplicates, extra limbs, fake text, logos, watermarks
```

### Copy-ready 10-second scaffold

```text
Format: 9:16 vertical video, 10 seconds.
Goal: [audience + intended response]

Scene: [place, time, weather, spatial relationships]
Subject: [3-5 stable identity anchors]
Subject motion: [ordered physical action]
Camera motion: [height, shot size, path, speed, focus]
Environment motion: [wind, light, water, particles, crowd]

[0-3s] [hook and spatial setup]
[3-7s] [core action and escalation]
[7-10s] [payoff and deliberate final frame]

Look: [medium, lighting, palette, materials]
Audio: [foreground foley, ambience, music entry/exit, silence]
Exact dialogue in [language], spoken once: "[verbatim line]"
Exact on-screen text in [language]: "[verbatim copy]"
Preserve: [identity, product, layout, motion, audio]
Do not include: [short concrete list]
```

[Read the complete prompt-design method →](../../docs/prompting-guide.md)


## 15-language localization

| Language group | Entry points |
|---|---|
| East Asia | [简体中文](../../README_ZH.md) · [繁體中文](../../README_ZH-TW.md) · [日本語](../../README_JA.md) · [한국어](../../README_KO.md) |
| Western Europe and the Americas | [English](../../README.md) · [Español](../../README_ES.md) · [Français](../../README_FR.md) · [Deutsch](../../README_DE.md) · [Português](../../README_PT.md) · [Italiano](../../README_IT.md) |
| Additional locales | [العربية](../../README_AR.md) · [Русский](../../README_RU.md) · [Bahasa Indonesia](../../README_ID.md) · [ไทย](../../README_TH.md) · [Tiếng Việt](../../README_VI.md) |

### Localization is not a full-prompt translation

For more stable results, keep camera and continuity instructions in English and lock only the target-language content:

```text
Spoken language: Japanese.
Exact dialogue at 6s, spoken once with natural conversational pacing: "今日は、遠回りして帰ろう。"
Do not translate, paraphrase, repeat or subtitle it.

On-screen language: Spanish.
Exact title, centered and fully readable from 7s to 10s: "PEQUEÑOS VIAJES"
Preserve accents and spelling exactly. No other text anywhere.
```

The [multilingual video guide](../../docs/multilingual-guide.md) covers locale codes, writing direction, type length, speech and subtitle rules, shared test scenes, a 15-language comparison phrase, native-speaker review, and acceptance checks.

## Image-to-video checklist

- Lock identity, wardrobe, product geometry, object count, composition, and key-light direction.
- Separate subject motion, environment motion, and camera motion.
- Give each reference file one job; avoid “use everything from every reference.”
- Define the camera's start, path, speed, focus, and final stopping point.
- Reserve the final 2–3 seconds for deceleration and a deliberate end frame.
- Treat dialogue, ambience, foley, and music as separate audio layers.
- Use only original or properly licensed people, voices, products, and visual assets.

## Gemini Omni 1.1 Flash FAQ

### Should I use text-to-video or image-to-video?

Use text-to-video to explore concepts, scripts, or atmosphere. Use image-to-video or references when a person, product, illustration, composition, first frame, or last frame must remain recognizable. Validate the most important anchor before adding elaborate effects.

### How do I reduce character or product drift?

Choose one primary identity or product anchor, list its invariant properties before motion, and give every additional reference only one role: wardrobe, prop, style, or movement. Explicitly reject redesign, part-count changes, label drift, and identity drift.

### Can I write the full prompt in Chinese or another language?

You can experiment, but English is the only officially fully evaluated language. For production, keep shot, movement, and continuity control in English; lock dialogue and on-screen text verbatim in the target language; then review each locale at the lowest suitable resolution offered in your selected interface. Google API examples include 360p; do not assume that the selected tool exposes it.

### Why should editing prompts be short?

Restating the full source video can cause unrelated details to regenerate. Use one change plus invariants, for example: `Change only the jacket to dark green. Keep everything else the same.`

### Are these prompts free to use?

The repository is released under the [MIT License](../../LICENSE). Generated output can still involve separate rights for source media, people, voices, music, trademarks, locations, claims, and the model or platform used.

## Known limitations and honest use

- English is the fully evaluated language; speech, text, and lip sync in other languages require per-version review.
- The current Gemini API does not support separate uploaded audio references; audio in a reference video is ignored.
- Uploaded videos for editing or extension generally need to be 10 seconds or shorter; extension appends only at the end.
- Voice editing is unsupported, and uploaded videos with speech cannot be extended with additional dialogue.
- YouTube media sources, cross-video reasoning, and a separate negative-prompt parameter are unsupported.
- Upscaled 1080p and 4K cannot repair bad composition, text, physics, or timing.
- People, minors, and uploaded-video editing can be restricted by region and safety policy.

## Contributing and sources

Original scenarios, careful localizations, accessibility improvements, reproducible media, and honest failure reports are welcome. Read [CONTRIBUTING.md](../../CONTRIBUTING.md) or use the [guided prompt-submission form](https://github.com/seaimagineai/awesome-gemini-omni-prompts/issues/new?template=prompt-submission.yml).

Capability sources:

- [Google AI: Generate and edit videos with Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni)
- [Google DeepMind: official Gemini Omni demos](https://deepmind.google/models/gemini-omni/)
- [Google DeepMind: Gemini Omni Flash model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)

For source clips and reuse conditions, use the [reference video and licensing guide](../../docs/reference-videos.md). It links rather than rehosts third-party media.

Review copyright, likeness, trademark, audio, advertising claims, safety policy, and platform terms before commercial release.


## Earlier source examples

![Source reference](../../assets/product-speaker.png)

```text
[# Sources <FIRST_FRAME>@Image1]
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

![Source reference](../../assets/travel-cyclist.png)

```text
[# Sources <FIRST_FRAME>@Image1]
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

![Source reference](../../assets/clockmaker-story.png)

```text
[# Sources <FIRST_FRAME>@Image1]
Bring this original illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

<a id="sea-practice"></a>

## Three SeaImagine exercises with original reference images

These AI-generated reference images are starting frames for practice, not tested Gemini video outputs. Use only the controls available in your SeaImagine interface.

### SEA-01 · A quiet morning with a teal ceramic cup

[![A quiet morning with a teal ceramic cup](../../assets/seaimagine-ceramic-cup.png)](../../assets/seaimagine-ceramic-cup.png)

Keep the handle, rim and liquid level consistent while the camera slowly moves closer. Leave space for a final caption.

Upload the cup image for image-to-video. Try one slow push-in; check the handle and liquid level before adding your caption.

[Image to video](https://seaimagine.com/image-to-video/) · [AI image generator](https://seaimagine.com/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · A paper harbor lights up

[![A paper harbor lights up](../../assets/seaimagine-paper-harbor.png)](../../assets/seaimagine-paper-harbor.png)

In a single shot, light the lighthouse, then brighten the windows of the three houses one by one. Preserve paper texture and geometry.

Upload the harbor image for image-to-video. Request the lighthouse light and sequentially brighter windows; compare the buildings at the beginning and end.

[Image to video](https://seaimagine.com/image-to-video/) · [AI image generator](https://seaimagine.com/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · A linen pouch for a multilingual shop

<a href="../../assets/seaimagine-linen-pouch.png"><img src="../../assets/seaimagine-linen-pouch.png" alt="A linen pouch for a multilingual shop" width="360"></a>

Make a clean vertical product clip without lettering, then add local-language captions in a regular video editor.

Upload the pouch image and request a vertical clip. Add translated captions afterward; use a short video-editing instruction only if that feature is available.

[Image to video](https://seaimagine.com/image-to-video/) · [AI image generator](https://seaimagine.com/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> Everyday, made simple
