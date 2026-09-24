<div align="center">

![Gemini Omni 提示词库](assets/seaimagine-omni-hero.png)

# Gemini Omni 提示词库

**60 条提示词，分为 7 类，附 6 张输入参考图；参考图不是经实测验证的生成效果。**

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)

[Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

[按分类浏览](#prompt-collections) · [六个可直接复制的案例](#source-examples) · [官方与社区效果展示](#video-studies) · [全部 60 条提示词索引](docs/prompt-index.md) · [下载全部提示词文本](prompts/copy/all-prompts.txt)

</div>

<a id="prompt-collections"></a>

## 按分类浏览

| 分类 | 提示词数 | 入口 |
|---|---:|---|
| [电影与叙事](prompts/cinematic-storytelling.md) | 8 | [查看](prompts/cinematic-storytelling.md#case-01) |
| [商业广告与社交媒体](prompts/commerce-social.md) | 8 | [查看](prompts/commerce-social.md#case-01) |
| [纪录片、旅行与教育](prompts/documentary-education.md) | 8 | [查看](prompts/documentary-education.md#case-01) |
| [动画、音乐与娱乐](prompts/stylized-entertainment.md) | 8 | [查看](prompts/stylized-entertainment.md#case-01) |
| [多模态控制、编辑与续写](prompts/control-editing-extension.md) | 10 | [查看](prompts/control-editing-extension.md#case-01) |
| [进阶编辑、镜头与视觉变换](prompts/advanced-editing-camera.md) | 9 | [查看](prompts/advanced-editing-camera.md#case-01) |
| [故事板、分屏、文字与评测](prompts/storyboard-text-evaluation.md) | 9 | [查看](prompts/storyboard-text-evaluation.md#case-01) |

[全部 60 条提示词索引](docs/prompt-index.md) · [下载全部提示词文本](prompts/copy/all-prompts.txt)

前 5 个集合的说明为中文，后 2 个为英文；可复制的控制提示词均为英文。集合正文尚未全部翻译为各入口语言。

<a id="source-examples"></a>

## 六个可直接复制的案例

参考图是输入素材，不是生成结果。

[01 · 产品音箱：水滴节拍](#example-01) · [02 · 山脊骑行：旅行纪录片开场](#example-02) · [03 · 钟表匠与纸鸟：手绘动画故事](#example-03) · [04 · 青绿色陶瓷杯：清晨商品短片](#example-04) · [05 · 纸艺海港：点亮灯塔与窗光](#example-05) · [06 · 亚麻收纳袋：多语言竖屏收尾](#example-06)

<a id="example-01"></a>

### 01 · 产品音箱：水滴节拍

<a href="assets/product-speaker.png"><img src="assets/product-speaker.png" alt="产品音箱：水滴节拍" width="420"></a>

[商业广告与社交媒体](prompts/commerce-social.md) · [参考首帧](assets/product-speaker.png) · [纯文本](prompts/copy/showcase-01.txt)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

<a id="example-02"></a>

### 02 · 山脊骑行：旅行纪录片开场

<a href="assets/travel-cyclist.png"><img src="assets/travel-cyclist.png" alt="山脊骑行：旅行纪录片开场" width="420"></a>

[纪录片、旅行与教育](prompts/documentary-education.md) · [参考首帧](assets/travel-cyclist.png) · [纯文本](prompts/copy/showcase-02.txt)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

<a id="example-03"></a>

### 03 · 钟表匠与纸鸟：手绘动画故事

<a href="assets/clockmaker-story.png"><img src="assets/clockmaker-story.png" alt="钟表匠与纸鸟：手绘动画故事" width="420"></a>

[动画、音乐与娱乐](prompts/stylized-entertainment.md) · [参考首帧](assets/clockmaker-story.png) · [纯文本](prompts/copy/showcase-03.txt)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

<a id="example-04"></a>

### 04 · 青绿色陶瓷杯：清晨商品短片

<a href="assets/seaimagine-ceramic-cup.png"><img src="assets/seaimagine-ceramic-cup.png" alt="青绿色陶瓷杯：清晨商品短片" width="420"></a>

[商业广告与社交媒体](prompts/commerce-social.md) · [参考首帧](assets/seaimagine-ceramic-cup.png) · [纯文本](prompts/copy/showcase-04.txt)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

<a id="example-05"></a>

### 05 · 纸艺海港：点亮灯塔与窗光

<a href="assets/seaimagine-paper-harbor.png"><img src="assets/seaimagine-paper-harbor.png" alt="纸艺海港：点亮灯塔与窗光" width="420"></a>

[动画、音乐与娱乐](prompts/stylized-entertainment.md) · [参考首帧](assets/seaimagine-paper-harbor.png) · [纯文本](prompts/copy/showcase-05.txt)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

<a id="example-06"></a>

### 06 · 亚麻收纳袋：多语言竖屏收尾

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="亚麻收纳袋：多语言竖屏收尾" width="420"></a>

[商业广告与社交媒体](prompts/commerce-social.md) · [参考首帧](assets/seaimagine-linen-pouch.png) · [纯文本](prompts/copy/showcase-06.txt)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

让日常更从容

<a id="video-studies"></a>

## 官方与社区效果展示

官方案例使用 Gemini Omni 1.1 Flash；社区案例来自 2026 年 5 月，使用早期 Omni 版本。链接指向原帖，本仓库未声称复现这些效果。 社区证据来自 FxTwitter，未核验 X 原生播放。

| Google · Omni 1.1 Flash | 入口 |
|---|---|
| 电影感镜头延长 | [观看视频](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| 首尾帧转场 | [观看视频](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| 360p 海洋硅藻草稿 | [观看视频](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/kw_omni-flash__capability-video__draft-360p__16x9__v1_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| 参考视频驱动舞蹈 | [观看视频](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__video-reference__16x9.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |

| X · Omni / Flash · 2026-05 | X · Omni / Flash · 2026-05 |
|---|---|
| **人物变成火烈鸟**<br><a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="人物变成火烈鸟" width="240"></a><br>CHRIS FIRST<br>[来源](https://x.com/chrisfirst/status/2056797606509158681) · [观看视频](https://video.twimg.com/amplify_video/2056797343085969408/vid/avc1/1080x1440/UYr_7RKomiginRgq.mp4?tag=27) | **拍手换帽**<br><a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="拍手换帽" width="240"></a><br>Justine Moore<br>[来源](https://x.com/venturetwins/status/2056793856843366789) · [观看视频](https://video.twimg.com/amplify_video/2056793760273686528/vid/avc1/720x1280/Q73liRfIjPtGSveL.mp4?tag=27) |
| **光合作用演示**<br><a href="https://x.com/mrfanduu/status/2056692235174097398"><img src="https://pbs.twimg.com/amplify_video_thumb/2056691792175833088/img/W0_pZkQwRicpRjjG.jpg" alt="光合作用演示" width="240"></a><br>Fandu<br>[来源](https://x.com/mrfanduu/status/2056692235174097398) · [观看视频](https://video.twimg.com/amplify_video/2056691792175833088/vid/avc1/1280x720/Ws-92fvVr5e-FkYZ.mp4?tag=14) | **伦敦眼手持变焦**<br><a href="https://x.com/fofrAI/status/2056789242274259242"><img src="https://pbs.twimg.com/amplify_video_thumb/2056503814874861569/img/mQnHwThYDypoS1H6.jpg" alt="伦敦眼手持变焦" width="240"></a><br>fofr<br>[来源](https://x.com/fofrAI/status/2056789242274259242) · [观看视频](https://video.twimg.com/amplify_video/2056503814874861569/vid/avc1/1280x720/Lc2C4YtTflfGA8qe.mp4?tag=27) |
| **原片与编辑结果对比**<br><a href="https://x.com/Mho_23/status/2057151867927601413"><img src="https://pbs.twimg.com/amplify_video_thumb/2057151701904146432/img/yhVQfdBM34BQJjV3.jpg" alt="原片与编辑结果对比" width="240"></a><br>Miko<br>[来源](https://x.com/Mho_23/status/2057151867927601413) · [观看视频](https://video.twimg.com/amplify_video/2057151701904146432/vid/avc1/1080x1920/JfeFoDd5udd_FRR7.mp4?tag=27) | **触碰水壶切换材质**<br><a href="https://x.com/alexanderchen/status/2057176690519089166"><img src="https://pbs.twimg.com/amplify_video_thumb/2057176000459612161/img/wTZ0HcgL_8PHxwbY.jpg" alt="触碰水壶切换材质" width="240"></a><br>Alexander Chen<br>[来源](https://x.com/alexanderchen/status/2057176690519089166) · [观看视频](https://video.twimg.com/amplify_video/2057176000459612161/vid/avc1/1280x720/LRzM8IueMomPMa7J.mp4?tag=27) · [完整提示词](https://x.com/alexanderchen/status/2057176691903279524) |
[来源 / FxTwitter](docs/community-examples.md)

## 进阶文档

教程已移至独立页面。 [查看](docs/guides/README_ZH.md)

[提示词设计](docs/prompting-guide.md) · [多语言指南](docs/multilingual-guide.md) · [参考素材与授权](docs/reference-videos.md)

<a id="brand-tools"></a>

## SeaImagine 创作入口

[Gemini Omni](https://seaimagine.com/cn/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/cn/model/gemini-omni-1-1-flash/)

[图生视频](https://seaimagine.com/cn/image-to-video/) · [文生视频](https://seaimagine.com/cn/text-to-video/) · [AI 图片生成](https://seaimagine.com/cn/ai-image-generator/)

可以把这些页面作为其它创作入口。具体模型、使用条款和价格以各页面当前显示为准，本仓库不保证服务持续可用。

[SeaImagine 使用流程](docs/seaimagine-workflow.md)

## 来源与许可

本仓库改编自 Flaq AI 项目，沿用了提示词集合和 3 张参考图，并非全部由 SeaImagine 原创。本项目为独立指南，不是 Google 官方产品。

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE) · [Contributing](CONTRIBUTING.md)
