# Gemini Omni 1.1 Flash 提示词设计指南

[← 返回中文主页](../README_ZH.md) · [English home](../README.md) · [15 种语言本地化](multilingual-guide.md) · [API 快速开始](api-quickstart.md)

## 1. 先选工作模式

| 目标 | 输入 | 写法 |
|---|---|---|
| 从零创作 | Text | 直接写场景；需要时声明 `text_to_video` |
| 让静态图成为开场 | Image + Text | `<FIRST_FRAME>`，明确主体/相机/环境运动 |
| 从一张图过渡到另一张 | 2 Images + Text | `<FIRST_FRAME>` + `<LAST_FRAME>`，写连续变化逻辑 |
| 保持角色或产品 | Images + Text | `<IMAGE_REF_N>`，为每张图指定一个职责 |
| 借用动作或主体信息 | Short video + Text | `<VIDEO_REF_N>`，明确它是参考而非编辑源 |
| 修改已有视频 | Video or previous interaction + Text | 一轮只写一个更改，追加保留句 |
| 延长故事 | Video or previous interaction + Text | 写清接续/切场、角色连续性和声音走向 |

## 2. 一条高成功率提示词的六层结构

### 意图层

先说视频为谁服务、希望产生什么反应。例如：

```text
Goal: make commuters feel that this compact raincoat is practical, calm and easy to carry.
```

这比 `cinematic premium 8K ad` 更能约束创作方向。

### 空间层

说明地点、时间、天气和重要物体之间的位置：

```text
Scene: a narrow tram shelter at blue hour; wet road behind the subject; warm tram approaching from frame right; no other people.
```

### 稳定层

把必须保持的特征写成少量可识别锚点。角色不宜写几十个形容词，使用 3–5 个稳定特征即可：

```text
Character: adult woman, short black curls, rust-red raincoat, silver square glasses, canvas satchel. Keep all five features unchanged.
```

### 运动层

分别写三种运动：

```text
Subject motion: she folds the raincoat once and places it in the satchel.
Camera motion: a slow chest-height arc from front-left to profile.
Environment motion: rain runs down glass; tram light sweeps across the shelter; loose hair reacts to one wind gust.
```

如果只写 `make it move`，模型需要替你决定几乎所有运动，结果通常泛化。

### 时间层

10 秒内有两个以上事件时，用自然语言时间点或时间码：

```text
[0-3s] Establish the space and visual hook.
[3-7s] Perform the core action.
[7-10s] Reveal the result and hold the final composition.
```

时间码是叙事优先级，不是逐帧保证。不要在 10 秒里塞 8 个复杂镜头、4 句台词和 3 次变身。

### 声音层

把声音按前景、中景、背景分层：

```text
Foreground: zipper, wet fabric, close breath.
Midground: tram bell and tires on rain.
Background: soft city room tone.
Music: one original low pulse begins at 5s and stops before dialogue.
Dialogue: exact Mandarin line, spoken once at 7s: "刚好赶上。"
```

如果不想要某类声音，直接写 `No music`、`No dialogue`、`No extra sound effects`。

## 3. 连续镜头与多镜头

Omni 默认可能设计多个镜头。需要长镜头时，使用完整约束：

```text
One continuous unbroken shot. No cuts, inserts, montage, time jump or drone view.
```

多镜头时，不要只写 `cinematic cuts`，而要给每个镜头一个任务：

```text
[0-3s] Wide shot establishes the empty station.
[3-6s] Medium tracking shot reveals the arriving traveler.
[6-10s] Close two-shot holds both performances and dialogue.
```

## 4. 参考素材角色标签

### 简单标签

```text
<FIRST_FRAME>
<LAST_FRAME>
<IMAGE_REF_0>
<VIDEO_REF_0>
```

### 完整声明

```text
[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]
[# References <IMAGE_REF_0>@Image3 <VIDEO_REF_0>@Video1]
```

随后在正文内复述职责：

```text
Use Image1 as the exact starting frame and Image2 as the exact final frame.
Use Image3 only for the character's identity.
Use Video1 only for movement timing; ignore its setting and audio.
```

### 一图一职责

常见失败来自职责冲突，例如同时要求 Image1 既是首帧、又只是服装参考、又不能出现在成片里。更稳的做法是分开准备：

- Image1：首帧与构图。
- Image2：角色身份。
- Image3：产品或道具。
- Video1：动作节奏。

## 5. 首尾帧不是普通转场

首尾帧控制要回答三个问题：

1. 哪些几何位置必须锁定？
2. 中间变化依靠什么物理或叙事机制发生？
3. 最后多久必须稳定在尾帧？

```text
Lock the camera, lens, wall geometry and horizon. Leaves change color continuously and fall; frost forms from the edges inward; snow accumulates with gravity. Settle exactly into the final frame for the last two seconds. No dissolve or jump cut.
```

