public class ch02_VariableBasic {
    public static void main(String[] args){
        //1. 변수 선언
        int studentNum;
        String name;
        double gradeJava;
        double gradeC;
        double avg;

        //2. 변수 정의(초기화)
        studentNum = 500;
        name = "Dong Hwan Yu";
        gradeJava = 4.0;
        gradeC = 3.8;
        avg = 0;

        //3. 연산(재정의)
        avg = (gradeJava + gradeC) / 2;
        name = "Yu, DongHwan";
        studentNum = 600;

        System.out.println(studentNum + name + avg);
        
        double d = 3.1412345789;
        float f = 3.14123456789F;
        System.out.println(d + f);
        
        long l = 1000000000000L;
        l = 1_000_000_000_000L;
        System.out.println(l);
    }
}
