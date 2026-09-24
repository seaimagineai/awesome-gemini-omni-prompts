# Prompts vidéo Gemini Omni pour SeaImagine

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![Prompts vidéo Gemini Omni pour SeaImagine](assets/seaimagine-omni-hero.png)

60 prompts adaptés du dépôt Flaq AI pour les utilisateurs de SeaImagine : publicité, voyage, animation et montage. Les trois exemples ci-dessous comprennent une image de référence et un prompt complet en anglais.

[Gemini Omni](https://seaimagine.com/fr/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/fr/model/gemini-omni-1-1-flash/)

## Premiers pas avec SeaImagine

1. Ouvrez la page du modèle et vérifiez l’accès, le prix et les réglages disponibles.
2. Pour conserver l’apparence d’un produit ou d’un personnage, choisissez image vers vidéo, importez une image et collez le prompt associé. Pour inventer une scène, essayez texte vers vidéo.
3. Réglez la durée et le format dans l’interface. Testez un plan, vérifiez l’apparence, le mouvement et le son, puis modifiez une seule consigne à la fois.

Ce sont des propositions de prompts, pas des résultats de génération vérifiés sur SeaImagine. Durée, son, montage, prolongement et références dépendent du modèle et de l’interface actuelle. Les fonctions de l’API Google ne sont pas automatiquement disponibles sur SeaImagine.

## Trois prompts à copier

Ces images sont des premières images de référence reprises du dépôt source, pas des résultats vidéo. Importez l’image correspondante comme Image1. Les 10 secondes et le son indiquent le résultat souhaité ; adaptez-les aux réglages disponibles.

### 01 · Enceinte : rythme des gouttes

![Enceinte : rythme des gouttes](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · Cyclisme sur une crête : ouverture documentaire

![Cyclisme sur une crête : ouverture documentaire](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · Horloger et oiseaux de papier : récit illustré

![Horloger et oiseaux de papier : récit illustré](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```

## Les 60 prompts

Les cinq premières collections sont expliquées en chinois et les deux dernières en anglais. Tous les prompts à copier sont en anglais. Les collections ne sont pas intégralement traduites.

- [Cinéma et narration : 8 prompts](prompts/cinematic-storytelling.md)
- [Commerce et réseaux sociaux : 8 prompts](prompts/commerce-social.md)
- [Documentaire, voyage et éducation : 8 prompts](prompts/documentary-education.md)
- [Animation, musique et divertissement : 8 prompts](prompts/stylized-entertainment.md)
- [Contrôle, édition et extension : 10 recettes](prompts/control-editing-extension.md)
- [Montage avancé, caméra et transformation visuelle : 9 prompts](prompts/advanced-editing-camera.md)
- [Storyboards, écrans partagés, texte et évaluation : 9 prompts](prompts/storyboard-text-evaluation.md)

## Dialogues en français

Vous pouvez conserver les consignes de mise en scène en anglais et préciser mot pour mot le dialogue et le texte visible en français. Vérifiez prononciation, orthographe et synchronisation.

```text
Spoken language: French.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Aujourd'hui, prenons le chemin le plus long pour rentrer."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen French title: "PETITS VOYAGES"
Preserve accents, apostrophes and spelling exactly. No other text.
```

## Pour aller plus loin

- [Parcours SeaImagine](docs/seaimagine-workflow.md)
- [Exemples officiels et communautaires](docs/community-examples.md)
- [Guide multilingue](docs/multilingual-guide.md)
- [Conception des prompts](docs/prompting-guide.md)
- [Références et autorisations](docs/reference-videos.md)

## Autres outils SeaImagine

Ces pages offrent d’autres points de départ. Consultez chaque page pour connaître les modèles, conditions et tarifs actuels. Ce dépôt ne garantit pas une disponibilité continue.

- [Créer](https://seaimagine.com/fr/create/)
- [Image vers vidéo](https://seaimagine.com/fr/image-to-video/)
- [Texte vers vidéo](https://seaimagine.com/fr/text-to-video/)
- [Générateur d’images IA](https://seaimagine.com/fr/ai-image-generator/)

## Source et licence

Adaptation du dépôt Flaq AI, dont les collections de prompts et trois images sont reprises. Tout ce contenu n’est pas une création originale de SeaImagine. Guide indépendant, non officiel Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
