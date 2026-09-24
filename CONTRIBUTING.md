# Contributing

感谢你帮助建设一份真正可执行、可验证、可合法分享的 Gemini Omni 1.1 Flash 提示词库。

## 提交什么

- 经过至少一次 360p 测试的原创提示词。
- 现有提示词的单变量改进，并说明改善了什么。
- 可重复的失败案例，以及失败发生的模型、日期和输入类型。
- 已获授权、可随仓库分发的原创首帧/尾帧/参考素材。
- 对官方能力、限制或 API 变化的修正，附官方来源。

## 不接受什么

- 从其他提示词集合、社交平台或创作者复制/轻改的内容。
- 保留第三方作者名、推广链接、追踪链接、平台水印或来源不明的媒体。
- 未授权品牌、真人、影视角色、音乐、艺术作品或数据。
- 要求模仿在世艺术家独特风格的提示词。
- 只有一串风格形容词、没有动作/镜头/声音设计的低信息提示词。
- 声称模型支持官方文档未确认的参数或能力。

## 提示词格式

每个条目至少包括：

```markdown
## 编号｜原创标题

**模式：** 文生视频 / 首帧 / 首尾帧 / 参考图 / 视频参考 / 编辑 / 续写
**画幅：** 16:9 / 9:16
**测试：** 360p，YYYY-MM-DD（可选但推荐）

```text
Format and goal...
Scene and subject...
Subject, camera and environment motion...
Timing...
Audio...
Preserve...
Do not include...
```

**观察：** 成功点、失败点和可调参数。
```

## 原创性与授权清单

提交前请确认：

- [ ] 提示词由我原创，或我的改动具有明确且实质性的新增价值。
- [ ] 没有复制第三方描述、标题、台词、角色设定或独特场景组合。
- [ ] 所有上传素材可合法使用并允许在 MIT 仓库中分发。
- [ ] 没有第三方品牌、个人信息、水印或未经同意的真人肖像。
- [ ] 音乐被描述为原创，不要求复现现有歌曲、旋律或艺人声音。
- [ ] 事实性内容已有可靠来源；高风险内容已由相关专业人士复核。

## 写作原则

1. 标题准确描述用途，避免堆关键词。
2. 用具体动作替代空泛质量词。
3. 每张参考素材只承担一种职责。
4. 对白和屏幕文字必须逐字引用并指定语言。
5. 编辑提示词一次只改一项。
6. 排除项保持短、具体、与该镜头相关。
7. 不承诺确定性结果；记录可观察到的表现。

## 图片规范

- 建议 16:9、至少 1280×720，PNG、JPEG 或 WebP。
- 文件名使用小写英文与连字符。
- 不包含文字、Logo、水印或不可验证的版权元素。
- 在条目中说明图片角色：首帧、尾帧、角色、产品、风格或其他参考。
- 尽量提供图片生成提示词或制作说明，便于追溯。

## 多语言贡献规范

- 使用 BCP 47 或清晰 locale 标记，例如 `zh-CN`、`zh-TW`、`pt-BR`、`ar`。
- 保持镜头、角色、动作和声音结构不变，只替换目标语言内容，方便横向比较。
- 对白必须标明说话人、语言、精确原文、出现时间、是否允许字幕，以及 `spoken once`。
- 屏幕文字必须标明精确字符、书写方向、位置、字号/安全区、显示时长和“无其他文字”。
- 阿拉伯语等 RTL 内容需要检查字符连接、顺序、标点、数字和拉丁文字混排。
- 中文应注明简体或繁体及目标地区；葡萄牙语应注明巴西或葡萄牙变体。
- 提交者应说明是否经过母语者审核；未经审核的翻译必须明确标注。
- 高风险、受监管或专业术语内容需要目标语言领域专家复核。
- 生成内文字或语音不稳定时，优先提交无字/无对白母版与后期本地化建议。

共享测试场景、15 种语言代码与验收清单见 [多语言视频指南](docs/multilingual-guide.md)。

## 提交前检查

- 所有相对链接都能打开。
- Markdown 代码围栏闭合。
- 统计数量与目录一致。
- 新增内容不包含敏感密钥或个人数据。
- 使用官方文档链接支持随时间变化的能力说明。

提交即表示你同意贡献内容按本仓库的 [MIT License](LICENSE) 发布。


## Maintain generated pages

Keep the homepage order: official and community examples → library introduction and usage → complete prompts and teaching → SeaImagine products and exercises. Edit neutral opening copy and contextual platform wording in `data/editorial-copy.json`, basic localized copy in `data/locale-copy.json`, the new practice/study explanations in `data/homepage-additions.json`, shared new prompts in `data/brand-examples.json`, and retained teaching templates in `templates/locales/`. Run `python3 scripts/build_locales.py` to regenerate language homepages and the illustrated practice section in the SeaImagine guide. English is authored in `README.md` outside its marked generated sections. Do not edit inside those sections; the generator owns them. Edit sourced case records in `data/community-examples.json` and run `python3 scripts/build_community.py`. Run `python3 scripts/validate.py` and `git diff --check` before submitting. Never replace evidence limits with an unsupported “tested” or “stable” claim.
