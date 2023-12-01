# Java
- 코딩은 처음이라 with 자바
1. 자바 입문
2. 자바 언어 기본
3. 제어문
4. 함수와 string 클래스
5. 객체지향 입문
6. 객체지향 핵심
7. 표준 API 활용
8. 자료구조
9. 입출력과 예외처리
10. 공공 API활용 프로젝트

[자바정리](https://www.notion.so/351d92ae68b4437bb2c01e77d939e4b9)

## day4 - 1차원 배열
```java
//로또
package day4;

public class LottoMachine1 {

	public static void main(String[] args) {
		int[] ary = new int[6];
		
		for (int i=0; i < ary.length; i++) {
			ary[i] = (int)(Math.random()*45) + 1;			
			for (int j=0; j < i; j++) {
				if(ary[i] == ary[j]) {
					i--;
					break;
				}
			}
		}
		System.out.print("오늘의 로또 번호 - ");
		for (int i=0; i < ary.length; i++)			
			if (i < ary.length-1)
				System.out.print(ary[i]+",");
			else
				System.out.print(ary[i]);

	}

}
```
## day5 - 2차원 배열
## day6 - 메서드
```java
package day6_p;

public class MethodLab7 {

	public static void main(String[] args) {
		printArray(powerArray(2));

	}
	static int[] powerArray(int a) {
		int[] num = new int[10];
		for (int i = 1; i < 11; i++) {
			num[i-1] = i * a;					
		}
		return num;	
	}
		
	static void printArray(int[] num) {
		for (int i = 0; i < num.length; i++) {
			System.out.print(num[i]);
			if (i != num.length-1) {
				System.out.print(",");
			}				
		}
	}
}
```

## day7 - 클래스
```java
package day7_p;

class Product {
	String name;
	int balance;
	int price;
	
	Product() {
		this("듀크인형", 5, 10000);
	}
	
	Product(String name, int balance, int price){
		this.name = name;
		this.balance = balance;
		this.price = price;
	}
	
	String getName() {
		return name;
	}
	
	int getBalance() {
		return balance;
	}
	
	int getPrice() {
		return price;
	}
} 

public class ProdcutTest {

	public static void main(String[] args) {
		
		Product ary[] = new Product[5];
		ary[0] = new Product("a", 5, 100);
		ary[1] = new Product("b", 4, 300);
		ary[2] = new Product();
		ary[3] = new Product("c", 3, 500);
		ary[4] = new Product("d", 2, 700);
		
		for (Product p : ary) 
			System.out.printf("%s\t%d\t%d\n",p.getName(),p.getBalance(),p.getPrice());
	}

}

```
## day8 - 상속
상속 구문
	자바에서 생성되는 클래스는 반드시 부모 클래스를 한 개 갖게 된다. 
	부모 클래스 정의를 생략한 경우 자동으로 java.lang.Object 클래스를 상속하게 된다.
- java.lang.Object 클래스는 자바에서 정해놓은 최상위 클래스이다.
- 반드시 한 개의 클래스만 상속 가능하다.(단일 상속)
- 상속을 통해서 조상이 가지고 있는 대부분의 멤버들을 물려받게 된다.
    (생성자와 private 멤버는 제외)
- 클래스를 객체 생성할 때 생성자를 호출한 클래스만 객체 생성하는 것이 아니고 조상 클래스들의 객체도 생성된다.
- String toString() : 객체에 대한 정보를 하나의 문자열로 리턴 
- 자바의 접근 제어자 : pulic, protected, 생략(default), private
- 자바의 활용 제어자 : static, final, abstract
- 클래스 : public, 생략
- 멤버변수, 메서드, 생성자 : public, protected, 생략(default), private
- static : 멤버변수, 메서드
- final : 클래스, 멤버변수, 메서드, 지역변수
- abstract : 클래스, 메서드

## day9 - 다형성
* 다형성 : 조상 타입의 변수로 자손 타입의 객체들을 담아서 사용할 수 있는 기능
조상 타입으로 자손 타입을 참조할 수 있다.

어떠한 클래스 타입의 변수냐에 따라 접근할 수 있는 멤버의 사양이 정해진다.

* Auto Boxing / Auto UnBoxing (Jave 5)
객체가 와야할 자리에 기본형 데이터가 지정될 때 컴파일시 객체로 변환해 주는 기능

## day10 - 예외처리
[자바의 예외처리]
- 컴파일 오류
- 실행 오류
    - 에러(Error) : JVM 영역에서 발생하는 실행 오류, 심각한 상황, JVM이 에러메시지를 출력하고 수행을 중지시킨다.
    - 예외(Exception) : 자바프로그램 영역에서 발생하는 실행 오류, 다소 가벼운 상황, 예외 처리 구문으로 대처하는 코드를 구현해서 적용할 수 있다.
    왜? 프로그램의 비정상적인 종료를 최소화 하기 위해서,
    런타임예외 : 예외처리 구현이 선택(JVM이 정해진 코드로 대신 처리한다.)
    not 런타임예외(일반예외) : 발생될 수 있는 예외의 처리코드 구현이 필수

* throw : 예외 발생 --> throw new 예외클래스명()
    예외 처리
    (1) try ~ catch ~ finally -> 적극적인 예외처리
    (2) throws -> 소극적인 예외처리(발생된 예외의 처리를 이 메서드를 호출한 메서드에 넘긴다)
    interger.parselnt() : "123" -> 123
* 예외 발생 : 예외를 발생시키는 기능을 가지고 있는 메서드의 경우 메서드 헤더에 throws 절을 지정해서 이 메서드 호출시 예외가 발생할 수도 있음을 알린다.
    
* 커스텀 예외클래스 : 개발자가 필요에 의해 직접 생성하는 예외클래스
    java.lang.Exception 클래스를 상속해야 한다.
    java.lang.RuntimeException 도 가능

## day11 - 자바의 API
    java.xxx - 기본(core)
    javax.xxx - 확장(extends)
    org.xxx - 
    
    java.lang, java.util, java.io, java.net, java.sql

    String --> 객체생성시 초기화되는 문자열 내용을 변경할 수 없다.
    StringBuffer(StringBuilder) --> 문자열을 저장할 버퍼를 만들고 이 버퍼안에 문자열 추가,삽입, 삭제 등 편집 위주

    "abc" + v1 + "def" + v2 + "!!" --> Java 5 - 최적화 컴파일

## day12 
    LinkedHashSet


## day13
    [자바 입출력(I/O) API의 특징]
    - OS에 의존적인 처리 과정을 거친다. -> 플랫폼에 무관한 프로그램 언어다.
    -----------------------------------> 스트림(Stream)이라는 논리적인 장치를 이용하여 I/O
                                                            --------------객체
    - 스트림 객체를 이용해서 입출력 작업을 처리한다.
    --> 단방향 처리만 가능
        입력스트림, 출력스트림 ---> API가 입력용과 출력으로 나눠진다.
    --> 입출력 단위에 따라 바이트스트림과 문자스트림으로 나눠진다.
    이진파일 : 바이트스트림 - InputStream, OutputStream
    텍스트파일 : 문자스트림 - Reader, Writer
    InputStreamReader, OutputStreamWriter --> 바이트스트림 객체를 문자스트림 객체로 변환
    파일이름에 File로 시작하는 클래스들을 파일을 오픈하는 기능을 지원한다.

    "c:/Temp/test.txt" ---> 절대패스
    "c:\\Temp\\test.txt"
    "../../../Temp/test.txt" ---> 상대패스

    [try ~ catch with resource]

    try 예약어와 오픈 중괄호 사이에 (객체생성코드)를 지정하면 생성된 객체는 try ~ catch 구문이 종료될 때 자동으로 close 된다.

    (객체생성코드) ---> close를 필요로 하는 객체의 생성식
                ----------- closable 이라는 인터페이스를 추가 상속하는 클래스의 객체
    
    ANSI == KSC5601 == EUC-KR == CP949

    UTF-8

## day14

JDBC --> Java DataBase Connectivity
         Java + SQL
        --> Mybatis
        --> JPA

Servlet & JSP --> Java Web Server Programming
                
                Spring & JSP
                        Spring & Tjym;eaf
직렬화 가능한 객체 구현
1. Serializable 또는 EXternalizable 인터페이스를 상속을 해야 한다.
2. 조상이 Serializable을 상속하고 있으면 자손에도 그대로 적용된다.
3. 자손은 Serializable을 상속하고 있지만 조상은 Serializable을 상속하고 있지 않으면 자손에서만 직렬화가 일어난다.
4. non-static, non-transient 멤버 변수들만 직렬화 대상이 된다.
5. 직렬화의 대상이 되는 멤버 변수가 참조형일 때는 참조하는 객체도 직렬화 가능한 객체여야 한다. 그렇지 않으면 실행 시 NotSerializableException이 발생된다.

java.net 패키지 -> 네트워크 프로그래밍 관련 API 들이 모여 있다.
                TCP 소켓프로그래밍, UDP 소켓프로그래밍
                웹 서버에 접속하여 컨텐츠를 요청하고 읽어오는 프로그래밍 ---> URL 클래스
URL --> Uniform Resource Locator
        어떠한 자원의 위치를 알리는 단일화된 형식의 문자열
        HTTP URL --> HTTP 프로토콜 기반으로 서비스하는 서버 자원의 주소 문자열

                http://서버도메인(서버IP주소)[:포트번호]/패스/파일  
                                                      ---------- URI

http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1171062000
                                        -----------------쿼리 문자열
"http://openapi.seoul.go.kr:8088/796143536a756e69313134667752417a/xml/LampScpgmtb/1/100/"

## day15

csv
json0

xml
    객체생성식{
        클래스의 바디
    }
    
    class 클래스명 extends 부모클래스명 implements 부모인터페이스명 {
        클래스의 바디

    }

javac
java
javap
jar

CGI(Common Gateway Interface)
    모든 웹서버(HTTP 서버)가 지원하는 웹 표준 기술
    구현 언어에 의존적이지 않다.
    멀티 프로세스로 웹 클라이언트 요청을 다중 처리한다.

---> Servlet
    Java 프로그래밍 기술
    멀티 스레드로 웹 클라이언트 요청을 다중 처리한다.

(1) 추가스레드로 수행할 기능은 무엇인가?
(2) 추가스레드를 몇개까지 기동시킬 건가?

    --> 기동시키려는 스레드의 기능에 따라 스레드 클래스를 생성한다.

        - java.lang.Thread를 상속하고 run() 메서드를 오버라이딩하여 스레드 기능 구현
        - java.lang.Runable을 추가 상속하고 run() 메서드를 오버라이딩하여 스레드 기능 구현

    --> MyThread1 my = new MyThread();
        my.start();

        MyThread2 my = new MyThread2();
        Thread t = new Thread(my2);
        t.start()

## day16
    daemon thread --> 다른 스래드들의 기능을 서포트하는 역할 
                    모든 스레드가 종료되면 자동으로 종료되는 스레드
                    무한루프 
                    스레드를 객체 생성한 후, start()를 호출하기 전에 setDaemon() 이라는 메서드로 데몬 스레드로 만든다.
    daemon process(서비스) --> 백그라운드에서 수행되는 프로세스로서 다른 프로세스들의 실행을 서포트하는 역할

    Vector --> ArrayList --> Collections.synchronizedList(...)
    old         new

    StringBuffer StringBuilder

    함수형프로그래밍 ---> 아규먼트로 함수를 전달하여 좀더 적용성 있는 프로그램을 개발할 수 있다. (파이썬,자바스크립트,R) ...
    함수형 인터페이스, 람다식, 스트림(데이터열)

    DB - mySQL

    CRUD : Create Read Update Delete
           삽입   읽기  수정   삭제
           INSERT SELECT UPDATE DELETE ---> DML
           -------------------------------게시판, 공지사항, 방명록
``` MySQL
    select 컬러명
    form 테이브명;

    select 컬러명리스트
    from 테이블명
    where 꺼내고싶은행에대조건식;

    select *
    from 테이블명
    order by 정렬기준컬럼1 asc, 정렬기준컬럼2 asc;

    select *
    from 테이블명
    order by 정렬기준컬럼1 desc, 정렬기준컬럼2 desc;

    select 컬럼명리스트
    from 테이블명
    where 꺼내고 싶은 조건식;
    order by 정렬기준컬럼 desc;

    where month = 1 or month = 5 or month = 4 or month = 10
    where month not in(1,5,4,10)
    where month not in(1,5,4,10)

    select * from emp where ename like 'A%'; 


    where ename like 'A%'
    where ename like '%A%';  : A시작, A포함하는, A끝 
    where ename like 'A__'
    where ename like '_A_'
    select ename,sal from emp;
    
    select ename 직원이름, sal * 12 as 연봉 from emp; /* as는 생략 가능
    as는 새로운 컬럼명 지정 */
    
    select ename "직원 이름", sal * 12 as 연봉 from emp;
    -- 컬럼에 공백을 넣고 싶으면 ""

    select ename, sal from emp order by sal;
    -- ASC(오름차순)는 디폴트 값이므로 생략 가능 
 
    select ename, sal from emp order by sal desc;

    select ename, sal, hiredate from emp where sal >= 2500 order by sal desc, ename desc;
    -- order by는 첫번째 기준이 똑같으면 두번째 기준

    select all job from emp;
    -- all는 생략가능
    
    select distinct job from emp;
    -- distinct는 중복값 제거

    select distinct job, deptno from emp;
    -- job, deptno 둘 다 동일하면 제거

    select * from emp order by sal desc limit 3;
    -- sal 내림차순 -> 3개만 출력
```
## day17

MySQL 내장 함수
숫자 관련 함수

dummy table = dual 특정 데이터에서 함수를 꺼내는 것

## day18

* SET Operator
    * UNION - 합집합
    * UNION ALL - 합집합(중복 결과 모두 표현)
    * INTERSECT - 교집합
    * MINUS - 차집합
* ROLLUP - 총합 또는 중간 합계가 필요할 경우 사용
* JOIN
    * INNER - 조건 일치하는 행들만 저장
    * OUTER - 조건 일치하지 않는 행들도 저장
    * CROSS - ex. 4행 * 3행 = 총 12행 결과값 

## day19

## day20 

executeQuery() --> SELECT -----> ResultSet, 비어있는 ResultSet 객체
executeUpdate() --> SELECT외의 SQL명령들 --> int(변경된 행의 갯수)

Java Application -> JVM에 의해 단독으로 수행되는 프로그램
Java Android App -> 안드로이드 운영체제에서 실행되는 심플한 프로그램
Java Servlet -> 웹 서버에서 수행되는 자바 프로그램(MVC)

MVC(Model View Controller)

프로그램을 개발할 때 역할을 나눠서 개발하는 패턴
Model --> Domain Model & Service Model(xxxDTO, xxxVO & Servie Model(xxxDAO))
View --> 사용자(user)와의 인터페이스(입출력) --> JSP, Thymeleaf, Vue.js
Controller --> Model 과 View 사이에서 여러 다양한 역할을 담당하는 객체(비지니스로직) --> Servlet

## day21

* 자바 기반의 웹프로그래밍

- Servlet, JSP --> 웹서버에서 실행

웹클라이언트(브라우저) --------> 웹서버
                     요청(http) / 백엔드 개발자
                    <--------- 
                     응답(http)
                     HTML, CSS, JavaScript --> 웹클라이언트 기술 / 프론트엔드 개발자
                    
AJAX
HTML
<hr> <hr/> : 분리선 

- 컨텐트의 존재 여부
double side tag  <시작태그명>xxxxxxxx</종료태그명>
single side tag(empty tag)  <태그명>, <태그명/>

- 랜더링 방식
블럭스타일 태그     랜더링될때 그 행 끝까지 이 태그의 공간(println)
인라인스타일 태그   랜더링될때 출력되는 컨텐트 만큼만 이 태그의 공간(print) img,a

```html
<br> : \n 
<img src="http://localhost:8088/edu/images/olaf.jpg"> : 절대 url
<a> : 하이퍼링크 텍스트
<ol></ol> : 순서가 있는 리스트
<ul></ul> : 순서가 없는 리스트
&nbsp; : 띄어쓰기, &lt; &gt; &amp;

<fieldset></fieldset> : 박스로 테두리 표시
```

## day22

```html
<style>
    CSS선택자 {
        속성명:속성값;
        속성명:속성값;
        속성명:속성값;
        color:green;
        font-weight:bold;
        background-color:yellow;
    }
</style>

1) 태그선택자 : 태그명 / 태그명, 태그명, 태그명
2) id 선택자 : 태그에 정의된 id 속성의 값(id 속성 : HTML 문서 내에서 값이 유일해야 한다.)
        #id속성값
3) class 선택자 : 태그에 정의된 class 속성의 값(class 속성 : HTML 문서 내에서 값을 중복정의 가능하다.)
        .class속성값
4) 전체 선택자 : 모든 태그
        *
5) 자식 선택자 : 부모태그명 > 자식태그명
            p > h1
            p > h1 > span

       
            
            <>21
margin : 20px : 상하좌우 전부 20px
margin : 10px 20px 30px 40px : 상 우 하 좌
margin : 10px 20px : 상하 10px 좌우 20px
margin : 10px 20px 30px : 상하 10 좌 20 우 30


h2:(shadow class)nth-of-type(?) : ?번째 h2 태그에 적용

a:hover {

}
a영역에 마우스를 올리면~


clear : both
<link rel="stylesheet"  href="mystyle.css"> : css 따라 작성
```
## day23

* document, window --> 내장객체, 객체 상태로 제공되는 API - BOM(Browser Oject Model) location, screen, history, navigator

* Math --> 생성자함수, 모든 멤버가 정적(static)
* Array, Date --> 생성자 함수, 객체 생성해서 사용
                new Array(), new Date()
[ &&, ||]

식1 && 식2
||

조건식 && 일반식

[let 으로 변수를 선언하면 얻게되는 장점]

(1) 동일한 명칭으로 변수를 두 번 이상 선언할 수 없다.
(2) 블록스코프를 지원한다.

- 변수의 스코프
    * 전역변수 스코프 - 함수 밖에 선언이후 모든 <script> 태그영역에서 사용 가능(var, let)
    * 지역변수 스코프 - 함수 안에 선언되는 변수로서 함수 수행이 종료되면 메모리 영역이 해제
    * 블록변수 스코프 - 특정 블록(if, for, while)에 선언 변수로서 블록이 종료되면 메모리 영역이 해제(let)

## day24
## day25

* JavaScript의 객체 정의와 활용
     * 객체 리터럴을 사용하는 방법
     ```javascript
     {
        속성명:속성값, 속성명:속성값,...
     }
     ```

     * 생성자 함수를 사용하는 방법
    생성자 함수란 객체를 초기화하기 위해 사용되는 함수로서 관례적으로 생성자 함수의 명칭은 첫 글자를 대문자로 사용한다.
    ```javascript
    function 함수명([매개변수]){
        this.속성명=값;
        this.속성명=값;
    }

    new 함수명()

    ```
    * filter
    return 값은 boolean

    * BOM(Browser Object Model) : 브라우저에서 실행되는 자바스크립트를 위해 브라우저가 제공하는 객체 window, document, location, navigator, screen, history

    window : 전역객체(global), 브라우저 자신 
             다른 BOM 객체들은 window 객체의 속성으로 정의된다.
             전역객체로서 멤버 사용시 객체명을 생략할 수 있음
             전역 코드영역에서의 this 는 window 객체를 참조한다.
             alert(), prompt(), confirm(), setInterval() - clearInterval(), setTimeout() - clearTimeout(), open()
    document : 브라우저의 도큐먼트 영역과 관련된 기능을 제공하는 객체
               write(), writeln()
               getElEmentsByTagName(태그명)
               getElementById(id속성값)
               getElementByClassName(class속성값)
               querySelector(CSS선택자)
               querySelectorAll(CSS선택자)
    location : 랜더링된 웹 페이지의 주소 문자열(URL) 정보를 담고 있는 객체
             href, reload()
    웹 페이지에서 어떠한 액션(이벤트)이 발생했을 때 수행되는 코드를 작성하여 등록하는 방법
    - 인라인 이벤트 모델 : 지역적
    - 고전 이벤트 모델 : 전역적
    - 표준 이벤트 모델 : 전역적

    이벤트 타입 : 발생되는 이벤트의 종류(click, mouseover, load, keydown, keyup, change, submit)
    이벤트 타켓 : 이벤트가 발생한 대상 DOM 객체
    이벤트 핸들러(리스너) : 이벤트 처리 코드를 구현한 함수
    //인라인
        이벤트 핸들러 : abc()
    <태그명 onxxx = "abc(); ">
    
    //고전
    let dom = doucument.querySelector("#target);
    dom.onxxx = abc;
    dom.onxxx = null;
    
    //표준 
    let dom = doucument.querySelector("#target);
    dom.addEventListener("xxx",abc);
    dom.removeEventListener("xxx",abc);

## day26 
JavaScript storage.exam5 - 

innerHTML
innerText 
live preview

## day27 
JSON

[Web Server Programming(Backend Programming)]

	1) Servlet
	2) JSP
	3) MVC 패텁(Servlet&LP
	4) Spring MVC - Framework

