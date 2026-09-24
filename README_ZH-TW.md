# Gemini Omni 提示詞庫

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

<a id="video-studies"></a>

## 從官方與社群案例學什麼

Google 影片是 Omni 1.1 Flash 官方展示。社群貼文發布於 2026 年 5 月，屬於早期 Omni / Flash 案例，未確認為 1.1 實測。社群證據來自 FxTwitter 鏡像的文字與媒體中繼資料，未驗證 X 原生播放。這些是獨立來源的案例，不代表你使用的平台所生成的結果；實際功能請查看所用工具。

### Google：首尾幀轉場

[查看原始案例](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

分別指定起始畫面、結束畫面，以及兩者之間連續的運動。

為同一物件準備兩張角度相容的照片；若支援首尾幀，以一個簡單動作連接兩張圖。

### Google：延長鏡頭

[查看原始案例](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

描述下一段鏡頭運動，同時維持主體與運動方向一致。

使用自己的短片；若支援延長，只接續一段動作，檢查接點的運動與光線是否突然改變。

### CHRIS FIRST：人物變成紅鶴

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST：人物變成紅鶴" width="300"></a>

[查看原始案例](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

替換主體時明確保留服裝和動作，並檢查肢體接觸的位置。

使用自己的影片；若支援影片編輯，只替換一個主體，比較前後的服裝、姿勢與觸地位置。

### Justine Moore：每次拍手換一頂帽子

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore：每次拍手換一頂帽子" width="300"></a>

[查看原始案例](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

以可見動作決定變化時機，同時維持臉孔、服裝和鏡頭一致。

固定攝影機，拍攝兩次清楚的拍手；若支援影片編輯，要求每次拍手換帽，逐格檢查時間點。

[官方與社群案例](docs/community-examples.md)

## 從看案例，到自己寫提示詞

本庫收錄原始資料庫的 60 組完整提示詞，分為 7 類。透過範例學習如何描述場景、安排動作時間、控制鏡頭與聲音，再改成自己的創意。

### 開始第一次嘗試

1. 選擇接近你想做的場景的完整範例，複製全部提示詞。
2. 下載範例對應的參考圖；若使用的工具支援首幀，請將圖片設為首幀。
3. 依工具可用的片長與解析度調整時間段，先生成草稿，檢查主體、文字與聲音，每次只改一項。

<a id="source-examples"></a>

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



## 專案內容

以下是提示詞可規劃的內容，不代表所選工具的每個模型都提供這些功能。輸入素材、編輯、續寫、聲音與解析度請以所選模型及目前介面為準。先用介面提供的預覽設定檢查構圖、對白與文字，再製作成片。Google API（程式呼叫介面）的規格不等於所選工具的網頁功能。

- 文字轉影片、圖片轉影片、首尾幀、角色/商品參考與短影片參考。
- 將環境聲、擬音、原創音樂、靜默與對白時間一起設計。
- 15 種語言的對白、螢幕文字、RTL、斷行與母語審核規則。
- 使用 `<FIRST_FRAME>`、`<LAST_FRAME>`、`<IMAGE_REF_N>`、`<VIDEO_REF_N>` 的完整範例。

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
On-screen script: Traditional Chinese used in Taiwan.
Exact dialogue at 6s, spoken once: "今天，繞遠一點回家吧。"
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen title: "小小旅程"
Do not convert any character to Simplified Chinese. No other text.
```

## 延伸閱讀

- [官方與社群案例](docs/community-examples.md)
- [多語言指南](docs/multilingual-guide.md)
- [提示詞設計](docs/prompting-guide.md)
- [參考素材與授權](docs/reference-videos.md)

<a id="brand-tools"></a>

## 從 SeaImagine 開始

![SeaImagine Gemini Omni 影片提示詞庫](assets/seaimagine-omni-hero.png)

本庫保留 Flaq AI 的 60 條原始配方，並新增三組附原創參考圖的 SeaImagine 練習。本頁可直接閱讀新練習、來源庫範例，以及官方與社群案例的學習說明。

[Gemini Omni](https://seaimagine.com/tw/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/tw/model/gemini-omni-1-1-flash/)

1. 開啟模型頁，確認目前是否可用、價格及可調整的設定。
2. 需要保留商品或人物外觀時，選擇圖片轉影片，上傳一張參考圖並貼上對應提示詞；從零構思場景時，可先試文字轉影片。
3. 在介面選擇片長及畫面比例，先試一個鏡頭。檢查外觀、動作與聲音，每次只調整一項指令。

這裡是提示詞設計範例，並非已驗證的 SeaImagine 生成結果。片長、聲音、編輯、延長及參考素材支援取決於所選模型與目前介面。Google API 功能不代表 SeaImagine 已提供相同功能。

<a id="sea-practice"></a>

## 三個 SeaImagine 原創參考圖練習

以下參考圖由 AI 生成，用於首幀練習，並非 Gemini 影片實測結果。請以 SeaImagine 介面實際提供的功能為準。

### SEA-01 · 青綠色陶瓷杯：清晨商品短片

[![青綠色陶瓷杯：清晨商品短片](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

鏡頭緩慢推近，保持杯把、杯口和液面高度不變，結尾預留字幕空間。

上傳杯子參考圖製作圖生影片。先只嘗試緩慢推近，檢查杯把和液面，再加入字幕。

[圖片轉影片](https://seaimagine.com/tw/image-to-video/) · [AI 圖片生成](https://seaimagine.com/tw/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · 紙藝海港：點亮燈塔與窗光

[![紙藝海港：點亮燈塔與窗光](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

以單一鏡頭讓燈塔亮起，再讓三棟房屋的窗光依序增強，保持紙張質感與幾何結構。

上傳海港參考圖製作圖生影片。要求燈塔亮起、窗光依序增強，比較片頭和片尾的建築形狀。

[圖片轉影片](https://seaimagine.com/tw/image-to-video/) · [AI 圖片生成](https://seaimagine.com/tw/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · 亞麻收納袋：多語言直式片尾

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="亞麻收納袋：多語言直式片尾" width="360"></a>

先製作不含文字的乾淨直式商品影片，再以一般影片編輯器加入在地語言字幕。

上傳收納袋參考圖製作直式短片，再加入翻譯好的字幕；僅在介面支援影片編輯時使用簡短編輯指令。

[圖片轉影片](https://seaimagine.com/tw/image-to-video/) · [AI 圖片生成](https://seaimagine.com/tw/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> 讓日常更從容

[SeaImagine 使用流程](docs/seaimagine-workflow.md)

## SeaImagine 其他創作入口

可將這些頁面作為其他創作入口。模型、使用條款及價格以各頁面目前顯示為準，本儲存庫不保證服務持續可用。

- [開始創作](https://seaimagine.com/tw/create/)
- [圖片轉影片](https://seaimagine.com/tw/image-to-video/)
- [文字轉影片](https://seaimagine.com/tw/text-to-video/)
- [AI 圖片生成](https://seaimagine.com/tw/ai-image-generator/)

## 來源與授權條款

本儲存庫改編自 Flaq AI 專案，沿用提示詞集合與 3 張參考圖，並非全部由 SeaImagine 原創。本專案是獨立指南，不是 Google 官方產品。

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
