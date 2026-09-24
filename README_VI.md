# Thư viện prompt video Gemini Omni cho SeaImagine

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![Thư viện prompt video Gemini Omni cho SeaImagine](assets/seaimagine-omni-hero.png)

Thư viện giữ nguyên 60 công thức gốc của Flaq AI và bổ sung ba bài tập SeaImagine với ảnh tham chiếu riêng. Trang này có các bài tập mới, ví dụ từ kho gốc và phần hướng dẫn học từ ví dụ chính thức cùng cộng đồng.

[Gemini Omni](https://seaimagine.com/vi/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/vi/model/gemini-omni-1-1-flash/)

[Ba bài tập SeaImagine với ảnh tham chiếu riêng](#sea-practice) · [Ba prompt để sao chép](#source-examples) · [Học gì từ ví dụ chính thức và cộng đồng](#video-studies)

## Bắt đầu với SeaImagine

1. Mở trang mô hình và kiểm tra quyền truy cập, giá cùng các thiết lập hiện có.
2. Để giữ ngoại hình sản phẩm hoặc nhân vật, chọn tạo video từ ảnh, tải lên một ảnh và dán prompt tương ứng. Với cảnh mới, hãy thử tạo video từ văn bản.
3. Chọn thời lượng và tỷ lệ khung hình trong giao diện. Thử một cảnh, kiểm tra ngoại hình, chuyển động và âm thanh, rồi sửa từng chỉ dẫn một.

Đây là các bản thiết kế prompt, chưa phải kết quả tạo video được kiểm chứng trên SeaImagine. Thời lượng, âm thanh, chỉnh sửa, kéo dài và ảnh tham chiếu phụ thuộc vào mô hình cùng giao diện hiện tại. Tính năng API Google không đồng nghĩa SeaImagine đã hỗ trợ.

<a id="sea-practice"></a>

## Ba bài tập SeaImagine với ảnh tham chiếu riêng

Các ảnh tham chiếu này được tạo bằng AI để làm khung hình đầu cho bài tập, không phải kết quả video Gemini đã được thử nghiệm. Hãy dùng các tính năng thực sự có trong giao diện SeaImagine.

### SEA-01 · Cốc gốm xanh ngọc trong ánh sáng ban mai

[![Cốc gốm xanh ngọc trong ánh sáng ban mai](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

Đưa máy quay lại gần từ từ, giữ nguyên quai, miệng cốc và mực chất lỏng. Chừa chỗ cho chữ ở cuối video.

Tải ảnh cốc lên để tạo video. Trước hết chỉ thử chuyển động tiến lại gần chậm, kiểm tra quai và mực chất lỏng rồi mới thêm chữ.

[Ảnh thành video](https://seaimagine.com/vi/image-to-video/) · [Tạo ảnh bằng AI](https://seaimagine.com/vi/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · Bến cảng giấy lần lượt lên đèn

[![Bến cảng giấy lần lượt lên đèn](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

Trong một cảnh quay, bật đèn hải đăng rồi lần lượt tăng độ sáng ở cửa sổ ba ngôi nhà. Giữ nguyên chất liệu giấy và hình khối.

Tải ảnh bến cảng lên, yêu cầu bật đèn hải đăng rồi tăng độ sáng các cửa sổ theo thứ tự. So sánh hình dạng công trình ở đầu và cuối video.

[Ảnh thành video](https://seaimagine.com/vi/image-to-video/) · [Tạo ảnh bằng AI](https://seaimagine.com/vi/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · Túi vải lanh cho video bán hàng đa ngôn ngữ

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="Túi vải lanh cho video bán hàng đa ngôn ngữ" width="360"></a>

Tạo video sản phẩm dọc không có chữ trước, rồi thêm phụ đề từng ngôn ngữ bằng phần mềm dựng video thông thường.

Tạo video dọc từ ảnh túi rồi thêm bản dịch sau. Chỉ dùng lệnh chỉnh sửa video ngắn khi giao diện có tính năng này.

[Ảnh thành video](https://seaimagine.com/vi/image-to-video/) · [Tạo ảnh bằng AI](https://seaimagine.com/vi/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> Mỗi ngày thêm nhẹ nhàng

<a id="source-examples"></a>

## Ba prompt để sao chép

Ảnh được dùng lại từ kho nguồn làm khung hình đầu tham chiếu, không phải kết quả video. Tải ảnh tương ứng lên dưới tên Image1. Yêu cầu 10 giây và âm thanh là mục tiêu; hãy điều chỉnh theo thiết lập hiện có.

### 01 · Loa sản phẩm: nhịp giọt nước

![Loa sản phẩm: nhịp giọt nước](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · Đạp xe trên sống núi: mở đầu phim tài liệu

![Đạp xe trên sống núi: mở đầu phim tài liệu](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · Thợ đồng hồ và chim giấy: câu chuyện minh họa

![Thợ đồng hồ và chim giấy: câu chuyện minh họa](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



<a id="video-studies"></a>

## Học gì từ ví dụ chính thức và cộng đồng

Video của Google minh họa Omni 1.1 Flash, không phải kết quả từ SeaImagine. Bài đăng cộng đồng được đăng vào tháng 5/2026, thuộc Omni / Flash ban đầu; chưa được xác nhận là thử nghiệm bản 1.1. Bằng chứng gồm văn bản và siêu dữ liệu phương tiện từ FxTwitter, chưa kiểm chứng phát video trực tiếp trên X. Hãy kiểm tra tính năng trong SeaImagine.

### Google: chuyển từ khung hình đầu đến cuối

[Xem ví dụ gốc](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4)

Xác định riêng ảnh đầu, ảnh cuối và chuyển động liên tục nối hai ảnh.

Chụp cùng một vật từ hai góc có thể nối với nhau. Nếu hỗ trợ khung hình đầu và cuối, hãy nối bằng một chuyển động đơn giản.

### Google: kéo dài cảnh quay

[Xem ví dụ gốc](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4)

Mô tả chuyển động máy quay tiếp theo, đồng thời giữ nguyên chủ thể và hướng chuyển động.

Dùng clip ngắn của bạn. Nếu có tính năng kéo dài, chỉ thêm một đoạn tiếp nối và kiểm tra xem chuyển động hoặc ánh sáng có bị nhảy ở điểm nối không.

### CHRIS FIRST: thay người bằng hồng hạc

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: thay người bằng hồng hạc" width="300"></a>

[Xem ví dụ gốc](https://x.com/chrisfirst/status/2056797606509158681)

Thay chủ thể nhưng yêu cầu giữ trang phục và hành động; kiểm tra các điểm tiếp xúc của tay chân.

Nếu có chỉnh sửa video, chỉ thay một chủ thể trong clip của bạn. So sánh trang phục, tư thế và tiếp xúc với mặt đất trước và sau.

### Justine Moore: đổi mũ sau mỗi tiếng vỗ tay

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: đổi mũ sau mỗi tiếng vỗ tay" width="300"></a>

[Xem ví dụ gốc](https://x.com/venturetwins/status/2056793856843366789)

Dùng một cử chỉ rõ ràng để xác định thời điểm đổi, đồng thời giữ nguyên khuôn mặt, trang phục và máy quay.

Cố định máy quay và quay hai lần vỗ tay rõ ràng. Nếu có chỉnh sửa video, yêu cầu đổi mũ mỗi lần vỗ tay rồi kiểm tra thời điểm theo từng khung hình.

[Ví dụ chính thức và cộng đồng](docs/community-examples.md)

## Nội dung

Danh sách này mô tả nội dung có thể lên kế hoạch trong prompt, không bảo đảm tính năng. Hãy kiểm tra đầu vào, chỉnh sửa, kéo dài, âm thanh và độ phân giải của mô hình đang chọn trên SeaImagine. Trước tiên, kiểm tra bố cục, lời nói và chữ bằng chế độ xem trước hiện có. API Google (giao diện lập trình) và giao diện SeaImagine là hai dịch vụ riêng.

- Văn bản thành video, hình ảnh thành video, khung đầu/cuối và tham chiếu nhân vật hoặc sản phẩm.
- Thiết kế đồng thời hình ảnh, âm thanh môi trường, foley, nhạc nguyên bản, khoảng lặng và lời thoại.
- Quy tắc lời thoại, chữ trên màn hình, xuống dòng và duyệt bởi người bản ngữ cho 15 ngôn ngữ.

## Toàn bộ 60 prompt

Năm nhóm đầu có phần giải thích bằng tiếng Trung, hai nhóm cuối bằng tiếng Anh. Tất cả prompt điều khiển đều bằng tiếng Anh. Nội dung các nhóm chưa được dịch đầy đủ.

- [Điện ảnh và kể chuyện: 8 prompt](prompts/cinematic-storytelling.md)
- [Quảng cáo và mạng xã hội: 8 prompt](prompts/commerce-social.md)
- [Tài liệu, du lịch và giáo dục: 8 prompt](prompts/documentary-education.md)
- [Hoạt hình, âm nhạc và giải trí: 8 prompt](prompts/stylized-entertainment.md)
- [Điều khiển, chỉnh sửa và mở rộng: 10 công thức](prompts/control-editing-extension.md)
- [Chỉnh sửa nâng cao, máy quay và biến đổi hình ảnh: 9 prompt](prompts/advanced-editing-camera.md)
- [Storyboard, chia màn hình, chữ và đánh giá: 9 prompt](prompts/storyboard-text-evaluation.md)

## Lời thoại tiếng Việt

Có thể giữ chỉ dẫn cảnh bằng tiếng Anh và ghi chính xác lời thoại, chữ trên màn hình bằng tiếng Việt. Kiểm tra phát âm, chính tả và thời điểm xuất hiện.

```text
Spoken language: Vietnamese.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Hôm nay mình đi đường vòng về nhà nhé."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Vietnamese title: "NHỮNG CHUYẾN ĐI NHỎ"
Preserve every Vietnamese tone mark exactly. No other text.
```

## Đọc thêm

- [Quy trình SeaImagine](docs/seaimagine-workflow.md)
- [Ví dụ chính thức và cộng đồng](docs/community-examples.md)
- [Hướng dẫn đa ngôn ngữ](docs/multilingual-guide.md)
- [Thiết kế prompt](docs/prompting-guide.md)
- [Tư liệu tham chiếu và quyền sử dụng](docs/reference-videos.md)

## Công cụ SeaImagine khác

Các trang này là những lựa chọn khởi đầu khác. Xem mô hình, điều khoản và giá hiện tại trên từng trang. Kho này không bảo đảm dịch vụ luôn sẵn có.

- [Tạo nội dung](https://seaimagine.com/vi/create/)
- [Ảnh thành video](https://seaimagine.com/vi/image-to-video/)
- [Văn bản thành video](https://seaimagine.com/vi/text-to-video/)
- [Tạo ảnh bằng AI](https://seaimagine.com/vi/ai-image-generator/)

## Nguồn và giấy phép

Chuyển thể từ kho Flaq AI, gồm bộ prompt và ba ảnh tham chiếu. Không phải mọi nội dung đều do SeaImagine tự sáng tạo. Đây là hướng dẫn độc lập, không phải sản phẩm chính thức của Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