edu -------------> 이클립스 : 웹 프로젝트
                    톰캣(WAS) : 컨텍스트
                    개발자 : 웹 애플리케이션

MIME 타입 - 전달된 메시지(컨텐트)의 타입, major type/minor type
            text/html, text/xml, text/plain, text/json(application/json)
            image/gif, image/jpg, image/png

CGI(Common Gateway Interface)
- 구현언어가 정해져 있지 않다.
- HTTP 표준
- API가 거의 없다. -> 개발자의 코딩량이 많아진다.
- 여러 클라이언트 요청에 대해 다중 프로세스로 서비스하므로 동시 요청수가 많을 수록 엄청 비효율적이다. 

CGI ------------> Fast CGI -----------> Servlet (다중스레드)
                                        -------------------> JSP
                                        -------------------> MVC 패턴(모델 2)
                                                            요청 : Servlet
                                                            응답 : JSP
    ------------> ASP, PHP

웹 컨테이너(서블릿컨테이너, 서블릿엔진) - 카탈리나
--> 클라이언트로 부터 서블릿이 요청되면 
    (1) 요청된 서블릿 객체가 이미 생성되어 있는지?
        Y -> service() 호출 -> 요청 방식에 따라서 doGet() 또는 doPost() 호출
        N -> 서블릿 객체를 생성 -> init() 호출 -> service() 호출
        -> 요청 방식에 따라서 doGet() 또는 doPost() 호출

        서블릿 객체가 삭제(서버가 종료될 때, 자동 리로드될 때) -> destory()

