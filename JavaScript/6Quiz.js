const btn = document.querySelector("button");

function randomGradient() {
  const nowColor1 = colors[Math.floor(Math.random() * colors.length)];
  const nowColor2 = colors[Math.floor(Math.random() * colors.length)];
  document.body.style.background = `linear-gradient(to right, ${nowColor1},${nowColor2})`;
}
btn.addEventListener("click", randomGradient);