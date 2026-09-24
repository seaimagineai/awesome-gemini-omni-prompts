<div align="center">

![Gemini Omni prompt library cover](assets/seaimagine-omni-hero.png)

# Awesome Gemini Omni Prompts

**Explore 60 complete source recipes in seven categories. Learn how to describe a scene, time its actions, direct the camera and shape the sound, then adapt an example to your own idea.**

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)

[العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [All 15 languages](docs/multilingual-guide.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-6f42c1.svg)](LICENSE)
[![Prompt recipes](https://img.shields.io/badge/prompt_recipes-60-00b8d9.svg)](#complete-prompt-library)
[![Languages](https://img.shields.io/badge/localization_guides-15-ff8a00.svg)](docs/multilingual-guide.md)
[![Model](https://img.shields.io/badge/model-gemini--omni--1.1--flash-4285f4.svg)](https://ai.google.dev/gemini-api/docs/omni)

[Browse 60 prompts](#complete-prompt-library) · [Find a prompt in one minute](#find-the-right-prompt-in-one-minute) · [Complete examples](#source-examples) · [Official and community examples](#video-studies) · [Localization guide](docs/multilingual-guide.md)

</div>

## Share your Gemini Omni prompt

Built a shot that another creator or developer can reproduce? Use the [guided submission form](https://github.com/seaimagineai/awesome-gemini-omni-prompts/issues/new?template=prompt-submission.yml) to share one original, tested prompt with its mode, input roles, aspect ratio, resolution, observed result, known problems, and iteration notes.

We especially welcome multilingual dialogue, real business workflows, accessibility-focused content, controlled local edits, first/last-frame experiments, honest failure reports, and original reference media that can legally be redistributed. Do not submit copied collections, unauthorized likenesses, branded media, protected characters, secrets, private data, undisclosed affiliate links, or unsupported capability claims. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full review checklist.

## Find the right prompt in one minute

| Your starting point or goal | Start here |
|---|---|
| A concept, script, atmosphere, or story beat | [Cinematic storytelling](prompts/cinematic-storytelling.md) |
| A product image, store, outfit, ad, or commercial goal | [Commerce and social media](prompts/commerce-social.md) |
| Travel, nature, history, science, education, or architecture | [Documentary, travel, and education](prompts/documentary-education.md) |
| Animation, music, dance, comedy, or a seamless loop | [Stylized entertainment](prompts/stylized-entertainment.md) |
| A first frame, last frame, character image, short reference clip, or video to edit | [Multimodal control, editing, and extension](prompts/control-editing-extension.md) |
| Object replacement, environment swap, re-camera, stylization, AR overlays, or effects | [Advanced editing, camera, and visual transformation](prompts/advanced-editing-camera.md) |
| A 3×3 storyboard, split screen, diagram, kinetic type, multilingual title, or benchmark | [Storyboards, text, and evaluation](prompts/storyboard-text-evaluation.md) |
| Official demos or reusable, license-aware source clips | [Reference video guide](docs/reference-videos.md) |
| Chinese, Japanese, Korean, Arabic, French, or another localized version | [15-language localization guide](docs/multilingual-guide.md) |
| Identity drift, broken text, crowded audio, or unstable continuity | [Failure diagnosis](docs/prompting-guide.md#11-失败诊断) |
| Python or JavaScript integration | [Gemini API quickstart](docs/api-quickstart.md) |

## What is included

- **60 complete recipes, not one-line prompt fragments.** Each covers mode, input roles, scene, timing, camera, audio, invariants, exclusions, or evaluation.
- **3 new illustrated practice briefs.** Ceramic-cup product motion, paper-harbor lighting, and a vertical linen-pouch clip with captions added in editing.
- **7 practical collections.** Storytelling, commerce, education, entertainment, multimodal control, advanced editing/camera, and storyboards/text/evaluation.
- **30+ production directions.** Film, action, products, UGC, travel, science, animation, local edits, environment replacement, camera reinterpretation, split screens, storyboards, kinetic type, localization, and controlled benchmarks.
- **Localization guidance for 15 languages.** Dialogue locking, exact text, RTL direction, line length, native review, and per-locale acceptance tests.
- **6 ready-to-use reference images:** 3 newly created practice inputs and 3 retained source-library inputs, plus a separate editorial cover. Reference images are inputs, not video outputs.
- **API and debugging guidance.** From 360p drafts and media-role tags to high-resolution delivery and interaction records.
- **License-aware video references.** Official demos are separated from public-domain, CC BY, institutional, and owned footage, with a provenance template.

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

[Read the complete prompt-design method →](docs/prompting-guide.md)

<!-- generated:library:start -->
## Try your first prompt

1. Choose a complete example that matches your scene and copy the full prompt.
2. Download its reference image and, in your chosen tool, assign it as the first frame if that option is available.
3. Adjust the timeline to the available duration and resolution. Make a draft, check the subject, text and sound, then change one thing at a time.
<!-- generated:library:end -->

<a id="source-examples"></a>

## Three complete prompts from the source library

### 01 | Unbranded outdoor speaker: water-beat product film

![Original unbranded speaker first frame](assets/product-speaker.png)

```text
[# Sources <FIRST_FRAME>@Image1]
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

[Browse all 8 commerce and social prompts →](prompts/commerce-social.md)

### 02 | Volcanic ridge: travel-documentary opener

![Original volcanic ridge cyclist first frame](assets/travel-cyclist.png)

```text
[# Sources <FIRST_FRAME>@Image1]
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

[Browse all 8 documentary, travel, and education prompts →](prompts/documentary-education.md)

### 03 | Clock-tower paper birds: illustrated animation

![Original clockmaker animation first frame](assets/clockmaker-story.png)

```text
[# Sources <FIRST_FRAME>@Image1]
Bring this original illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

[Browse all 8 stylized entertainment prompts →](prompts/stylized-entertainment.md)

## Complete prompt library

| Collection | Scenarios | Count | Core capabilities |
|---|---|---:|---|
| [Cinematic storytelling](prompts/cinematic-storytelling.md) | Reunion, chase, historical craft, suspense, seasons, noir, comedy, sci-fi | 8 | Text-to-video, dialogue, timeline, continuous camera |
| [Commerce and social media](prompts/commerce-social.md) | Product, skincare, café UGC, fashion, food, property, app, ecommerce localization | 8 | Image-to-video, references, vertical format, text |
| [Documentary, travel, and education](prompts/documentary-education.md) | Travel, geology, nature, reconstruction, science, museums, language, architecture | 8 | World knowledge, narration, labels, grounded physics |
| [Stylized entertainment](prompts/stylized-entertainment.md) | Illustration, 2D action, clay, meme comedy, jazz, dance, paper craft, loops | 8 | Stylization, native audio, one-takes, first/last frame |
| [Multimodal control, editing, and extension](prompts/control-editing-extension.md) | Character/prop roles, first/last frames, motion reference, add/remove, localization, 40-second chain | 10 | Media tags, edit, extend, multi-turn interaction |
| [Advanced editing, camera, and visual transformation](prompts/advanced-editing-camera.md) | Replace/remove, environment swap, style isolation, re-camera, tilt/reveal, poster dive, AR, light trails | 9 | Local edits, invariants, generated viewpoints, occlusion |
| [Storyboards, split screens, text, and evaluation](prompts/storyboard-text-evaluation.md) | 3×3 storyboard, nine-window grid, action replay, diagram, role boards, kinetic type, localization, science, A/B/C test | 9 | Planning inputs, exact text, multilingual variants, evaluation |

Total: **60 complete recipes retained from the attributed source library**. Image provenance and generation briefs are recorded in [Visual Assets](assets/README.md). The five original collection introductions are in Simplified Chinese; the two advanced collections and every copy-ready control prompt are in English. See the [reference video guide](docs/reference-videos.md) for official demonstrations, reuse-aware source catalogs, four clip-study starters, and a provenance record.

## 15-language localization

| Language group | Entry points |
|---|---|
| East Asia | [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) |
| Western Europe and the Americas | [English](README.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) |
| Additional locales | [العربية](README_AR.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) |

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

The [multilingual video guide](docs/multilingual-guide.md) covers locale codes, writing direction, type length, speech and subtitle rules, shared test scenes, a 15-language comparison phrase, native-speaker review, and acceptance checks.

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

The repository is released under the [MIT License](LICENSE). Generated output can still involve separate rights for source media, people, voices, music, trademarks, locations, claims, and the model or platform used.

## Known limitations and honest use

- English is the fully evaluated language; speech, text, and lip sync in other languages require per-version review.
- The current Gemini API does not support separate uploaded audio references; audio in a reference video is ignored.
- Uploaded videos for editing or extension generally need to be 10 seconds or shorter; extension appends only at the end.
- Voice editing is unsupported, and uploaded videos with speech cannot be extended with additional dialogue.
- YouTube media sources, cross-video reasoning, and a separate negative-prompt parameter are unsupported.
- Upscaled 1080p and 4K cannot repair bad composition, text, physics, or timing.
- People, minors, and uploaded-video editing can be restricted by region and safety policy.

## Contributing and sources

Original scenarios, careful localizations, accessibility improvements, reproducible media, and honest failure reports are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) or use the [guided prompt-submission form](https://github.com/seaimagineai/awesome-gemini-omni-prompts/issues/new?template=prompt-submission.yml).

Capability sources:

- [Google AI: Generate and edit videos with Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni)
- [Google DeepMind: official Gemini Omni demos](https://deepmind.google/models/gemini-omni/)
- [Google DeepMind: Gemini Omni Flash model card](https://deepmind.google/models/model-cards/gemini-omni-flash/)

For source clips and reuse conditions, use the [reference video and licensing guide](docs/reference-videos.md). It links rather than rehosts third-party media.

Review copyright, likeness, trademark, audio, advertising claims, safety policy, and platform terms before commercial release.

<!-- generated:studies:start -->
<a id="video-studies"></a>

## What to learn from official and community examples

Google’s official videos demonstrate Omni 1.1 Flash. The community posts are from May 2026 and concern the original Omni / Flash; they are not verified 1.1 tests. Community evidence comes from the FxTwitter mirror’s text and media metadata; native playback on X has not been verified. These are external examples, not results from the platform you choose to use. Check which features your tool offers.

### Google: first-to-last-frame transition

[View the source example](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Set the starting image, ending image and the continuous movement between them separately.

Prepare two photos of the same object from compatible angles. If first/last-frame controls are available, connect them with one simple movement.

### Google: extend a shot

[View the source example](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Describe the next camera move while preserving the subject and the direction of motion.

Use your own short clip. If extension is available, request one continuation and inspect the join for jumps in motion or lighting.

### CHRIS FIRST: people become flamingos

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: people become flamingos" width="300"></a>

[View the source example](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

Change the subject while explicitly preserving clothing and action; inspect limb contacts.

With your own footage and an available video editor, replace one subject. Compare clothing, pose and contact with the ground before and after.

### Justine Moore: change hats on each clap

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: change hats on each clap" width="300"></a>

[View the source example](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

Use a visible gesture to time each change while keeping the face, outfit and camera consistent.

Film two clear claps with a fixed camera. If video editing is available, request a hat change at each clap and check the timing frame by frame.

[Official and community examples](docs/community-examples.md)
<!-- generated:studies:end -->

<a id="brand-tools"></a>

## Create with SeaImagine

[SeaImagine](https://seaimagine.com/) brings image and video creation into a browser workflow. Start with the task you have, then choose the model and settings actually offered in the editor.

| Your task | SeaImagine entry | What to do next |
|---|---|---|
| Explore the Gemini Omni family | [Gemini Omni](https://seaimagine.com/model/gemini-omni/) | Read the model overview, then check the editor |
| Plan an Omni 1.1 Flash shot | [Gemini Omni 1.1 Flash](https://seaimagine.com/model/gemini-omni-1-1-flash/) | Check the exact model and available input controls |
| Animate a product or illustration | [Image to video](https://seaimagine.com/image-to-video/) | Upload a permitted first frame and describe movement |
| Start from an idea | [Text to video](https://seaimagine.com/text-to-video/) | Paste one complete recipe and set the available format |
| Prepare a coherent first frame | [AI image generator](https://seaimagine.com/ai-image-generator/) | Make the subject, framing, and background readable first |
| Continue everyday image/video work | [Create workspace](https://seaimagine.com/create/) | Compare currently listed options for your input type |

These are durable task-based entry points, not a promise of continuous model availability. Public pages were checked on **2026-09-24**; no paid generation, uptime study, or end-to-end output test was performed. Check credits, duration, resolution, and model availability in your account. Google API features described in this guide are not automatically SeaImagine editor features.

[Step-by-step SeaImagine guide and three additional practice briefs →](docs/seaimagine-workflow.md)

## Start in SeaImagine

1. Pick a prompt below. For image-to-video, open its image and save the original file.
2. Open [Gemini Omni 1.1 Flash](https://seaimagine.com/model/gemini-omni-1-1-flash/) or the [creation workspace](https://seaimagine.com/create/). Check the selected model and available mode.
3. Upload the image as the first frame **if the editor provides that control**. Paste the matching prompt. The `<FIRST_FRAME>` notation explains an input role; it does not attach a file by itself.
4. Select the available duration and aspect ratio in the interface. If 10 seconds is unavailable, shorten the timeline to fit; use the lowest available draft resolution first.
5. Check subject consistency, motion, text, and sound. Change one instruction at a time. See [troubleshooting and browser/API differences](docs/seaimagine-workflow.md).

<!-- generated:brand:start -->
<a id="sea-practice"></a>

## Three SeaImagine exercises with original reference images

These AI-generated reference images are starting frames for practice, not tested Gemini video outputs. Use only the controls available in your SeaImagine interface.

### SEA-01 · A quiet morning with a teal ceramic cup

[![A quiet morning with a teal ceramic cup](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

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

[![A paper harbor lights up](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

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

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="A linen pouch for a multilingual shop" width="360"></a>

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
<!-- generated:brand:end -->

> [!NOTE]
> Adapted from [Flaq AI’s prompt library](https://github.com/flaqai/awesome-gemini-omni-flash), with attribution and the original MIT notice retained. The reference images are first-frame inputs, not generated-video results. New SeaImagine guidance and a new cover are identified in [Sources & assets](docs/sources.md). Recipes are starting points, not a tested-output guarantee.

## License and disclaimer

Code and documentation are released under the [MIT License](LICENSE). This is an independent community project, not an official Google product or endorsement. Gemini, SeaImagine, Flaq AI, and other product names belong to their respective owners.

If this library saves you one unnecessary high-resolution render, consider starring the repository and sharing a real test result.
