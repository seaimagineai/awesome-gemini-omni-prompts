# Gemini Omni プロンプト集

![Gemini Omni プロンプト集](assets/seaimagine-omni-hero.png)

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

<a id="video-studies"></a>

## 公式・コミュニティ事例から学ぶ

Google の公式動画は Omni 1.1 Flash の紹介です。コミュニティの投稿は2026年5月の初期 Omni / Flash の作例で、1.1の実測とは確認できていません。根拠は FxTwitter ミラーの本文とメディア情報で、X 上での直接再生は未確認です。いずれも外部の作例であり、利用するサービスでの生成結果ではありません。使える機能は各ツールで確認してください。

### Google：開始・終了フレームをつなぐ

[元の事例を見る](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

開始画像、終了画像、その間の連続した動きを別々に決めます。

同じ物を自然につながる角度で2枚撮影します。開始・終了フレームが使えれば、単純な動きでつなぎます。

### Google：ショットを延長する

[元の事例を見る](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

被写体と動く方向を保ちながら、続くカメラの動きを指定します。

自分の短い動画を使います。延長機能があれば、一続きの動作を追加し、つなぎ目の動きと光を確認します。

### CHRIS FIRST：人物をフラミンゴに

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST：人物をフラミンゴに" width="300"></a>

[元の事例を見る](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

被写体だけを変え、服と動作は残すよう指定します。手足の接触部分も確認します。

自分の動画を使い、動画編集が可能なら被写体を一つだけ置き換えます。服、姿勢、地面との接触を前後で比較します。

### Justine Moore：手拍子ごとに帽子を変える

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore：手拍子ごとに帽子を変える" width="300"></a>

[元の事例を見る](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

目に見える動作を変化の合図にし、顔、服、カメラを維持します。

カメラを固定して2回の明確な手拍子を撮影します。動画編集が可能なら手拍子ごとの帽子変更を指示し、タイミングをコマごとに確認します。

[公式・コミュニティ事例](docs/community-examples.md)

## 作例を見て、自分のプロンプトへ

元のライブラリの完全なレシピ60件を、7つのカテゴリで紹介します。場面、動作のタイミング、カメラ、音の指定方法を学び、自分のアイデアに合わせて書き換えてみましょう。

### 最初のプロンプトを試す

1. 作りたい場面に近い作例を選び、プロンプト全文をコピーします。
2. 対応する参考画像をダウンロードします。使うツールに開始フレームの指定があれば、その画像を設定します。
3. 利用できる動画の長さと解像度に合わせて時間指定を調整します。まず試作し、被写体、文字、音を確認してから、一度に一つずつ修正します。

<a id="source-examples"></a>

## コピーして試す 3 例

画像は元リポジトリから引き継いだ開始フレームの参考画像で、動画の生成結果ではありません。対応する画像を Image1 としてアップロードしてください。10 秒や音声の指定は目標であり、実際の設定に合わせて調整してください。

### 01 · 商品スピーカー：水滴のリズム

![商品スピーカー：水滴のリズム](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · 稜線を走る自転車：ドキュメンタリーの導入

![稜線を走る自転車：ドキュメンタリーの導入](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · 時計職人と紙の鳥：手描きの物語

![時計職人と紙の鳥：手描きの物語](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



## 特長

以下はプロンプトで設計する内容です。利用できる入力、編集、延長、音声、解像度は、使用するツールで選択中のモデルと画面を確認してください。まず利用可能なプレビュー設定で構図・台詞・文字を確認し、その後に仕上げます。Google の API（プログラム用インターフェース）の仕様と、使用するツールの画面上の機能は別です。

- テキスト、開始フレーム、終了フレーム、人物・商品画像、短い動画参照に対応。
- 映像だけでなく、環境音、効果音、オリジナル音楽、台詞、無音区間まで設計。
- 日本語を含む15言語の台詞、画面テキスト、RTL、改行、母語話者レビューの方法。
- `<FIRST_FRAME>`、`<LAST_FRAME>`、`<IMAGE_REF_N>`、`<VIDEO_REF_N>` の具体例。

## 60 本のプロンプト一覧

最初の 5 分類の説明は中国語、最後の 2 分類は英語です。コピー用の制御プロンプトはすべて英語で、各分類ページの全文翻訳ではありません。

- [映画・ストーリーテリング：8 例](prompts/cinematic-storytelling.md)
- [広告・SNS：8 例](prompts/commerce-social.md)
- [ドキュメンタリー・旅行・教育：8 例](prompts/documentary-education.md)
- [アニメーション・音楽・エンタメ：8 例](prompts/stylized-entertainment.md)
- [マルチモーダル制御・編集・延長：10 例](prompts/control-editing-extension.md)
- [高度な編集・カメラ・視覚変換：9 例](prompts/advanced-editing-camera.md)
- [ストーリーボード・分割画面・文字・評価：9 例](prompts/storyboard-text-evaluation.md)

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

## 関連ガイド

- [公式・コミュニティ事例](docs/community-examples.md)
- [多言語ガイド](docs/multilingual-guide.md)
- [プロンプト設計](docs/prompting-guide.md)
- [参照素材と利用許諾](docs/reference-videos.md)

<a id="brand-tools"></a>

## SeaImagine で始める

Flaq AI の元のレシピ60件を残し、独自の参考画像を使った SeaImagine の練習を3つ追加しました。このページで新しい練習、元の作例、公式・コミュニティ事例の学習ポイントを読めます。

[Gemini Omni](https://seaimagine.com/ja/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/ja/model/gemini-omni-1-1-flash/)

1. モデルページを開き、現在の利用条件、料金、設定項目を確認します。
2. 商品や人物の見た目を保つなら画像から動画を選び、参照画像を 1 枚アップロードして対応するプロンプトを貼り付けます。新しい場面はテキストから動画で試します。
3. 画面上で長さと形式を選び、まず 1 カットを試します。外見、動き、音を確認し、指示を 1 つずつ調整します。

掲載内容はプロンプトの設計例で、SeaImagine での生成結果を検証したものではありません。長さ、音声、編集、延長、参照素材への対応は選択モデルと現在の画面によります。Google API の機能が SeaImagine でも使えるとは限りません。

<a id="sea-practice"></a>

## SeaImagine 独自の参考画像で試す3つの練習

参考画像は AI で生成した練習用の開始フレームです。Gemini による動画の実測結果ではありません。SeaImagine の画面で利用できる機能に合わせて試してください。

### SEA-01 · 青緑の陶器カップで朝の商品動画

[![青緑の陶器カップで朝の商品動画](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

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

[![ペーパークラフトの港に灯りをともす](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

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

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="リネンのポーチで多言語の縦型動画" width="360"></a>

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

[SeaImagine の手順](docs/seaimagine-workflow.md)

## SeaImagine の関連ツール

別の制作入口として利用できます。現在のモデル、利用条件、料金は各ページで確認してください。本リポジトリは継続的な提供を保証しません。

- [作成する](https://seaimagine.com/ja/create/)
- [画像から動画](https://seaimagine.com/ja/image-to-video/)
- [テキストから動画](https://seaimagine.com/ja/text-to-video/)
- [AI 画像生成](https://seaimagine.com/ja/ai-image-generator/)

## 出典とライセンス

Flaq AI のリポジトリを改編し、プロンプト集と 3 枚の参照画像を引き継いでいます。すべてが SeaImagine のオリジナルではありません。Google の公式製品ではない独立したガイドです。

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