同一图片同时作为首尾帧时，可以制作循环。让每个运动闭合：风回到初始强度、对象回到原位、相机不漂移、声音尾部能接回开头。

## 6. 多语言对白和文字

官方目前只完整评估英语。为了提高其他语言的稳定性，推荐用英文写控制层，用目标语言写精确内容：

```text
Spoken language: Spanish.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Llegamos justo a tiempo."
Do not translate, paraphrase, repeat or subtitle it.
```

屏幕文字需要写明五件事：原文、语言、位置、出现区间、唯一性。

```text
Exact on-screen Japanese text: "小さな旅"
Centered in the upper third from 6s to 9s, large and fully readable.
Preserve the characters exactly. No other text anywhere.
```

制作多语言版本时，先生成无文字母版，再用多轮编辑只替换文案。每种语言都以 360p 独立校验，不要假设一个语言成功意味着其他语言也成功。

## 7. 编辑：短、单一、可验证

官方建议编辑提示词保持简单。一个可靠编辑句由“唯一变化 + 保留项”构成：

```text
Change only the jacket from red to dark green. Keep everything else the same, including face, motion, timing, camera, background and audio.
```

不推荐重新描述原片，因为被重新提到的内容也可能被重新生成。复杂修改拆成多轮：先改光线，再改文字，再加对象；每轮验收后继续。

## 8. 续写：让连续性有抓手

续写会使用已有视频末尾上下文。提示词应覆盖：

- 动作是否接续，还是新增片段一开始就切场。
- 哪个角色、物体、服装、镜头和色彩必须一致。
- 音乐是否延续、进入副歌或停止。
- 新增时间码从 0 秒重新计算。

```text
Extend by 8 seconds. Continue the same shot and camera speed. The same cyclist reaches the observatory gate, brakes, and places one foot on the ground. The existing wind continues; the music drops out at 5s so the bicycle freewheel becomes clear. Preserve identity, jacket, bicycle, weather, lens and color grade.
```

## 9. 排除项写在普通提示词里

模型没有独立 negative prompt 参数。将真正重要的排除项放在正文末尾：

```text
Do not include: extra people, subtitles, logos, watermark, camera shake, duplicate product, altered hands.
```

排除项应具体且短。列出几十个不相关错误会稀释重点。

## 10. 草稿到交付

1. **360p 构图草稿：** 验证主体、镜头、动作数量和结尾画面。
2. **360p 声音草稿：** 验证对白语言、音乐进入点、拟音空间。
3. **单项编辑：** 每轮只修复一个最明显问题。
4. **720p 审核：** 检查面部、手、产品几何、文字、口型与物理。
5. **1080p/4K 交付：** 仅在内容已经正确时放大。
6. **来源与授权记录：** 保存参考素材许可、提示词版本和 interaction ID。

## 11. 失败诊断

| 现象 | 常见原因 | 优先修改 |
|---|---|---|
| 像幻灯片 | 动作只按镜头罗列 | 增加连续主体/相机/环境运动，写 `not a slideshow` |
| 角色漂移 | 特征过多或参考职责冲突 | 保留 3–5 个锚点，一图一职责 |
| 产品变形 | 同时要求复杂相机和复杂变身 | 锁定产品，先测试简单轨道运动 |
| 对白重复 | 台词太长或时间不足 | 缩成一句，写 `spoken once` |
| 文字乱码 | 文案太长、太小、出现太短 | 减字、加大、至少停留两秒、禁止其他文字 |
| 编辑改坏整片 | 编辑提示词重述太多 | 只写唯一变化 + `Keep everything else the same` |
| 续写跳场 | 没说明连续还是切镜头 | 明确 `continue without a cut` 或 `cut at the start` |
| 声音拥挤 | 音乐/环境/对白同时抢占 | 分层并安排进入/退出时间 |

## 12. 可复制母版

```text
[# Sources ...] [# References ...]
Format: [16:9 / 9:16], [duration], [single shot / shot sequence].
Goal: [audience + intended response].

Scene: [place, time, weather, spatial relationships].
Subject: [3-5 stable anchors].
Subject motion: [physical action sequence].
Camera motion: [lens impression, height, path, focus].
Environment motion: [wind, light, particles, crowds, water].

[0-Xs] [beat 1]
[X-Ys] [beat 2]
[Y-end] [payoff and final hold]

Look: [medium, palette, lighting, texture].
Audio foreground: [specific effects].
Audio background: [ambience].
Music: [original style, tempo, entry/exit] or No music.
Exact dialogue in [language], spoken once at [time]: "[verbatim]"
Exact on-screen text in [language], [placement/time]: "[verbatim]"

Preserve: [identity, product geometry, layout, motion, audio].
Do not include: [short concrete list].
```

能力与限制以 [Google AI 官方文档](https://ai.google.dev/gemini-api/docs/omni) 为准。
