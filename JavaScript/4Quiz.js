const form = document.querySelector(".numForm"),
  paintChose = document.querySelector(".paintChose"),
  paintResult = document.querySelector(".paintResult");

function result(myNum, randNum) {
  paintChose.innerText = `You chose: ${myNum}, the machine chose ${randNum}`;
  myNum = parseInt(myNum);
  if (myNum === randNum) {
    paintResult.innerText = `You won!`;
  } else if (myNum > randNum || myNum < 0) {
    paintResult.innerText = `This is wrong number.`;
  } else {
    paintResult.innerText = `You lose!`;
  }
}
