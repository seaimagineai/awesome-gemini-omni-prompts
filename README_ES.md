# Biblioteca de prompts de Gemini Omni

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

<a id="video-studies"></a>

## Qué aprender de los ejemplos oficiales y de la comunidad

Los vídeos oficiales de Google muestran Omni 1.1 Flash. Las publicaciones de la comunidad son de mayo de 2026 y corresponden al Omni / Flash inicial; no se han confirmado como pruebas de 1.1. La evidencia procede del texto y los metadatos del espejo FxTwitter; no se ha verificado la reproducción directa en X. Son ejemplos externos, no resultados de la plataforma que elijas. Consulta las funciones disponibles en tu herramienta.

### Google: transición entre el primer y el último fotograma

[Ver el ejemplo original](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Define por separado la imagen inicial, la final y el movimiento continuo que las une.

Prepara dos fotos del mismo objeto desde ángulos compatibles. Si se admiten fotogramas inicial y final, únelas con un movimiento sencillo.

### Google: prolongar una toma

[Ver el ejemplo original](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4) · [Google](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)

Describe el siguiente movimiento de cámara manteniendo el sujeto y la dirección del movimiento.

Usa un clip propio. Si hay función de extensión, pide una sola continuación y revisa los saltos de movimiento o luz en la unión.

### CHRIS FIRST: convertir personas en flamencos

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST: convertir personas en flamencos" width="300"></a>

[Ver el ejemplo original](https://x.com/chrisfirst/status/2056797606509158681) · [FxTwitter](https://api.fxtwitter.com/status/2056797606509158681) · [Google AI](https://x.com/GoogleAI/status/2056829479696400608)

Cambia el sujeto, pero conserva explícitamente la ropa y la acción; revisa los puntos de contacto de las extremidades.

Si puedes editar vídeo, sustituye un solo sujeto en una grabación propia. Compara la ropa, la postura y el contacto con el suelo.

### Justine Moore: cambiar de sombrero con cada palmada

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore: cambiar de sombrero con cada palmada" width="300"></a>

[Ver el ejemplo original](https://x.com/venturetwins/status/2056793856843366789) · [FxTwitter](https://api.fxtwitter.com/status/2056793856843366789) · [Google AI](https://x.com/GoogleAI/status/2056829481218949533)

Usa un gesto visible para marcar cada cambio y mantén la cara, la ropa y la cámara.

Graba dos palmadas claras con la cámara fija. Si puedes editar vídeo, pide un sombrero nuevo en cada palmada y revisa el momento fotograma a fotograma.

[Ejemplos oficiales y de la comunidad](docs/community-examples.md)

## De los ejemplos a tus propios prompts

Explora las 60 recetas completas de la biblioteca original, divididas en siete categorías. Aprende a describir la escena, ordenar las acciones en el tiempo y dirigir la cámara y el sonido; después adapta un ejemplo a tu idea.

### Prueba tu primer prompt

1. Elige un ejemplo completo parecido a la escena que quieres crear y copia todo el prompt.
2. Descarga su imagen de referencia y asígnala como primer fotograma si tu herramienta ofrece esa opción.
3. Ajusta los tiempos a la duración y resolución disponibles. Genera un borrador, revisa el sujeto, el texto y el sonido, y cambia una sola cosa cada vez.

<a id="source-examples"></a>

## Tres prompts para copiar

Las imágenes son fotogramas iniciales de referencia del repositorio original, no resultados de vídeo. Sube la imagen correspondiente como Image1. Los 10 segundos y el audio son objetivos; adáptalos a los controles disponibles.

### 01 · Altavoz: ritmo de gotas

![Altavoz: ritmo de gotas](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · Ciclismo en la cresta: apertura documental

![Ciclismo en la cresta: apertura documental](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · Relojero y pájaros de papel: relato ilustrado

![Relojero y pájaros de papel: relato ilustrado](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



## Qué encontrarás

La lista describe lo que puedes planificar con los prompts. Confirma las entradas, la edición, la extensión, el audio y la resolución disponibles para el modelo seleccionado en tu herramienta. Revisa primero la composición, el diálogo y el texto con una vista previa disponible. La API de Google (interfaz para programas) y la interfaz de tu herramienta son servicios distintos.

- Flujos de texto a video, imagen a video, fotograma inicial/final y referencias de sujetos.
- Diseño conjunto de imagen y audio: ambiente, foley, música original, silencios y diálogo.
- Guía de localización para 15 idiomas, con diálogo exacto, texto, RTL, longitud de línea y revisión nativa.
- Ediciones breves con `Keep everything else the same.` y extensiones coherentes.

## Los 60 prompts

Las cinco primeras colecciones tienen explicaciones en chino y las dos últimas en inglés. Todos los prompts de control están en inglés. Las colecciones no están traducidas por completo.

- [Cine y narrativa: 8 prompts](prompts/cinematic-storytelling.md)
- [Comercio y redes sociales: 8 prompts](prompts/commerce-social.md)
- [Documental, viajes y educación: 8 prompts](prompts/documentary-education.md)
- [Animación, música y entretenimiento: 8 prompts](prompts/stylized-entertainment.md)
- [Control multimodal, edición y extensión: 10 recetas](prompts/control-editing-extension.md)
- [Edición avanzada, cámara y transformación visual: 9 prompts](prompts/advanced-editing-camera.md)
- [Storyboards, pantalla dividida, texto y evaluación: 9 prompts](prompts/storyboard-text-evaluation.md)

## Diálogos en español

Puedes mantener las instrucciones de escena en inglés y fijar literalmente el diálogo y los textos en español. Revisa pronunciación, ortografía y tiempos.

```text
Spoken language: Spanish.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Hoy volvamos por el camino largo."
Do not translate, paraphrase, repeat or subtitle the dialogue.

Exact on-screen Spanish title, centered from 7s to 10s: "PEQUEÑOS VIAJES"
Preserve accents and spelling exactly. No other text anywhere in the video.
```

## Cambiar solo el texto en pantalla

Si el modelo seleccionado permite editar video, pide únicamente el cambio necesario sobre la versión terminada. Este ejercicio modifica texto dentro de la imagen, no un archivo de subtítulos.

```text
Change only the final on-screen text to Spanish: "CALIDEZ EN CAMINO". Preserve its original position, size, material and timing. Keep everything else the same.
```

## Plantilla de 10 segundos

```text
Format: 9:16 vertical, 10 seconds.
Goal: [audience and intended response]
Scene: [place, time, weather, layout]
Subject: [3-5 stable identity anchors]
Subject motion: [ordered action]
Camera motion: [height, path, focus]
Environment motion: [wind, light, water, particles]
[0-3s] [hook]
[3-7s] [core action]
[7-10s] [payoff and final hold]
Audio: [foley, ambience, music, silence]
Exact dialogue in Spanish, spoken once: "[diálogo literal]"
Preserve: [identity, object, layout, audio]
Do not include: [short concrete list]
```

## Más información

- [Ejemplos oficiales y de la comunidad](docs/community-examples.md)
- [Guía multilingüe](docs/multilingual-guide.md)
- [Diseño de prompts](docs/prompting-guide.md)
- [Referencias y permisos](docs/reference-videos.md)

<a id="brand-tools"></a>

## Empieza con SeaImagine

![Prompts de vídeo Gemini Omni para SeaImagine](assets/seaimagine-omni-hero.png)

Esta biblioteca conserva las 60 recetas originales de Flaq AI y añade tres ejercicios de SeaImagine con imágenes propias. Aquí encontrarás los nuevos ejercicios, ejemplos del repositorio original y lecciones de casos oficiales y de la comunidad.

[Gemini Omni](https://seaimagine.com/es/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/es/model/gemini-omni-1-1-flash/)

1. Abre la página del modelo y comprueba el acceso, el precio y los ajustes disponibles.
2. Para conservar un producto o personaje, elige imagen a vídeo, sube una imagen y pega su prompt. Para una escena nueva, prueba texto a vídeo.
3. Elige duración y formato en la interfaz. Prueba un plano; revisa apariencia, movimiento y sonido, y cambia una sola instrucción cada vez.

Son diseños de prompts, no resultados verificados en SeaImagine. Duración, audio, edición, extensión y referencias dependen del modelo y de la interfaz actual. Las funciones de la API de Google no implican que SeaImagine las ofrezca.

<a id="sea-practice"></a>

## Tres ejercicios de SeaImagine con imágenes originales

Estas imágenes de referencia se generaron con IA para practicar con el primer fotograma. No son resultados de vídeo probados con Gemini. Usa solo las funciones que aparezcan en SeaImagine.

### SEA-01 · Una mañana con una taza de cerámica verde azulada

[![Una mañana con una taza de cerámica verde azulada](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

Acerca la cámara despacio sin alterar el asa, el borde ni el nivel del líquido. Deja espacio para un texto final.

Sube la imagen de la taza para animarla. Prueba solo un acercamiento lento y revisa el asa y el líquido antes de añadir el texto.

[Imagen a vídeo](https://seaimagine.com/es/image-to-video/) · [Generador de imágenes con IA](https://seaimagine.com/es/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · Luces en un puerto de papel

[![Luces en un puerto de papel](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

En una sola toma, enciende el faro y aumenta por turnos la luz de las ventanas de las tres casas. Conserva la textura del papel y la geometría.

Sube la imagen del puerto y pide encender el faro e intensificar las luces de las ventanas en secuencia. Compara la forma de los edificios al principio y al final.

[Imagen a vídeo](https://seaimagine.com/es/image-to-video/) · [Generador de imágenes con IA](https://seaimagine.com/es/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · Una bolsa de lino para una tienda multilingüe

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="Una bolsa de lino para una tienda multilingüe" width="360"></a>

Crea un vídeo vertical limpio, sin letras, y añade los subtítulos en cada idioma con un editor de vídeo convencional.

Anima la imagen de la bolsa en formato vertical y añade después los subtítulos traducidos. Usa una instrucción breve de edición de vídeo solo si esa función está disponible.

[Imagen a vídeo](https://seaimagine.com/es/image-to-video/) · [Generador de imágenes con IA](https://seaimagine.com/es/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> Un día a día más sencillo

[Flujo de trabajo en SeaImagine](docs/seaimagine-workflow.md)

## Otras herramientas de SeaImagine

Usa estas páginas como otros puntos de partida. Consulta en cada una los modelos, condiciones y precios actuales. Este repositorio no garantiza disponibilidad continua.

- [Crear](https://seaimagine.com/es/create/)
- [Imagen a vídeo](https://seaimagine.com/es/image-to-video/)
- [Texto a vídeo](https://seaimagine.com/es/text-to-video/)
- [Generador de imágenes con IA](https://seaimagine.com/es/ai-image-generator/)

## Fuente y licencia

Adaptado del repositorio de Flaq AI, con sus colecciones y tres imágenes de referencia. No todo el contenido es original de SeaImagine. Es una guía independiente, no un producto oficial de Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
