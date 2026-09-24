# คลังพรอมป์วิดีโอ Gemini Omni สำหรับ SeaImagine

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![คลังพรอมป์วิดีโอ Gemini Omni สำหรับ SeaImagine](assets/seaimagine-omni-hero.png)

คลังนี้เก็บสูตรต้นฉบับทั้ง 60 รายการของ Flaq AI ไว้ และเพิ่มแบบฝึกหัด SeaImagine อีก 3 แบบพร้อมภาพอ้างอิงที่สร้างขึ้นใหม่ หน้านี้รวมแบบฝึกหัดใหม่ ตัวอย่างจากคลังต้นฉบับ และสิ่งที่เรียนรู้ได้จากตัวอย่างทางการกับชุมชน

[Gemini Omni](https://seaimagine.com/th/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/th/model/gemini-omni-1-1-flash/)

[แบบฝึกหัด SeaImagine 3 แบบพร้อมภาพอ้างอิงที่สร้างขึ้นใหม่](#sea-practice) · [พรอมป์ 3 ชุดสำหรับคัดลอก](#source-examples) · [เรียนรู้อะไรจากตัวอย่างทางการและชุมชน](#video-studies)

## เริ่มใช้ SeaImagine

1. เปิดหน้ารุ่นโมเดลเพื่อตรวจสอบการเข้าใช้งาน ราคา และการตั้งค่าที่มีในขณะนี้
2. หากต้องการรักษารูปลักษณ์สินค้าหรือตัวละคร ให้เลือกสร้างวิดีโอจากภาพ อัปโหลดภาพหนึ่งภาพ แล้ววางพรอมป์ที่ตรงกัน หากต้องการฉากใหม่ ให้ลองสร้างวิดีโอจากข้อความ
3. เลือกความยาวและสัดส่วนภาพในหน้าจอ ทดลองหนึ่งช็อต ตรวจสอบรูปลักษณ์ การเคลื่อนไหว และเสียง แล้วปรับคำสั่งทีละข้อ

เนื้อหานี้เป็นแนวทางเขียนพรอมป์ ไม่ใช่ผลลัพธ์ที่ทดสอบแล้วบน SeaImagine ความยาว เสียง การแก้ไข การต่อวิดีโอ และสื่ออ้างอิงขึ้นอยู่กับโมเดลและหน้าจอปัจจุบัน ฟีเจอร์ใน Google API ไม่ได้หมายความว่า SeaImagine รองรับด้วย

<a id="sea-practice"></a>

## แบบฝึกหัด SeaImagine 3 แบบพร้อมภาพอ้างอิงที่สร้างขึ้นใหม่

ภาพอ้างอิงเหล่านี้สร้างด้วย AI เพื่อใช้เป็นเฟรมแรกสำหรับฝึก ไม่ใช่ผลวิดีโอ Gemini ที่ผ่านการทดสอบ ให้ใช้เฉพาะฟังก์ชันที่มีในหน้า SeaImagine ของคุณ

### SEA-01 · แก้วเซรามิกสีเขียวอมฟ้าในแสงยามเช้า

[![แก้วเซรามิกสีเขียวอมฟ้าในแสงยามเช้า](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

เคลื่อนกล้องเข้าใกล้ช้า ๆ โดยคงหูจับ ขอบแก้ว และระดับของเหลวไว้ พร้อมเว้นพื้นที่ท้ายคลิปสำหรับข้อความ

อัปโหลดภาพแก้วเพื่อสร้างวิดีโอ เริ่มจากการเคลื่อนกล้องเข้าใกล้เพียงอย่างเดียว ตรวจหูจับและระดับของเหลวก่อนใส่ข้อความ

[ภาพเป็นวิดีโอ](https://seaimagine.com/th/image-to-video/) · [สร้างภาพด้วย AI](https://seaimagine.com/th/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · ท่าเรือกระดาษที่ค่อย ๆ เปิดไฟ

[![ท่าเรือกระดาษที่ค่อย ๆ เปิดไฟ](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

ในช็อตเดียว ให้ประภาคารเปิดไฟ แล้วเพิ่มความสว่างที่หน้าต่างบ้านทั้งสามหลังทีละหลัง โดยคงพื้นผิวกระดาษและรูปทรงเดิม

อัปโหลดภาพท่าเรือ ขอให้ประภาคารเปิดไฟแล้วเพิ่มความสว่างของหน้าต่างตามลำดับ เปรียบเทียบรูปทรงอาคารตอนต้นกับตอนท้าย

[ภาพเป็นวิดีโอ](https://seaimagine.com/th/image-to-video/) · [สร้างภาพด้วย AI](https://seaimagine.com/th/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · ถุงผ้าลินินสำหรับวิดีโอขายสินค้าหลายภาษา

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="ถุงผ้าลินินสำหรับวิดีโอขายสินค้าหลายภาษา" width="360"></a>

สร้างวิดีโอสินค้าแนวตั้งที่ไม่มีตัวอักษรก่อน แล้วใส่ข้อความแต่ละภาษาด้วยโปรแกรมตัดต่อทั่วไป

ใช้ภาพถุงผ้าสร้างวิดีโอแนวตั้ง แล้วใส่ข้อความที่แปลไว้ภายหลัง ใช้คำสั่งแก้ไขวิดีโอแบบสั้นเฉพาะเมื่อมีฟังก์ชันนี้

[ภาพเป็นวิดีโอ](https://seaimagine.com/th/image-to-video/) · [สร้างภาพด้วย AI](https://seaimagine.com/th/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> ให้ทุกวันเรียบง่ายขึ้น

<a id="source-examples"></a>

## พรอมป์ 3 ชุดสำหรับคัดลอก

ภาพเหล่านี้นำมาจากคลังต้นฉบับเพื่อใช้เป็นเฟรมแรกอ้างอิง ไม่ใช่ผลลัพธ์วิดีโอ ให้อัปโหลดภาพที่ตรงกันเป็น Image1 ความยาว 10 วินาทีและเสียงเป็นเป้าหมายที่ต้องปรับตามการตั้งค่าที่มี

### 01 · ลำโพงสินค้า: จังหวะหยดน้ำ

![ลำโพงสินค้า: จังหวะหยดน้ำ](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · ปั่นจักรยานบนสันเขา: เปิดสารคดี

![ปั่นจักรยานบนสันเขา: เปิดสารคดี](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · ช่างนาฬิกากับนกกระดาษ: เรื่องเล่าภาพวาด

![ช่างนาฬิกากับนกกระดาษ: เรื่องเล่าภาพวาด](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



<a id="video-studies"></a>

## เรียนรู้อะไรจากตัวอย่างทางการและชุมชน

วิดีโอของ Google เป็นการสาธิต Omni 1.1 Flash ไม่ใช่ผลงานจาก SeaImagine โพสต์ชุมชนเผยแพร่ในเดือนพฤษภาคม 2026 และเกี่ยวกับ Omni / Flash รุ่นแรก ยังไม่ยืนยันว่าเป็นการทดสอบรุ่น 1.1 หลักฐานมาจากข้อความและข้อมูลสื่อของ FxTwitter โดยไม่ได้ตรวจการเล่นวิดีโอบน X โดยตรง โปรดตรวจฟังก์ชันใน SeaImagine ก่อนใช้

### Google: เชื่อมเฟรมแรกกับเฟรมสุดท้าย

[ดูตัวอย่างต้นฉบับ](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4)

กำหนดภาพเริ่มต้น ภาพสุดท้าย และการเคลื่อนไหวต่อเนื่องระหว่างสองภาพแยกกัน

ถ่ายวัตถุชิ้นเดียวกันสองภาพจากมุมที่เชื่อมกันได้ หากมีฟังก์ชันเฟรมแรกและเฟรมสุดท้าย ให้เชื่อมด้วยการเคลื่อนไหวง่าย ๆ

### Google: ต่อความยาวของช็อต

[ดูตัวอย่างต้นฉบับ](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4)

อธิบายการเคลื่อนกล้องถัดไปโดยคงตัวแบบและทิศทางการเคลื่อนไหว

ใช้คลิปสั้นของคุณเอง หากต่อความยาวได้ ให้เพิ่มเพียงช่วงเดียว แล้วตรวจรอยต่อว่าการเคลื่อนไหวหรือแสงกระโดดหรือไม่

### CHRIS FIRST: เปลี่ยนคนเป็นนกฟลามิงโก

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: เปลี่ยนคนเป็นนกฟลามิงโก" width="300"></a>

[ดูตัวอย่างต้นฉบับ](https://x.com/chrisfirst/status/2056797606509158681)

เปลี่ยนตัวแบบแต่ระบุให้คงเสื้อผ้าและท่าทางไว้ ตรวจจุดสัมผัสของแขนขาด้วย

หากแก้ไขวิดีโอได้ ให้เปลี่ยนตัวแบบเพียงตัวเดียวในคลิปของคุณ เปรียบเทียบเสื้อผ้า ท่าทาง และจุดสัมผัสพื้นก่อนกับหลัง

### Justine Moore: เปลี่ยนหมวกทุกครั้งที่ปรบมือ

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: เปลี่ยนหมวกทุกครั้งที่ปรบมือ" width="300"></a>

[ดูตัวอย่างต้นฉบับ](https://x.com/venturetwins/status/2056793856843366789)

ใช้ท่าทางที่มองเห็นชัดเป็นจังหวะเปลี่ยน โดยคงใบหน้า เสื้อผ้า และกล้องไว้

ตั้งกล้องนิ่งและถ่ายการปรบมือชัด ๆ สองครั้ง หากแก้ไขวิดีโอได้ ให้เปลี่ยนหมวกทุกครั้งที่ปรบมือ แล้วตรวจจังหวะทีละเฟรม

[ตัวอย่างทางการและจากชุมชน](docs/community-examples.md)

## เนื้อหา

รายการนี้เป็นสิ่งที่วางแผนในพรอมป์ได้ ไม่ใช่การรับรองว่ามีทุกฟังก์ชัน โปรดตรวจสอบข้อมูลนำเข้า การแก้ไข การต่อวิดีโอ เสียง และความละเอียดในโมเดลและหน้าจอ SeaImagine ที่เลือก เริ่มตรวจองค์ประกอบ คำพูด และข้อความด้วยการตั้งค่าตัวอย่างที่มีให้ API ของ Google (ช่องทางเรียกใช้ด้วยโปรแกรม) เป็นคนละบริการกับหน้าเว็บ SeaImagine

- ข้อความเป็นวิดีโอ ภาพเป็นวิดีโอ เฟรมแรก/สุดท้าย และภาพอ้างอิงตัวละครหรือสินค้า
- การออกแบบภาพ เสียงบรรยากาศ โฟลีย์ ดนตรีต้นฉบับ ความเงียบ และบทพูดร่วมกัน
- แนวทางบทพูด ข้อความบนจอ การตัดบรรทัด และการตรวจโดยเจ้าของภาษา 15 ภาษา

## พรอมป์ทั้งหมด 60 รายการ

คำอธิบายของ 5 หมวดแรกเป็นภาษาจีน และ 2 หมวดสุดท้ายเป็นภาษาอังกฤษ พรอมป์ควบคุมที่คัดลอกได้ทั้งหมดเป็นภาษาอังกฤษ เนื้อหาแต่ละหมวดยังไม่ได้แปลครบทุกภาษา

- [ภาพยนตร์และการเล่าเรื่อง: 8 รายการ](prompts/cinematic-storytelling.md)
- [โฆษณาและโซเชียลมีเดีย: 8 รายการ](prompts/commerce-social.md)
- [สารคดี ท่องเที่ยว และการศึกษา: 8 รายการ](prompts/documentary-education.md)
- [แอนิเมชัน ดนตรี และความบันเทิง: 8 รายการ](prompts/stylized-entertainment.md)
- [การควบคุม การแก้ไข และการต่อวิดีโอ: 10 รายการ](prompts/control-editing-extension.md)
- [การแก้ไขขั้นสูง กล้อง และการแปลงภาพ: 9 รายการ](prompts/advanced-editing-camera.md)
- [สตอรีบอร์ด แบ่งหน้าจอ ข้อความ และการประเมิน: 9 รายการ](prompts/storyboard-text-evaluation.md)

## บทพูดภาษาไทย

อาจคงคำสั่งฉากเป็นภาษาอังกฤษ และระบุบทพูดกับข้อความบนจอเป็นภาษาไทยให้ตรงตามต้องการ ตรวจสอบการออกเสียง การสะกด และจังหวะเวลา

```text
Spoken language: Thai.
Exact dialogue at 6s, spoken once with natural conversational pacing: "วันนี้กลับบ้านทางอ้อมกันเถอะ"
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Thai title: "การเดินทางเล็ก ๆ"
Keep it on one line with large readable Thai text. No other text.
```

## อ่านเพิ่มเติม

- [ขั้นตอนใช้งาน SeaImagine](docs/seaimagine-workflow.md)
- [ตัวอย่างทางการและจากชุมชน](docs/community-examples.md)
- [คู่มือหลายภาษา](docs/multilingual-guide.md)
- [การออกแบบพรอมป์](docs/prompting-guide.md)
- [สื่ออ้างอิงและสิทธิ์ใช้งาน](docs/reference-videos.md)

## เครื่องมืออื่นของ SeaImagine

ใช้หน้าเหล่านี้เป็นทางเลือกเริ่มต้นอื่นได้ ตรวจสอบโมเดล เงื่อนไข และราคาปัจจุบันในแต่ละหน้า คลังนี้ไม่รับประกันว่าบริการจะพร้อมใช้ตลอดเวลา

- [เริ่มสร้าง](https://seaimagine.com/th/create/)
- [ภาพเป็นวิดีโอ](https://seaimagine.com/th/image-to-video/)
- [ข้อความเป็นวิดีโอ](https://seaimagine.com/th/text-to-video/)
- [สร้างภาพด้วย AI](https://seaimagine.com/th/ai-image-generator/)

## แหล่งที่มาและสัญญาอนุญาต

ดัดแปลงจากคลัง Flaq AI รวมถึงชุดพรอมป์และภาพอ้างอิง 3 ภาพ เนื้อหาจึงไม่ได้สร้างขึ้นใหม่โดย SeaImagine ทั้งหมด คู่มือนี้เป็นโครงการอิสระ ไม่ใช่ผลิตภัณฑ์ทางการของ Google

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
