# 商业广告与社交媒体：8 个原创提示词

[← 上一篇：电影与叙事](cinematic-storytelling.md) · [返回中文主页](../README_ZH.md) · [English home](../README.md) · 下一篇：[纪录片、旅行与教育 →](documentary-education.md)

> Source: adapted from [Flaq AI](https://github.com/flaqai/awesome-gemini-omni-flash), under MIT. Prompts are practice briefs, not SeaImagine-verified results. Advanced controls depend on the selected interface.

商业场景最重要的是产品几何、材质、文字和品牌安全。本页所有产品与店铺均为虚构，不依赖现有品牌资产。

<a id="case-index"></a>

<!-- catalog:toc:start -->
**本页案例 / Cases** · [全部 76 例 / All 76 cases](../docs/prompt-index.md)

- [01 · 户外音箱水滴节拍广告](#case-01) · [TXT](copy/commerce-social-01.txt)
- [02 · 护肤精华：微距质感而非夸张特效](#case-02) · [TXT](copy/commerce-social-02.txt)
- [03 · 巷口咖啡店：中文 UGC 探店](#case-03) · [TXT](copy/commerce-social-03.txt)
- [04 · 三套造型：多参考图时尚切换](#case-04) · [TXT](copy/commerce-social-04.txt)
- [05 · 辣椒面馆：食物 ASMR](#case-05) · [TXT](copy/commerce-social-05.txt)
- [06 · 空房到生活空间：房产转场](#case-06) · [TXT](copy/commerce-social-06.txt)
- [07 · 效率 App：清晰文字驱动的发布短片](#case-07) · [TXT](copy/commerce-social-07.txt)
- [08 · 冬日围巾：多语言电商变体](#case-08) · [TXT](copy/commerce-social-08.txt)
<!-- catalog:toc:end -->

<a id="case-01"></a>

## 01｜户外音箱水滴节拍广告

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/commerce-social-01.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**模式：** 首帧图生视频 · **素材：** [源库参考首帧](../assets/product-speaker.png) · **画幅：** 16:9

```text
[# Sources <FIRST_FRAME>@Image1]
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] The camera makes a slow 20-degree clockwise orbit. The suspended droplets begin traveling around the speaker in clean concentric paths, each orbit landing on a deep electronic kick. Keep the speaker perfectly rigid and preserve its coral color, grille weave and proportions.
[3-7s] The sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist. The camera lowers slightly without changing lens perspective.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle. End on a steady three-quarter hero angle with clear negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, deep clean kick, water-drop percussion, distant ocean ambience. No vocals.
Look: photorealistic commercial cinematography, physically correct water, restrained contrast.
Constraints: preserve the exact product identity from Image1; no morphing; no added buttons or labels.
Do not include: text, logo, watermark, hands, duplicate product, camera shake.
```

<a id="case-02"></a>

## 02｜护肤精华：微距质感而非夸张特效

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/commerce-social-02.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**模式：** 文生视频 · **画幅：** 9:16 · **重点：** 包装文字、液体物理、移动端广告

```text
Format: 9:16 vertical beauty ad, 10 seconds.
Product: a fictional clear glass serum bottle with a matte ivory cap and one exact label line: "MORNING DEW". No other label text.

[0-3s] Extreme macro of one transparent serum drop descending inside the pipette. Soft window caustics move across the glass; the camera slides left by only five centimeters.
[3-7s] Cut to the bottle standing on pale limestone beside a fresh green leaf. A single droplet rolls down the exterior and magnifies the label without distorting the spelling.
[7-10s] Gentle pullback reveals early morning light and a shallow water tray. Exact on-screen text appears once in the upper third: "LIGHT, NOT LOUD". Hold fully readable for two seconds.

Audio: glass touch, one water drop, airy room tone, three soft original marimba notes. No voiceover.
Look: honest skin-care photography, neutral whites, realistic viscosity, subtle texture.
Do not include: skin transformation claims, faces, extra bottles, flowers, glitter, illegible text, logos, watermark.
```

<a id="case-03"></a>

## 03｜巷口咖啡店：中文 UGC 探店

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/commerce-social-03.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**模式：** 文生视频 · **画幅：** 9:16 · **重点：** 自然口播、手持镜头、真实小店

```text
Create a 9:16 vertical 10-second creator-style café discovery video that feels spontaneous but visually coherent.

Character: one adult creator in a denim overshirt, natural appearance, speaking directly to a handheld phone camera. Keep face, hairstyle and clothing unchanged.
Location: a tiny independent corner café with unbranded cups, late-afternoon window light, two customers softly out of focus.

[0-3s] The creator pushes open the door and turns the camera from the hand-painted menu wall to their face. Mandarin Chinese dialogue, spoken once: "这家店，藏在巷子最里面。"
[3-7s] Match cut to a close view of citrus peel being expressed over iced coffee; the creator's hand enters frame and rotates the glass once.
[7-10s] Back to the creator taking one sip and giving a surprised, restrained smile. Exact Mandarin dialogue: "先是橙香，最后才是咖啡。"

Audio: door bell, low café room tone, ice, citrus spray, clear close voice. No background music and no subtitles.
Avoid influencer beauty filters, exaggerated reaction, other speech, brand marks, price text, watermark, face drift.
```

<a id="case-04"></a>

## 04｜三套造型：多参考图时尚切换

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/commerce-social-04.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**模式：** 多参考图 · **画幅：** 9:16 · **输入：** Image1 角色、Image2/3/4 三套服装

```text
[# References <IMAGE_REF_0>@Image1 <IMAGE_REF_1>@Image2 <IMAGE_REF_2>@Image3 <IMAGE_REF_3>@Image4]
Create a 9:16, 10-second studio fashion sequence. Use Image1 only for the model's identity; use Images2-4 only for the three outfits. Do not use any reference as a literal first frame.

[0-3s] The model from <IMAGE_REF_0> walks toward camera wearing outfit <IMAGE_REF_1>. Warm white cyc wall, slow 85mm dolly back.
[3-6s] As the model passes behind a narrow black panel, reveal the same person in outfit <IMAGE_REF_2>. Camera direction and walking cadence continue seamlessly.
[6-9s] A controlled flash creates the final change into outfit <IMAGE_REF_3>. The person turns once and stops on the same floor mark.
[9-10s] Hold a clean full-body hero frame.

Audio: heel steps remain continuous through all transitions, fabric movement, three low original bass notes aligned to reveals. No dialogue.
Preserve identity, body proportions and hair; preserve each outfit's construction and color. No blended garments, extra accessories, text, logos, audience or watermark.
```

<a id="case-05"></a>

## 05｜辣椒面馆：食物 ASMR

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/commerce-social-05.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**模式：** 文生视频 · **画幅：** 9:16 · **重点：** 声音、食物物理、近景

```text
Create a 10-second vertical food film in one continuous tabletop shot.

A wide ceramic bowl of hand-pulled noodles sits on a worn walnut counter. Begin close on clear broth trembling as noodles drop into the bowl. A cook's hands add exactly three toppings in order: green scallions, one spoon of toasted chili flakes, then hot sesame oil poured from a small brass ladle. The oil blooms across the surface in realistic red-gold patterns. At 8s, chopsticks lift one clean bundle; steam passes the lens without obscuring it.

Camera: 70mm macro look, very slow push-in, no cuts, stable horizon.
Audio is the hero: broth pour, noodle slap, dry chili texture, strong oil sizzle, wood counter creak. No music, no speech, no eating sounds.
Lighting: warm side light with natural highlights, appetizing but not oversaturated.
No face, no text, no brand, no extra hands, no ingredient teleportation, no impossible liquid, no watermark.
```

<a id="case-06"></a>

## 06｜空房到生活空间：房产转场

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/commerce-social-06.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**模式：** 首帧 + 尾帧 · **画幅：** 16:9 · **输入：** Image1 空房，Image2 同机位软装完成

```text
[# Sources <FIRST_FRAME>@Image1 <LAST_FRAME>@Image2]
Interpolate from the empty room in Image1 to the furnished room in Image2 over 10 seconds. Lock the camera, lens, walls, windows, floor and architectural geometry exactly.

Furniture enters through believable coordinated motion rather than appearing: a rug unrolls from foreground, the sofa slides gently from frame left, the table assembles from aligned components, curtains descend and catch a light breeze, then two plants settle into their final positions. Natural daylight warms gradually as the room becomes complete. Every object must arrive at the exact placement and design shown in Image2.

Audio: soft room reverb, rug roll, wood contact, curtain rings, one warm non-melodic tonal swell. No dialogue.
No construction workers, no floating objects, no wall changes, no extra decor, no text, logo or watermark. End exactly on Image2.
```

<a id="case-07"></a>

## 07｜效率 App：清晰文字驱动的发布短片

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/commerce-social-07.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**模式：** 文生视频 · **画幅：** 9:16 · **重点：** 动态字效、界面克制、SEO/社媒钩子

```text
Create a clean 9:16 launch teaser for a fictional focus timer, 10 seconds. Use abstract interface motion rather than a realistic phone brand.

[0-2s] On a deep navy background, one exact word appears centered in large ivory type: "DISTRACTED?" The question mark draws on last.
[2-5s] The word collapses into a simple circular 25-minute timer. A small amber dot travels smoothly around one quarter of the ring. Soft ticking begins.
[5-8s] Three cluttered notification cards slide away from the timer and dissolve. Exact centered text replaces them: "ONE THING."
[8-10s] The timer locks into a calm completed ring. Final exact text below it: "START SMALL". Hold both lines readable until the end.

Motion: precise editorial easing, no fake operating-system chrome, no tiny unreadable copy.
Audio: dry tick, three soft card swishes, a single warm completion tone. No voiceover, no music.
Only the three quoted text strings may appear. Preserve spelling and punctuation. No logo, phone hardware, watermark or extra icons.
```

<a id="case-08"></a>

## 08｜冬日围巾：多语言电商变体

<!-- catalog:copy:start -->
[复制全文 / Download TXT](copy/commerce-social-08.txt) · [本页索引 / Case index](#case-index)
<!-- catalog:copy:end -->

**模式：** 文生视频 + 对话式文字编辑 · **画幅：** 9:16 · **重点：** 一支母版、多语言本地化

**母版提示词：**

```text
Create a 9:16, 10-second winter product story for a fictional handwoven cobalt-blue scarf.

[0-4s] In a quiet tram shelter at dawn, wind lifts the scarf's loose end around an adult commuter's charcoal coat. Close handheld framing shows the woven fibers and natural breath in cold air.
[4-7s] The commuter wraps the scarf once, then looks up as the tram's warm light arrives across their face.
[7-10s] Cut to the scarf folded on a simple wooden bench. Exact on-screen English text: "WARMTH, ON THE WAY". Hold readable for two seconds.

Audio: winter wind, wool movement, distant tram bell, restrained original piano chord. No dialogue.
Preserve the scarf's cobalt color, weave and fringe. No brand, price, sale badge, extra text, logo or watermark.
```

**后续编辑（任选一条，单独发送）：**

```text
Change only the final on-screen text to Simplified Chinese: "温暖，在路上". Preserve exact punctuation and keep everything else the same.
```

```text
Change only the final on-screen text to Japanese: "ぬくもりを、連れて。" Preserve the Japanese characters and keep everything else the same.
```

```text
Change only the final on-screen text to Spanish: "CALIDEZ EN CAMINO". Preserve spelling and keep everything else the same.
```

## 商业视频检查表

- 产品的颜色、比例、接口和文字是否从头到尾一致？
- 竖屏安全区内是否保留了标题与平台按钮空间？
- 音乐、拟音、对白是否争抢同一频段或同一秒？
- 是否出现未经授权的品牌、包装、人物、价格或效果承诺？
- 本地化编辑是否真的只改了文字，而没有改变产品和镜头？
