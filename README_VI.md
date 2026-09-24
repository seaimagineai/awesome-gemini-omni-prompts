<div align="center">

![Thư viện prompt Gemini Omni](assets/seaimagine-omni-hero.png)

# Thư viện prompt Gemini Omni

**60 câu lệnh thuộc 7 danh mục, kèm 6 ảnh tham chiếu dùng làm đầu vào, không phải kết quả tạo đã được kiểm chứng.**

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)

[Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

[Duyệt theo danh mục](#prompt-collections) · [Sáu ví dụ có thể sao chép ngay](#source-examples) · [Kết quả từ nguồn chính thức và cộng đồng](#video-studies) · [Mục lục đầy đủ 60 câu lệnh](docs/prompt-index.md) · [Tải toàn bộ câu lệnh dạng văn bản](prompts/copy/all-prompts.txt)

</div>

<a id="prompt-collections"></a>

## Duyệt theo danh mục

| Danh mục | Số câu lệnh | Liên kết |
|---|---:|---|
| [Điện ảnh và kể chuyện](prompts/cinematic-storytelling.md) | 8 | [Xem](prompts/cinematic-storytelling.md#case-01) |
| [Quảng cáo và mạng xã hội](prompts/commerce-social.md) | 8 | [Xem](prompts/commerce-social.md#case-01) |
| [Tài liệu, du lịch và giáo dục](prompts/documentary-education.md) | 8 | [Xem](prompts/documentary-education.md#case-01) |
| [Hoạt hình, âm nhạc và giải trí](prompts/stylized-entertainment.md) | 8 | [Xem](prompts/stylized-entertainment.md#case-01) |
| [Điều khiển, chỉnh sửa và mở rộng](prompts/control-editing-extension.md) | 10 | [Xem](prompts/control-editing-extension.md#case-01) |
| [Chỉnh sửa nâng cao, máy quay và biến đổi hình ảnh](prompts/advanced-editing-camera.md) | 9 | [Xem](prompts/advanced-editing-camera.md#case-01) |
| [Storyboard, chia màn hình, chữ và đánh giá](prompts/storyboard-text-evaluation.md) | 9 | [Xem](prompts/storyboard-text-evaluation.md#case-01) |

[Mục lục đầy đủ 60 câu lệnh](docs/prompt-index.md) · [Tải toàn bộ câu lệnh dạng văn bản](prompts/copy/all-prompts.txt)

Năm nhóm đầu có phần giải thích bằng tiếng Trung, hai nhóm cuối bằng tiếng Anh. Tất cả prompt điều khiển đều bằng tiếng Anh. Nội dung các nhóm chưa được dịch đầy đủ.

<a id="source-examples"></a>

## Sáu ví dụ có thể sao chép ngay

Ảnh tham chiếu là tư liệu đầu vào, không phải kết quả tạo.

[01 · Loa sản phẩm: nhịp giọt nước](#example-01) · [02 · Đạp xe trên sống núi: mở đầu phim tài liệu](#example-02) · [03 · Thợ đồng hồ và chim giấy: câu chuyện minh họa](#example-03) · [04 · Cốc gốm xanh ngọc trong ánh sáng ban mai](#example-04) · [05 · Bến cảng giấy lần lượt lên đèn](#example-05) · [06 · Túi vải lanh cho video bán hàng đa ngôn ngữ](#example-06)

<a id="example-01"></a>

### 01 · Loa sản phẩm: nhịp giọt nước

<a href="assets/product-speaker.png"><img src="assets/product-speaker.png" alt="Loa sản phẩm: nhịp giọt nước" width="420"></a>

[Quảng cáo và mạng xã hội](prompts/commerce-social.md) · [Khung hình đầu tham chiếu](assets/product-speaker.png) · [Văn bản thuần](prompts/copy/showcase-01.txt)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

<a id="example-02"></a>

### 02 · Đạp xe trên sống núi: mở đầu phim tài liệu

<a href="assets/travel-cyclist.png"><img src="assets/travel-cyclist.png" alt="Đạp xe trên sống núi: mở đầu phim tài liệu" width="420"></a>

[Tài liệu, du lịch và giáo dục](prompts/documentary-education.md) · [Khung hình đầu tham chiếu](assets/travel-cyclist.png) · [Văn bản thuần](prompts/copy/showcase-02.txt)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

<a id="example-03"></a>

### 03 · Thợ đồng hồ và chim giấy: câu chuyện minh họa

<a href="assets/clockmaker-story.png"><img src="assets/clockmaker-story.png" alt="Thợ đồng hồ và chim giấy: câu chuyện minh họa" width="420"></a>

[Hoạt hình, âm nhạc và giải trí](prompts/stylized-entertainment.md) · [Khung hình đầu tham chiếu](assets/clockmaker-story.png) · [Văn bản thuần](prompts/copy/showcase-03.txt)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

<a id="example-04"></a>

### 04 · Cốc gốm xanh ngọc trong ánh sáng ban mai

<a href="assets/seaimagine-ceramic-cup.png"><img src="assets/seaimagine-ceramic-cup.png" alt="Cốc gốm xanh ngọc trong ánh sáng ban mai" width="420"></a>

[Quảng cáo và mạng xã hội](prompts/commerce-social.md) · [Khung hình đầu tham chiếu](assets/seaimagine-ceramic-cup.png) · [Văn bản thuần](prompts/copy/showcase-04.txt)

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

### 05 · Bến cảng giấy lần lượt lên đèn

<a href="assets/seaimagine-paper-harbor.png"><img src="assets/seaimagine-paper-harbor.png" alt="Bến cảng giấy lần lượt lên đèn" width="420"></a>

[Hoạt hình, âm nhạc và giải trí](prompts/stylized-entertainment.md) · [Khung hình đầu tham chiếu](assets/seaimagine-paper-harbor.png) · [Văn bản thuần](prompts/copy/showcase-05.txt)

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

### 06 · Túi vải lanh cho video bán hàng đa ngôn ngữ

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="Túi vải lanh cho video bán hàng đa ngôn ngữ" width="420"></a>

[Quảng cáo và mạng xã hội](prompts/commerce-social.md) · [Khung hình đầu tham chiếu](assets/seaimagine-linen-pouch.png) · [Văn bản thuần](prompts/copy/showcase-06.txt)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

Mỗi ngày thêm nhẹ nhàng

<a id="video-studies"></a>

## Kết quả từ nguồn chính thức và cộng đồng

Ví dụ chính thức sử dụng Gemini Omni 1.1 Flash; ví dụ cộng đồng được đăng vào tháng 5 năm 2026 và sử dụng các phiên bản Omni trước đó. Liên kết dẫn đến bài đăng gốc; kho này không tuyên bố đã tái tạo các kết quả đó. Bằng chứng cộng đồng lấy từ FxTwitter; chưa kiểm chứng việc phát video trực tiếp trên X.

| Google · Omni 1.1 Flash | Liên kết |
|---|---|
| Kéo dài cảnh đậm chất điện ảnh | [Xem video](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| Chuyển tiếp giữa khung hình đầu và cuối | [Xem video](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| Bản nháp tảo cát biển 360p | [Xem video](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/kw_omni-flash__capability-video__draft-360p__16x9__v1_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |
| Vũ đạo theo video tham chiếu | [Xem video](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__video-reference__16x9.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/) |

| X · Omni / Flash · 2026-05 | X · Omni / Flash · 2026-05 |
|---|---|
| **Biến người thành hồng hạc**<br><a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="Biến người thành hồng hạc" width="240"></a><br>CHRIS FIRST<br>[Nguồn](https://x.com/chrisfirst/status/2056797606509158681) · [Xem video](https://video.twimg.com/amplify_video/2056797343085969408/vid/avc1/1080x1440/UYr_7RKomiginRgq.mp4?tag=27) | **Đổi mũ theo từng tiếng vỗ tay**<br><a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Đổi mũ theo từng tiếng vỗ tay" width="240"></a><br>Justine Moore<br>[Nguồn](https://x.com/venturetwins/status/2056793856843366789) · [Xem video](https://video.twimg.com/amplify_video/2056793760273686528/vid/avc1/720x1280/Q73liRfIjPtGSveL.mp4?tag=27) |
| **Minh họa quá trình quang hợp**<br><a href="https://x.com/mrfanduu/status/2056692235174097398"><img src="https://pbs.twimg.com/amplify_video_thumb/2056691792175833088/img/W0_pZkQwRicpRjjG.jpg" alt="Minh họa quá trình quang hợp" width="240"></a><br>Fandu<br>[Nguồn](https://x.com/mrfanduu/status/2056692235174097398) · [Xem video](https://video.twimg.com/amplify_video/2056691792175833088/vid/avc1/1280x720/Ws-92fvVr5e-FkYZ.mp4?tag=14) | **Zoom cầm tay vào London Eye**<br><a href="https://x.com/fofrAI/status/2056789242274259242"><img src="https://pbs.twimg.com/amplify_video_thumb/2056503814874861569/img/mQnHwThYDypoS1H6.jpg" alt="Zoom cầm tay vào London Eye" width="240"></a><br>fofr<br>[Nguồn](https://x.com/fofrAI/status/2056789242274259242) · [Xem video](https://video.twimg.com/amplify_video/2056503814874861569/vid/avc1/1280x720/Lc2C4YtTflfGA8qe.mp4?tag=27) |
| **So sánh video gốc và bản chỉnh sửa**<br><a href="https://x.com/Mho_23/status/2057151867927601413"><img src="https://pbs.twimg.com/amplify_video_thumb/2057151701904146432/img/yhVQfdBM34BQJjV3.jpg" alt="So sánh video gốc và bản chỉnh sửa" width="240"></a><br>Miko<br>[Nguồn](https://x.com/Mho_23/status/2057151867927601413) · [Xem video](https://video.twimg.com/amplify_video/2057151701904146432/vid/avc1/1080x1920/JfeFoDd5udd_FRR7.mp4?tag=27) | **Bình nước đổi chất liệu khi chạm**<br><a href="https://x.com/alexanderchen/status/2057176690519089166"><img src="https://pbs.twimg.com/amplify_video_thumb/2057176000459612161/img/wTZ0HcgL_8PHxwbY.jpg" alt="Bình nước đổi chất liệu khi chạm" width="240"></a><br>Alexander Chen<br>[Nguồn](https://x.com/alexanderchen/status/2057176690519089166) · [Xem video](https://video.twimg.com/amplify_video/2057176000459612161/vid/avc1/1280x720/LRzM8IueMomPMa7J.mp4?tag=27) · [Câu lệnh đầy đủ](https://x.com/alexanderchen/status/2057176691903279524) |
[Nguồn / FxTwitter](docs/community-examples.md)

## Tài liệu nâng cao

Các bài hướng dẫn nằm ở trang riêng. [Xem](docs/guides/README_VI.md)

[Thiết kế prompt](docs/prompting-guide.md) · [Hướng dẫn đa ngôn ngữ](docs/multilingual-guide.md) · [Tư liệu tham chiếu và quyền sử dụng](docs/reference-videos.md)

<a id="brand-tools"></a>

## Sáng tạo với SeaImagine

[Gemini Omni](https://seaimagine.com/vi/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/vi/model/gemini-omni-1-1-flash/)

[Ảnh thành video](https://seaimagine.com/vi/image-to-video/) · [Văn bản thành video](https://seaimagine.com/vi/text-to-video/) · [Tạo ảnh bằng AI](https://seaimagine.com/vi/ai-image-generator/)

Các trang này là những lựa chọn khởi đầu khác. Xem mô hình, điều khoản và giá hiện tại trên từng trang. Kho này không bảo đảm dịch vụ luôn sẵn có.

[Quy trình SeaImagine](docs/seaimagine-workflow.md)

## Nguồn và giấy phép

Chuyển thể từ kho Flaq AI, gồm bộ prompt và ba ảnh tham chiếu. Không phải mọi nội dung đều do SeaImagine tự sáng tạo. Đây là hướng dẫn độc lập, không phải sản phẩm chính thức của Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE) · [Contributing](CONTRIBUTING.md)