## day28

* 요청 재지정
    * 요청재지정이란 클라이언트에서 요청한 페이지 대신 다른 페이지를 클라이언트가 보게 되는 기능으로서 redirect 방법과 forward 방법으로 나뉜다.
        * redirect : HttpServletResponse 의 sendRedirect() 메서드를 사용한다. 
        * forward : RequestDispatcher 의 forward() 메서드를 사용한다. 
        * RequestDispatcher
            * forward() : 요청 페이지 대신 다른 페이지가 대신 응답하게 한다. 
            * include() : 요청 페이지 안에 다른 페이지의 처리 내용이 포함되어 같이 응답하게 된다.

## day29
JSP(JavaServer Pages)

* 서블릿으로 구현할 수 있는 모든 기능을 JSP로도 구현 가능
* 서블릿에 비해 구현하기 쉽다는 평가
* HTML 태그, JSP 태그, JSP 내장객체, 약간의 자바 코드
* 수행되기 전에 Servlet 소스로 변경되어 수행되므로 서블릿의 수행상의 장점이 그대로 지원됨
        ----------> JSP Converter(JSP 엔진) : Jasper
* JSP 태그
* JSP 내장 객체
* EL, JSTL
        ```java
	<%           %> : 스크립트릿(수행문) 태그 
        <%!          %> : 선언문(변수선언, 메서드정의) 태그 <%=         %> : 표현식
        <%--        --%> : 주석문 태그
        <%@         %> : 지시자 태그


	client 실행 : java
	server 실행 : jsp
	trimDirectiveWhitespaces="true"%

	선언문 태그 빈행으로 실행

	<%@ page [ language="java" ]  
	[ extends="package.class" ]  
	[ import="{package.class | package.*}, ..." ]  
	[ session="true|false" ]  
	[ buffer="none|8kb|sizekb" ]  
	[ autoFlush="true|false" ]  
	[ isThreadSafe="true|false" ]  
	[ info="text" ]  
	[ errorPage="relativeURL" ]  
	[ contentType="mimeType [ ; charset=characterSet ]" |         
	"text/html ; charset=ISO-8859-1" ]  
	[ isErrorPage="true|false" ] 
	[ pageEncoding="characterSet | ISO-8859-1" ]  
	[ isELIgnored="true|false"] 
	```
