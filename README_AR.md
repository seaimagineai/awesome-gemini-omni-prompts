<div align="center">

![مكتبة أوامر Gemini Omni](assets/seaimagine-omni-hero.png)

# مكتبة أوامر Gemini Omni

**استكشف 60 وصفة كاملة من المكتبة الأصلية، موزعة على سبع فئات. تعلّم وصف المشهد وتوقيت الأفعال وتوجيه الكاميرا والصوت، ثم عدّل أحد الأمثلة ليناسب فكرتك.**

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)

[Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)



[المطالبات الستون كاملة](#prompt-collections) · [ثلاث مطالبات للنسخ](#source-examples) · [أمثلة رسمية ومن المجتمع](#video-studies) · [دليل اللغات](docs/multilingual-guide.md)

</div>

## ما الذي يتضمنه المشروع؟

تصف القائمة ما يمكن تخطيطه بالمطالبات، ولا تضمن توفر كل ميزة. تحقّق من المدخلات والتحرير والتمديد والصوت والدقة المتاحة للنموذج المحدد في أداتك. اختبر التكوين والحوار والنص بإعداد المعاينة المتاح أولًا. واجهة Google البرمجية وواجهة أداتك خدمتان مختلفتان.

- تحويل النص أو الصورة إلى فيديو، واستخدام الإطار الأول/الأخير، ومراجع الشخصيات والمنتجات.
- تخطيط الصورة والأجواء والمؤثرات الصوتية والموسيقى الأصلية والصمت والحوار معًا.
- قواعد للحوار والنص واتجاه الكتابة والمراجعة البشرية في 15 لغة.

## الحوار بالعربية

يمكن إبقاء تعليمات المشهد بالإنجليزية وتحديد الحوار والنص الظاهر بالعربية حرفيًا. تحقق من النطق والإملاء والتوقيت.

```text
Spoken language: Modern Standard Arabic.
Exact dialogue at 6s, spoken once with natural pacing: "لنعد إلى المنزل اليوم عبر الطريق الأطول."
Do not translate, paraphrase, repeat or subtitle it.

On-screen language: Modern Standard Arabic.
Text direction: right-to-left.
Exact title: "رحلات صغيرة"
Keep the full phrase connected and right-aligned. No other text.
```

<a id="prompt-collections"></a>

## المطالبات الستون كاملة

شروح المجموعات الخمس الأولى بالصينية، وشروح المجموعتين الأخيرتين بالإنجليزية. جميع مطالبات التحكم القابلة للنسخ بالإنجليزية. لم تُترجم نصوص المجموعات بالكامل.

- [السينما والسرد: 8 مطالبات](prompts/cinematic-storytelling.md)
- [الإعلانات ووسائل التواصل: 8 مطالبات](prompts/commerce-social.md)
- [الوثائقي والسفر والتعليم: 8 مطالبات](prompts/documentary-education.md)
- [الرسوم المتحركة والموسيقى والترفيه: 8 مطالبات](prompts/stylized-entertainment.md)
- [التحكم والتحرير والتمديد: 10 وصفات](prompts/control-editing-extension.md)
- [التحرير المتقدم والكاميرا والتحويل البصري: 9 مطالبات](prompts/advanced-editing-camera.md)
- [لوحات القصة وتقسيم الشاشة والنص والتقييم: 9 مطالبات](prompts/storyboard-text-evaluation.md)



## جرّب أمرك الأول

1. اختر مثالًا كاملًا قريبًا من المشهد الذي تريد إنشاءه وانسخ نص الأمر بالكامل.
2. نزّل الصورة المرجعية المطابقة وحددها بوصفها الإطار الأول إذا كانت أداتك تدعم ذلك.
3. عدّل توقيت الأفعال وفق المدة والدقة المتاحتين. أنشئ مسودة، وراجع العنصر الرئيسي والنص والصوت، ثم غيّر عنصرًا واحدًا في كل مرة.

<a id="source-examples"></a>

## ثلاث مطالبات للنسخ

الصور إطارات أولى مرجعية مأخوذة من المستودع الأصلي، وليست نتائج فيديو مولّدة. ارفع الصورة المناسبة باسم Image1. مدة عشر ثوانٍ وتعليمات الصوت تصف النتيجة المطلوبة؛ عدّلها حسب الإعدادات المتاحة.

### 01 · مكبر صوت: إيقاع قطرات الماء

![مكبر صوت: إيقاع قطرات الماء](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · دراجة على حافة جبل: افتتاحية وثائقية

![دراجة على حافة جبل: افتتاحية وثائقية](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · صانع الساعات والطيور الورقية: قصة مرسومة

![صانع الساعات والطيور الورقية: قصة مرسومة](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



<a id="video-studies"></a>

## ما الذي نتعلمه من الأمثلة الرسمية وأمثلة المجتمع؟

تعرض فيديوهات Google الرسمية نموذج Omni 1.1 Flash. أما منشورات المجتمع فتعود إلى مايو 2026 وتتعلق بالإصدار الأول من Omni / Flash، ولم يُتحقق من كونها اختبارات للإصدار 1.1. تستند أدلة المجتمع إلى النصوص وبيانات الوسائط الوصفية في نسخة FxTwitter، ولم يُتحقق من التشغيل المباشر على X. هذه أمثلة من مصادر خارجية وليست نتائج المنصة التي تستخدمها. راجع الوظائف المتاحة في أداتك.

### Google: الانتقال بين الإطار الأول والأخير

[شاهد المثال الأصلي](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

حدّد صورة البداية وصورة النهاية والحركة المتصلة بينهما كلًا على حدة.

التقط صورتين للغرض نفسه من زاويتين مناسبتين للوصل. إذا توفرت وظيفة الإطار الأول والأخير، اربطهما بحركة بسيطة.

### Google: تمديد اللقطة

[شاهد المثال الأصلي](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

صِف حركة الكاميرا التالية مع الحفاظ على العنصر الرئيسي واتجاه الحركة.

استخدم مقطعًا قصيرًا من تصويرك. إذا توفر التمديد، أضف جزءًا متصلًا واحدًا وافحص نقطة الوصل بحثًا عن قفزات في الحركة أو الإضاءة.

### CHRIS FIRST: استبدال الأشخاص بطيور النحام

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: استبدال الأشخاص بطيور النحام" width="300"></a>

[شاهد المثال الأصلي](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

غيّر الشخصية مع طلب الإبقاء على الملابس والحركة، وافحص مواضع تلامس الأطراف.

إذا توفر تعديل الفيديو، استبدل شخصية واحدة في مقطع من تصويرك. قارن الملابس والوضعية والتلامس مع الأرض قبل التعديل وبعده.

### Justine Moore: تبديل القبعة مع كل تصفيقة

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: تبديل القبعة مع كل تصفيقة" width="300"></a>

[شاهد المثال الأصلي](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

استخدم إيماءة واضحة لتوقيت كل تغيير، مع الحفاظ على الوجه والملابس والكاميرا.

ثبّت الكاميرا وصوّر تصفيقتين واضحتين. إذا توفر تعديل الفيديو، اطلب تغيير القبعة عند كل تصفيقة وافحص التوقيت إطارًا بإطار.

[أمثلة رسمية ومن المجتمع](docs/community-examples.md)

## للمزيد

- [أمثلة رسمية ومن المجتمع](docs/community-examples.md)
- [دليل اللغات](docs/multilingual-guide.md)
- [تصميم المطالبات](docs/prompting-guide.md)
- [المواد المرجعية والأذونات](docs/reference-videos.md)

<a id="brand-tools"></a>

## ابدأ مع SeaImagine

تحتفظ هذه المكتبة بوصفات Flaq AI الأصلية الستين، وتضيف ثلاثة تمارين SeaImagine بصور مرجعية خاصة. تضم هذه الصفحة التمارين الجديدة وأمثلة المستودع الأصلي ودروسًا من الأمثلة الرسمية وأعمال المجتمع.

[Gemini Omni](https://seaimagine.com/ar/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/ar/model/gemini-omni-1-1-flash/)

1. افتح صفحة النموذج وتحقق من إمكانية الوصول والسعر والإعدادات المتاحة حاليًا.
2. للحفاظ على مظهر منتج أو شخصية، اختر تحويل صورة إلى فيديو، وارفع صورة واحدة ثم الصق المطالبة المناسبة. لإنشاء مشهد جديد، جرّب تحويل نص إلى فيديو.
3. اختر المدة والأبعاد من الواجهة. اختبر لقطة واحدة وراجع المظهر والحركة والصوت، ثم غيّر تعليمة واحدة في كل مرة.

هذه تصاميم مطالبات وليست نتائج توليد جرى التحقق منها على SeaImagine. تعتمد المدة والصوت والتحرير والتمديد والمراجع على النموذج والواجهة الحالية. قدرات واجهة Google البرمجية لا تعني توفرها تلقائيًا في SeaImagine.

<a id="sea-practice"></a>

## ثلاثة تمارين في SeaImagine بصور مرجعية أصلية

هذه الصور المرجعية مولّدة بالذكاء الاصطناعي لتكون إطارات أولى للتدريب، وليست نتائج فيديو جرى اختبارها باستخدام Gemini. استخدم فقط الوظائف المتاحة في واجهة SeaImagine.

### SEA-01 · كوب خزفي فيروزي في ضوء الصباح

[![كوب خزفي فيروزي في ضوء الصباح](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

قرّب الكاميرا ببطء مع الحفاظ على المقبض وحافة الكوب ومستوى السائل. اترك مساحة للنص في النهاية.

ارفع صورة الكوب لتحويلها إلى فيديو. جرّب تقرّبًا بطيئًا فقط، وافحص المقبض ومستوى السائل قبل إضافة النص.

[صورة إلى فيديو](https://seaimagine.com/ar/image-to-video/) · [مولّد صور بالذكاء الاصطناعي](https://seaimagine.com/ar/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · أضواء تتعاقب في ميناء ورقي

[![أضواء تتعاقب في ميناء ورقي](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

في لقطة واحدة، أشعل ضوء المنارة ثم زِد سطوع نوافذ المنازل الثلاثة بالتتابع. حافظ على ملمس الورق والأشكال الهندسية.

ارفع صورة الميناء واطلب إضاءة المنارة ثم زيادة سطوع النوافذ بالتتابع. قارن أشكال المباني في البداية والنهاية.

[صورة إلى فيديو](https://seaimagine.com/ar/image-to-video/) · [مولّد صور بالذكاء الاصطناعي](https://seaimagine.com/ar/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · كيس كتاني لفيديو متجر متعدد اللغات

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="كيس كتاني لفيديو متجر متعدد اللغات" width="360"></a>

أنشئ فيديو رأسيًا نظيفًا للمنتج بلا كتابة، ثم أضف النصوص المترجمة ببرنامج تحرير فيديو عادي.

أنشئ فيديو رأسيًا من صورة الكيس، ثم أضف الترجمات لاحقًا. استخدم أمر تعديل فيديو قصيرًا فقط إذا كانت هذه الوظيفة متاحة.

[صورة إلى فيديو](https://seaimagine.com/ar/image-to-video/) · [مولّد صور بالذكاء الاصطناعي](https://seaimagine.com/ar/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> لحياة يومية أبسط

[خطوات العمل في SeaImagine](docs/seaimagine-workflow.md)

## أدوات SeaImagine الأخرى

يمكن استخدام هذه الصفحات كنقاط بداية بديلة. راجع كل صفحة لمعرفة النماذج والشروط والأسعار الحالية. لا يضمن هذا المستودع توفر الخدمة دون انقطاع.

- [إنشاء](https://seaimagine.com/ar/create/)
- [صورة إلى فيديو](https://seaimagine.com/ar/image-to-video/)
- [نص إلى فيديو](https://seaimagine.com/ar/text-to-video/)
- [مولّد صور بالذكاء الاصطناعي](https://seaimagine.com/ar/ai-image-generator/)

## المصدر والترخيص

مقتبس من مستودع Flaq AI، بما فيه مجموعات المطالبات وثلاث صور مرجعية. ليست جميع المواد من إنتاج SeaImagine الأصلي. هذا دليل مستقل وليس منتجًا رسميًا من Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
