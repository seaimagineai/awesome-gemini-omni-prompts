# SeaImagine용 Gemini Omni 영상 프롬프트 모음

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![SeaImagine용 Gemini Omni 영상 프롬프트 모음](assets/seaimagine-omni-hero.png)

Flaq AI 원본 저장소의 프롬프트 60개를 SeaImagine 사용자를 위해 정리했습니다. 제품 광고, 여행, 애니메이션, 편집 아이디어를 살펴보세요. 아래 예시 3개에는 참고 이미지와 복사할 수 있는 영어 프롬프트가 있습니다.

[Gemini Omni](https://seaimagine.com/ko/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/ko/model/gemini-omni-1-1-flash/)

## SeaImagine 시작하기

1. 모델 페이지에서 현재 이용 가능 여부, 가격, 설정 항목을 확인합니다.
2. 제품이나 인물의 외형을 유지하려면 이미지로 영상 만들기를 선택하고 참고 이미지 한 장과 해당 프롬프트를 넣습니다. 새로운 장면은 텍스트로 영상 만들기부터 시도합니다.
3. 화면에서 길이와 비율을 선택합니다. 한 장면을 먼저 시험하고 외형, 움직임, 소리를 확인한 뒤 지시를 하나씩 수정합니다.

프롬프트 설계 예시이며 SeaImagine에서 검증한 생성 결과가 아닙니다. 길이, 음성, 편집, 연장, 참고 자료 지원은 선택한 모델과 현재 화면에 따라 다릅니다. Google API 기능이 SeaImagine에서도 제공된다는 뜻은 아닙니다.

## 복사해서 사용할 예시 3개

이미지는 원본 저장소의 첫 프레임 참고 이미지를 재사용한 것이며 실제 영상 생성 결과가 아닙니다. 해당 이미지를 Image1로 업로드하세요. 10초와 소리 지시는 목표이며 사용 가능한 설정에 맞게 조정해야 합니다.

### 01 · 제품 스피커: 물방울 리듬

![제품 스피커: 물방울 리듬](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · 능선의 자전거: 여행 다큐멘터리 도입

![능선의 자전거: 여행 다큐멘터리 도입](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · 시계공과 종이 새: 손그림 이야기

![시계공과 종이 새: 손그림 이야기](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

## 프롬프트 60개 전체

앞의 5개 모음은 중국어 설명, 뒤의 2개는 영어 설명입니다. 복사할 제어 프롬프트는 모두 영어입니다. 모음 본문 전체가 번역된 것은 아닙니다.

- [영화와 스토리텔링: 8개](prompts/cinematic-storytelling.md)
- [광고와 소셜 미디어: 8개](prompts/commerce-social.md)
- [다큐멘터리, 여행, 교육: 8개](prompts/documentary-education.md)
- [애니메이션, 음악, 엔터테인먼트: 8개](prompts/stylized-entertainment.md)
- [멀티모달 제어, 편집, 확장: 10개](prompts/control-editing-extension.md)
- [고급 편집, 카메라, 시각 변환: 9개](prompts/advanced-editing-camera.md)
- [스토리보드, 분할 화면, 텍스트, 평가: 9개](prompts/storyboard-text-evaluation.md)

## 한국어 대사 지정하기

필요하면 장면 지시는 영어로 유지하고 대사와 화면 문구는 한국어로 정확히 지정하세요. 발음, 맞춤법, 타이밍을 확인하세요.

```text
Spoken language: Korean.
Exact dialogue at 6s, spoken once with natural conversational pacing: "오늘은 조금 돌아서 집에 가자."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Korean title: "작은 여행"
Use large readable Hangul syllable blocks. No other text.
```

## 더 읽기

- [SeaImagine 사용 순서](docs/seaimagine-workflow.md)
- [공식 및 커뮤니티 사례](docs/community-examples.md)
- [다국어 안내](docs/multilingual-guide.md)
- [프롬프트 설계](docs/prompting-guide.md)
- [참고 자료와 이용 허락](docs/reference-videos.md)

## SeaImagine의 다른 도구

다른 제작 시작점으로 활용할 수 있습니다. 현재 모델, 이용 조건, 가격은 각 페이지에서 확인하세요. 이 저장소는 지속적인 서비스 제공을 보장하지 않습니다.

- [만들기](https://seaimagine.com/ko/create/)
- [이미지로 영상 만들기](https://seaimagine.com/ko/image-to-video/)
- [텍스트로 영상 만들기](https://seaimagine.com/ko/text-to-video/)
- [AI 이미지 생성기](https://seaimagine.com/ko/ai-image-generator/)

## 출처와 라이선스

Flaq AI 저장소의 프롬프트 모음과 참고 이미지 3장을 바탕으로 재구성했습니다. 모든 자료가 SeaImagine의 자체 창작물은 아닙니다. Google 공식 제품이 아닌 독립 안내서입니다.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