## day30

* HTTPSession : 객체 공유 -> session 직접 추출하여 setattribute
* ServletContext : 서버 종료시 사라진다. 
* HttpSession 객체에 cart 라는 명칭으로 저장된 객체의 getApple() 을 호출하여 리턴된 결과를  표현하려면 다 음과 같이 구현한다. 
 ```java
 ${ sessionScope.cart.apple } 또는 ${ cart.apple } 
 ```
- EL 에서의 . 연산자   
     변수명.xxx 
 (1) 변수의 참조 대상이 일반 Java 객체이면  getXxx() 를 호출한 결과가 된다. 
 (2) 변수의 참조 대상이 Map 객체이면 get(“xxx”) 을 호출한 결과가 된다.

 ### mvc

 JSP(스크립팅방식)
 JSP+자바클래스(자바빈) --> 모델1
 Servlett+JSP+자바클래스(자바빈) --> 모델2(MVC)
 C         V        M

Web Server(HTTP Server) + Application Server
------------------------------------------
Web Application Server(WAS) --> Tomcat

JSTL - JSP 커스텀태그의 표준 
       코어라이브러리, 포매팅라이브러리, XML라이브러리, SQL라이브러리

### XML(Extensible Markup Language)

* 반드시 맨 앞에 명세, XML 문서 유형을 지정 
* XML 문서 구조를 정의한 DTD(또는 XML Schema) 선언, 스타일을 정의한 CSS 연결 에 대한 선언도 명세

