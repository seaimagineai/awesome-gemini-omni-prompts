# Gemini Omni — Tài liệu nâng cao

[Mục lục đầy đủ 60 câu lệnh](../../README_VI.md)

## Nội dung

Danh sách này mô tả nội dung có thể lên kế hoạch trong prompt, không bảo đảm tính năng. Hãy kiểm tra đầu vào, chỉnh sửa, kéo dài, âm thanh và độ phân giải mà mô hình đang chọn hỗ trợ trong công cụ của bạn. Trước tiên, kiểm tra bố cục, lời nói và chữ bằng chế độ xem trước hiện có. API Google (giao diện lập trình) và giao diện công cụ của bạn là hai dịch vụ riêng.

- Văn bản thành video, hình ảnh thành video, khung đầu/cuối và tham chiếu nhân vật hoặc sản phẩm.
- Thiết kế đồng thời hình ảnh, âm thanh môi trường, foley, nhạc nguyên bản, khoảng lặng và lời thoại.
- Quy tắc lời thoại, chữ trên màn hình, xuống dòng và duyệt bởi người bản ngữ cho 15 ngôn ngữ.

## Lời thoại tiếng Việt

Có thể giữ chỉ dẫn cảnh bằng tiếng Anh và ghi chính xác lời thoại, chữ trên màn hình bằng tiếng Việt. Kiểm tra phát âm, chính tả và thời điểm xuất hiện.

```text
Spoken language: Vietnamese.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Hôm nay mình đi đường vòng về nhà nhé."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Vietnamese title: "NHỮNG CHUYẾN ĐI NHỎ"
Preserve every Vietnamese tone mark exactly. No other text.
```



<a id="sea-practice"></a>

## Ba bài tập SeaImagine với ảnh tham chiếu riêng

Các ảnh tham chiếu này được tạo bằng AI để làm khung hình đầu cho bài tập, không phải kết quả video Gemini đã được thử nghiệm. Hãy dùng các tính năng thực sự có trong giao diện SeaImagine.

### SEA-01 · Cốc gốm xanh ngọc trong ánh sáng ban mai

[![Cốc gốm xanh ngọc trong ánh sáng ban mai](../../assets/seaimagine-ceramic-cup.png)](../../assets/seaimagine-ceramic-cup.png)

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

[![Bến cảng giấy lần lượt lên đèn](../../assets/seaimagine-paper-harbor.png)](../../assets/seaimagine-paper-harbor.png)

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

<a href="../../assets/seaimagine-linen-pouch.png"><img src="../../assets/seaimagine-linen-pouch.png" alt="Túi vải lanh cho video bán hàng đa ngôn ngữ" width="360"></a>

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
