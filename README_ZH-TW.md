# SeaImagine Gemini Omni 影片提示詞庫

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![SeaImagine Gemini Omni 影片提示詞庫](assets/seaimagine-omni-hero.png)

從 Flaq AI 原始儲存庫改編 60 則提示詞，為 SeaImagine 使用者整理商品廣告、旅行鏡頭、動畫與影片編輯靈感。以下 3 個範例附參考圖及完整英文提示詞，可複製並依實際介面調整。

[Gemini Omni](https://seaimagine.com/tw/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/tw/model/gemini-omni-1-1-flash/)

## 從 SeaImagine 開始

1. 開啟模型頁，確認目前是否可用、價格及可調整的設定。
2. 需要保留商品或人物外觀時，選擇圖片轉影片，上傳一張參考圖並貼上對應提示詞；從零構思場景時，可先試文字轉影片。
3. 在介面選擇片長及畫面比例，先試一個鏡頭。檢查外觀、動作與聲音，每次只調整一項指令。

這裡是提示詞設計範例，並非已驗證的 SeaImagine 生成結果。片長、聲音、編輯、延長及參考素材支援取決於所選模型與目前介面。Google API 功能不代表 SeaImagine 已提供相同功能。

## 三個可複製的範例

圖片沿用原始儲存庫的參考首幀，並非實際影片生成結果。請將對應圖片上傳為 Image1。10 秒及音效是目標要求，請依實際可用設定調整。

### 01 · 商品音箱：水滴節拍

![商品音箱：水滴節拍](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · 山稜單車：旅行紀錄片開場

![山稜單車：旅行紀錄片開場](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · 鐘錶匠與紙鳥：手繪動畫故事

![鐘錶匠與紙鳥：手繪動畫故事](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

## 全部 60 則提示詞

前 5 個分類的說明為簡體中文，後 2 個為英文；可複製的控制提示詞皆為英文。分類內文尚未完整翻譯成各入口語言。

- [電影與敘事：8 條](prompts/cinematic-storytelling.md)
- [商業廣告與社群媒體：8 條](prompts/commerce-social.md)
- [紀錄片、旅行與教育：8 條](prompts/documentary-education.md)
- [動畫、音樂與娛樂：8 條](prompts/stylized-entertainment.md)
- [多模態控制、編輯與續寫：10 條](prompts/control-editing-extension.md)
- [進階編輯、鏡頭與視覺變換：9 條](prompts/advanced-editing-camera.md)
- [故事板、分割畫面、文字與評測：9 條](prompts/storyboard-text-evaluation.md)

## 指定中文對白

可保留英文鏡頭指令，以中文逐字指定對白與畫面文字。生成後檢查發音、字形及出現時間。

```text
Spoken language: Mandarin Chinese.
Exact dialogue, spoken once: "今天，我們走遠一點。"
Do not translate, paraphrase, repeat or subtitle it.
```

## 延伸閱讀

- [SeaImagine 使用流程](docs/seaimagine-workflow.md)
- [官方與社群案例](docs/community-examples.md)
- [多語言指南](docs/multilingual-guide.md)
- [提示詞設計](docs/prompting-guide.md)
- [參考素材與授權](docs/reference-videos.md)

## SeaImagine 其他創作入口

可將這些頁面作為其他創作入口。模型、使用條款及價格以各頁面目前顯示為準，本儲存庫不保證服務持續可用。

- [開始創作](https://seaimagine.com/tw/create/)
- [圖片轉影片](https://seaimagine.com/tw/image-to-video/)
- [文字轉影片](https://seaimagine.com/tw/text-to-video/)
- [AI 圖片生成](https://seaimagine.com/tw/ai-image-generator/)

## 來源與授權條款

本儲存庫改編自 Flaq AI 專案，沿用提示詞集合與 3 張參考圖，並非全部由 SeaImagine 原創。本專案是獨立指南，不是 Google 官方產品。

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