### JSON
JavaScript Object Notation : 인터넷에서 자료를 주고 받을 때 그 자료를 표현하는 방법이다. 자료의 종류에 큰 제한은 없으며, 특히 컴퓨터 프로그램의 변수값을 표현하는 데 적합하다. 형식은 자바스크립트의 구문 형식을 따르지만, 프로그래밍 언어나 플랫폼에 독립적이므로 C, C++, C#, 자바, 자바스크립트, 펄, 파이썬 등 많은 언어에서 이용할 수 있다.

(1) XMLHttpRequest 객체
(2) fetch() 함수를 이용하는 방법
(3) axios 추가 라이브러리를 이용하는 방법

## day31

AJAX 
* XMLHttpRequest 객체 : 서버 측과의 비동기 통신을 제어하는 것은 XMLHttpRequest 객체의 역할이다. 
* XMLHttpRequest 객체를 이용함으로써 지금까지 브라우저가 실행해 온 서버와의 통신 부분을 JavaScript가 제어할 수 있게 된다. 
* XMLHttpRequest  객체 생성 :  new XMLHttpRequest()

* Same Origin Policy(SOP) : 브라우저에서 보안상의 이슈로동일 사이트의자원(Resource)만접근해야 한다는 제약이다

## day32

ServletJSP : Filter 

