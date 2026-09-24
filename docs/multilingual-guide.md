# Gemini Omni 1.1 Flash 多语言视频指南：15 种语言

[← 返回中文主页](../README_ZH.md) · [English home](../README.md) · [提示词设计指南](prompting-guide.md) · [API 快速开始](api-quickstart.md)

本指南面向需要多语言对白、旁白、屏幕文字或地区版本的创作者与开发者。Gemini Omni 官方当前只说明英语经过完整评估；其他语言可能可用，但发音、口型、字符和排版稳定性会随语言、镜头和版本变化。以下方法的目标是让问题可测试、可定位，而不是承诺所有语言一次成功。

SeaImagine 网站现有 15 种语言的入口与本仓库对应。注意：网站简体中文路径为 `/cn/`，繁体中文为 `/tw/`，并非表中的标准语言代码。各语言首页有本地化说明和三个完整示例；共享提示词仍为英文，辅助指南没有全部翻译。

## 15 种语言入口

| 语言 | Locale | 入口 | 推荐的语言声明 | 书写与排版提示 |
|---|---|---|---|---|
| English | `en` | [README](../README.md) | `Spoken language: English.` | 拉丁字母，注意大小写与标点 |
| 简体中文 | `zh-CN` | [README_ZH](../README_ZH.md) | `Spoken language: Mandarin Chinese.` | 汉字较密，屏幕文案宜短 |
| 繁體中文 | `zh-TW` | [README_ZH-TW](../README_ZH-TW.md) | `Spoken language: Mandarin Chinese. On-screen script: Traditional Chinese.` | 明确繁体字形，不要自动转简体 |
| 日本語 | `ja` | [README_JA](../README_JA.md) | `Spoken language: Japanese.` | 汉字、假名混排；逐字锁定 |
| 한국어 | `ko` | [README_KO](../README_KO.md) | `Spoken language: Korean.` | 韩文音节块要有足够字号 |
| Español | `es` | [README_ES](../README_ES.md) | `Spoken language: Spanish.` | 保留重音符号与倒问号/倒叹号 |
| Français | `fr` | [README_FR](../README_FR.md) | `Spoken language: French.` | 保留重音、撇号与空格规范 |
| Deutsch | `de` | [README_DE](../README_DE.md) | `Spoken language: German.` | 复合词较长，预留更宽版面 |
| Português (Brasil) | `pt-BR` | [README_PT](../README_PT.md) | `Spoken language: Brazilian Portuguese.` | 明确巴西葡语，保留重音与 ç |
| Italiano | `it` | [README_IT](../README_IT.md) | `Spoken language: Italian.` | 关注自然重音和台词长度 |
| العربية | `ar` | [README_AR](../README_AR.md) | `Spoken language: Modern Standard Arabic. On-screen direction: right-to-left.` | RTL；标点、数字和混排需单独验收 |
| Русский | `ru` | [README_RU](../README_RU.md) | `Spoken language: Russian.` | 西里尔字母；防止混入拉丁字母 |
| Bahasa Indonesia | `id` | [README_ID](../README_ID.md) | `Spoken language: Indonesian.` | 明确 Indonesian，避免误判为其他语言 |
| ไทย | `th` | [README_TH](../README_TH.md) | `Spoken language: Thai.` | 泰文无常规词间空格，字号和换行需测试 |
| Tiếng Việt | `vi` | [README_VI](../README_VI.md) | `Spoken language: Vietnamese.` | 声调符号必须完整，防止去音标 |

## 一条统一测试句

为了比较不同语言版本，保持镜头、角色、时长和声音完全一致，只替换以下精确对白：

