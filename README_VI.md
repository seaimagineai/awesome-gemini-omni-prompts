# Thư viện prompt video Gemini Omni cho SeaImagine

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![Thư viện prompt video Gemini Omni cho SeaImagine](assets/seaimagine-omni-hero.png)

60 prompt được chuyển thể từ kho Flaq AI cho người dùng SeaImagine: quảng cáo sản phẩm, du lịch, hoạt hình và chỉnh sửa. Ba ví dụ dưới đây có ảnh tham chiếu và prompt tiếng Anh đầy đủ để sao chép.

[Gemini Omni](https://seaimagine.com/vi/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/vi/model/gemini-omni-1-1-flash/)

## Bắt đầu với SeaImagine

1. Mở trang mô hình và kiểm tra quyền truy cập, giá cùng các thiết lập hiện có.
2. Để giữ ngoại hình sản phẩm hoặc nhân vật, chọn tạo video từ ảnh, tải lên một ảnh và dán prompt tương ứng. Với cảnh mới, hãy thử tạo video từ văn bản.
3. Chọn thời lượng và tỷ lệ khung hình trong giao diện. Thử một cảnh, kiểm tra ngoại hình, chuyển động và âm thanh, rồi sửa từng chỉ dẫn một.

Đây là các bản thiết kế prompt, chưa phải kết quả tạo video được kiểm chứng trên SeaImagine. Thời lượng, âm thanh, chỉnh sửa, kéo dài và ảnh tham chiếu phụ thuộc vào mô hình cùng giao diện hiện tại. Tính năng API Google không đồng nghĩa SeaImagine đã hỗ trợ.

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