Filter : 웹 클라이언트에서 요청한 웹 자원들(Servlet 또는 JSP)이 수행되기 전 또는 후에 수행되는 객체로 서 request 또는 response에 영향을 주거나 또는 특정 처리를 할 수 있다. Filter의 응용 예로 인증, 로깅, 이미 지 변환, 데이터 압축, 암호화, 스트림 토큰화, XML 변환 등이 있다.

Filter 구현 시에는 javax.servlet.Filter 라는 인터페이스를 상속하여 init(), doFilter(), destroy() 를 오버라이딩 한다.

lambdastream

람다 스트림

## day33

스프링부트
springboot

"스프링 프레임워크"는 자바 기반의 애플리케이션 프레임워크로 엔터프라이즈급 애플리케이션을 개발하기 위한 다양한 기능을 제공한다.

spring ioc 제어역전(IoC)

* 의존성 주입(DI)
* DL


* 관점지향프로그래밍(AOP)

스프링 프레임워크의 모듈

* spring ioc

DI의 예

1. Construction Injection : 생성자를 통해서 객체 바인딩(의존관계를 연결)     
2. Setter Injection : setter 메서드를 이용해서 객체 바인딩(의존관계를 연결)     
3. method Injection : 어노테이션을 정의한 메서드를 이용해서 객체 바인딩(의존관계를 연결)     
4. field Injection : 어노테이션을 정의한 메서드를 이용해서 객체 바인딩(의존관계를 연결) 

[ ANNOTATION 설정 ] 

@Component 클래스에 선언하며 해당 클래스를 bean 객체로 등록한다. bean의 이름은 해당 클래스명(첫 글자는 소문자로 변경해서)이 사용된다. 범위는 디폴트로 singleton이며 @Scope를 사용하여 지정할 수 있다. 

@Scope 스프링은 기본적으로 빈의 범위를 "singleton" 으로 설정한다. "singleton" 이 아닌 다른 범위를 지 정하고 싶다면 @Scope 어노테이션을 이용하여 범위를 지정한다. 설정 : prototype, singleton, request, session, globalSession

## day34

스프링 mvc

컨트롤러 메서드의 리턴값
(1) String - 뷰이름 ---> templates/뷰이름.html
(2) ModelAndView - 뷰에게전달한데이터 + 뷰이름 ---> templates/뷰이름.html
(3) void - 뷰이름으로 매핑명을 사용 ---> 매핑명.html

Thymeleaf

## day35

queryForm - Query DTO

memberForm

@RequestParam() => required = true : 무조건 입력
defaultValue는 기본값 설정

[ Lombok이란 ]

- Java의 확장 라이브러리이다. 
- 반복해서 구현하게 되는 메소드를 Annotation을 사용해서 자동으로 작성해주는 
  라이브러리다.

- 주요 Annotation

@NonNull 
  null을 허용하지 않는 매개변수 정의

@Getter, @Setter
  getter, setter를 생성한다.

@ToString
  ToString 메소드를 생성한다.

@EqualsAndHashCode
  hashCode, equals를 구현한다.

@NoArgsConstructor
  매개변수가 없는 생성자 구현한다.

@RequiredArgsConstructor
  final, @NonNull이 있는 필드에 값을 초기화 하는 생성자를 구현한다.

@AllArgsConstructor
  모든 필드에 값을 초기화 하는 생성자를 구현한다.

@Data
  다음에 제시된 모든 Annotation 을 정의한 것과 동일한다.
  @ToString, 
  @EqualsAndHashCode
  @Getter on all fields,
  @Setter on all non-final fields,
  @RequiredArgsConstructor!

  DTO : 변경 가능 - getter setter  --> HttpServletRequest 보관
  VO : 변경? - getter만
