<div align="center">

![مكتبة أوامر Gemini Omni](assets/seaimagine-omni-hero.png)

# مكتبة أوامر Gemini Omni

**60 موجّهًا في 7 فئات، مع 6 صور مرجعية تُستخدم كمدخلات وليست نتائج توليد جرى التحقق منها.**

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)

[Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

[تصفّح حسب الفئة](#prompt-collections) · [ستة أمثلة جاهزة للنسخ](#source-examples) · [نتائج رسمية ومن المجتمع](#video-studies) · [فهرس الموجّهات الستين](docs/prompt-index.md) · [تنزيل جميع الموجّهات كنص](prompts/copy/all-prompts.txt)

</div>

<a id="prompt-collections"></a>

## تصفّح حسب الفئة

| الفئة | عدد الموجّهات | الروابط |
|---|---:|---|
| [السينما والسرد](prompts/cinematic-storytelling.md) | 8 | [عرض](prompts/cinematic-storytelling.md#case-01) |
| [الإعلانات ووسائل التواصل](prompts/commerce-social.md) | 8 | [عرض](prompts/commerce-social.md#case-01) |
| [الوثائقي والسفر والتعليم](prompts/documentary-education.md) | 8 | [عرض](prompts/documentary-education.md#case-01) |
| [الرسوم المتحركة والموسيقى والترفيه](prompts/stylized-entertainment.md) | 8 | [عرض](prompts/stylized-entertainment.md#case-01) |
| [التحكم والتحرير والتمديد](prompts/control-editing-extension.md) | 10 | [عرض](prompts/control-editing-extension.md#case-01) |
| [التحرير المتقدم والكاميرا والتحويل البصري](prompts/advanced-editing-camera.md) | 9 | [عرض](prompts/advanced-editing-camera.md#case-01) |
| [لوحات القصة وتقسيم الشاشة والنص والتقييم](prompts/storyboard-text-evaluation.md) | 9 | [عرض](prompts/storyboard-text-evaluation.md#case-01) |

[فهرس الموجّهات الستين](docs/prompt-index.md) · [تنزيل جميع الموجّهات كنص](prompts/copy/all-prompts.txt)

شروح المجموعات الخمس الأولى بالصينية، وشروح المجموعتين الأخيرتين بالإنجليزية. جميع مطالبات التحكم القابلة للنسخ بالإنجليزية. لم تُترجم نصوص المجموعات بالكامل.

<a id="source-examples"></a>

## ستة أمثلة جاهزة للنسخ

الصور المرجعية مواد إدخال وليست نتائج مولّدة.

[01 · مكبر صوت: إيقاع قطرات الماء](#example-01) · [02 · دراجة على حافة جبل: افتتاحية وثائقية](#example-02) · [03 · صانع الساعات والطيور الورقية: قصة مرسومة](#example-03) · [04 · كوب خزفي فيروزي في ضوء الصباح](#example-04) · [05 · أضواء تتعاقب في ميناء ورقي](#example-05) · [06 · كيس كتاني لفيديو متجر متعدد اللغات](#example-06)

<a id="example-01"></a>

### 01 · مكبر صوت: إيقاع قطرات الماء

<a href="assets/product-speaker.png"><img src="assets/product-speaker.png" alt="مكبر صوت: إيقاع قطرات الماء" width="420"></a>

[الإعلانات ووسائل التواصل](prompts/commerce-social.md) · [إطار أول مرجعي](assets/product-speaker.png) · [نص عادي](prompts/copy/showcase-01.txt)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

<a id="example-02"></a>

### 02 · دراجة على حافة جبل: افتتاحية وثائقية

<a href="assets/travel-cyclist.png"><img src="assets/travel-cyclist.png" alt="دراجة على حافة جبل: افتتاحية وثائقية" width="420"></a>

[الوثائقي والسفر والتعليم](prompts/documentary-education.md) · [إطار أول مرجعي](assets/travel-cyclist.png) · [نص عادي](prompts/copy/showcase-02.txt)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

<a id="example-03"></a>

### 03 · صانع الساعات والطيور الورقية: قصة مرسومة

<a href="assets/clockmaker-story.png"><img src="assets/clockmaker-story.png" alt="صانع الساعات والطيور الورقية: قصة مرسومة" width="420"></a>

[الرسوم المتحركة والموسيقى والترفيه](prompts/stylized-entertainment.md) · [إطار أول مرجعي](assets/clockmaker-story.png) · [نص عادي](prompts/copy/showcase-03.txt)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

<a id="example-04"></a>

### 04 · كوب خزفي فيروزي في ضوء الصباح

<a href="assets/seaimagine-ceramic-cup.png"><img src="assets/seaimagine-ceramic-cup.png" alt="كوب خزفي فيروزي في ضوء الصباح" width="420"></a>

[الإعلانات ووسائل التواصل](prompts/commerce-social.md) · [إطار أول مرجعي](assets/seaimagine-ceramic-cup.png) · [نص عادي](prompts/copy/showcase-04.txt)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

<a id="example-05"></a>

### 05 · أضواء تتعاقب في ميناء ورقي

<a href="assets/seaimagine-paper-harbor.png"><img src="assets/seaimagine-paper-harbor.png" alt="أضواء تتعاقب في ميناء ورقي" width="420"></a>

[الرسوم المتحركة والموسيقى والترفيه](prompts/stylized-entertainment.md) · [إطار أول مرجعي](assets/seaimagine-paper-harbor.png) · [نص عادي](prompts/copy/showcase-05.txt)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

<a id="example-06"></a>

### 06 · كيس كتاني لفيديو متجر متعدد اللغات

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="كيس كتاني لفيديو متجر متعدد اللغات" width="420"></a>

[الإعلانات ووسائل التواصل](prompts/commerce-social.md) · [إطار أول مرجعي](assets/seaimagine-linen-pouch.png) · [نص عادي](prompts/copy/showcase-06.txt)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

لحياة يومية أبسط

<a id="video-studies"></a>

## نتائج رسمية ومن المجتمع

تستخدم الأمثلة الرسمية Gemini Omni 1.1 Flash، أما أمثلة المجتمع فمن مايو 2026 وتستخدم إصدارات مبكرة من Omni. تقود الروابط إلى المنشورات الأصلية؛ ولا يدّعي هذا المستودع أنه أعاد إنتاج هذه النتائج. أدلة المجتمع مستمدة من FxTwitter؛ ولم يُتحقق من تشغيل الفيديو داخل X.

| Google · Omni 1.1 Flash | الروابط |
|---|---|
| تمديد مشهد سينمائي | [شاهد الفيديو](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| انتقال بين الإطار الأول والأخير | [شاهد الفيديو](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| مسودة لطحالب الدياتوم البحرية بدقة 360p | [شاهد الفيديو](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/kw_omni-flash__capability-video__draft-360p__16x9__v1_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| رقص موجّه بفيديو مرجعي | [شاهد الفيديو](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__video-reference__16x9.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |

| X · Omni / Flash · 2026-05 | X · Omni / Flash · 2026-05 |
|---|---|
| **تحويل الأشخاص إلى طيور فلامنغو**<br><a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="تحويل الأشخاص إلى طيور فلامنغو" width="240"></a><br>CHRIS FIRST<br>[المصدر](https://x.com/chrisfirst/status/2056797606509158681) · [شاهد الفيديو](https://video.twimg.com/amplify_video/2056797343085969408/vid/avc1/1080x1440/UYr_7RKomiginRgq.mp4?tag=27) | **قبعة جديدة مع كل تصفيقة**<br><a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="قبعة جديدة مع كل تصفيقة" width="240"></a><br>Justine Moore<br>[المصدر](https://x.com/venturetwins/status/2056793856843366789) · [شاهد الفيديو](https://video.twimg.com/amplify_video/2056793760273686528/vid/avc1/720x1280/Q73liRfIjPtGSveL.mp4?tag=27) |
| **شرح البناء الضوئي**<br><a href="https://x.com/mrfanduu/status/2056692235174097398"><img src="https://pbs.twimg.com/amplify_video_thumb/2056691792175833088/img/W0_pZkQwRicpRjjG.jpg" alt="شرح البناء الضوئي" width="240"></a><br>Fandu<br>[المصدر](https://x.com/mrfanduu/status/2056692235174097398) · [شاهد الفيديو](https://video.twimg.com/amplify_video/2056691792175833088/vid/avc1/1280x720/Ws-92fvVr5e-FkYZ.mp4?tag=14) | **تقريب يدوي نحو عين لندن**<br><a href="https://x.com/fofrAI/status/2056789242274259242"><img src="https://pbs.twimg.com/amplify_video_thumb/2056503814874861569/img/mQnHwThYDypoS1H6.jpg" alt="تقريب يدوي نحو عين لندن" width="240"></a><br>fofr<br>[المصدر](https://x.com/fofrAI/status/2056789242274259242) · [شاهد الفيديو](https://video.twimg.com/amplify_video/2056503814874861569/vid/avc1/1280x720/Lc2C4YtTflfGA8qe.mp4?tag=27) |
| **مقارنة المقطع الأصلي والمعدّل**<br><a href="https://x.com/Mho_23/status/2057151867927601413"><img src="https://pbs.twimg.com/amplify_video_thumb/2057151701904146432/img/yhVQfdBM34BQJjV3.jpg" alt="مقارنة المقطع الأصلي والمعدّل" width="240"></a><br>Miko<br>[المصدر](https://x.com/Mho_23/status/2057151867927601413) · [شاهد الفيديو](https://video.twimg.com/amplify_video/2057151701904146432/vid/avc1/1080x1920/JfeFoDd5udd_FRR7.mp4?tag=27) | **تغيّر مادة الإبريق عند لمسه**<br><a href="https://x.com/alexanderchen/status/2057176690519089166"><img src="https://pbs.twimg.com/amplify_video_thumb/2057176000459612161/img/wTZ0HcgL_8PHxwbY.jpg" alt="تغيّر مادة الإبريق عند لمسه" width="240"></a><br>Alexander Chen<br>[المصدر](https://x.com/alexanderchen/status/2057176690519089166) · [شاهد الفيديو](https://video.twimg.com/amplify_video/2057176000459612161/vid/avc1/1280x720/LRzM8IueMomPMa7J.mp4?tag=27) · [الموجّه الكامل](https://x.com/alexanderchen/status/2057176691903279524) |
[المصدر / FxTwitter](docs/community-examples.md)

## وثائق متقدمة

الشروحات متاحة في صفحات منفصلة. [عرض](docs/guides/README_AR.md)

[تصميم المطالبات](docs/prompting-guide.md) · [دليل اللغات](docs/multilingual-guide.md) · [المواد المرجعية والأذونات](docs/reference-videos.md)

<a id="brand-tools"></a>

## أنشئ باستخدام SeaImagine

[Gemini Omni](https://seaimagine.com/ar/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/ar/model/gemini-omni-1-1-flash/)

[صورة إلى فيديو](https://seaimagine.com/ar/image-to-video/) · [نص إلى فيديو](https://seaimagine.com/ar/text-to-video/) · [مولّد صور بالذكاء الاصطناعي](https://seaimagine.com/ar/ai-image-generator/)

يمكن استخدام هذه الصفحات كنقاط بداية بديلة. راجع كل صفحة لمعرفة النماذج والشروط والأسعار الحالية. لا يضمن هذا المستودع توفر الخدمة دون انقطاع.

[خطوات العمل في SeaImagine](docs/seaimagine-workflow.md)

## المصدر والترخيص

مقتبس من مستودع Flaq AI، بما فيه مجموعات المطالبات وثلاث صور مرجعية. ليست جميع المواد من إنتاج SeaImagine الأصلي. هذا دليل مستقل وليس منتجًا رسميًا من Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE) · [Contributing](CONTRIBUTING.md)
