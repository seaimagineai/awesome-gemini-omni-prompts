# Videoprompts für Gemini Omni auf SeaImagine

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![Videoprompts für Gemini Omni auf SeaImagine](assets/seaimagine-omni-hero.png)

60 Prompts aus dem Flaq-AI-Quellrepository, für SeaImagine aufbereitet: Produktwerbung, Reisen, Animation und Schnitt. Die drei Beispiele enthalten Referenzbilder und vollständige englische Prompts.

[Gemini Omni](https://seaimagine.com/de/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/de/model/gemini-omni-1-1-flash/)

## Mit SeaImagine beginnen

1. Öffne die Modellseite und prüfe Zugang, Preis und verfügbare Einstellungen.
2. Soll ein Produkt oder eine Figur wiedererkennbar bleiben, wähle Bild zu Video, lade ein Bild hoch und füge den passenden Prompt ein. Für neue Szenen eignet sich Text zu Video als Einstieg.
3. Wähle Dauer und Format in der Oberfläche. Teste eine Einstellung, prüfe Aussehen, Bewegung und Ton und ändere jeweils nur eine Anweisung.

Dies sind Promptentwürfe, keine auf SeaImagine geprüften Videoergebnisse. Dauer, Ton, Bearbeitung, Verlängerung und Referenzen hängen vom Modell und der aktuellen Oberfläche ab. Funktionen der Google-API sind nicht automatisch in SeaImagine verfügbar.

## Drei Prompts zum Kopieren

Die Bilder sind übernommene Referenz-Startbilder aus dem Quellrepository, keine erzeugten Videoergebnisse. Lade das passende Bild als Image1 hoch. Zehn Sekunden und Ton sind Zielvorgaben; passe sie an die verfügbaren Einstellungen an.

### 01 · Lautsprecher: Wassertropfen im Takt

![Lautsprecher: Wassertropfen im Takt](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · Radfahrt auf dem Grat: Dokumentarfilmauftakt

![Radfahrt auf dem Grat: Dokumentarfilmauftakt](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · Uhrmacher und Papiervögel: illustrierte Geschichte

![Uhrmacher und Papiervögel: illustrierte Geschichte](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

## Alle 60 Prompts

Die ersten fünf Sammlungen haben chinesische Erläuterungen, die letzten zwei englische. Alle kopierbaren Steuerprompts sind englisch. Die Sammlungen sind nicht vollständig übersetzt.

- [Film und Storytelling: 8 Prompts](prompts/cinematic-storytelling.md)
- [Werbung und Social Media: 8 Prompts](prompts/commerce-social.md)
- [Dokumentation, Reise und Bildung: 8 Prompts](prompts/documentary-education.md)
- [Animation, Musik und Unterhaltung: 8 Prompts](prompts/stylized-entertainment.md)
- [Steuerung, Bearbeitung und Erweiterung: 10 Rezepte](prompts/control-editing-extension.md)
- [Fortgeschrittene Bearbeitung, Kamera und visuelle Transformation: 9 Prompts](prompts/advanced-editing-camera.md)
- [Storyboards, Split-Screens, Text und Evaluierung: 9 Prompts](prompts/storyboard-text-evaluation.md)

## Deutsche Dialoge

Bei Bedarf bleiben Szenenanweisungen englisch; Dialog und sichtbarer Text werden auf Deutsch wortgetreu festgelegt. Prüfe Aussprache, Schreibweise und Timing.

```text
Spoken language: German.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Lass uns heute den längeren Weg nach Hause nehmen."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen German title: "KLEINE REISEN"
Allow enough width for German compound words. No other text.
```

## Weiterlesen

- [SeaImagine-Arbeitsablauf](docs/seaimagine-workflow.md)
- [Offizielle und Community-Beispiele](docs/community-examples.md)
- [Mehrsprachiger Leitfaden](docs/multilingual-guide.md)
- [Prompts entwerfen](docs/prompting-guide.md)
- [Referenzmaterial und Rechte](docs/reference-videos.md)

## Weitere SeaImagine-Werkzeuge

Diese Seiten bieten weitere Einstiegsmöglichkeiten. Aktuelle Modelle, Bedingungen und Preise stehen auf der jeweiligen Seite. Dieses Repository garantiert keine ununterbrochene Verfügbarkeit.

- [Erstellen](https://seaimagine.com/de/create/)
- [Bild zu Video](https://seaimagine.com/de/image-to-video/)
- [Text zu Video](https://seaimagine.com/de/text-to-video/)
- [KI-Bildgenerator](https://seaimagine.com/de/ai-image-generator/)

## Quelle und Lizenz

Bearbeitung des Flaq-AI-Repositories einschließlich der Promptsammlungen und drei Referenzbilder. Nicht alle Inhalte wurden von SeaImagine neu erstellt. Unabhängiger Leitfaden, kein offizielles Google-Produkt.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
