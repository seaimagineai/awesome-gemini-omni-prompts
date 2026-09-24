<div align="center">

![Gemini Omni 프롬프트 모음](assets/seaimagine-omni-hero.png)

# Gemini Omni 프롬프트 모음

**원본 라이브러리의 완전한 레시피 60개를 7개 분류로 모았습니다. 장면, 동작의 시점, 카메라와 소리를 설명하는 법을 배우고 원하는 아이디어에 맞게 바꿔 보세요.**

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)

[Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)



[프롬프트 60개 전체](#prompt-collections) · [복사해서 사용할 예시 3개](#source-examples) · [공식 및 커뮤니티 사례](#video-studies) · [다국어 안내](docs/multilingual-guide.md)

</div>

## 포함 내용

아래 목록은 프롬프트에서 계획할 내용이며 기능 제공을 보장하지 않습니다. 사용하는 도구에서 선택한 모델과 현재 화면을 살펴보고 입력 자료, 편집, 연장, 소리, 해상도 지원 여부를 확인하세요. 먼저 제공되는 미리보기 설정으로 구도, 발음, 글자를 확인하세요. Google API(프로그램 호출 인터페이스)와 사용하는 도구의 웹 화면은 별개입니다.

- 텍스트-비디오, 이미지-비디오, 첫/마지막 프레임, 인물·제품 이미지, 짧은 비디오 참조.
- 환경음, 폴리, 오리지널 음악, 침묵, 대사 타이밍을 함께 설계하는 방법.
- 15개 언어의 대사, 화면 문자, 줄바꿈, 발음, 원어민 검수 가이드.

## 한국어 대사 지정하기

필요하면 장면 지시는 영어로 유지하고 대사와 화면 문구는 한국어로 정확히 지정하세요. 발음, 맞춤법, 타이밍을 확인하세요.

```text
Spoken language: Korean.
Exact dialogue at 6s, spoken once with natural conversational pacing: "오늘은 조금 돌아서 집에 가자."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Korean title: "작은 여행"
Use large readable Hangul syllable blocks. No other text.
```

<a id="prompt-collections"></a>

## 프롬프트 60개 전체

앞의 5개 모음은 중국어 설명, 뒤의 2개는 영어 설명입니다. 복사할 제어 프롬프트는 모두 영어입니다. 모음 본문 전체가 번역된 것은 아닙니다.

- [영화와 스토리텔링: 8개](prompts/cinematic-storytelling.md)
- [광고와 소셜 미디어: 8개](prompts/commerce-social.md)
- [다큐멘터리, 여행, 교육: 8개](prompts/documentary-education.md)
- [애니메이션, 음악, 엔터테인먼트: 8개](prompts/stylized-entertainment.md)
- [멀티모달 제어, 편집, 확장: 10개](prompts/control-editing-extension.md)
- [고급 편집, 카메라, 시각 변환: 9개](prompts/advanced-editing-camera.md)
- [스토리보드, 분할 화면, 텍스트, 평가: 9개](prompts/storyboard-text-evaluation.md)



## 첫 프롬프트 사용하기

1. 만들고 싶은 장면과 비슷한 예시를 골라 프롬프트 전체를 복사하세요.
2. 예시에 맞는 참고 이미지를 내려받으세요. 사용하는 도구가 첫 프레임 설정을 지원하면 해당 이미지를 지정하세요.
3. 도구가 제공하는 길이와 해상도에 맞춰 시간 구간을 조정하세요. 먼저 초안을 만들고 대상, 글자, 소리를 확인한 뒤 한 번에 한 가지만 수정하세요.

<a id="source-examples"></a>

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



<a id="video-studies"></a>

## 공식·커뮤니티 사례에서 배울 점

Google 공식 영상은 Omni 1.1 Flash 시연입니다. 커뮤니티 게시물은 2026년 5월의 초기 Omni / Flash 사례이며 1.1 실측으로 확인되지 않았습니다. 근거는 FxTwitter 미러의 글과 미디어 정보이고, X에서의 원본 재생은 검증하지 않았습니다. 외부 사례이므로 사용 중인 플랫폼의 생성 결과를 뜻하지 않습니다. 지원 기능은 각 도구에서 확인하세요.

### Google: 첫 프레임과 마지막 프레임 연결

[원본 사례 보기](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

시작 이미지, 끝 이미지, 그 사이의 연속 동작을 각각 정합니다.

같은 물체를 자연스럽게 연결할 수 있는 각도로 두 장 촬영하세요. 첫·마지막 프레임 기능이 있다면 단순한 동작으로 연결하세요.

### Google: 장면 연장

[원본 사례 보기](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

대상과 이동 방향을 유지하면서 다음 카메라 움직임을 설명합니다.

직접 찍은 짧은 영상을 사용하세요. 연장 기능이 있다면 한 동작만 이어 붙이고 연결 지점의 움직임과 조명을 확인하세요.

### CHRIS FIRST: 사람을 홍학으로 바꾸기

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: 사람을 홍학으로 바꾸기" width="300"></a>

[원본 사례 보기](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

대상은 바꾸되 의상과 동작은 유지하도록 지정하고 팔다리가 닿는 부분을 확인합니다.

직접 찍은 영상에서 편집 기능을 사용할 수 있다면 대상 하나만 바꾸세요. 전후의 의상, 자세, 지면 접촉을 비교하세요.

### Justine Moore: 박수마다 모자 바꾸기

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: 박수마다 모자 바꾸기" width="300"></a>

[원본 사례 보기](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

눈에 보이는 동작으로 변경 시점을 정하고 얼굴, 의상, 카메라는 유지합니다.

카메라를 고정하고 박수를 두 번 분명하게 치는 영상을 찍으세요. 영상 편집이 가능하면 박수마다 모자를 바꾸도록 요청하고 프레임별로 시점을 확인하세요.

[공식 및 커뮤니티 사례](docs/community-examples.md)

## 더 읽기

- [공식 및 커뮤니티 사례](docs/community-examples.md)
- [다국어 안내](docs/multilingual-guide.md)
- [프롬프트 설계](docs/prompting-guide.md)
- [참고 자료와 이용 허락](docs/reference-videos.md)

<a id="brand-tools"></a>

## SeaImagine 시작하기

Flaq AI의 원본 레시피 60개를 보존하고, 자체 참고 이미지를 활용한 SeaImagine 연습 세 가지를 추가했습니다. 이 페이지에서 새 연습, 원본 예시, 공식·커뮤니티 사례의 학습 내용을 확인하세요.

[Gemini Omni](https://seaimagine.com/ko/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/ko/model/gemini-omni-1-1-flash/)

1. 모델 페이지에서 현재 이용 가능 여부, 가격, 설정 항목을 확인합니다.
2. 제품이나 인물의 외형을 유지하려면 이미지로 영상 만들기를 선택하고 참고 이미지 한 장과 해당 프롬프트를 넣습니다. 새로운 장면은 텍스트로 영상 만들기부터 시도합니다.
3. 화면에서 길이와 비율을 선택합니다. 한 장면을 먼저 시험하고 외형, 움직임, 소리를 확인한 뒤 지시를 하나씩 수정합니다.

프롬프트 설계 예시이며 SeaImagine에서 검증한 생성 결과가 아닙니다. 길이, 음성, 편집, 연장, 참고 자료 지원은 선택한 모델과 현재 화면에 따라 다릅니다. Google API 기능이 SeaImagine에서도 제공된다는 뜻은 아닙니다.

<a id="sea-practice"></a>

## SeaImagine 전용 참고 이미지로 해 보는 세 가지 연습

아래 이미지는 AI로 만든 첫 프레임 연습 자료이며 Gemini 동영상 실측 결과가 아닙니다. SeaImagine 화면에서 실제로 제공하는 기능에 맞춰 사용하세요.

### SEA-01 · 청록색 도자기 컵으로 아침 상품 영상 만들기

[![청록색 도자기 컵으로 아침 상품 영상 만들기](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

카메라를 천천히 가까이 이동하면서 손잡이, 컵 가장자리, 액체 높이를 유지합니다. 마지막에는 자막 공간을 남깁니다.

컵 이미지를 올려 이미지 기반 영상을 만드세요. 먼저 천천히 다가가는 동작만 시험하고 손잡이와 액체 높이를 확인한 뒤 자막을 넣으세요.

[이미지로 영상 만들기](https://seaimagine.com/ko/image-to-video/) · [AI 이미지 생성기](https://seaimagine.com/ko/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · 종이 공예 항구에 차례로 불 켜기

[![종이 공예 항구에 차례로 불 켜기](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

한 장면에서 등대에 불을 켠 뒤 집 세 채의 창문 불빛을 차례로 밝게 합니다. 종이 질감과 형태를 유지합니다.

항구 이미지를 올리고 등대가 켜진 뒤 창문 불빛이 차례로 밝아지도록 요청하세요. 시작과 끝의 건물 형태를 비교하세요.

[이미지로 영상 만들기](https://seaimagine.com/ko/image-to-video/) · [AI 이미지 생성기](https://seaimagine.com/ko/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · 리넨 파우치로 다국어 세로 영상 마무리하기

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="리넨 파우치로 다국어 세로 영상 마무리하기" width="360"></a>

글자 없는 세로 상품 영상을 먼저 만든 뒤 일반 영상 편집기로 각 언어의 자막을 넣습니다.

파우치 이미지로 세로 영상을 만들고 번역한 자막을 나중에 넣으세요. 짧은 영상 편집 지시는 해당 기능을 지원할 때만 사용하세요.

[이미지로 영상 만들기](https://seaimagine.com/ko/image-to-video/) · [AI 이미지 생성기](https://seaimagine.com/ko/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> 매일을 조금 더 여유롭게

[SeaImagine 사용 순서](docs/seaimagine-workflow.md)

## SeaImagine의 다른 도구

다른 제작 시작점으로 활용할 수 있습니다. 현재 모델, 이용 조건, 가격은 각 페이지에서 확인하세요. 이 저장소는 지속적인 서비스 제공을 보장하지 않습니다.

- [만들기](https://seaimagine.com/ko/create/)
- [이미지로 영상 만들기](https://seaimagine.com/ko/image-to-video/)
- [텍스트로 영상 만들기](https://seaimagine.com/ko/text-to-video/)
- [AI 이미지 생성기](https://seaimagine.com/ko/ai-image-generator/)

## 출처와 라이선스

Flaq AI 저장소의 프롬프트 모음과 참고 이미지 3장을 바탕으로 재구성했습니다. 모든 자료가 SeaImagine의 자체 창작물은 아닙니다. Google 공식 제품이 아닌 독립 안내서입니다.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
