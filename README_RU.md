<div align="center">

![Библиотека промптов Gemini Omni](assets/seaimagine-omni-hero.png)

# Библиотека промптов Gemini Omni

**Здесь собраны все 60 полных рецептов исходной библиотеки в семи категориях. Учитесь описывать сцену, задавать время действий, движение камеры и звук, а затем адаптируйте пример под свою идею.**

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)

[Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)



[Все 60 промптов](#prompt-collections) · [Три промпта для копирования](#source-examples) · [Официальные примеры и работы сообщества](#video-studies) · [Многоязычное руководство](docs/multilingual-guide.md)

</div>

## Что включено

Список описывает задачи для промптов, а не гарантирует функции. Проверьте доступные входные данные, редактирование, продление, звук и разрешение для выбранной модели в вашем инструменте. Сначала оцените композицию, речь и текст в доступном режиме предпросмотра. API Google (программный интерфейс) и интерфейс вашего инструмента — разные сервисы.

- Текст-в-видео, изображение-в-видео, первый/последний кадр и референсы персонажей или продуктов.
- Совместное проектирование изображения, атмосферы, шумов, оригинальной музыки, тишины и реплик.
- Правила диалога, экранного текста, переноса строк и проверки для 15 языков.

## Диалоги на русском

Инструкции для сцены можно оставить на английском, а реплики и надписи задать дословно на русском. Проверьте произношение, написание и время появления.

```text
Spoken language: Russian.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Давай сегодня пойдём домой длинной дорогой."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Russian title: "МАЛЕНЬКИЕ ПУТЕШЕСТВИЯ"
Use Cyrillic characters only and preserve spelling exactly. No other text.
```

<a id="prompt-collections"></a>

## Все 60 промптов

Первые пять подборок содержат пояснения на китайском, последние две — на английском. Все управляющие промпты написаны по-английски. Подборки переведены не полностью.

- [Кино и повествование: 8 промптов](prompts/cinematic-storytelling.md)
- [Реклама и социальные сети: 8 промптов](prompts/commerce-social.md)
- [Документалистика, путешествия и образование: 8 промптов](prompts/documentary-education.md)
- [Анимация, музыка и развлечения: 8 промптов](prompts/stylized-entertainment.md)
- [Управление, редактирование и продолжение: 10 рецептов](prompts/control-editing-extension.md)
- [Продвинутое редактирование, камера и визуальные преобразования: 9 промптов](prompts/advanced-editing-camera.md)
- [Раскадровки, разделённый экран, текст и оценка: 9 промптов](prompts/storyboard-text-evaluation.md)



## Попробуйте первый промпт

1. Выберите полный пример, близкий к задуманной сцене, и скопируйте весь промпт.
2. Скачайте соответствующее изображение и задайте его как первый кадр, если ваш инструмент поддерживает эту функцию.
3. Настройте временные отрезки с учётом доступной длительности и разрешения. Создайте черновик, проверьте главный объект, текст и звук, затем меняйте по одному элементу.

<a id="source-examples"></a>

## Три промпта для копирования

Изображения взяты из исходного репозитория как референсы первого кадра, а не как результаты генерации видео. Загрузите нужное изображение как Image1. Длительность 10 секунд и звук — желаемые параметры; адаптируйте их к доступным настройкам.

### 01 · Колонка: ритм капель

![Колонка: ритм капель](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · Велосипед на хребте: начало документального фильма

![Велосипед на хребте: начало документального фильма](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · Часовщик и бумажные птицы: рисованная история

![Часовщик и бумажные птицы: рисованная история](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



<a id="video-studies"></a>

## Чему учат официальные примеры и работы сообщества

Официальные видео Google демонстрируют Omni 1.1 Flash. Публикации сообщества относятся к маю 2026 года и первоначальному Omni / Flash; они не подтверждены как тесты версии 1.1. Доступные свидетельства — текст и метаданные медиа из зеркала FxTwitter; воспроизведение непосредственно в X не проверялось. Это внешние примеры, а не результаты платформы, которой вы пользуетесь. Проверяйте доступность функций в своём инструменте.

### Google: переход между начальным и конечным кадрами

[Посмотреть исходный пример](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Отдельно задайте начальный кадр, конечный кадр и непрерывное движение между ними.

Сделайте два снимка одного предмета с совместимых ракурсов. Если доступны начальный и конечный кадры, соедините их простым движением.

### Google: продление плана

[Посмотреть исходный пример](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Опишите следующее движение камеры, сохранив объект и направление движения.

Возьмите свой короткий ролик. Если доступно продление, добавьте одно продолжение и проверьте стык на скачки движения и света.

### CHRIS FIRST: люди превращаются во фламинго

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: люди превращаются во фламинго" width="300"></a>

[Посмотреть исходный пример](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

Меняйте персонажа, явно сохраняя одежду и действие; проверяйте точки контакта конечностей.

Если доступно редактирование видео, замените одного персонажа в своей записи. Сравните одежду, позу и контакт с землёй до и после.

### Justine Moore: новая шляпа после каждого хлопка

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: новая шляпа после каждого хлопка" width="300"></a>

[Посмотреть исходный пример](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

Используйте видимый жест как сигнал смены, сохраняя лицо, одежду и положение камеры.

Снимите два чётких хлопка неподвижной камерой. Если доступно редактирование видео, попросите менять шляпу при каждом хлопке и проверьте момент смены покадрово.

[Официальные примеры и работы сообщества](docs/community-examples.md)

## Дополнительные материалы

- [Официальные примеры и работы сообщества](docs/community-examples.md)
- [Многоязычное руководство](docs/multilingual-guide.md)
- [Составление промптов](docs/prompting-guide.md)
- [Референсы и разрешения](docs/reference-videos.md)

<a id="brand-tools"></a>

## Начало работы с SeaImagine

Библиотека сохраняет 60 исходных рецептов Flaq AI и добавляет три упражнения SeaImagine с оригинальными изображениями. На этой странице собраны новые упражнения, примеры из исходного репозитория и уроки из официальных работ и примеров сообщества.

[Gemini Omni](https://seaimagine.com/ru/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/ru/model/gemini-omni-1-1-flash/)

1. Откройте страницу модели и проверьте доступ, цену и настройки.
2. Чтобы сохранить облик товара или персонажа, выберите создание видео из изображения, загрузите один референс и вставьте его промпт. Для новой сцены попробуйте создание видео из текста.
3. Выберите длительность и формат в интерфейсе. Проверьте один план: внешний вид, движение и звук. Меняйте по одной инструкции.

Это проекты промптов, а не проверенные результаты генерации в SeaImagine. Длительность, звук, монтаж, продление и референсы зависят от модели и текущего интерфейса. Функции API Google не обязательно доступны в SeaImagine.

<a id="sea-practice"></a>

## Три упражнения SeaImagine с оригинальными изображениями

Эти изображения созданы ИИ как начальные кадры для упражнений. Это не проверенные результаты генерации видео в Gemini. Используйте только функции, доступные в интерфейсе SeaImagine.

### SEA-01 · Бирюзовая керамическая чашка в утреннем свете

[![Бирюзовая керамическая чашка в утреннем свете](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

Медленно приближайте камеру, сохраняя ручку, край чашки и уровень жидкости. В конце оставьте место для надписи.

Загрузите изображение чашки для создания видео. Сначала попробуйте только медленное приближение; проверьте ручку и уровень жидкости перед добавлением надписи.

[Видео из изображения](https://seaimagine.com/ru/image-to-video/) · [Генератор изображений ИИ](https://seaimagine.com/ru/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · В бумажной гавани загораются огни

[![В бумажной гавани загораются огни](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

В одном плане включите свет маяка, затем по очереди усильте свет в окнах трёх домов. Сохраните фактуру бумаги и геометрию.

Загрузите изображение гавани. Попросите включить маяк и по очереди усилить свет в окнах. Сравните форму зданий в начале и конце.

[Видео из изображения](https://seaimagine.com/ru/image-to-video/) · [Генератор изображений ИИ](https://seaimagine.com/ru/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · Льняной мешочек для многоязычного магазина

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="Льняной мешочек для многоязычного магазина" width="360"></a>

Сначала создайте чистое вертикальное видео товара без текста, затем добавьте переведённые подписи в обычном видеоредакторе.

Создайте вертикальное видео по изображению мешочка и добавьте переводы после генерации. Короткую команду редактирования видео используйте только при наличии этой функции.

[Видео из изображения](https://seaimagine.com/ru/image-to-video/) · [Генератор изображений ИИ](https://seaimagine.com/ru/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> Больше лёгкости каждый день

[Порядок работы в SeaImagine](docs/seaimagine-workflow.md)

## Другие инструменты SeaImagine

Эти страницы предлагают другие способы начать работу. Актуальные модели, условия и цены указаны на каждой странице. Репозиторий не гарантирует бесперебойную доступность.

- [Создать](https://seaimagine.com/ru/create/)
- [Видео из изображения](https://seaimagine.com/ru/image-to-video/)
- [Видео из текста](https://seaimagine.com/ru/text-to-video/)
- [Генератор изображений ИИ](https://seaimagine.com/ru/ai-image-generator/)

## Источник и лицензия

Адаптировано из репозитория Flaq AI, включая подборки промптов и три референса. Не все материалы созданы SeaImagine с нуля. Это независимое руководство, не официальный продукт Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
