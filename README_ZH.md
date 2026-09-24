# SeaImagine Gemini Omni 视频提示词库

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![SeaImagine Gemini Omni 视频提示词库](assets/seaimagine-omni-hero.png)

从 Flaq AI 源仓库改编 60 条提示词，面向 SeaImagine 用户整理产品广告、旅行镜头、动画和视频编辑思路。下面 3 个示例包含参考图和完整英文提示词，可直接复制后按页面实际选项调整。

[Gemini Omni](https://seaimagine.com/cn/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/cn/model/gemini-omni-1-1-flash/)

## 从 SeaImagine 开始

1. 打开模型页，确认当前是否可用、价格以及页面提供的设置。
2. 需要保留产品或人物外观时，选择图生视频，上传一张参考图并粘贴对应提示词；从零构思场景时，可先尝试文生视频。
3. 在界面选择时长和画幅，先试一个镜头。检查外观、动作和声音，每次只修改一项指令。

这里展示的是提示词设计，未作为 SeaImagine 实际生成结果验收。时长、声音、编辑、续写和参考素材支持以所选模型及当前界面为准，Google API 的能力不等于 SeaImagine 页面已支持。

## 三个可复制的示例

图片沿用源仓库的参考首帧，并非实际视频生成结果。请将对应图片上传为 Image1。10 秒和音效是目标要求，需按实际可用设置调整。

### 01 · 产品音箱：水滴节拍

![产品音箱：水滴节拍](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · 山脊骑行：旅行纪录片开场

![山脊骑行：旅行纪录片开场](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · 钟表匠与纸鸟：手绘动画故事

![钟表匠与纸鸟：手绘动画故事](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

## 全部 60 条提示词

前 5 个集合的说明为中文，后 2 个为英文；可复制的控制提示词均为英文。集合正文尚未全部翻译为各入口语言。

| 分类 | 内容 | 数量 | 提示词涉及的设计目标 |
|---|---|---:|---|
| [电影与叙事](prompts/cinematic-storytelling.md) | 重逢、追逐、历史工艺、惊悚、季节插值、黑色电影、喜剧、科幻 | 8 | 文生视频、对白、时间轴、连续镜头 |
| [商业广告与社交媒体](prompts/commerce-social.md) | 产品、护肤、咖啡 UGC、时尚、美食、房产、App、电商本地化 | 8 | 图生视频、参考图、竖屏、文字 |
| [纪录片、旅行与教育](prompts/documentary-education.md) | 旅行、地质、自然、历史重建、科学、博物馆、语言、建筑 | 8 | 世界知识、解说、可读标签、真实物理 |
| [动画、音乐与娱乐](prompts/stylized-entertainment.md) | 手绘、2D 动作、黏土、Meme、爵士、舞蹈、剪纸、循环 | 8 | 风格化、原生声音、单镜头、首尾帧 |
| [多模态控制、编辑与续写](prompts/control-editing-extension.md) | 角色/道具、首尾帧、动作参考、增删对象、文字本地化、40 秒叙事 | 10 | 参考标签、编辑、extend、多轮交互 |
| [进阶编辑、镜头与视觉变换](prompts/advanced-editing-camera.md) | 对象替换/移除、环境换景、风格隔离、换机位、倾斜揭示、海报穿越、AR、光轨 | 9 | 局部编辑、不变量、生成式视角、遮挡关系 |
| [故事板、分屏、文字与评测](prompts/storyboard-text-evaluation.md) | 3×3 故事板、九宫格、动作回放、流程图、职责板、动效字、多语言、科学、A/B/C 测试 | 9 | 规划输入、精确文字、本地化、可重复评测 |

## 指定中文对白

可保留英文镜头指令，用中文逐字指定对白和画面文字。生成后检查发音、字形和出现时间。

```text
Spoken language: Mandarin Chinese.
Exact dialogue, spoken once: "今天，我们走远一点。"
Do not translate, paraphrase, repeat or subtitle it.
```

## 一条强提示词应该像导演简报

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

### 10 秒可复制母版

```text
Format: 9:16 vertical video, 10 seconds.
Goal: [让哪类观众产生什么感受或行动]

Scene: [地点、时间、天气、空间关系]
Subject: [3-5 个稳定识别锚点]
Subject motion: [按顺序写主体动作]
Camera motion: [机位、景别、路径、速度、焦点]
Environment motion: [风、光、水、粒子、人群]

[0-3s] [钩子与空间建立]
[3-7s] [核心动作与升级]
[7-10s] [结果与明确尾帧]

Look: [媒介、光线、色彩、材料]
Audio: [前景拟音、环境、音乐进入/退出、静默]
Exact dialogue in [language], spoken once: "[逐字对白]"
Exact on-screen text in [language]: "[逐字文案]"
Preserve: [身份、产品、场景、动作、声音]
Do not include: [短而具体的排除项]
```

[查看完整提示词设计方法 →](docs/prompting-guide.md)

## 图生视频检查表

- 锁定身份、服装、产品几何、对象数量、构图与主光方向。
- 分开描述主体运动、环境运动和相机运动。
- 每个参考素材只有一个职责，避免“使用所有参考图中的全部内容”。
- 写清相机起点、路径、速度和最终停止位置。
- 为减速和明确尾帧预留最后 2–3 秒。
- 将对白、环境、拟音与音乐拆成不同声音层。
- 只使用原创或已获适当授权的人物、声音、产品和视觉资产。

## Gemini Omni 1.1 Flash FAQ

### 应该用文生视频还是图生视频？

探索概念、剧本或气氛时用文生视频；人物、产品、插画、构图、首帧或尾帧必须可识别时，若所选模型支持，可用图生视频或参考素材。先验证最重要的锚点，再增加复杂特效。

### 怎样减少角色或产品漂移？

指定一个主要身份/产品锚点，先列出不可改变的属性，再描述动作；每个额外参考素材只负责服装、道具、风格或动作中的一项，并明确拒绝重新设计、部件数量变化、标签漂移和身份变化。

### 可以直接用中文或其他语言写完整提示词吗？

可以尝试。此库为方便复用保留英文镜头指令，并用目标语言逐字指定对白与屏幕文字；每个语言版本应单独检查。请以当前界面实际提供的预览分辨率测试，不预设 SeaImagine 提供 360p。

### 编辑视频时为什么要写得更短？

如果所选模型和界面提供视频编辑，编辑轮次中重述整个原片会增加无关元素被重新生成的机会。使用“唯一变化 + 保留项”，例如：`Change only the jacket to dark green. Keep everything else the same.`

### 这些提示词可以免费使用吗？

仓库按 [MIT License](LICENSE) 发布。生成结果仍可能涉及参考图、人物、声音、音乐、商标、场所、广告声明以及所用平台/模型的独立权利和条款。

## 继续阅读

- [SeaImagine 使用流程](docs/seaimagine-workflow.md)
- [官方与社区案例](docs/community-examples.md)
- [多语言指南](docs/multilingual-guide.md)
- [提示词设计](docs/prompting-guide.md)
- [参考素材与授权](docs/reference-videos.md)

## SeaImagine 其它创作入口

可以把这些页面作为其它创作入口。具体模型、使用条款和价格以各页面当前显示为准，本仓库不保证服务持续可用。

- [开始创作](https://seaimagine.com/cn/create/)
- [图生视频](https://seaimagine.com/cn/image-to-video/)
- [文生视频](https://seaimagine.com/cn/text-to-video/)
- [AI 图片生成](https://seaimagine.com/cn/ai-image-generator/)

## 来源与许可

本仓库改编自 Flaq AI 项目，沿用了提示词集合和 3 张参考图，并非全部由 SeaImagine 原创。本项目为独立指南，不是 Google 官方产品。

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
