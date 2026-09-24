# Gemini Omni 提示词库

![Gemini Omni 提示词库](assets/seaimagine-omni-hero.png)

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

<a id="video-studies"></a>

## 从官方与社区案例学什么

Google 视频是 Omni 1.1 Flash 官方展示。社区帖子发布于 2026 年 5 月，属于早期 Omni / Flash 案例，未核实为 1.1 实测。社区证据来自 FxTwitter 镜像的文字和媒体元数据，未核验 X 原生播放。这些是独立来源的案例，不代表你所用平台的生成结果；具体功能请查看所用工具。

### Google：首尾帧转场

[查看原始案例](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

分别确定起始画面、结束画面和两者之间连续的运动。

为同一物体准备两张角度相容的照片；如果支持首尾帧，用一个简单动作连接两张图。

### Google：延长镜头

[查看原始案例](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

续写下一段镜头运动，同时保持主体与运动方向一致。

使用自己的短片；如果支持延长，只增加一段连续动作，检查接缝处的运动和光线是否跳变。

### CHRIS FIRST：人物换成火烈鸟

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST：人物换成火烈鸟" width="300"></a>

[查看原始案例](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

更换主体时明确保留服装和动作，并检查肢体接触位置。

使用自己的视频；如果支持视频编辑，只替换一个主体，对比前后的服装、姿势及与地面的接触。

### Justine Moore：每次拍手换一顶帽子

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore：每次拍手换一顶帽子" width="300"></a>

[查看原始案例](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

用可见动作决定变化时刻，同时保持人脸、服装和镜头一致。

固定机位拍摄两次清楚的拍手；如果支持视频编辑，要求每次拍手换帽，逐帧检查变化时刻。

[官方与社区案例](docs/community-examples.md)

## 从看案例，到动手写提示词

本库收录源库的 60 条完整配方，分为 7 类。跟着示例学习如何交代场景、安排动作时间、控制镜头和声音，再改成自己的创意。

### 开始你的第一次尝试

1. 选择一个接近你想做的场景的完整示例，复制全部提示词。
2. 下载示例对应的参考图；如果所用工具支持首帧，请将图片设为首帧。
3. 按工具可用的时长和分辨率调整时间段，先生成草稿，检查主体、文字和声音，每次只改一项。

<a id="source-examples"></a>

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



## 一分钟找到合适的提示词

| 你的起点或目标 | 从这里开始 |
|---|---|
| 只有一个概念、剧本或镜头想法 | [电影与叙事](prompts/cinematic-storytelling.md) |
| 有产品图、店铺、服装或商业目标 | [商业广告与社交媒体](prompts/commerce-social.md) |
| 需要旅行、自然、历史、科学或建筑内容 | [纪录片、旅行与教育](prompts/documentary-education.md) |
| 想做动画、音乐、舞蹈、喜剧或无缝循环 | [动画、音乐与娱乐](prompts/stylized-entertainment.md) |
| 已有首帧、尾帧、角色图、短视频或待编辑视频 | [多模态控制、编辑与续写](prompts/control-editing-extension.md) |
| 需要对象替换、环境换景、换机位、风格隔离、AR 或特效 | [进阶编辑、镜头与视觉变换](prompts/advanced-editing-camera.md) |
| 已有九宫格故事板、流程图，或要做分屏、动效文字、多语言标题与评测 | [故事板、文字与评测](prompts/storyboard-text-evaluation.md) |
| 想看官方演示，或寻找授权条件清晰的参考视频 | [参考视频与授权指南](docs/reference-videos.md) |
| 需要中文、日语、韩语、法语等对白或屏幕文字 | [15 种语言本地化指南](docs/multilingual-guide.md) |
| 提示词出现角色漂移、文字乱码或声音拥挤 | [失败诊断与提示词设计指南](docs/prompting-guide.md) |
| 准备用 Python、JavaScript 或 REST 接入 | [Google Gemini API 快速开始（程序调用，与所选工具网页分开）](docs/api-quickstart.md) |

## 按创作目标理解提示词

以下对照表帮助你写清素材职责、动作与修改范围，不代表所选工具已支持全部方式。先在所选模型页面确认输入类型、编辑、续写、声音和时长，再复制对应提示词。`<FIRST_FRAME>` 等是素材职责标签；如果网页没有对应输入栏，它们不能开启额外功能。

| 创作方式 | 最适合的任务 | 提示词重点 |
|---|---|---|
| 文本 → 带声音视频 | 概念片、叙事、广告、短视频 | 场景、主体动作、镜头、光线、声音、时间点 |
| 图片 → 视频 | 产品图、照片、插画 | 明确首帧或参考；分别描述主体、相机、环境运动 |
| 首帧 + 尾帧 | 转场、变身、季节变化、循环 | 锁定几何，解释连续变化机制，预留稳定尾帧 |
| 多张参考图 | 角色、服装、道具与美术组合 | 使用 `<IMAGE_REF_N>`，每个素材只承担一个职责 |
| 视频参考 | 动作、主体或镜头路径 | 使用 `<VIDEO_REF_N>`，明确不是待编辑源并忽略参考音频 |
| 对话式编辑 | 换光线、增删物体、改风格、换文字 | 一轮只改一项，结尾写 `Keep everything else the same.` |
| 片尾续写 | 连续故事、角色进场、音乐段落 | 说明接续或切场，并同步定义画面与声音连续性 |
| 可读文字 | 标牌、标题卡、包装、动态字效 | 逐字引用，指定语言、位置、出现时间与唯一性 |

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
Exact dialogue at 6s, spoken once: "今天，我们走远一点。"
Do not translate, paraphrase, repeat or subtitle it.

On-screen script: Simplified Chinese.
Exact on-screen title, centered from 7s to 10s: "小小旅程"
Preserve the exact characters. No other text.
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

可以尝试。此库为方便复用保留英文镜头指令，并用目标语言逐字指定对白与屏幕文字；每个语言版本应单独检查。请以当前界面实际提供的预览分辨率测试，不预设所选工具提供 360p。

### 编辑视频时为什么要写得更短？

如果所选模型和界面提供视频编辑，编辑轮次中重述整个原片会增加无关元素被重新生成的机会。使用“唯一变化 + 保留项”，例如：`Change only the jacket to dark green. Keep everything else the same.`

### 这些提示词可以免费使用吗？

仓库按 [MIT License](LICENSE) 发布。生成结果仍可能涉及参考图、人物、声音、音乐、商标、场所、广告声明以及所用平台/模型的独立权利和条款。

## 对白语言与屏幕文字可以分别指定

需要日语对白、西班牙语标题时，分别锁定语言、出现时间和逐字内容。不要把整段提示词直接翻译后就当作已完成本地化；逐项检查发音、字形和时间。

```text
Spoken language: Japanese.
Exact dialogue at 6s, spoken once with natural conversational pacing: "今日は、遠回りして帰ろう。"
Do not translate, paraphrase, repeat or subtitle it.

On-screen language: Spanish.
Exact title, centered and fully readable from 7s to 10s: "PEQUEÑOS VIAJES"
Preserve accents and spelling exactly. No other text anywhere.
```

## 已知限制与使用前检查

- 不同语言的发音、字形和口型需要分别验收；英文指令也不能保证生成结果正确。
- Google Gemini API 与所选工具网页是不同入口。源库的 API 教程涉及独立音频参考、参考视频音频、上传片长、片尾续写、语音编辑和独立排除参数等限制；使用程序调用前，请核对[当前 Google 官方文档](https://ai.google.dev/gemini-api/docs/omni)。不要把这些参数直接套到所选工具网页。
- 先在所选工具中确认当前模型是否支持首尾帧、多个参考素材、视频编辑、续写或声音；不存在的上传栏和参数不会因写入提示词而启用。
- 预览分辨率、成片分辨率、时长、价格及地区支持以当前界面为准。高分辨率或放大不能补救错误构图、乱码、动作穿帮或节奏。
- 使用人物、声音、音乐、商标和参考视频前，确认你有相应使用权。官方展示和社区视频的链接不等于素材授权。

## 贡献与官方来源

欢迎分享原创提示词、可靠的本地化修订和诚实的失败记录。请阅读[贡献指南](CONTRIBUTING.md)，并通过[提示词提交表单](https://github.com/seaimagineai/awesome-gemini-omni-prompts/issues/new?template=prompt-submission.yml)提供实际模型、输入素材职责、画幅、界面可选分辨率、结果、已知问题及修改记录。请勿提交未授权素材、个人私密信息、密钥或无法核验的能力声明。

- [Google AI：Gemini Omni 视频生成与编辑文档](https://ai.google.dev/gemini-api/docs/omni)
- [Google DeepMind：Gemini Omni 官方演示](https://deepmind.google/models/gemini-omni/)
- [Google DeepMind：Gemini Omni Flash 模型卡](https://deepmind.google/models/model-cards/gemini-omni-flash/)

参考视频的使用边界见[素材与授权指南](docs/reference-videos.md)。本项目是独立整理的学习资料，不代表 Google 官方背书；提示词的开源许可不替代生成平台条款或第三方素材授权。

## 继续阅读

- [官方与社区案例](docs/community-examples.md)
- [多语言指南](docs/multilingual-guide.md)
- [提示词设计](docs/prompting-guide.md)
- [参考素材与授权](docs/reference-videos.md)

<a id="brand-tools"></a>

## 从 SeaImagine 开始

本库保留 Flaq AI 的 60 条源配方，并新增三组带原创参考图的 SeaImagine 练习。本页可直接阅读新练习、源库示例，以及官方与社区案例的学习说明。

[Gemini Omni](https://seaimagine.com/cn/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/cn/model/gemini-omni-1-1-flash/)

1. 打开模型页，确认当前是否可用、价格以及页面提供的设置。
2. 需要保留产品或人物外观时，选择图生视频，上传一张参考图并粘贴对应提示词；从零构思场景时，可先尝试文生视频。
3. 在界面选择时长和画幅，先试一个镜头。检查外观、动作和声音，每次只修改一项指令。

这里展示的是提示词设计，未作为 SeaImagine 实际生成结果验收。时长、声音、编辑、续写和参考素材支持以所选模型及当前界面为准，Google API 的能力不等于 SeaImagine 页面已支持。

<a id="sea-practice"></a>

## 三个 SeaImagine 原创参考图练习

以下参考图由 AI 生成，用于首帧练习，不是 Gemini 视频实测结果。操作时以 SeaImagine 界面实际提供的功能为准。

### SEA-01 · 青绿色陶瓷杯：清晨商品短片

[![青绿色陶瓷杯：清晨商品短片](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

镜头缓慢推进，保持杯把、杯口和液位不变，结尾留出字幕位置。

上传杯子参考图进行图生视频。先只尝试缓慢推进，检查杯把和液位，再添加字幕。

[图生视频](https://seaimagine.com/cn/image-to-video/) · [AI 图片生成](https://seaimagine.com/cn/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · 纸艺海港：点亮灯塔与窗光

[![纸艺海港：点亮灯塔与窗光](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

用单一镜头让灯塔亮起，再让三幢房屋的窗光依次增强，保持纸张质感与几何结构。

上传海港参考图进行图生视频。要求灯塔亮起、窗光依次增强，对比开头与结尾的建筑形状。

[图生视频](https://seaimagine.com/cn/image-to-video/) · [AI 图片生成](https://seaimagine.com/cn/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · 亚麻收纳袋：多语言竖屏收尾

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="亚麻收纳袋：多语言竖屏收尾" width="360"></a>

先制作无文字的干净竖屏商品片，再用常规视频编辑器添加本地语言字幕。

上传收纳袋参考图制作竖屏短片，之后添加翻译好的字幕；仅在界面支持视频编辑时使用简短编辑指令。

[图生视频](https://seaimagine.com/cn/image-to-video/) · [AI 图片生成](https://seaimagine.com/cn/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> 让日常更从容

[SeaImagine 使用流程](docs/seaimagine-workflow.md)

## SeaImagine 其它创作入口

可以把这些页面作为其它创作入口。具体模型、使用条款和价格以各页面当前显示为准，本仓库不保证服务持续可用。

- [开始创作](https://seaimagine.com/cn/create/)
- [图生视频](https://seaimagine.com/cn/image-to-video/)
- [文生视频](https://seaimagine.com/cn/text-to-video/)
- [AI 图片生成](https://seaimagine.com/cn/ai-image-generator/)

## 来源与许可

本仓库改编自 Flaq AI 项目，沿用了提示词集合和 3 张参考图，并非全部由 SeaImagine 原创。本项目为独立指南，不是 Google 官方产品。

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
