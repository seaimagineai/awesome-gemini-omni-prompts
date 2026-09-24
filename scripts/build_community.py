#!/usr/bin/env python3
"""Render attributed community study notes from the checked source manifest."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'data/community-examples.json').read_text())
s='''# Official and community video studies

[Home](../README.md) · [中文主页](../README_ZH.md) · [SeaImagine workflow](seaimagine-workflow.md) · [Media reuse guide](reference-videos.md)

Learn one technique from each linked original, then test it with your own media. These are Google or creator examples, **not SeaImagine-generated outputs**. Links and metadata were checked on **2026-09-24**; videos were not independently played or regenerated.

## Official Gemini Omni 1.1 Flash examples

Google's [1.1 Flash announcement](OFFICIAL) provides these specific video assets. The original page explains their context. An API demonstration does not mean the same controls are exposed in every web editor. These are viewing links, not a grant to reuse the footage.

| Study | Official video | What to practice |
|---|---|---|
'''.replace('OFFICIAL',d['official']['url'])
for c in d['official']['suggested_cases']:
 s+=f"| {c['title']} | [Watch Google's video]({c['url']}) | {c['learning_note']} |\n"
s+='''
Also see [Google DeepMind's full showcase](https://deepmind.google/models/gemini-omni/) and [official prompting guide](https://deepmind.google/models/gemini-omni/prompt-guide/). Start with a single edit, explicit reference roles, or a first/last-frame transition rather than combining every control in one shot.

## Six X community examples

These May 2026 examples concern the initial **Gemini Omni / Flash** release; they are **not confirmed 1.1 Flash tests**. The first three were quoted by Google AI. Others are included for a clear teaching technique and observable engagement, not a claim that they passed a reproducibility benchmark.

Native X pages were access-blocked during research. Author text, attachment metadata, quote relationships, and the dated engagement snapshots below were read through **FxTwitter, a third-party mirror**. Thumbnail previews link to original posts; open the original for full context. Views are not proof of quality, and the numbers can change.

'''
for i,c in enumerate(d['community'],1):
 m=c['mirror_engagement'];media=c['media'][0]
 s+=f"### {i}. {c['title']} — {c['author']}\n\n[![Preview of {c['title']} by {c['author']}]({media['thumbnail_url']})]({c['url']})\n\n[Original X post]({c['url']}) · [Mirror evidence]({c['evidence_url']})"
 if c.get('official_quote_url'):s+=f" · [Google AI quote]({c['official_quote_url']})"
 if c.get('prompt_reply_url'):s+=f" · [Author's prompt/input reply]({c['prompt_reply_url']})"
 s+=f"\n\n**Practice:** {c['learning_note']}\n\n**Source limit:** {c['limitations']}\n\n**Mirror snapshot, 2026-09-24:** {m['views']:,} views · {m['likes']:,} likes · {m['retweets']:,} reposts. Not a live popularity ranking.\n\n"
s+='''## Turn a study into your own experiment

1. Open the original and identify one visible change: subject, clothing, material, camera, or text.
2. Prepare your own permitted input. Keep the timing and camera simple.
3. State the change and what must stay fixed. If the original prompt is absent, write your own brief and label it as your adaptation.
4. Compare source and result at the beginning, middle, and end. Record failures as well as wins.

Do not infer a model's maximum duration from the length of a posted video: creators may combine clips, add comparison footage, or edit externally. Linked third-party media remains under its owners' rights and is outside the repository's MIT grant.

## 中文说明

这里收录四个谷歌官方 1.1 Flash 演示和六个 X 社区案例。社区案例来自 2026 年 5 月的 Omni / Flash，不能当成 1.1 Flash 实测。前三个案例曾被 Google AI 引用；浏览量、点赞量是 2026-09-24 的第三方镜像快照，不代表现在的排名。X 原页访问受限，未完成原生播放核验。建议学习动作触发、单项修改、参考图分工等方法，再用自己的素材测试；没有公开原提示词的案例不补造“原版提示词”。
'''
(R/'docs/community-examples.md').write_text(s)
