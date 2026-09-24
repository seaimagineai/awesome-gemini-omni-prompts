# คลังพรอมป์วิดีโอ Gemini Omni สำหรับ SeaImagine

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![คลังพรอมป์วิดีโอ Gemini Omni สำหรับ SeaImagine](assets/seaimagine-omni-hero.png)

พรอมป์ 60 รายการดัดแปลงจากคลัง Flaq AI สำหรับผู้ใช้ SeaImagine ครอบคลุมโฆษณาสินค้า การท่องเที่ยว แอนิเมชัน และการตัดต่อ ตัวอย่าง 3 ชุดด้านล่างมีภาพอ้างอิงและพรอมป์ภาษาอังกฤษฉบับเต็มให้คัดลอก

[Gemini Omni](https://seaimagine.com/th/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/th/model/gemini-omni-1-1-flash/)

## เริ่มใช้ SeaImagine

1. เปิดหน้ารุ่นโมเดลเพื่อตรวจสอบการเข้าใช้งาน ราคา และการตั้งค่าที่มีในขณะนี้
2. หากต้องการรักษารูปลักษณ์สินค้าหรือตัวละคร ให้เลือกสร้างวิดีโอจากภาพ อัปโหลดภาพหนึ่งภาพ แล้ววางพรอมป์ที่ตรงกัน หากต้องการฉากใหม่ ให้ลองสร้างวิดีโอจากข้อความ
3. เลือกความยาวและสัดส่วนภาพในหน้าจอ ทดลองหนึ่งช็อต ตรวจสอบรูปลักษณ์ การเคลื่อนไหว และเสียง แล้วปรับคำสั่งทีละข้อ

เนื้อหานี้เป็นแนวทางเขียนพรอมป์ ไม่ใช่ผลลัพธ์ที่ทดสอบแล้วบน SeaImagine ความยาว เสียง การแก้ไข การต่อวิดีโอ และสื่ออ้างอิงขึ้นอยู่กับโมเดลและหน้าจอปัจจุบัน ฟีเจอร์ใน Google API ไม่ได้หมายความว่า SeaImagine รองรับด้วย

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
