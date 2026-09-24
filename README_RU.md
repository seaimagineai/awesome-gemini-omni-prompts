# Видеопромпты Gemini Omni для SeaImagine

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![Видеопромпты Gemini Omni для SeaImagine](assets/seaimagine-omni-hero.png)

60 промптов из репозитория Flaq AI, адаптированных для пользователей SeaImagine: реклама, путешествия, анимация и монтаж. Три примера ниже содержат референсы и полные промпты на английском.

[Gemini Omni](https://seaimagine.com/ru/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/ru/model/gemini-omni-1-1-flash/)

## Начало работы с SeaImagine

1. Откройте страницу модели и проверьте доступ, цену и настройки.
2. Чтобы сохранить облик товара или персонажа, выберите создание видео из изображения, загрузите один референс и вставьте его промпт. Для новой сцены попробуйте создание видео из текста.
3. Выберите длительность и формат в интерфейсе. Проверьте один план: внешний вид, движение и звук. Меняйте по одной инструкции.

Это проекты промптов, а не проверенные результаты генерации в SeaImagine. Длительность, звук, монтаж, продление и референсы зависят от модели и текущего интерфейса. Функции API Google не обязательно доступны в SeaImagine.

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

## Все 60 промптов

Первые пять подборок содержат пояснения на китайском, последние две — на английском. Все управляющие промпты написаны по-английски. Подборки переведены не полностью.

- [Кино и повествование: 8 промптов](prompts/cinematic-storytelling.md)
- [Реклама и социальные сети: 8 промптов](prompts/commerce-social.md)
- [Документалистика, путешествия и образование: 8 промптов](prompts/documentary-education.md)
- [Анимация, музыка и развлечения: 8 промптов](prompts/stylized-entertainment.md)
- [Управление, редактирование и продолжение: 10 рецептов](prompts/control-editing-extension.md)
- [Продвинутое редактирование, камера и визуальные преобразования: 9 промптов](prompts/advanced-editing-camera.md)
- [Раскадровки, разделённый экран, текст и оценка: 9 промптов](prompts/storyboard-text-evaluation.md)

## Диалоги на русском

Инструкции для сцены можно оставить на английском, а реплики и надписи задать дословно на русском. Проверьте произношение, написание и время появления.

```text
Spoken language: Russian.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Давай сегодня пойдём домой длинной дорогой."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Russian title: "МАЛЕНЬКИЕ ПУТЕШЕСТВИЯ"
Use Cyrillic characters only and preserve spelling exactly. No other text.
```

## Дополнительные материалы

- [Порядок работы в SeaImagine](docs/seaimagine-workflow.md)
- [Официальные примеры и работы сообщества](docs/community-examples.md)
- [Многоязычное руководство](docs/multilingual-guide.md)
- [Составление промптов](docs/prompting-guide.md)
- [Референсы и разрешения](docs/reference-videos.md)

## Другие инструменты SeaImagine

Эти страницы предлагают другие способы начать работу. Актуальные модели, условия и цены указаны на каждой странице. Репозиторий не гарантирует бесперебойную доступность.

- [Создать](https://seaimagine.com/ru/create/)
- [Видео из изображения](https://seaimagine.com/ru/image-to-video/)
- [Видео из текста](https://seaimagine.com/ru/text-to-video/)
- [Генератор изображений ИИ](https://seaimagine.com/ru/ai-image-generator/)

## Источник и лицензия

Адаптировано из репозитория Flaq AI, включая подборки промптов и три референса. Не все материалы созданы SeaImagine с нуля. Это независимое руководство, не официальный продукт Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
