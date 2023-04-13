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
