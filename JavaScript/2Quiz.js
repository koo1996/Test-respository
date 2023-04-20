const superEventHandler = document.querySelector("h2");

function handleTitleClick() {
  superEventHandler.style.color = "blue";
}

function handleMouseEnter() {
  superEventHandler.innerText = "Mouse is here!";
  superEventHandler.style.color = "green";
}

function handleMouseLeave() {
  superEventHandler.innerText = "Mouse is gone!";
  superEventHandler.style.color = "blue";
}

function handleWindowResize() {
  superEventHandler.innerText = "You just resized!";
  superEventHandler.style.color = "purple";
}

function handleWindowContextmenu() {
  superEventHandler.innerText = "That was a rigth click!";
  superEventHandler.style.color = "red";
}

superEventHandler.addEventListener("click", handleTitleClick);
superEventHandler.addEventListener("mouseenter", handleMouseEnter);
superEventHandler.addEventListener("mouseleave", handleMouseLeave);
window.addEventListener("resize", handleWindowResize);
window.addEventListener("contextmenu", handleWindowContextmenu);