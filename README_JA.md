# SeaImagine の Gemini Omni 動画プロンプト集

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![SeaImagine の Gemini Omni 動画プロンプト集](assets/seaimagine-omni-hero.png)

Flaq AI の元リポジトリにある 60 本のプロンプトを SeaImagine の読者向けに再構成しました。商品広告、旅の映像、アニメーション、編集のアイデアを探せます。下の 3 例には参照画像とコピーできる英語プロンプトを添えています。

[Gemini Omni](https://seaimagine.com/ja/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/ja/model/gemini-omni-1-1-flash/)

## SeaImagine で始める

1. モデルページを開き、現在の利用条件、料金、設定項目を確認します。
2. 商品や人物の見た目を保つなら画像から動画を選び、参照画像を 1 枚アップロードして対応するプロンプトを貼り付けます。新しい場面はテキストから動画で試します。
3. 画面上で長さと形式を選び、まず 1 カットを試します。外見、動き、音を確認し、指示を 1 つずつ調整します。

掲載内容はプロンプトの設計例で、SeaImagine での生成結果を検証したものではありません。長さ、音声、編集、延長、参照素材への対応は選択モデルと現在の画面によります。Google API の機能が SeaImagine でも使えるとは限りません。

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

## 関連ガイド

- [SeaImagine の手順](docs/seaimagine-workflow.md)
- [公式・コミュニティ事例](docs/community-examples.md)
- [多言語ガイド](docs/multilingual-guide.md)
- [プロンプト設計](docs/prompting-guide.md)
- [参照素材と利用許諾](docs/reference-videos.md)

## SeaImagine の関連ツール

別の制作入口として利用できます。現在のモデル、利用条件、料金は各ページで確認してください。本リポジトリは継続的な提供を保証しません。

- [作成する](https://seaimagine.com/ja/create/)
- [画像から動画](https://seaimagine.com/ja/image-to-video/)
- [テキストから動画](https://seaimagine.com/ja/text-to-video/)
- [AI 画像生成](https://seaimagine.com/ja/ai-image-generator/)

## 出典とライセンス

Flaq AI のリポジトリを改編し、プロンプト集と 3 枚の参照画像を引き継いでいます。すべてが SeaImagine のオリジナルではありません。Google の公式製品ではない独立したガイドです。

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
