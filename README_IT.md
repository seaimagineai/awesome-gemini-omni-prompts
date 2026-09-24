<div align="center">

![Raccolta di prompt per Gemini Omni](assets/seaimagine-omni-hero.png)

# Raccolta di prompt per Gemini Omni

**Esplora le 60 ricette complete della raccolta originale, suddivise in sette categorie. Impara a descrivere la scena, scandire le azioni e guidare la camera e il suono, poi adatta un esempio alla tua idea.**

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md)

[Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)



[Tutti i 60 prompt](#prompt-collections) · [Tre prompt da copiare](#source-examples) · [Esempi ufficiali e della community](#video-studies) · [Guida multilingue](docs/multilingual-guide.md)

</div>

## Contenuti

L’elenco descrive cosa pianificare nei prompt, senza garantire la disponibilità delle funzioni. Verifica input, modifica, estensione, audio e risoluzione disponibili per il modello selezionato nello strumento che usi. Controlla prima composizione, dialogo e testo con un’anteprima disponibile. L’API di Google (interfaccia di programmazione) è distinta dall’interfaccia del tuo strumento.

- Testo-video, immagine-video, primo/ultimo fotogramma e riferimenti per soggetti o prodotti.
- Progettazione coordinata di immagini, ambiente, effetti, musica originale, silenzio e dialogo.
- Regole per dialogo, testo sullo schermo e revisione in 15 lingue.

## Dialoghi in italiano

Puoi mantenere le istruzioni di scena in inglese e indicare esattamente dialoghi e testi visibili in italiano. Controlla pronuncia, ortografia e tempi.

```text
Spoken language: Italian.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Oggi torniamo a casa facendo la strada più lunga."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen Italian title: "PICCOLI VIAGGI"
Preserve spelling and punctuation exactly. No other text.
```

<a id="prompt-collections"></a>

## Tutti i 60 prompt

Le prime cinque raccolte hanno spiegazioni in cinese, le ultime due in inglese. Tutti i prompt di controllo sono in inglese. Le raccolte non sono tradotte integralmente.

- [Cinema e narrazione: 8 prompt](prompts/cinematic-storytelling.md)
- [Commercio e social media: 8 prompt](prompts/commerce-social.md)
- [Documentari, viaggi e formazione: 8 prompt](prompts/documentary-education.md)
- [Animazione, musica e intrattenimento: 8 prompt](prompts/stylized-entertainment.md)
- [Controllo, modifica ed estensione: 10 ricette](prompts/control-editing-extension.md)
- [Montaggio avanzato, camera e trasformazione visiva: 9 prompt](prompts/advanced-editing-camera.md)
- [Storyboard, schermi divisi, testo e valutazione: 9 prompt](prompts/storyboard-text-evaluation.md)



## Prova il tuo primo prompt

1. Scegli un esempio completo simile alla scena che vuoi creare e copia tutto il prompt.
2. Scarica l’immagine di riferimento corrispondente e impostala come primo fotogramma, se lo strumento offre questa opzione.
3. Adatta i tempi alla durata e alla risoluzione disponibili. Genera una bozza, controlla il soggetto, il testo e il suono, poi modifica un solo elemento alla volta.

<a id="source-examples"></a>

## Tre prompt da copiare

Le immagini sono fotogrammi iniziali di riferimento ripresi dal repository originale, non risultati video. Carica l’immagine corrispondente come Image1. I 10 secondi e l’audio sono obiettivi: adattali ai controlli disponibili.

### 01 · Altoparlante: ritmo di gocce

![Altoparlante: ritmo di gocce](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · Ciclismo sul crinale: apertura documentaria

![Ciclismo sul crinale: apertura documentaria](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · Orologiaio e uccelli di carta: racconto illustrato

![Orologiaio e uccelli di carta: racconto illustrato](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



<a id="video-studies"></a>

## Cosa imparare dagli esempi ufficiali e della community

I video ufficiali di Google mostrano Omni 1.1 Flash. I post della comunità risalgono a maggio 2026 e riguardano l’Omni / Flash originale; non sono stati confermati come test della versione 1.1. Le prove provengono dal testo e dai metadati multimediali del mirror FxTwitter; la riproduzione diretta su X non è stata verificata. Sono esempi esterni, non risultati della piattaforma che utilizzi. Controlla le funzioni disponibili nel tuo strumento.

### Google: transizione tra fotogramma iniziale e finale

[Guarda l’esempio originale](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Definisci separatamente l’immagine iniziale, quella finale e il movimento continuo che le unisce.

Scatta due foto dello stesso oggetto da angoli compatibili. Se sono disponibili i fotogrammi iniziale e finale, collegale con un movimento semplice.

### Google: prolungare un’inquadratura

[Guarda l’esempio originale](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Descrivi il movimento di camera successivo mantenendo il soggetto e la direzione del movimento.

Usa un tuo breve video. Se è disponibile l’estensione, chiedi una sola continuazione e controlla salti di movimento o luce nel raccordo.

### CHRIS FIRST: persone trasformate in fenicotteri

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: persone trasformate in fenicotteri" width="300"></a>

[Guarda l’esempio originale](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

Cambia il soggetto chiedendo di mantenere vestiti e azione; controlla i punti di contatto degli arti.

Se puoi modificare video, sostituisci un solo soggetto in una tua ripresa. Confronta vestiti, postura e contatto con il suolo.

### Justine Moore: un cappello diverso a ogni battito di mani

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: un cappello diverso a ogni battito di mani" width="300"></a>

[Guarda l’esempio originale](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

Usa un gesto visibile per stabilire quando avviene ogni cambio, mantenendo volto, vestiti e camera.

Filma due battiti di mani ben visibili con la camera fissa. Se puoi modificare video, chiedi un cambio di cappello a ogni battito e controlla il momento fotogramma per fotogramma.

[Esempi ufficiali e della community](docs/community-examples.md)

## Approfondimenti

- [Esempi ufficiali e della community](docs/community-examples.md)
- [Guida multilingue](docs/multilingual-guide.md)
- [Progettazione dei prompt](docs/prompting-guide.md)
- [Riferimenti e autorizzazioni](docs/reference-videos.md)

<a id="brand-tools"></a>

## Inizia con SeaImagine

Questa raccolta conserva le 60 ricette originali di Flaq AI e aggiunge tre esercizi SeaImagine con immagini proprie. Qui trovi i nuovi esercizi, gli esempi del repository di origine e le lezioni tratte dai casi ufficiali e della community.

[Gemini Omni](https://seaimagine.com/it/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/it/model/gemini-omni-1-1-flash/)

1. Apri la pagina del modello e verifica accesso, prezzo e impostazioni disponibili.
2. Per mantenere riconoscibile un prodotto o personaggio, scegli immagine in video, carica un’immagine e incolla il relativo prompt. Per inventare una scena, prova testo in video.
3. Seleziona durata e formato nell’interfaccia. Prova una ripresa, controlla aspetto, movimento e suono e modifica una sola istruzione alla volta.

Sono proposte di prompt, non risultati verificati su SeaImagine. Durata, audio, montaggio, estensione e riferimenti dipendono dal modello e dall’interfaccia attuale. Le funzioni dell’API Google non sono automaticamente disponibili su SeaImagine.

<a id="sea-practice"></a>

## Tre esercizi SeaImagine con immagini originali

Queste immagini di riferimento sono state generate con IA come fotogrammi iniziali per esercitarsi. Non sono risultati video testati con Gemini. Usa le funzioni effettivamente disponibili in SeaImagine.

### SEA-01 · Una tazza in ceramica verde petrolio al mattino

[![Una tazza in ceramica verde petrolio al mattino](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

Avvicina lentamente la camera senza modificare manico, bordo o livello del liquido. Lascia spazio per il testo finale.

Carica l’immagine della tazza per animarla. Prova solo un lento avvicinamento e controlla manico e liquido prima di aggiungere il testo.

[Immagine in video](https://seaimagine.com/it/image-to-video/) · [Generatore di immagini IA](https://seaimagine.com/it/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · Un porto di carta si illumina

[![Un porto di carta si illumina](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

In un’unica inquadratura, accendi il faro e intensifica a turno le luci delle finestre delle tre case. Conserva la consistenza della carta e la geometria.

Carica l’immagine del porto e chiedi di accendere il faro, poi di intensificare le luci delle finestre in sequenza. Confronta le forme degli edifici all’inizio e alla fine.

[Immagine in video](https://seaimagine.com/it/image-to-video/) · [Generatore di immagini IA](https://seaimagine.com/it/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · Una pochette di lino per un negozio multilingue

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="Una pochette di lino per un negozio multilingue" width="360"></a>

Crea un video verticale pulito e senza scritte, poi aggiungi i sottotitoli tradotti con un normale programma di montaggio.

Crea un video verticale della pochette e aggiungi le traduzioni in seguito. Usa una breve istruzione di modifica video solo se la funzione è disponibile.

[Immagine in video](https://seaimagine.com/it/image-to-video/) · [Generatore di immagini IA](https://seaimagine.com/it/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> Ogni giorno, più semplice

[Procedura SeaImagine](docs/seaimagine-workflow.md)

## Altri strumenti SeaImagine

Usa queste pagine come altri punti di partenza. Verifica modelli, condizioni e prezzi attuali su ciascuna pagina. Questo repository non garantisce disponibilità continua.

- [Crea](https://seaimagine.com/it/create/)
- [Immagine in video](https://seaimagine.com/it/image-to-video/)
- [Testo in video](https://seaimagine.com/it/text-to-video/)
- [Generatore di immagini IA](https://seaimagine.com/it/ai-image-generator/)

## Fonte e licenza

Adattato dal repository Flaq AI, con le sue raccolte e tre immagini di riferimento. Non tutto il contenuto è originale di SeaImagine. Guida indipendente, non ufficiale di Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
