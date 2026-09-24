# Gemini Omni — 進階文件

[全部 60 則提示詞索引](../../README_ZH-TW.md)

## 專案內容

以下是提示詞可規劃的內容，不代表所選工具的每個模型都提供這些功能。輸入素材、編輯、續寫、聲音與解析度請以所選模型及目前介面為準。先用介面提供的預覽設定檢查構圖、對白與文字，再製作成片。Google API（程式呼叫介面）的規格不等於所選工具的網頁功能。

- 文字轉影片、圖片轉影片、首尾幀、角色/商品參考與短影片參考。
- 將環境聲、擬音、原創音樂、靜默與對白時間一起設計。
- 15 種語言的對白、螢幕文字、RTL、斷行與母語審核規則。
- 使用 `<FIRST_FRAME>`、`<LAST_FRAME>`、`<IMAGE_REF_N>`、`<VIDEO_REF_N>` 的完整範例。

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



<a id="sea-practice"></a>

## 三個 SeaImagine 原創參考圖練習

以下參考圖由 AI 生成，用於首幀練習，並非 Gemini 影片實測結果。請以 SeaImagine 介面實際提供的功能為準。

### SEA-01 · 青綠色陶瓷杯：清晨商品短片

[![青綠色陶瓷杯：清晨商品短片](../../assets/seaimagine-ceramic-cup.png)](../../assets/seaimagine-ceramic-cup.png)

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

[![紙藝海港：點亮燈塔與窗光](../../assets/seaimagine-paper-harbor.png)](../../assets/seaimagine-paper-harbor.png)

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

<a href="../../assets/seaimagine-linen-pouch.png"><img src="../../assets/seaimagine-linen-pouch.png" alt="亞麻收納袋：多語言直式片尾" width="360"></a>

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