```html
<li><span th:inline="none">[[...]] = </span>[[${data}]]</li>
th:text //controlloer -> 태그가 있으면 형식 그대로 출력
  
th:utext //태그 x 출력
<li><span th:inline="none">[(...)] = </span>[(${data})]</li>

<h3 th:text="'시청 불가'" th:if="${age lt 14}"></h3> //참이면 출력 (자식태그도 출력 x)
<h3 th:text="'시청 가능'" th:unless="${age lt 14}"></h3> //거짓이면 출력


<th:block th:if="${today == '금요일'}">
    <h2>즐거운 금요일</h2>
    <h3>행복한 금요일</h3>
</th:block></body>  //블럭으로 태그내용을 묶을 수 있다.

```

## day36

Thymeleaf

* SpringEL
    * Spring Expression Language라는 뜻의 SpringEL (SpEL)은 런타임 시 메서드 호출 및 기본 문자열 템플릿 등의 기능을 제공한다.
    * ${...} 표현식을 이용해 컨트롤러에서 전달받은 변수에 접근할 수 있으며 th:속성명 그리고 [[ ]] 안에서 사용 가능하다.
    * 표현식
        1) ${...} 표현식 – 변수 표현식
            * ${...} 표현식을 이용해 컨트롤러에서 전달받은 변수에 접근할 수 있으며 th:속성명 그리고 [[ ]] 안에서 사용 가능하다.
        2) @{...} 표현식 – URL 표현식
            * @{...} 표현식은 서버의 contextPath를 반영한 URI 로 변경된다. 
        3) 문자 합치기
            * 합치고 싶은 문자열을 "|" 으로 감싸거나 + 연산자를 이용해 문자를 합칠 수 있다.
        4) 비교 연산자 
            ```html
            <!-- 이항 연산자 -->    <div th:text="${info.name != 'kim'}"></div>    <div th:text="${info.age >= 30}"></div> 
            <!-- 삼항 연산자 -->     <div th:text="${info.name == 'kim' ? 'ok' : 'no'}"></div> 
            ```
        5) HTML 태그의 컨텐츠 설정 - th:text 
        6) HTML 태그의 value 속성의 값 설정 - th:value
        7) th:if, th:unless
            * if~else 구문과 비슷하다. 조건을 체크하여 참이면<th:if> 그리고 거짓이면<th:unless> 컨텐츠를 표현한다.
        8) th:switch, th:case
            * switch 구문과 비슷하다. th:case 속성에 지정된 값과 동일한 서브 태그를 표현한다.
        9) th:each
            * for 반복문과 비슷하다
        10) 링크될 대상 URL : th:href="@{}" 
        11) th:with="${}"
            * <div th:with=”userId=${number}” th:text=”${usesrId}”>
            * 변수형태의 값을 재정의하는 속성이다. th:with를 이용하여 새로운 변수 값을 생성할 수 있다.

## day37 

ModelAttribute - 같이 실행 requestscope 보관도 해준다.

@SessionAttributes({"count1", "count2"}) : 배열 형식으로 저장한다.

s.setcomplete(); : 전체 삭제
s.removeAttribute(who); : 부분 삭제

public String memberHandle(@ModelAttribute("kkk") StepVO vo) : 다른 이름으로 저장

@ResponseBody 어노테이션 적용 : @ResponseBody 어노테이션이 적용된 경우, 리턴 객체를 http응답으로 전송한다.
HttpMessageConverter를 이용해서 객체를 HTTP 응답스트림으로 변환한다.

## day38

[ HTTP ]

- 요청(client) - 응답(server)
- 요청 - GET : 요청헤더
        POST : 요청헤더+요청바디(application/x-www-urlencoded)
- 응답 - 응답헤더+ 응답바디

@ResponseBody : 뷰를 통하지 않고 컨트롤러가 직접 응답 바디 구성
@RequestBody : 요청바디를 다른 형식으로 받겠다.(JSON)

import org.slf4j.Logger; -

logger.error
logger.warn
logger.info
logger.debug
logger.trace

form 태그에 multipart/form-data 서버에 알리고 전달한다.
```
xxx(MultipartFile mfile)
xxx(MultipartFile 타입을 멤버변수로 정의한 VO클래스 vo)
xxx(MultipartFile[] 타입을 멤버변수로 정의한 VO클래스 vo) → 다중 파일일 때
xxx(MultipartRequest mreq)    → 다중 파일일 때 
```

MultipartFile 의 주요 메소드 
```
 String getName()    파라미터의 이름을 리턴한다.   
 String getOriginalFilename()   업로드 한 파일의 실제!! 이름을 리턴한다.  boolean isEmpty()     업로드 한 파일이 존재하지 않으면 true를 리턴한다.  
 long getSize()     업로드 한 파일의 크기를 리턴한다.  
 byte[] getBytes() throws IOException 업로드 한 파일의 데이터를 byte 배열로 리턴다.   
 InputStream getInputStream()  InputStrem 객체을 리턴한다.  
 void transferTo(File dest)    업로드 한 파일 데이터를 지정한 파일에 저장한다.
 ```

upload 



 <input type="file" name="uploadFiles" multiple/> : 여러 파일

Mybatis

## day39


```java
@Update("update meeting set name = #{name}, title = #{title}, meetingdate =    date_format(#{meetingDate}, '%Y/%m/%d %H:%i')  where id = #{id}")  public boolean updateM(MeetingDTO vo) //id 히든 타입
```

import org.w3c.dom.Document;

