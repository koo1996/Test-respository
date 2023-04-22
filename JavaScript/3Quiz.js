const body = document.body;

import "./styles.css";

const BIG_SCREEN = "bigScreen";
const MEDIUM_SCREEN = "mediumScreen";
const SMALL_SCREEN = "smallScreen";

function handleResize() {
  const length = window.innerWidth;
  if (length < 700) {
    body.classList.add(BIG_SCREEN);
    body.classList.remove(MEDIUM_SCREEN);
  } else if (length > 700 && length < 1100) {
    body.classList.add(MEDIUM_SCREEN);
    body.classList.remove(BIG_SCREEN, SMALL_SCREEN);
  } else {
    body.classList.remove(MEDIUM_SCREEN);
    body.classList.add(SMALL_SCREEN);
  }
}

window.addEventListener("resize", handleResize);

```css
h2 {
  color: white;
}

.bigScreen {
  background-color: #f1c40f;
}

.mediumScreen {
  background-color: #9b59b6;
}

.smallScreen {
  background-color: #3498db;
}
```
