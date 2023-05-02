# JavaScript

- Nomad Coders(노마드코더) : 바닐라 JS로 크롬 앱 만들기 (23.04.10 ~ 23.04.24)


* variable : 변수 공백x

* const(constant) 변하지 않는 값
    const a = 5;

* 띄어쓰기 원하면 다음 단어 앞에 대문자 ex) const amIFat
* let vs const 
    const는 상수라는 것이고 값이 바뀔수 없다, let은 새로운 것을 생성할 때 사용하는 것
* undefined은 variable에 대해서 인지하고 있지만, 값이 없는것
* null은 값이 없는것

* push
```JavaScript
daysOfWeek.push() : 항목 하나를 array 안에 추가 
```
* array

``` JavaScript
const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"];

console.log(daysOfWeek[4]);

daysOfWeek.push("sun");

console.log(daysOfWeek);
```

* object
    * argument는 function을 실행하는 동안 어떤 정보를 function에게 보낼 수 있는 방법

``` JavaScript
const player = {
    name: "nico",
    points: 10,
    fat: true,

};
console.log(player);
player.points = player.points + 15;
console.log(player.points);
```
* function

(1)

``` JavaScript
function sayHello(nameOfPerson, age){
    console.log("Hello my name is " + nameOfPerson + " and I'm " + age);
}

sayHello("nico", 10);
sayHello("dal", 23);
sayHello("lynn", 21);

function plus(a, b){
    console.log(a + b);
}

function divide(a, b){
    console.log(a / b);
}
plus(8, 60);
divide(98, 20);
```

(2)

``` JavaScript
const player = {
    name: "nico",
    sayhello: function (otherPersonsName) {
        console.log("hello " + otherPersonsName + " nice to meet you");
    },
};

console.log(player.name);
player.sayhello("lynn");
player.sayhello("nico");
```

* 1번 퀴즈
[계산기 만들기](1Quiz.js/)

* return

```JavaScript
const age = 96;
function calculateKrAge(ageOfForeigner){
    return ageOfForeigner + 2; 
}

const krAge = calculateKrAge(age);

console.log(krAge);
```

* condition
    * prompt(message?) : 사용자에게 message를 보여주고 값을 넣으라고 말한다.
    * parseInt() : string을 number로 변환한다.
    * typeof : 변수의 타입을 출력한다. 
    * isNaN(number: number) : 변수가 NaN인지 아닌지 알려준다.(boolean - true, false)

```javascript
// 조건문(1)
const age = parseInt(prompt("How old are you?"));

console.log(typeof age, age);
```

```javascript
// 조건문(2)
const age = parseInt(prompt("How old are you?"));

if(isNaN(age)){
    console.log("Please write a number");
} else {
    console.log("Thank you for writing your age.");
}
```

```javascript
// 조건문(3)
const age = parseInt(prompt("How old are you?"));

if(isNaN(age) || age < 0) {
    console.log("Please write a real positive number");
} else if(age < 18){
    console.log("You are too young.");
} else if(age >= 18 && age <= 50) {
    console.log("You can drink");
} else if(age > 50 && age <= 80){
    console.log("You should exercise");
} else if(age > 80) {
    console.log("You can do whatever you want.");
}
```

```javascript
// 조건문(4)
const age = parseInt(prompt("How old are you?"));

if(isNaN(age) || age < 0) {
    console.log("Please write a real positive number");
} else if(age < 18){
    console.log("You are too young.");
} else if(age >= 18 && age <= 50) {
    console.log("You can drink");
} else if(age > 50 && age <= 80){
    console.log("You should exercise");
} else if(age === 100) { //age === 100 : age가 100이라면? / age !== 100 : age가 100이 아니라면?
    console.log("wow you are wise");
} else if(age > 80) {
    console.log("You can do whatever you want.");
}
```

* HTML JavaScript
    * JavaScript는 HTML에 이미 연결되어 있다.
    * document (object) 는 모든 것들의 시작점
    
```javascript
const title = document.getElementById("title") //HTML에서 id를 통해 element를 찾아준다.

title.innerText = "Got you!" // innerText 변경

console.log(title.id); // title.id 출력
console.log(title.className); // title.className 출력

document.title // JavaScirpt에서 title을 읽을 수 있다.
document.body // JavaScript에서 HTML 항목을 읽을 수 있다.
```

```javascript
const title = document.querySelectorAll(".hello hi");
const title = document.getElementById("hello");

console.log(title);
```

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
    title.style.color = "blue";
}

title.addEventListener("Click", handleTitleClick);
```

```javascript
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
    h1.style.color = "blue";
}

function handleMouseEnter() {
    h1.innerText = "Mouse is here!";
}

function handleMouseLeave() {
    h1.innerText = "Mouse is gone!";
}

function handleWindowResize() {
    document.body.style.backgroundColor = "red";
}

function handleWindowCopy() {
    alert("copier");
}

function handleWindowOffline() {
    alert("SOS NO WIFI");
}

function handleWindowOnline() {
    alert("ALL GOOOD");
}

h1.addEventListener("click", handleTitleClick);
h1.addEventListener("mouseenter", handleMouseEnter);
h1.addEventListener("mouseleave", handleMouseLeave);

window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline);
```

* 2번 퀴즈
[애플리케이션 만들기](2Quiz.js/)

```javascript
const h1 = document.querySelector("div.hello:first-child h1");

function handleTitleClick() {
    const currentColor = h1.style.color;
    let newColor;   
    if(currentColor === "blue") {
        newColor = "tomato";
    } else {
        newColor = "blue";
    }
    h1.style.color = newColor;
}

function handleMouseEnter() {
    h1.innerText = "Mouse is here!";
}

h1.addEventListener("click", handleTitleClick);
```

* 3번 퀴즈
[if..else](3Quiz.js/)

* 4번 퀴즈
[JS Casino](4Quiz.js)

```javascript
const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");

function onLoginBtnClick() {
    console.log(loginInput.value);
}

loginButton.addEventListener("click", onLoginBtnClick);
```

* Form Submission

```javascript
const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");

function onLoginBtnClick() {
    const username = loginInput.value;
    console.log(username);
}

loginButton.addEventListener("click", onLoginBtnClick);
```

* Events

```javascript
(1)
const loginInput = document.querySelector("#login-form input");
const loginForm = document.querySelector("#login-form");

function onLoginSubmit(event) {
    event.preventDefault();
    console.log(loginInput.value);
}

loginForm.addEventListener("submit", onLoginSubmit);

(2)

const link = document.querySelector("a");

function onLoginSubmit(event) {
    event.preventDefault();
    console.log(loginInput.value);
}

function handleLinkclick(event) {
    event.preventDefault();
    console.log(event);
    alert("clicked!");
}

loginForm.addEventListener("submit", onLoginSubmit);
link.addEventListener("click", handleLinkclick)
```

* 5번 퀴즈
[Clock](5Quiz.js)

* 6번 퀴즈
[Click](6Quiz.js)

* 프로젝트 
[Project](https://koo1996.github.io/)