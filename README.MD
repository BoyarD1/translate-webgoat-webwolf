### 🇷🇺 Русский (Russian)  🇪🇸 Español (Spanish)  🇬🇧 English (English)

Привет!

Этот проект начат по двум причинам:
1. Для автоматизации добавления различных языков в проект Webgoat.  
2. Для добавления обучающих уроков, что может быть полезно для специалистов в области информационной безопасности, разработки программного обеспечения и devops.


Этот образ Docker основан на оригинальном образе WebGoat и предлагает полную русификацию всех уроков, а также их перевод на испанский язык с поддержкой выбора новых языков в языковом меню. 

Возможности:

* Все уроки WebGoat переведены на русский язык.
* Добавлен перевод всех уроков на испанский язык.
* Идеально подходит для изучения вопросов безопасности веб-приложений на русском или испанском языках.

Запуск:

1. Скачайте образ: `docker pull <ваше_имя_пользователя_dockerhub>/webgoat:1.0-ru-es`
2. Запустите контейнер: `docker run -p 8080:8080 boyarvaryag1/webgoat:1.0-ru-es`
3. Откройте в браузере: `http://localhost:8080`

---

### 🇪🇸 Español (Spanish)

Esta imagen de Docker se basa en la imagen original de WebGoat y ofrece una traducción completa al español de todas las lecciones, así como su traducción al ruso.

Características:

* Todas las lecciones de WebGoat están traducidas al español.
* Se ha añadido la traducción de todas las lecciones al ruso.
* Ideal para aprender sobre seguridad de aplicaciones web en español o ruso.

Puesta en marcha:

1. Descarga la imagen: `docker pull boyarvaryag1/webgoat:1.0-ru-es`
2. Inicia el contenedor: `docker run -p 8080:8080 <ваше_имя_пользователя_dockerhub>/webgoat:1.0-ru-es`
3. Abre en tu navegador: `http://localhost:8080`

---

### 🇬🇧 English (English)

This Docker image is based on the original WebGoat image and provides a full Russian translation of all lessons, as well as their translation into Spanish.

Features:

* All WebGoat lessons are translated into Russian.
* Translation of all lessons into Spanish has been added.
* Perfect for learning about web application security in Russian or Spanish.

Launch:

1. Download the image: `docker pull boyarvaryag1/webgoat:1.0-ru-es`
2. Run the container: `docker run -p 8080:8080 <ваше_имя_пользователя_dockerhub>/webgoat:1.0-ru-es`
3. Open in browser: `http://localhost:8080`

Note: Replace `<ваше_имя_пользователя_dockerhub>` with your actual Docker Hub username.
