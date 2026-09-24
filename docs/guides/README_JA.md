# Gemini Omni — 詳しいドキュメント

[全 60 件のプロンプト一覧](../../README_JA.md)

## 特長

以下はプロンプトで設計する内容です。利用できる入力、編集、延長、音声、解像度は、使用するツールで選択中のモデルと画面を確認してください。まず利用可能なプレビュー設定で構図・台詞・文字を確認し、その後に仕上げます。Google の API（プログラム用インターフェース）の仕様と、使用するツールの画面上の機能は別です。

- テキスト、開始フレーム、終了フレーム、人物・商品画像、短い動画参照に対応。
- 映像だけでなく、環境音、効果音、オリジナル音楽、台詞、無音区間まで設計。
- 日本語を含む15言語の台詞、画面テキスト、RTL、改行、母語話者レビューの方法。
- `<FIRST_FRAME>`、`<LAST_FRAME>`、`<IMAGE_REF_N>`、`<VIDEO_REF_N>` の具体例。

## 日本語の台詞を指定する

必要に応じて演出指示を英語にし、台詞と画面文字は日本語で正確に指定します。結果の発音、表記、タイミングを確認してください。

```text
Spoken language: Japanese.
Exact dialogue at 6s, spoken once with natural conversational pacing: "今日は、遠回りして帰ろう。"
Do not translate, paraphrase, repeat or subtitle the dialogue.

Exact on-screen Japanese text, centered from 7s to 10s: "小さな旅"
Preserve the characters exactly. No other text anywhere in the video.
```

## 画面文字だけを変更する

選択中のモデルが動画編集に対応している場合、完成した母版には変更点だけを短く指示します。これは字幕ファイルの編集ではなく、映像内の文字を変更する練習です。

```text
Change only the final on-screen text to Japanese: "ぬくもりを、連れて。" Preserve the exact characters, position, size and timing. Keep everything else the same.
```

## 10 秒用テンプレート

```text
Format: 9:16 vertical, 10 seconds.
Goal: [audience and intended response]
Scene: [place, time, weather, layout]
Subject: [3-5 stable identity anchors]
Subject motion: [ordered action]
Camera motion: [height, path, focus]
Environment motion: [wind, light, water, particles]
[0-3s] [hook]
[3-7s] [core action]
[7-10s] [payoff and final hold]
Audio: [foley, ambience, music, silence]
Exact dialogue in Japanese, spoken once: "[台詞]"
Preserve: [identity, object, layout, audio]
Do not include: [short concrete list]
```

<a id="sea-practice"></a>

## SeaImagine 独自の参考画像で試す3つの練習

参考画像は AI で生成した練習用の開始フレームです。Gemini による動画の実測結果ではありません。SeaImagine の画面で利用できる機能に合わせて試してください。

### SEA-01 · 青緑の陶器カップで朝の商品動画

[![青緑の陶器カップで朝の商品動画](../../assets/seaimagine-ceramic-cup.png)](../../assets/seaimagine-ceramic-cup.png)

ゆっくり寄るカメラに合わせ、取っ手、飲み口、液面を保ちます。最後に字幕用の余白を残します。

カップの画像をアップロードして動画化します。まずはゆっくり寄る動きだけを試し、取っ手と液面を確認してから字幕を加えます。

[画像から動画](https://seaimagine.com/ja/image-to-video/) · [AI 画像生成](https://seaimagine.com/ja/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · ペーパークラフトの港に灯りをともす

[![ペーパークラフトの港に灯りをともす](../../assets/seaimagine-paper-harbor.png)](../../assets/seaimagine-paper-harbor.png)

一つのショットで灯台を点灯させ、3軒の家の窓明かりを順に強めます。紙の質感と形を維持します。

港の画像をアップロードし、灯台の点灯と窓明かりの段階的な変化を指定します。最初と最後で建物の形を比べます。

[画像から動画](https://seaimagine.com/ja/image-to-video/) · [AI 画像生成](https://seaimagine.com/ja/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · リネンのポーチで多言語の縦型動画

<a href="../../assets/seaimagine-linen-pouch.png"><img src="../../assets/seaimagine-linen-pouch.png" alt="リネンのポーチで多言語の縦型動画" width="360"></a>

文字のない縦型の商品動画を作り、通常の動画編集ソフトで各言語の字幕を加えます。

ポーチの画像から縦型動画を作り、翻訳した字幕を後から加えます。短い動画編集指示は、その機能が使える場合に限ります。

[画像から動画](https://seaimagine.com/ja/image-to-video/) · [AI 画像生成](https://seaimagine.com/ja/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> 毎日を、もっと心地よく
