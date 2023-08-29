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

- 자바에서 생성되는 클래스는 반드시 부모 클래스를 한 개 갖게 된다. 
- 부모 클래스 정의를 생략한 경우 자동으로 java.lang.Object 클래스를 상속하게 된다.
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