| Locale | Exact dialogue |
|---|---|
| `en` | `Let's take the long way home today.` |
| `zh-CN` | `今天，绕远一点回家吧。` |
| `zh-TW` | `今天，繞遠一點回家吧。` |
| `ja` | `今日は、遠回りして帰ろう。` |
| `ko` | `오늘은 조금 돌아서 집에 가자.` |
| `es` | `Hoy volvamos a casa por el camino largo.` |
| `fr` | `Aujourd'hui, prenons le chemin le plus long pour rentrer.` |
| `de` | `Lass uns heute den längeren Weg nach Hause nehmen.` |
| `pt-BR` | `Hoje, vamos voltar para casa pelo caminho mais longo.` |
| `it` | `Oggi torniamo a casa facendo la strada più lunga.` |
| `ar` | `لنعد إلى المنزل اليوم عبر الطريق الأطول.` |
| `ru` | `Давай сегодня пойдём домой длинной дорогой.` |
| `id` | `Hari ini, mari kita pulang lewat jalan yang lebih panjang.` |
| `th` | `วันนี้กลับบ้านทางอ้อมกันเถอะ` |
| `vi` | `Hôm nay mình đi đường vòng về nhà nhé.` |

这些句子用于技术测试，不代表所有地区唯一或最佳的表达。面向正式营销、教育或公共信息时，应由目标地区的母语审校者确认语气、文化和术语。

## 推荐提示词结构

### 对白

```text
Spoken language: {LANGUAGE_NAME}.
Speaker: the person in the blue jacket only.
Exact dialogue at 6s, spoken once with natural conversational pacing: "{EXACT_DIALOGUE}"
Do not translate, paraphrase, repeat, overlap or subtitle the dialogue.
All other people remain silent.
```

### 屏幕文字

```text
On-screen language: {LANGUAGE_NAME}.
Exact title: "{EXACT_TEXT}"
Place it centered in the upper third from 7s to 10s, large and fully readable.
Preserve every character, accent, punctuation mark and capitalization exactly.
No other text anywhere in the video.
```

### 阿拉伯语 RTL

```text
On-screen language: Modern Standard Arabic.
Text direction: right-to-left.
Exact title: "رحلات صغيرة"
Keep the full phrase connected and right-aligned. Do not reverse character order.
No Latin placeholder text and no other text.
```

### 繁体中文

```text
Spoken language: Mandarin Chinese.
On-screen script: Traditional Chinese used in Taiwan.
Exact title: "小小旅程"
Do not convert any character to Simplified Chinese. No other text.
```

## 六个共享测试场景

使用相同的场景 ID 和镜头设置，团队可以比较各语言的语音、口型、文字、节奏和本地化质量。

### ML-01｜一句单人对白

```text
Format: 16:9, 10 seconds, one continuous medium shot.
At a quiet tram stop after rain, one adult in a blue jacket watches warm tram lights approach. At 6s, they turn slightly toward a silent companion and speak one exact line.

Spoken language: {LANGUAGE_NAME}.
Exact dialogue, spoken once: "{ML-01_TRANSLATION}"
Do not translate, paraphrase, repeat or subtitle it. The companion remains silent.
Audio: rain drips, distant tram, clear close voice. No music.
Keep face, clothing, camera and lighting unchanged. No text, logos or watermark.
```

**测试：** 发音、口型、说话人归属、重复台词、静默角色。

### ML-02｜产品结束卡

```text
Create a 9:16, 10-second unbranded product film for a cobalt-blue scarf. The final frame is a clean folded product on a wooden bench.

From 7s to 10s show one exact localized title: "{LOCALIZED_TAGLINE}"
Language: {LANGUAGE_NAME}. Preserve every character and punctuation mark exactly. Use large, high-contrast type within the vertical safe area. No other text.
Audio: wool movement, winter wind, one original piano chord. No dialogue.
```

**测试：** 字符完整性、拼写、RTL、自动换行、移动端安全区。

### ML-03｜两人轮流对白

```text
Format: 16:9, 10 seconds, locked two-shot in a small bakery.
[3s] Speaker A says exactly: "{LINE_A}"
[7s] Speaker B answers exactly: "{LINE_B}"
Spoken language: {LANGUAGE_NAME}. Each line is spoken once. Never swap, overlap, translate, repeat or subtitle the lines.
Audio: room tone and two spatially distinct voices. No music.
```

**测试：** 说话人分配、重叠、口型、两种声线、时间点。

### ML-04｜旁白与环境声

```text
Create a 10-second museum artifact close-up. No person appears.
One calm narrator speaks exactly once in {LANGUAGE_NAME}: "{NARRATION}"
Keep the voice centered and intelligible while soft gallery ambience remains in the background. No subtitles, music or extra speech.
```

