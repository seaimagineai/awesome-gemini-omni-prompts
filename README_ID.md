# Koleksi Prompt Gemini Omni

![Koleksi Prompt Gemini Omni](assets/seaimagine-omni-hero.png)

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

<a id="video-studies"></a>

## Pelajaran dari contoh resmi dan komunitas

Video resmi Google menampilkan Omni 1.1 Flash. Unggahan komunitas berasal dari Mei 2026 dan membahas Omni / Flash awal; belum terverifikasi sebagai pengujian versi 1.1. Bukti berasal dari teks dan metadata media di mirror FxTwitter; pemutaran langsung di X belum diverifikasi. Ini adalah contoh dari sumber lain, bukan hasil platform yang Anda gunakan. Periksa fitur yang tersedia pada alat Anda.

### Google: transisi bingkai awal ke akhir

[Lihat contoh asli](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Tentukan gambar awal, gambar akhir, dan gerakan berkesinambungan di antaranya secara terpisah.

Siapkan dua foto objek yang sama dari sudut yang sesuai. Jika bingkai awal dan akhir didukung, hubungkan dengan satu gerakan sederhana.

### Google: memperpanjang adegan

[Lihat contoh asli](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Jelaskan gerakan kamera berikutnya dengan mempertahankan subjek dan arah gerak.

Gunakan klip milik sendiri. Jika tersedia fitur perpanjangan, minta satu kelanjutan dan periksa perubahan mendadak pada gerak atau cahaya di sambungan.

### CHRIS FIRST: mengganti orang dengan flamingo

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: mengganti orang dengan flamingo" width="300"></a>

[Lihat contoh asli](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

Ganti subjek sambil secara tegas mempertahankan pakaian dan aksinya; periksa titik kontak anggota tubuh.

Jika penyuntingan video tersedia, ganti satu subjek dalam rekaman sendiri. Bandingkan pakaian, pose, dan kontak dengan tanah sebelum dan sesudahnya.

### Justine Moore: mengganti topi setiap tepukan

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: mengganti topi setiap tepukan" width="300"></a>

[Lihat contoh asli](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

Gunakan gerakan yang terlihat sebagai penanda pergantian; pertahankan wajah, pakaian, dan kamera.

Rekam dua tepukan jelas dengan kamera tetap. Jika penyuntingan video tersedia, minta topi berganti setiap tepukan dan periksa waktunya bingkai demi bingkai.

[Contoh resmi dan komunitas](docs/community-examples.md)

## Dari contoh ke prompt buatan sendiri

Jelajahi 60 resep lengkap dari koleksi sumber, yang dibagi menjadi tujuh kategori. Pelajari cara menjelaskan adegan, mengatur waktu aksi, serta mengarahkan kamera dan suara, lalu sesuaikan contoh dengan ide Anda.

### Coba prompt pertama Anda

1. Pilih contoh lengkap yang mendekati adegan yang ingin Anda buat, lalu salin seluruh prompt.
2. Unduh gambar referensi yang sesuai dan tetapkan sebagai bingkai pertama jika alat yang Anda gunakan mendukungnya.
3. Sesuaikan pembagian waktu dengan durasi dan resolusi yang tersedia. Buat draf, periksa subjek, teks, dan suara, lalu ubah satu hal setiap kali mencoba.

<a id="source-examples"></a>

## Tiga prompt untuk disalin

Gambar ini adalah referensi bingkai awal dari repositori sumber, bukan hasil video. Unggah gambar yang sesuai sebagai Image1. Durasi 10 detik dan audio adalah sasaran; sesuaikan dengan pengaturan yang tersedia.

### 01 · Speaker produk: irama tetesan air

![Speaker produk: irama tetesan air](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · Bersepeda di punggung bukit: pembuka dokumenter

![Bersepeda di punggung bukit: pembuka dokumenter](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · Pembuat jam dan burung kertas: kisah ilustrasi

![Pembuat jam dan burung kertas: kisah ilustrasi](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



## Isi proyek

Daftar ini berisi hal yang dapat direncanakan dalam prompt, bukan jaminan fitur. Periksa dukungan masukan, penyuntingan, perpanjangan, audio, dan resolusi pada model yang dipilih dalam alat Anda. Periksa komposisi, ucapan, dan teks melalui pratinjau yang tersedia terlebih dahulu. API Google (antarmuka pemrograman) berbeda dari antarmuka alat Anda.

- Teks-ke-video, gambar-ke-video, bingkai pertama/terakhir, serta referensi karakter dan produk.
- Perencanaan visual, ambience, foley, musik orisinal, keheningan, dan dialog secara terpadu.
- Aturan dialog, teks layar, tata letak, dan tinjauan penutur asli untuk 15 bahasa.

## Semua 60 prompt

Lima koleksi pertama memiliki penjelasan berbahasa Mandarin, dua terakhir berbahasa Inggris. Semua prompt kontrol menggunakan bahasa Inggris. Isi koleksi belum diterjemahkan seluruhnya.

- [Film dan penceritaan: 8 prompt](prompts/cinematic-storytelling.md)
- [Iklan dan media sosial: 8 prompt](prompts/commerce-social.md)
- [Dokumenter, perjalanan, dan pendidikan: 8 prompt](prompts/documentary-education.md)
- [Animasi, musik, dan hiburan: 8 prompt](prompts/stylized-entertainment.md)
- [Kontrol, penyuntingan, dan perpanjangan: 10 resep](prompts/control-editing-extension.md)
- [Penyuntingan lanjutan, kamera, dan transformasi visual: 9 prompt](prompts/advanced-editing-camera.md)
- [Storyboard, layar terbagi, teks, dan evaluasi: 9 prompt](prompts/storyboard-text-evaluation.md)

## Dialog dalam bahasa Indonesia

Jika perlu, pertahankan instruksi adegan dalam bahasa Inggris dan tentukan dialog serta teks layar dalam bahasa Indonesia secara persis. Periksa pelafalan, ejaan, dan waktu.

```text
Spoken language: Indonesian.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Hari ini, mari kita pulang lewat jalan yang lebih panjang."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Indonesian title: "PERJALANAN KECIL"
Preserve spelling exactly. No other text.
```

## Bacaan lanjutan

- [Contoh resmi dan komunitas](docs/community-examples.md)
- [Panduan multibahasa](docs/multilingual-guide.md)
- [Perancangan prompt](docs/prompting-guide.md)
- [Referensi dan izin](docs/reference-videos.md)

<a id="brand-tools"></a>

## Mulai dengan SeaImagine

Pustaka ini mempertahankan 60 resep asli Flaq AI dan menambahkan tiga latihan SeaImagine dengan gambar referensi sendiri. Halaman ini memuat latihan baru, contoh dari repositori asal, serta pelajaran dari contoh resmi dan komunitas.

[Gemini Omni](https://seaimagine.com/id/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/id/model/gemini-omni-1-1-flash/)

1. Buka halaman model dan periksa akses, harga, serta pengaturan yang tersedia.
2. Untuk menjaga tampilan produk atau karakter, pilih gambar ke video, unggah satu gambar, lalu tempel prompt yang sesuai. Untuk adegan baru, coba teks ke video.
3. Pilih durasi dan format pada antarmuka. Uji satu adegan, periksa tampilan, gerakan, dan suara, lalu ubah satu instruksi setiap kali.

Ini rancangan prompt, bukan hasil generasi yang telah diuji di SeaImagine. Durasi, audio, penyuntingan, perpanjangan, dan referensi bergantung pada model serta antarmuka saat ini. Fitur API Google tidak otomatis tersedia di SeaImagine.

<a id="sea-practice"></a>

## Tiga latihan SeaImagine dengan gambar referensi orisinal

Gambar referensi ini dibuat dengan AI sebagai bingkai awal latihan, bukan hasil video Gemini yang telah diuji. Gunakan fitur yang benar-benar tersedia di antarmuka SeaImagine.

### SEA-01 · Cangkir keramik hijau kebiruan di pagi hari

[![Cangkir keramik hijau kebiruan di pagi hari](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

Dekatkan kamera perlahan sambil mempertahankan gagang, bibir cangkir, dan ketinggian cairan. Sisakan ruang untuk teks penutup.

Unggah gambar cangkir untuk membuat video. Coba satu gerakan mendekat yang lambat; periksa gagang dan cairan sebelum menambahkan teks.

[Gambar ke video](https://seaimagine.com/id/image-to-video/) · [Generator gambar AI](https://seaimagine.com/id/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · Lampu pelabuhan kertas menyala bergantian

[![Lampu pelabuhan kertas menyala bergantian](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

Dalam satu pengambilan gambar, nyalakan mercusuar, lalu terangkan cahaya jendela ketiga rumah secara bergantian. Pertahankan tekstur kertas dan bentuknya.

Unggah gambar pelabuhan. Minta mercusuar menyala dan cahaya jendela bertambah terang secara berurutan. Bandingkan bentuk bangunan di awal dan akhir.

[Gambar ke video](https://seaimagine.com/id/image-to-video/) · [Generator gambar AI](https://seaimagine.com/id/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · Kantong linen untuk toko multibahasa

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="Kantong linen untuk toko multibahasa" width="360"></a>

Buat video produk vertikal tanpa tulisan, lalu tambahkan teks terjemahan di aplikasi penyunting video biasa.

Buat video vertikal dari gambar kantong, lalu tambahkan terjemahan. Gunakan instruksi penyuntingan video singkat hanya jika fitur tersebut tersedia.

[Gambar ke video](https://seaimagine.com/id/image-to-video/) · [Generator gambar AI](https://seaimagine.com/id/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> Keseharian jadi lebih mudah

[Alur kerja SeaImagine](docs/seaimagine-workflow.md)

## Alat SeaImagine lainnya

Gunakan halaman ini sebagai pilihan awal lainnya. Periksa model, ketentuan, dan harga terkini pada setiap halaman. Repositori ini tidak menjamin ketersediaan tanpa henti.

- [Buat](https://seaimagine.com/id/create/)
- [Gambar ke video](https://seaimagine.com/id/image-to-video/)
- [Teks ke video](https://seaimagine.com/id/text-to-video/)
- [Generator gambar AI](https://seaimagine.com/id/ai-image-generator/)

## Sumber dan lisensi

Diadaptasi dari repositori Flaq AI, termasuk kumpulan prompt dan tiga gambar referensi. Tidak semua materi merupakan karya asli SeaImagine. Panduan independen, bukan produk resmi Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
