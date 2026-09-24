# Gemini Omni — 심화 문서

[전체 프롬프트 60개 색인](../../README_KO.md)

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



<a id="sea-practice"></a>

## SeaImagine 전용 참고 이미지로 해 보는 세 가지 연습

아래 이미지는 AI로 만든 첫 프레임 연습 자료이며 Gemini 동영상 실측 결과가 아닙니다. SeaImagine 화면에서 실제로 제공하는 기능에 맞춰 사용하세요.

### SEA-01 · 청록색 도자기 컵으로 아침 상품 영상 만들기

[![청록색 도자기 컵으로 아침 상품 영상 만들기](../../assets/seaimagine-ceramic-cup.png)](../../assets/seaimagine-ceramic-cup.png)

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

[![종이 공예 항구에 차례로 불 켜기](../../assets/seaimagine-paper-harbor.png)](../../assets/seaimagine-paper-harbor.png)

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

<a href="../../assets/seaimagine-linen-pouch.png"><img src="../../assets/seaimagine-linen-pouch.png" alt="리넨 파우치로 다국어 세로 영상 마무리하기" width="360"></a>

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