**测试：** 旁白清晰度、专有名词、环境声遮蔽、无人物口型。

### ML-05｜一句安全口令

```text
Create a grounded maritime training scene with two adult crew members. At 5s the lead crew member gives one short safety call in {LANGUAGE_NAME}: "{SAFETY_CALL}"
The second person acknowledges only with a hand signal and stays silent. No panic, injury or emergency claim.
Audio: engine, wind, water, one clear voice. No music or subtitles.
```

**测试：** 简短指令、噪声中的可懂度、行业术语、说话人唯一性。正式安全内容必须由专业人员复核。

### ML-06｜无对白无障碍版本

```text
Create a 9:16, 10-second silent instructional video showing three clear steps for folding a paper envelope. Fixed top-down camera; one pair of adult hands; each step ends in a two-second hold.
No dialogue, narration or music. Use only paper contact sounds.
Do not generate text inside the video. Reserve empty lower-third space for professionally authored captions in post-production.
```

**测试：** 在模型内生成文字不稳定时，是否能保留后期字幕安全区；动作能否在无声音的情况下理解。

## 本地化工作流

1. **先建立语言无关母版。** 锁定镜头、角色、动作、产品和声音结构，暂不加入文字。
2. **制作英文 360p 基准。** 因英语经过完整评估，用它判断场景本身是否成立。
3. **每次只替换一种内容。** 先测试对白，再测试屏幕文字，不要同时改场景和语言。
4. **每种语言独立生成。** 不在同一次 10 秒生成中塞入多个语言版本。
5. **母语审核。** 检查语义、语气、口音、字符、断行、文化与行业术语。
6. **失败时使用局部编辑。** 例如：`Change only the final title to ... Keep everything else the same.`
7. **无法稳定时转后期。** 生成无字、无字幕画面，在后期添加经过审核的文字、字幕或配音。
8. **记录版本。** 文件名、locale、提示词、模型、日期、interaction ID、素材版本和审核者都应可追溯。

建议文件名：

```text
campaign_scene01_zh-CN_v03_360p.mp4
campaign_scene01_ar_v02_textless.mp4
campaign_scene01_pt-BR_v05_approved.mp4
```

## 不同语言的版面风险

- **德语、法语、葡萄牙语：** 翻译常比英语长，不能沿用同一窄文本框。
- **中文、日文、韩文：** 字符信息密度高，但小字号笔画容易糊；减少字数而不是无限缩小。
- **阿拉伯语：** 需要从右到左布局；数字、拉丁品牌名和标点混排要逐帧检查。
- **泰语：** 自动断行可能破坏阅读；尽量使用单行短标题。
- **越南语：** 多个附加符号不可丢失；检查字体是否完整支持。
- **俄语：** 防止形似拉丁字母混入西里尔词语。
- **西班牙语：** 问句和感叹句需要保留开头的 `¿`、`¡`（如果原文包含）。
- **繁体中文：** 明确目标地区用字，不要把简繁转换当作完整本地化。

## 验收清单

- [ ] 只有指定人物说话，其他人物保持静默。
- [ ] 台词只出现一次，没有翻译、复述或自动字幕。
- [ ] 每个字符、音标、标点、大小写与原文一致。
- [ ] 文字显示时间足够，移动端安全区内可读。
- [ ] RTL 方向、断行和字符连接正确。
- [ ] 环境声和音乐没有遮盖语音。
- [ ] 角色、产品、镜头和时长没有因本地化发生变化。
- [ ] 母语审校者确认语气、术语和文化适配。
- [ ] 高风险或受监管内容由相关专业人士复核。
- [ ] 若模型内文字/语音仍不稳定，已切换为后期制作方案。

## 官方限制提醒

Gemini Omni 当前 API 不支持独立音频参考，视频参考内的音频会被忽略，也不支持语音编辑。多语言配音不能通过“上传一段目标声音让模型照读”的方式实现。请查看最新的 [Google AI 官方文档](https://ai.google.dev/gemini-api/docs/omni)。
