const btn = document.querySelector("button");

function handleClick() {
  const a = colors[Math.floor(Math.random() * colors.length)];
  const b = colors[Math.floor(Math.random() * colors.length)];
  if (a === b) {
    return handleClick();
  }
  document.body.style.background = `linear-gradient(to left, ${a}, ${b})`;
}

btn.addEventListener("click", handleClick);