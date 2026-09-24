# Create a video with SeaImagine

[Home](../README.md) · [中文主页](../README_ZH.md) · [60 recipes](../README.md#complete-prompt-library) · [Official and community examples](community-examples.md)

This guide is for creators who want to work in a browser. No API key is needed to read or copy the prompts. SeaImagine may require an account and credits to generate; check the selected model and price before starting.

## Choose an entry by the input you have

| You have | Open | First decision |
|---|---|---|
| A script or idea | [Text to video](https://seaimagine.com/text-to-video/) | Choose a model and one clear action |
| A product photo, illustration, or first frame | [Image to video](https://seaimagine.com/image-to-video/) | Upload an image you can use and specify motion |
| No usable reference image yet | [AI image generator](https://seaimagine.com/ai-image-generator/) | Create the composition before animating it |
| An Omni-specific workflow | [Omni overview](https://seaimagine.com/model/gemini-omni/) / [Omni 1.1 Flash](https://seaimagine.com/model/gemini-omni-1-1-flash/) | Confirm which exact model and controls are offered |
| An ongoing project | [Create](https://seaimagine.com/create/) | Reopen the available image/video workspace |

These task pages are useful alternatives when planning a project across models. They were publicly reachable on 2026-09-24. We have not established long-term uptime or tested a paid generation, so “available page” must not be read as “guaranteed working generation.” A substitute model can require a different prompt or input format.

## Your first shot

1. Save [the speaker reference image](../assets/product-speaker.png). This image was inherited from the attributed Flaq AI library, not produced by an Omni video run.
2. Open the image-to-video entry. Select the model shown in your account. Upload the reference using the available first-frame/image input.
3. Copy the complete [speaker recipe](../prompts/commerce-social.md#01户外音箱水滴节拍广告). If the editor has no special tag field, use ordinary language: “Use the uploaded image as the first frame.” A tag in the prompt cannot upload or bind a missing file.
4. Match the prompt to the duration, aspect ratio, and resolution actually offered. The library’s 10-second timeline is a creative brief, not a control override. If only a shorter clip is available, reduce the action and keep a final hold.
5. Generate a draft using the lowest suitable available resolution. Check the grille, silhouette, number of objects, camera path, and audio before spending credits on a final version.
6. Keep the input file, prompt, selected model/version, date, settings, and result together. For the next attempt, change one variable.

## Google model, Google API, and SeaImagine editor

| Layer | What the repository can establish | What it does not establish |
|---|---|---|
| Google official showcases | Published model examples and illustrated techniques | That every public app exposes those controls |
| Google Gemini API documentation | Current documented request syntax and limits | SeaImagine API compatibility or account access |
| SeaImagine public model pages | Published model descriptions and entry routes | An actual successful generation in your account |
| Your own recorded test | Result for your input, account, and settings | Future uptime or universal quality |

First/last-frame pairs, video references, conversational editing, 360p output, extension, and 4K upscaling depend on the selected interface. If a control is absent, do not paste API parameters into a web prompt and expect them to create it. Use the supported mode or follow the separate [Google API guide](api-quickstart.md).

## Three additional SeaImagine practice briefs

These are new editorial adaptations for this repository, outside the inherited 60-recipe count. They have not been generation-tested. Use your own references; the examples specify creative intent, not guaranteed model behavior.

### 1. Product photo to a calm storefront loop

**Input:** one unbranded ceramic cup photographed clearly. **Use:** image-to-video. **Check:** handle count, rim shape, liquid level, and final frame stability.

```text
Use the uploaded photograph as the first frame. Create a 10-second single-shot product video in the same aspect ratio as the reference.
Preserve the cup's exact silhouette, handle, glaze, liquid level and tabletop position.
[0-3s] A thin ribbon of steam rises naturally. The camera begins a very slow forward move.
[3-7s] Soft morning light moves across the glaze; only steam and the light reflection change.
[7-10s] The camera gently stops. Hold a clean product frame with room above it for a caption added later.
Audio: quiet room ambience and distant birds. No speech or music.
No pouring, extra cup, new handle, floating objects, generated text, logo or watermark.
```

If the endpoint differs from the start, use a short crossfade in your editor; a seamless loop is not guaranteed by this brief.

### 2. A travel idea without a reference photo

**Input:** text only. **Use:** text-to-video. **Check:** one continuous shot, believable contact, and simple motion.

```text
Create a 10-second, 16:9 travel atmosphere shot of an imagined coastal village at dawn. No real landmark is required.
One adult carrying a small canvas bag walks along a stone path toward a quiet harbor. A low sea wall stays on the right.
[0-3s] Establish the person and the path in a wide rear three-quarter view.
[3-7s] Track forward at walking speed. A breeze moves the coat hem and nearby grass; footsteps stay in contact with the stones.
[7-10s] The person pauses at the harbor entrance. The camera slows and holds without crossing the wall.
Audio: footsteps, mild sea wind, distant boat rigging. No speech or music.
Keep the person, bag and path consistent. No cut, aerial rise, extra people, readable signage, logo or watermark.
```

### 3. One product film, different language captions

**Input:** an approved product clip. **Use:** video editing only if the selected interface supports it; otherwise add captions in a conventional editor. **Check:** exact text, accents, readability, and unchanged product.

```text
Change only the final caption from 7s to 10s to exactly: "Un petit moment pour soi."
On-screen language: French. Preserve the exact spelling, punctuation and accents.
Place it in the existing caption area, high contrast, comfortably inside the frame.
Keep the product, composition, camera, action, timing and audio unchanged.
Do not translate the caption, add a second line, invent packaging text or change the product.
```

Replace the caption with a short phrase from your target language. Review it with a fluent speaker; keep the visual control instructions in English as a shared starting point.

## Fix the first failure, then iterate

| Problem | First change |
|---|---|
| Product changes shape | Reduce camera travel; state the silhouette and part count that must remain fixed |
| Too much happens at once | Keep one subject action and one camera action |
| Reference file is ignored | Check the uploaded file and selected input mode; describe its role in plain language |
| Text is misspelled | Shorten it; reserve caption space and add final typography outside generation if necessary |
| Audio is crowded | Remove music first and keep one foreground sound |
| Edit alters unrelated details | Request one change and list only the key invariants |
| Draft is attractive but inconsistent | Compare first, middle, and last frames before raising resolution |

## 中文速读

先按素材选择文生视频、图生视频或图片生成入口，再确认编辑器实际提供的模型和参数。保存首帧图，粘贴完整提示词，并把时长改成界面可选的时长。先做草稿，检查主体是否变形、动作是否连贯、文字和声音是否正确，再提高分辨率。标签不能替代上传文件；谷歌 API 支持的功能也不代表 SeaImagine 网页一定提供。上方三个新增配方分别练习商品短片、旅行氛围和法语字幕变体。
