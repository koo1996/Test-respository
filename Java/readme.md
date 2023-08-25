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


* day4 - 1차원 배열
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
* day5 - 2차원 배열
* day6 - 메서드
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
