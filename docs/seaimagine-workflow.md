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

<!-- generated:practice:start -->
<a id="sea-practice"></a>

## Three SeaImagine exercises with original reference images

These AI-generated reference images are starting frames for practice, not tested Gemini video outputs. Use only the controls available in your SeaImagine interface.

### SEA-01 · A quiet morning with a teal ceramic cup

[![A quiet morning with a teal ceramic cup](../assets/seaimagine-ceramic-cup.png)](../assets/seaimagine-ceramic-cup.png)

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

[![A paper harbor lights up](../assets/seaimagine-paper-harbor.png)](../assets/seaimagine-paper-harbor.png)

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

<a href="../assets/seaimagine-linen-pouch.png"><img src="../assets/seaimagine-linen-pouch.png" alt="A linen pouch for a multilingual shop" width="360"></a>

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
<!-- generated:practice:end -->

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

先按素材选择文生视频、图生视频或图片生成入口，再确认编辑器实际提供的模型和参数。保存首帧图，粘贴完整提示词，并把时长改成界面可选的时长。先做草稿，检查主体是否变形、动作是否连贯、文字和声音是否正确，再提高分辨率。标签不能替代上传文件；谷歌 API 支持的功能也不代表 SeaImagine 网页一定提供。上方三个新增配方分别练习陶瓷杯商品短片、纸艺海港灯光变化和亚麻袋竖屏电商短片；字幕在后期添加，不预设网页提供视频编辑。
