# Reference Videos for Gemini Omni 1.1 Flash

[← English home](../README.md) · [中文主页](../README_ZH.md) · [Prompting guide](prompting-guide.md) · [API quickstart](api-quickstart.md)

This page separates **videos to watch for capability study** from **videos that may be reused as model inputs**. A public web page is not automatically a reusable media license. This repository links to original source pages and does not mirror third-party video files.

[Four specific official videos and six community studies →](community-examples.md)

## 1. Official demos to watch

Use these pages to study shot design, editing behavior, reference roles, text synchronization, first/last-frame transitions, and extension. They are official product demonstrations—not a blanket license to download, repost, train on, or use the clips as commercial input.

| Official page | Useful demonstrations | How to use it here |
|---|---|---|
| [Google DeepMind: Gemini Omni](https://deepmind.google/models/gemini-omni/) | Conversational edits, references, physics, text timing, interpolation, extension, video references, and resolution examples | Watch a clip, identify one control variable, then test an original scene from this repository |
| [Google DeepMind: Introducing Gemini Omni](https://deepmind.google/blog/introducing-gemini-omni/) | Product overview and selected video examples | Study capability framing; verify API availability separately |
| [Google AI: Generate and edit video with Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni) | Current request formats, media-role tags, editing, extension, limits, and code examples | Treat this as the source of truth for API behavior |
| [Gemini Omni Flash model card](https://deepmind.google/models/model-cards/gemini-omni-flash/) | Evaluation context, intended use, safety, and limitations | Read before publishing claims or designing an evaluation |

Official showcase pages may demonstrate broader product behavior than the currently documented API. If they differ, follow the current API documentation for implementation.

## 2. Reference clips with clearer reuse paths

Always open the source page, confirm the item-level credit and license immediately before use, and keep a copy of that record with your project. Rights can differ by item, territory, person, logo, music, or third-party contribution.

| Source | Example or catalog | Reuse status | Required action |
|---|---|---|---|
| Your own or commissioned footage | A 3-second hand movement, camera arc, product turntable, or texture plate | Best default when the recording agreement covers generative editing | Keep releases, contributor consent, and the unedited source |
| Wikimedia Commons | [Arrival of a Train at La Ciotat (1895)](https://commons.wikimedia.org/wiki/File:Arrival_of_a_Train_at_La_Ciotat_(The_Lumi%C3%A8re_Brothers,_1895).webm) | The item page marks this file public domain; status can vary by jurisdiction | Record the item page, author, date, and public-domain statement; do not imply endorsement |
| Blender Studio | [Open Movies catalog](https://studio.blender.org/films/) and [remixing guidance](https://studio.blender.org/remixing/) | Studio content is generally CC BY, but each asset can carry its own license and exclusions | Check the exact film or asset, give required attribution, and avoid excluded logos, title designs, personality rights, or separately licensed music |
| NASA | [Image and Video Library](https://images.nasa.gov/) and [media usage guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/) | NASA content is generally available for factual educational or informational use in the US, with important exceptions | Credit NASA, check for third-party notices and identifiable people, avoid protected insignia and endorsement, and follow the current AI/media rules |

### Do not use by default

- Commercial films, television, music videos, sports broadcasts, social posts, or news footage without explicit permission.
- A clip merely because it is embeddable, downloadable, old, or visible on a public site.
- Footage of a real person for identity, voice, or behavior transformation without informed permission.
- Watermarked footage, protected characters, recognizable brand campaigns, or a living artist's signature style.
- Media with uncertain music rights. Reference-video audio is ignored by the current API, but distributing the source may still infringe rights.

## 3. Prepare clips for the current API

| Intended role | Preparation | Prompt declaration |
|---|---|---|
| Edit source | Use one authorized video, generally 10 seconds or shorter; keep the action and camera readable | Describe one change and end with the important invariants |
| Video reference | Up to three short references are currently documented, each up to 3 seconds; give each one role | `<VIDEO_REF_0>` is movement only; `<VIDEO_REF_1>` is camera path only |
| Extension source | Use an eligible clip, generally 10 seconds or shorter; extension adds to the tail | State continue vs cut and define visual and audio continuity |
| Evaluation source | Use the exact same file for every variant | Record model, date, resolution, inputs, prompt, and observed result |

Current API cautions:

- Audio inside video references is ignored; do not ask the model to copy it.
- A separately uploaded audio reference is not supported.
- Cross-video reasoning is not supported. Multiple reference clips can have separate guidance roles, but do not ask for factual comparison or event reconstruction across them.
- YouTube URLs are not supported media sources in the documented API.
- A new camera angle is a generated interpretation, not recovered footage.
- Regional restrictions and safety filtering may apply to people, minors, and video editing.

Verify details in the [current official guide](https://ai.google.dev/gemini-api/docs/omni) before production.

## 4. Four original clip-study recipes

These adaptation starters are not included in the repository's 60-prompt count. Use only footage you are allowed to process.

### A. Public-domain train: material restoration study

Use a short crop from the public-domain train clip linked above, keeping its provenance with the test.

```text
Restore only physical film damage: reduce large dust spots, vertical scratches, gate weave, and unstable exposure while preserving the source framing, timing, train movement, platform geography, people, period clothing, grain character, and silent-film cadence.

Do not colorize, sharpen faces into new identities, add frames that change action, invent signage, add audio, crop, reframe, add a logo, or present the result as an untouched historical record. Keep everything else the same.
```

Label the result as an AI-assisted restoration experiment.

### B. Owned movement clip: identity-separated motion reference

```text
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]
Use Image1 only for the original character's identity and plain rehearsal clothing. Use the owned 3-second Video1 only for the timing and weight shift of the two-step movement; ignore its person, room, camera, and audio.

Create a 10-second fixed full-body rehearsal shot in an empty pale-green studio. The character performs the referenced two-step movement once, adds one original recovery turn, and returns to the opening mark. Preserve floor contact and left/right orientation.

Audio: original hand percussion aligned to steps, shoe contact, natural room reverb. No dialogue. No copied background, audio, brand, text, logo, or watermark.
```

### C. Owned camera move: transfer only the path

```text
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]
Use Image1 only for the original tabletop product and set design. Use Video1 only for its smooth camera path: a low 25-degree clockwise arc followed by a short forward settle. Do not copy Video1's subject, background, lighting, people, or audio.

Create a 10-second unbranded product film that applies that camera path once at constant speed. Keep the product's geometry, materials, part count, label-free surfaces, and table contact unchanged. Add subtle environment motion only: one soft window-light reflection moves across the surface.

Audio: quiet room tone and one original soft tonal rise. No dialogue, text, logo, or watermark.
```

### D. Licensed open animation: line-art analysis

Choose a short, license-verified clip from the Blender Open Movies catalog and retain the required attribution outside the generated frame.

```text
Convert only the selected environment into sparse monochrome construction-line animation while preserving the source subject, action order, camera, timing, and occlusion. Use consistent perspective guides, light pencil grain, and no decorative color.

Do not imitate a named artist, remove required external attribution, add new characters, alter identity, reproduce title graphics, copy audio, add text, logo, or watermark. Keep everything else the same.
```

## 5. Provenance record template

```text
Asset title:
Canonical source page:
Creator / institution:
Item-level license or usage policy:
Date checked:
Allowed purpose:
Attribution required:
People / voice / trademark / music restrictions:
Local filename and checksum:
Trim used (time in / time out):
Model and interaction ID:
Edits requested:
Output disclosure:
Reviewer:
```

This record is production hygiene, not legal advice. When rights or commercial use are unclear, replace the clip with original footage or obtain permission.
