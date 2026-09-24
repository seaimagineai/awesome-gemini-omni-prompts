# 多模态控制、编辑与续写：10 个原创配方

[← 上一篇：动画、音乐与娱乐](stylized-entertainment.md) · [返回中文主页](../README_ZH.md) · [English home](../README.md) · 下一篇：[进阶编辑、镜头与视觉变换 →](advanced-editing-camera.md)

> Source: adapted from [Flaq AI](https://github.com/flaqai/awesome-gemini-omni-flash), under MIT. Prompts are practice briefs, not SeaImagine-verified results. Advanced controls depend on the selected interface.

本页重点不是题材，而是把 Gemini Omni 1.1 Flash 的输入角色、短编辑指令和多轮续写用对。尖括号标签按上传顺序编号，从 0 开始。

<a id="case-index"></a>

<!-- catalog:toc:start -->
**本页案例 / Cases** · [全部 76 例 / All 76 cases](../docs/prompt-index.md)

- [01 · 角色 + 道具：职责分离](#case-01) · [TXT](copy/control-editing-extension-01.txt)
- [02 · 首尾帧：纸模型变成真实建筑](#case-02) · [TXT](copy/control-editing-extension-02.txt)
- [03 · 同图首尾帧：可复用商品循环](#case-03) · [TXT](copy/control-editing-extension-03.txt)
- [04 · 动作视频参考 + 独立角色参考](#case-04) · [TXT](copy/control-editing-extension-04.txt)
- [05 · 局部编辑：只添加一个对象](#case-05) · [TXT](copy/control-editing-extension-05.txt)
- [06 · 局部编辑：移除对象并保持物理合理](#case-06) · [TXT](copy/control-editing-extension-06.txt)
- [07 · 屏幕文字本地化](#case-07) · [TXT](copy/control-editing-extension-07.txt)
- [08 · 换时间与光线，不换内容](#case-08) · [TXT](copy/control-editing-extension-08.txt)
- [09 · 一次自然续写](#case-09) · [TXT](copy/control-editing-extension-09.txt)
- [10 · 四段式 40 秒叙事链](#case-10) · [TXT](copy/control-editing-extension-10.txt)
<!-- catalog:toc:end -->

<a id="case-01"></a>

## 01｜角色 + 道具：职责分离

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-01.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**输入：** Image1 角色正面全身，Image2 虚构手提灯产品图。

```text
[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2]
Create a 10-second dusk hiking scene. Use Image1 only as the hiker's identity and clothing reference. Use Image2 only as the exact lantern reference. Do not use either image as a literal first frame.

The hiker from <IMAGE_REF_0> walks through waist-high grass holding the lantern from <IMAGE_REF_1>. Camera tracks beside them at chest height. At 5s the lantern changes from low warm light to brighter warm light, illuminating seed heads and the hiker's unchanged face. At 8s they place it on a stone and look toward distant rain.

Audio: grass, footsteps, distant thunder, lantern switch click. No dialogue or music.
Preserve identity, clothes, lantern geometry and color. No extra people, product text, logo or watermark.
```

<a id="case-02"></a>

## 02｜首尾帧：纸模型变成真实建筑

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-02.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**输入：** Image1 纸模型，Image2 同构图建成后的建筑。

```text
[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]
Transition from the paper architectural model in Image1 to the completed real building in Image2 over 10 seconds. Keep camera position and silhouette aligned.

Paper walls gain thickness and material grain; cut-paper trees become real young trees through continuous unfolding; the tabletop expands into the site ground while the background grows from studio gray into overcast sky. Construction is shown as a material transformation, not workers building at impossible speed. The final two seconds settle exactly into Image2.

Audio evolves from paper scoring and tabletop contact to outdoor wind and distant city ambience. No narration or music.
No dissolve, explosion, cranes, people, text, logo or watermark. End exactly on Image2.
```

<a id="case-03"></a>

## 03｜同图首尾帧：可复用商品循环

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-03.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

```text
[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image1]
Use Image1 as both the exact first and final frame. Create a seamless 8-10 second product loop.

A narrow band of light travels once from left to right across the product. As it passes, three nearby material samples lift by two centimeters and rotate exactly 360 degrees, then settle into their original positions. The camera remains locked. All shadows, reflections and objects return precisely to the starting state before the final frame.

Audio: one soft spatial sweep that loops without a click. No music, voice or extra effects.
Preserve every product detail. No morphing, new text, logo, watermark or camera movement.
```

<a id="case-04"></a>

## 04｜动作视频参考 + 独立角色参考

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-04.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**输入：** Video1 为已授权的 3 秒舞步参考，Image1 为原创角色。

```text
[# References <IMAGE_REF_0>@Image1 <VIDEO_REF_0>@Video1]
Create a 10-second rehearsal video. Use Image1 for the dancer's identity and outfit. Use Video1 only as the movement and timing reference; do not edit or reproduce its setting.

The dancer from <IMAGE_REF_0> performs the movement rhythm demonstrated in <VIDEO_REF_0> inside a sunlit empty gym, then continues with one original recovery step and returns to a neutral stance. Keep full body and floor contact visible. Fixed camera, 16:9, no cuts.

Audio: original dry percussion matching the movement timing, shoe contact and room reverb. Ignore all audio from Video1. No dialogue.
Do not copy the reference background, other people, branding or audio. No identity drift, text, logo or watermark.
```

<a id="case-05"></a>

## 05｜局部编辑：只添加一个对象

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-05.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

在生成视频的下一轮发送：

```text
Add one small black cat that enters from frame right, jumps onto the empty chair, and settles there. Keep everything else the same, including people, timing, camera, lighting and audio.
```

如果猫改变了人物动作，再发送：

```text
Restore the original person's exact pose and movement. Keep the cat on the chair and keep everything else the same.
```

<a id="case-06"></a>

## 06｜局部编辑：移除对象并保持物理合理

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-06.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

```text
Remove the red suitcase beside the doorway. Reconstruct the floor and its existing shadow naturally. Keep everything else exactly the same, including the person's hands, walking path, camera motion, lighting and audio.
```

原则：编辑提示词不要重新描述整段原视频；重述越多，意外变化越多。

<a id="case-07"></a>

## 07｜屏幕文字本地化

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-07.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

原片末尾文字为 `OPEN LATE`，分别制作本地化版本：

```text
Change only the final sign text from "OPEN LATE" to Simplified Chinese: "营业至深夜". Keep its original position, size, material, lighting and display time. No other text. Keep everything else the same.
```

```text
Change only the final sign text from "OPEN LATE" to Japanese: "深夜まで営業". Preserve the characters exactly. Keep everything else the same.
```

```text
Change only the final sign text from "OPEN LATE" to Spanish: "ABIERTO HASTA TARDE". Preserve spelling exactly. Keep everything else the same.
```

<a id="case-08"></a>

## 08｜换时间与光线，不换内容

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-08.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

```text
Change only the time of day from overcast noon to blue hour just after sunset. Turn on the existing practical lamps and add physically consistent reflections. Preserve all people, faces, actions, objects, camera motion, timing and audio. Keep everything else the same.
```

若只想改天气：

```text
Add light rain outside the windows only. Keep the interior dry and keep everything else the same.
```

<a id="case-09"></a>

## 09｜一次自然续写

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-09.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

在已生成视频后，通过 `previous_interaction_id` 发送：

```text
Extend the scene by 8 seconds. Continue the same camera movement and show the same character opening the workshop door, stepping into the quiet street, and pausing as the first snow begins. The existing piano motif continues with one new higher note; interior room tone crossfades naturally to outdoor wind. Keep the same face, clothing, object in hand, color grade and lens. No dialogue, no scene cut, no text or new characters.
```

如果希望切到下一场，明确写：

```text
Extend by 8 seconds with a clean scene cut at the start of the extension. Show the same character the next morning in the same clothing, arriving at the river ferry. Continue the musical theme in a lighter arrangement.
```

<a id="case-10"></a>

## 10｜四段式 40 秒叙事链

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/control-editing-extension-10.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

每轮只描述新增长的 10 秒，并通过上一轮的 interaction ID 续写。

### 第 1 段：发现

```text
10-second opening. A night-shift radio technician in a coastal weather station detects a repeating signal hidden under storm static. Slow push from rain-covered window to the analog receiver. At 8s the signal resolves into three clear notes. She writes the time on paper. Grounded 1980s equipment, practical amber light, ocean storm audio, no dialogue, no text visible to camera.
```

### 第 2 段：确认

```text
Extend by 10 seconds. Continue without a cut. She retunes the same receiver and taps the three-note rhythm on the desk; the signal immediately answers with the same rhythm. Camera arcs to reveal the empty operator chair beside her. Storm and receiver audio remain continuous. Keep her identity, clothes, room layout, equipment and color grade unchanged.
```

### 第 3 段：来源

```text
Extend by 10 seconds. At the start of this extension, cut to the same character climbing the exterior stairs toward the station antenna in heavy wind. The three-note signal now comes through her handheld radio. Lightning briefly reveals an unlit research buoy offshore. No impossible lightning strike, no new character, same storm and music motif.
```

### 第 4 段：收束

```text
Extend by 10 seconds. Continue from the exterior stairs. The weather clears enough to reveal dawn. The buoy flashes the same three-note rhythm, then a nearby lighthouse answers with three warm light pulses. She realizes it is an old automated safety test and laughs once with relief. The storm texture fades into gulls and calm surf; the three notes resolve as an original soft chord. End on a wide steady shot. No explanatory text or narration.
```

## 什么时候使用 `task`

优先让自然语言说明意图。只有模型持续误判时，再在 `generation_config.video_config.task` 中使用 `text_to_video`、`image_to_video`、`reference_to_video`、`edit` 或 `extend`。显式 task 会增加约束，不是每次都更好。

## 关键限制速查

- 上传的视频参考最多 3 段、每段最长 3 秒；其中的音频会被忽略。
- 不支持独立音频参考，也不支持跨多个视频进行推理。
- 上传视频编辑/续写通常要求输入不超过 10 秒；只能向片尾追加。
- 多轮续写最多形成 40 秒视频；0 秒时间码指当前新增片段的开始。
- 要保留多轮可编辑状态，不要设置 `store=false`。
