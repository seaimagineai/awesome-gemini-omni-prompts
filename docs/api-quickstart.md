# Gemini Omni 1.1 Flash API 快速开始

[← 返回中文主页](../README_ZH.md) · [English home](../README.md) · [15 种语言本地化](multilingual-guide.md) · [提示词设计指南](prompting-guide.md)

**这是 Google 官方 API（应用编程接口）参考，不是 SeaImagine 网页或 SeaImagine 接口教程。** 本仓库未实际调用这些代码；网页用户先看 [SeaImagine 创作指南](seaimagine-workflow.md)。

以下示例依据 Gemini API 的 Interactions API 形态编写。接口仍可能变化；运行前请查看 [官方 Omni 文档](https://ai.google.dev/gemini-api/docs/omni)。不要把 API key 写进仓库。

## 运行前准备

这是直接调用 Google Gemini API 的可选开发者路线。API key（接口密钥）需要从 [Google AI Studio](https://aistudio.google.com/apikey) 创建，并确认账号有该模型所需的访问权限和计费设置；SeaImagine 的账号或积分不能代替 Google API 账号。

Python 先创建虚拟环境，再安装 [官方 SDK（开发工具包）](https://ai.google.dev/gemini-api/docs/libraries)：

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade google-genai
```

JavaScript 使用 Node.js，并安装同一套官方工具包：

```sh
npm install @google/genai
```

将下面 JavaScript 示例保存为 `example.mjs`，用 `node example.mjs` 运行。Python 示例可保存为 `example.py`，用 `python3 example.py` 运行。两者都需要在本机按 [官方密钥设置说明](https://ai.google.dev/gemini-api/docs/api-key) 配置环境变量 `GEMINI_API_KEY`。不要把密钥写入代码、提交到仓库或放入截图。本文的 shell 命令适用于 macOS/Linux；Windows 按官方文档设置环境变量和激活虚拟环境。

这些示例未在本项目中实际发起生成。如果出现权限、余额、模型名称或字段错误，先查看官方当前文档；不要把失败解释为提示词本身无效。

## Python：360p 文生视频草稿

```python
import base64
from google import genai

client = genai.Client()

result = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=(
        "A single continuous shot of a paper boat traveling through a rainy "
        "street gutter at blue hour. Realistic water flow and close rain audio. "
        "No dialogue, text, logo or watermark."
    ),
    response_format={
        "type": "video",
        "aspect_ratio": "16:9",
        "resolution": "360p",
    },
)

with open("draft.mp4", "wb") as video:
    video.write(base64.b64decode(result.output_video.data))
```

分辨率可设为 `360p`、`720p`、`1080p` 或 `4k`；后两者为放大输出。默认画幅是 16:9，也可使用 9:16。

## JavaScript：竖屏视频

```javascript
import { GoogleGenAI } from "@google/genai";
import { writeFileSync } from "node:fs";

const ai = new GoogleGenAI({});

const result = await ai.interactions.create({
  model: "gemini-omni-1.1-flash",
  input:
    "A 10-second vertical macro food film of citrus peel over iced coffee. " +
    "Natural café audio, no dialogue, no text, no logo or watermark.",
  response_format: {
    type: "video",
    aspect_ratio: "9:16",
    resolution: "360p",
  },
});

writeFileSync(
  "vertical-draft.mp4",
  Buffer.from(result.output_video.data, "base64"),
);
```

## Python：图片作为首帧

```python
import base64
from pathlib import Path
from google import genai

client = genai.Client()
image_b64 = base64.b64encode(Path("first-frame.jpg").read_bytes()).decode()

result = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": image_b64, "mime_type": "image/jpeg"},
        {
            "type": "text",
            "text": (
                "<FIRST_FRAME> Use this image as the exact first frame. "
                "Animate a slow forward camera move while wind travels through "
                "the grass from left to right. Preserve the person and landscape."
            ),
        },
    ],
    generation_config={"video_config": {"task": "image_to_video"}},
)

Path("image-to-video.mp4").write_bytes(
    base64.b64decode(result.output_video.data)
)
```

`task` 通常不必设置；只有自然语言持续被误判时再显式指定。

## Python：首尾帧插值

```python
import base64
from pathlib import Path
from google import genai

def encoded(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode()

client = genai.Client()
result = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input=[
        {"type": "image", "data": encoded("summer.jpg"), "mime_type": "image/jpeg"},
        {"type": "image", "data": encoded("winter.jpg"), "mime_type": "image/jpeg"},
        {
            "type": "text",
            "text": (
                "<FIRST_FRAME> <LAST_FRAME> Transition continuously from summer "
                "to winter. Lock camera and landscape geometry. Leaves yellow, "
                "fall, frost forms, then snow accumulates. End exactly on Image2."
            ),
        },
    ],
)

Path("seasons.mp4").write_bytes(base64.b64decode(result.output_video.data))
```

## 多轮编辑

```python
import base64
from pathlib import Path
from google import genai

client = genai.Client()

first = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A woman reading beside a greenhouse window. No dialogue.",
)

edited = client.interactions.create(
    model="gemini-omni-1.1-flash",
    previous_interaction_id=first.id,
    input=(
        "Add light rain outside the window only. Keep the interior, person, "
        "camera, timing and audio exactly the same."
    ),
)

Path("edited.mp4").write_bytes(base64.b64decode(edited.output_video.data))
```

要继续编辑，交互必须被保存。追求一次性低延迟而设置 `store=false` 后，不能再依赖 `previous_interaction_id` 修改该视频。

## 多轮续写

```python
continued = client.interactions.create(
    model="gemini-omni-1.1-flash",
    previous_interaction_id=first.id,
    input=(
        "Extend by 8 seconds. Continue the same shot as she closes the book, "
        "opens the window, and listens to the rain. Preserve identity, room, "
        "camera and color. The rain becomes louder; no dialogue."
    ),
)
```

一次续写会追加 3–10 秒，最长可形成 40 秒视频。时间码的 0 秒指新增片段开始，而不是整条视频开头。

## 大文件使用 URI 交付

高于 720p 的视频通常超过 4 MB，建议请求 URI：

```python
result = client.interactions.create(
    model="gemini-omni-1.1-flash",
    input="A wide mountain sunrise, slow aerial move, natural wind, no dialogue.",
    response_format={
        "type": "video",
        "resolution": "1080p",
        "delivery": "uri",
    },
)
```

随后按官方示例轮询文件状态并下载。创建响应中的 URI 最可靠；稍后读取 interaction 时可能返回内联 base64。

## 生产前检查

- API key 只放环境变量或密钥管理服务。
- 高分辨率前先以 360p 验证构图、时间线和声音。
- 大文件使用 URI 交付，避免内联响应大小限制。
- 为每次生成记录提示词、素材版本、interaction ID、模型名和日期。
- 编辑时一次修改一个变量；保留未修改项。
- 根据地区确认上传人物、未成年人素材与视频编辑能力是否可用。
- 生成视频含不可见 SynthID；对外发布时保留适当的 AI 内容披露。