#{ ... } where ename = #{ name } :  값으로 시작하는 곳에서 사용가능


${ ... } from emp ${}


    Select .... from 테이블 이름 ${ mycoondition } s

동적 param -> 2개 이상이면 @Param("")

## day40
* Mybatis : 자바에서는 DB 연동 프로그램을 구현하기 위해 JDBC 기술을 사용한다. JDBC는 관계형 데이터 베이스를 연동하기 위한 다양한 API를 제공한다.

* MyBatis의 특징
    * 간단하다 : 간단한 퍼시스턴스 프레임워크
    * 생산성 : 62%정도 줄어드는 코드 , 간단한 설정, 예외 처리도 선택적
    * 성능 : 구조적 강점(데이터 접근 속도를 높여주는 Join 매핑)
    * SQL문과 애플리케이션 소스 코드의 분리
    * SQL쿼리 변경 시마다 자바코드를 수정하거나 따로 컴파일 할 필요가 없다.
    * 이식성 : 어떤 프로그래밍 언어로도 구현가능 (자바,C#,.NET,RUBY)
    * 오픈소스이며 무료이다.

## day41
10.12 ~ 10.23 [미니프로젝트1](https://www.notion.so/KOSA-1-269f5493e9d5451e84b011cd82f2a131)

## day42
* ERD 생성, 개발 환경 정리
## day43
* dao(Mapper), domain(DTO,VO) 생성
## day44
* controller 생성
## day45
* HTML, CSS, JS 

* HTML & CSS Test
```html
<style>
.inner {
    position: relative;
    width: 600px;
    height: 40px;
    margin: 20px auto;
    border: 1px solid #bdc1c6;
    border-radius: 20px;
}
input{
    width: 90%;
    height: 90%;
    margin-left: 13px ;
    margin-top: 2px;
    border-style: solid;
    border: 1px;
    font-size: 15px;
}
</style>
<body>
    <div class="container">
        <img src="#">
        <div class="inner">
            <input type="search">
            <div class="searching">
                <i class="abc"></i>
            </div>
            <div class="abc">
            </div>
        </div>
        <div>            
    </div>
</body>
</html>
```

## 10월24일
[10월24일.정리](https://www.notion.so/10-24-2587cfc48d2249268339144c2f1b8cb1)

## 10월25일
[10월25일.정리](https://www.notion.so/10-25-4dd002b9f003472da6b4e7da46265c4c)

## 10월26일
[10월26일.정리](https://www.notion.so/10-26-3ddbc472e01d4b348bd08b6cdf324503)

## 10월27일
[10월27일.정리](https://www.notion.so/10-27-15996f6b90c540ddb6c988b685502870)

## 10월30일
[10월30일.정리](https://www.notion.so/10-30-6b176714fd7347c8a79d9fa73284aa82)

## 10월31일
[10월31일.정리](https://www.notion.so/10-31-0ba736341e6048aeae421676274b5647)

## 11월1일
[11월1일.정리](https://www.notion.so/11-01-e9192b38e71d45b8adcfa5f899c366ee)

## 11월2일
[11월2일.정리](https://www.notion.so/11-02-3e8b4e5e5e144491929a9852182157a5)

## 11월3일
[11월3일.정리](https://www.notion.so/11-03-19f88bb2005d4d6a8342a54dc7b696a6)

## 11월6일
[11월6일.정리](https://www.notion.so/11-06-f524e86c5d724b3ca425aab4cd7feef4)

## 11월7일
[11월7일.정리](https://www.notion.so/11-07-16a4ef3c5e4e441ba4ffa2318058015c)

## 2차
[2차 미니프로젝트](https://github.com/jeon-aelim/UniMeeting2)

## 11월8일
[11월8일.정리](https://www.notion.so/11-08-210805bf78ce49b586ae71ddbcd2f6db)

## 11월9일
[11월9일.정리](https://www.notion.so/11-09-20291cdd2fa54b42ade37a923923c001)

## 11월10일
[11월10일.정리](https://www.notion.so/11-10-e1b3b20abd1f4fb3bd4c6f57988427d0)

## 11월13일
[11월13일.정리](https://www.notion.so/11-13-a6ee3fe54b3349e19eac60270e0430ce)

## 11월14일 ~ 11월23일
[2차 프로젝트 진행](https://www.notion.so/KOSA-1-269f5493e9d5451e84b011cd82f2a131)

## SQLD
[SQLD준비](https://www.notion.so/SQLD-1f044f55e8944fc682db895aa93316e6)

## 면접준비
[면접준비](https://www.notion.so/fa1b523c4eef4a74902ebe4018ac20f9?v=2bb2a2e3c55b494ea7110c10634f1dfa)

## 최종 프로젝트
[최종 프로젝트](https://www.notion.so/155f9433df7d42a2b14ed3663d0d39b6?v=2e540e6efc7e4d4c8ba951c37a4346c3)
[피그마](https://www.figma.com/files/recents-and-sharing/recently-viewed?fuid=1290841793067032706)

## 11월29일
[11월29일.정리](https://www.notion.so/11-29-468c9797875a4fc6a9919f191c46ae8c)

## 11월30일
[11월30일.정리](https://www.notion.so/11-30-e786c1b25aaa42fea5bc302006959d04)

## 최종프로젝트 11월24일 ~ 12월29일
[최종프로젝트]()
