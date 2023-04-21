const h2 = document.querySelector("h2");

function handleTitleResize() {
  const length = window.innerWidth;
  if (length < 700) {
    h2.body.style.backgroundColor = "blue";
  } else if (length > 700 && length < 1100) {
    h2.body.style.backgroundColor = "purple";
  } else if (length > 1100) {
    h2.body.style.backgroundColor = "yellow";
  }
}
window.addEventListener("resize", handleTitleResize);