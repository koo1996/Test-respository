use edudb;
-- QUESTION

-- [ course1 테이블과 course2 테이블을 가지고 문제 해결 ]

-- 1. course1 을 수강하는 학생들과 course2 를 수강하는 학생들의 이름, 전화 번호 그리고 
--    나이를 출력하는데 나이가 많은 순으로 출력하시오.
--    단, 두 코스를 모두 수강하는 학생들의 정보는 한 번만 출력한다.
select name, phone, age from course1
UNION
select name, phone, age from course2 order by age desc;

-- name   phone        age  
-- ----------------------------
-- 토토로  010-555-5555    13 
-- 도우너  010-333-3333    12 
-- 또치    010-222-2222    11 
-- 듀크    010-777-7777    11 
-- 둘리    010-111-1111    10 
-- 짱구    010-666-6666     7 
-- 희동이  010-444-4444     6

-- 2. course1 을 수강하는 학생들과 course2 를 수강하는 학생들의 이름, 전화 번호 그리고 
--    나이를 출력하는데 나이가 많은 순으로 출력하시오.
--    단, 두 코스를 모두 수강하는 학생들의 정보를 중복해서 출력한다. 
select name, phone, age from course1
UNION ALL
select name, phone, age from course2 order by age desc;

-- name   phone        age 
-- ----------------------------
-- 토토로 010-555-5555   13 
-- 도우너 010-333-3333   12 
-- 또치   010-222-2222   11 
-- 듀크   010-777-7777   11
-- 또치   010-222-2222   11 
-- 둘리   010-111-1111   10 
-- 둘리   010-111-1111   10 
-- 짱구   010-666-6666    7 
-- 희동이 010-444-4444    6 

-- 3. 직무별 그리고 입사년도별 직원들 수를 출력하는데 직무별 직원수(소합계)와 전체 직원수(전체 합계)도 
--      함께 출력한다.
select job 직무, year(hiredate) 입사년도, count(*) 직원수 from emp group by job,year(hiredate) with rollup;

-- 직무      	입사년도 	직원수
-- -------------------------------------------
-- ANALYST       	1981      1
-- ANALYST       	1982      1
-- ANALYST       	NULL      2
-- CLERK         	1980      1
-- CLERK         	1981      1
-- CLERK         	1982      1
-- CLERK         	1983      1
-- CLERK         	NULL      4
-- MANAGER       	1981      3
-- MANAGER       	NULL      3
-- PRESIDENT     	1981      1
-- PRESIDENT     	NULL      1
-- SALESMAN      	1981      4
-- SALESMAN      	NULL      4
-- NULL         	 NULL     14

-- [ emp 테이블(dept, locations, salgrade 테이블)을 가지고 문제 해결 ]

-- 4. RESEARCH 부서에서 근무하는 직원의 이름, 직무, 부서이름을 출력하시오.
select ename 이름, job 직무, dname 부서이름 from emp e join dept d on e.deptno = d.deptno where d.dname = 'RESEARCH';

-- 이름         직무         	부서이름          
-- ---------- --------- ------------------
-- SMITH CLERK   RESEARCH 
-- JONES MANAGER RESEARCH 
-- SCOTT ANALYST RESEARCH 
-- FORD  ANALYST RESEARCH 

-- 5. 이름에 'A'가 들어가는 직원들의 이름과 부서이름을 출력하시오.
select ename 이름, dname 부서이름 from emp e join dept d on e.deptno = d.deptno where e.ename like '%A%';

-- 이름        부서이름          
-- --------    --------------
-- ALLEN  SALES      
-- WARD   SALES      
-- MARTIN SALES     
-- BLAKE  SALES      
-- CLARK  ACCOUNTING 
-- JAMES  SALES

-- 6. 직원이름과 그 직원이 속한 부서의 부서명, 그리고 월급을 
-- 출력하는데 월급이 3000이상인 직원을 출력하시오.
select ename 직원이름, dname 부서명, concat(format(sal,0),'원') 월급 from emp e join dept d on e.deptno = d.deptno where e.sal >= 3000;
-- 직원이름   부서명               월급
-- ---------- -------------- ----------
-- SCOTT   RESEARCH	3,000원
-- KING	   ACCOUNTING	5,000원
-- FORD	   RESEARCH	3,000원

-- 7. 커미션이 책정된 직원들의 직원번호, 이름, 연봉, 연봉커미션,
-- 급여등급을 출력하되, 각각의 컬럼명을 '직원번호', '직원이름',
-- '연봉','실급여', '급여등급'으로 하여 출력하시오. 
-- 또한 실급여가 적은 순으로 출력하시오.
select empno 직원번호, ename 직원이름, (sal * 12) 연봉, (sal * 12 + comm) 실급여 from emp where comm != 'null' order by (sal * 12 + comm);
--  직원번호 직원이름      연봉           실급여       급여등급
-- ---------- ---------- ---------- --------------- ----------
--  7521 WARD             15000         15200          2
--  7654 MARTIN          15000         15300          2
--  7844 TURNER          18000         18000          3
--  7499	ALLEN	       19200         19500	   3
--  7566 JONES    	       35700         35730         4 
--  7839 KING              60000         63500         5
  
  
-- 8. 부서번호가 10번인 직원들의 부서번호, 부서이름, 직원이름,
-- 월급, 급여등급을 출력하시오. 
-- select deptno 부서번호, dname 부서이름, ename 직원이름, sal 월급, grade 급여등급 from emp e,dept d join salgrade s on s.losal <= e.sal and e.sal <= s.hisal; 
--   
-- 부서번호 부서이름           직원이름      월급           급여등급
-- ---------- -------------- ---------- -------------- -------------
--      10 ACCOUNTING     CLARK            2450          4
--      10 ACCOUNTING     KING              5000          5
--      10 ACCOUNTING     MILLER           1300          2 

-- 9. 직무가 'SALESMAN'인 직원들의 직무와 그 직원이름, 그리고
-- 그 직원이 속한 부서 이름을 출력하시오. 
select job 직무, ename 직원이름, dname 부서이름 from emp e join dept d on e.deptno = d.deptno where job = 'SALESMAN';

-- 직무          직원이름       부서이름          
-- --------- ---------- --------------
-- SALESMAN  TURNER     SALES         
-- SALESMAN  MARTIN     SALES         
-- SALESMAN  WARD       SALES         
-- SALESMAN  ALLEN      SALES 

-- 10. 부서번호가 10번, 20번인 직원들의 부서번호, 부서이름, 
-- 직원이름, 월급, 급여등급을 출력하시오. 그리고 그 출력된 
-- 결과물을 부서번호가 낮은 순으로, 월급이 많은 순으로 정렬하시오. (7개 행)

-- select deptno 부서번호, dname 부서이름, ename 직원이름, sal 월급, grade 급여등급 from emp join salgrade on 
--   부서번호 부서이름              직원이름               월급       급여등급
-- ---------- -------------- ---------- ---------- ------------ ----------
--    10 ACCOUNTING         KING                   5000          5
--    10 ACCOUNTING         CLARK                 2450          4
--    10 ACCOUNTING         MILLER                 1300          2
--    20 RESEARCH             SCOTT    	3000           4
--    20  RESEARCH    	FORD      	3000           4 
--    20  RESEARCH   	JONES     	2975           4 
--    20  RESEARCH    	SMITH      	800            1 
                                                 
-- 11. 사원들의 이름, 부서번호, 부서이름을 출력하시오. 
-- 단, 직원이 없는 부서도 출력하며 이경우 이름을 '없음'이라고 출력한다.     
-- 부서번호별로 정렬한다.
select ename 이름, deptno 부서번호, dname 부서이름 from emp e join dept d on e.deptno = d.deptno;
-- 이름               부서번호 부서이름          
-- ---------- ---------- --------------
-- CLARK         10  ACCOUNTING 
-- KING          10  ACCOUNTING 
-- MILLER        10  ACCOUNTING 
-- SMITH         20  RESEARCH   
-- JONES         20  RESEARCH   
-- SCOTT         20  RESEARCH   
-- FORD          20  RESEARCH   
-- ALLEN         30  SALES      
-- WARD          30  SALES      
-- MARTIN        30  SALES      
-- BLAKE         30  SALES      
-- TURNER        30  SALES      
-- JAMES         30  SALES      
-- 없음          40  OPERATIONS 
-- 없음          50  INSA       

-- 12. 직원들의 이름, 부서번호, 부서이름을 출력하시오. 
-- 단, 아직 부서 배치를 못받은 직원도  출력하며 이경우 부서번호와 부서명은  null 로
-- 출력한다.  또한 직원들의 이름순으로 정렬한다. 
-- --이름               부서번호     부서이름          
-- ---------- ---------- --------------
-- ADAMS       NULL          	NULL       
-- ALLEN        30             	SALES      
-- BLAKE         30            	SALES  
-- CLARK         10  	ACCOUNTING 
--  FORD          20  	RESEARCH   
-- JAMES         30  	SALES      
-- JONES         20  	RESEARCH   
-- KING          10  	ACCOUNTING 
-- MARTIN        30  	SALES      
-- MILLER        10  	ACCOUNTING 
-- SCOTT         20  	RESEARCH   
-- SMITH         20  	RESEARCH   
-- TURNER        30  	SALES      
-- WARD          30  	SALES                              

-- 13. 커미션이 정해진 모든 직원의 이름, 커미션, 부서이름, 도시명을 출력하시오.
select ename 직원명, comm 커미션, dname 부서명, city 도시명 from emp join 
-- 직원명 		커미션 	부서명     		도시명  
-- ---------------------------------------------
-- KING     	3500 	ACCOUNTING 	SEOUL   
-- JONES      	30 	RESEARCH   	DALLAS  
-- ALLEN     	300 	SALES      	CHICAGO 
-- WARD     	 200 	SALES      	CHICAGO 
-- MARTIN   	 300 	SALES      	CHICAGO 
-- TURNER      	0 	SALES      	CHICAGO 

-- 14. DALLAS에서 근무하는 사원의 이름,  월급, 등급을 출력하시오.
select ename 이름, sal 월급, grade 등급 from emp e inner join salgrade s on e.sal >= s.losal and e.sal <= s.hisal inner join locations l
-- 이름         월급             등급          
-- ---------- --------- --------------
-- SMITH      800            1      
-- JONES      2975          4   
-- SCOTT     3000	        4
-- FORD       3000          4     

-- 15. 사원들의 이름, 부서번호, 부서이름을 출력하시오. 
-- 단, 직원이 없는 부서도 출력하며 이경우 직원 이름을 '누구?'라고
-- 출력한다. 아직 부서 배치를 못받은 직원도  출력하며 부서 번호와 부서 이름을
-- '어디?' 이라고 출력한다.     (16행)
-- 부서명을 기준으로 정렬한다.
-- 직원명   부서번호   부서명    
-- ------------------------------
-- CLARK  10       ACCOUNTING
-- KING   10       ACCOUNTING
-- MILLER 10       ACCOUNTING
-- 누구?  NULL     INSA      
-- 누구?  NULL     OPERATIONS
-- SMITH  20       RESEARCH  
-- JONES  20       RESEARCH  
-- SCOTT  20       RESEARCH  
-- FORD   20       RESEARCH  
-- ALLEN  30       SALES     
-- WARD   30       SALES     
-- MARTIN 30       SALES     
-- BLAKE  30       SALES     
-- TURNER 30       SALES     
-- JAMES  30       SALES     
-- ADAMS  어디?    어디?     


-- 16. 'CHICAGO' 에서 근무하는 직원들의 이름, 입사날짜, 급여를 출력한다.ㅇ
--      (서브쿼리로 해결한다.)
select ename, hiredate, sal from emp e inner join dept d on e.deptno = d.deptno 
inner join locations l on d.loc_code = l.loc_code where city = 'CHICAGO';
-- ename   hiredate    sal  
-- --------------------------
-- ALLEN   1981-02-20  1600 
-- WARD    1981-02-22  1250 
-- MARTIN  1981-09-28  1250 
-- BLAKE   1981-04-01  2850 
-- TURNER  1981-09-08  1500 
-- JAMES   1981-10-03   950 


-- 17. 'CHICAGO' 에서 근무하는 직원들의 이름, 입사년도, 부서명을 출력한다.ㅇ
--      (조인로 해결한다.)
select ename, hiredate, dname from emp e inner join dept d on e.deptno = d.deptno 
inner join locations l on d.loc_code = l.loc_code where city = 'CHICAGO';
-- ename   hiredate    dname 
-- ---------------------------
-- ALLEN   1981-02-20  SALES 
-- WARD    1981-02-22  SALES 
-- MARTIN  1981-09-28  SALES 
-- BLAKE   1981-04-01  SALES 
-- TURNER  1981-09-08  SALES 
-- JAMES   1981-10-03  SALES 


-- 18. 직원의 이름과 그 직원원 매니저명을 출력하는데 매니저가 없는 직원은 '없음' 이라고 
--      출력한다.

-- 직원명  매니저명 
-- ------------------
-- SMITH   FORD     
-- ALLEN   BLAKE    
-- WARD    BLAKE    
-- JONES   KING     
-- MARTIN  BLAKE    
-- BLAKE   KING     
-- CLARK   KING     
-- SCOTT   JONES    
-- KING      없음     
-- TURNER  BLAKE    
-- ADAMS   SCOTT    
-- JAMES   BLAKE    
-- FORD    JONES    
-- MILLER  CLARK    

-- 19. 'DALLAS' 에서 근무하는 직원들의 이름, 연봉, 부서명을 연봉이 큰 순으로 출력하는데
--      연봉의 계산은 (급여커미션)*12  을 적용하는데 커미션이 정해지지않은 직원은 0으로 계산한다.
     
-- 이름   연봉   부서명   
-- ------------------------
-- JONES  36060  RESEARCH 
-- SCOTT  36000  RESEARCH 
-- FORD   36000  RESEARCH 
-- SMITH   9600  RESEARCH 

-- 20. 부서별로 최고 월급을 받는 직원들의 부서번호, 직원이름과 급여를 출력하시오. ㅇ
select deptno, ename, sal from emp group by deptno;
-- deptno  ename  sal  
-- ---------------------
--     30  BLAKE  2850 
--     20  SCOTT  3000 
--     10  KING   5000 
--     20  FORD   3000 


-- 21 직무별로 입사한지 가장 오래된 직원들의 직무와 직원이름 그리고 입사날짜를 출력하시오.
select job, ename, hiredate from emp group by job order by hiredate;
-- job        ename  hiredate   
-- ------------------------------
-- CLERK      SMITH  1980-12-17 
-- SALESMAN   ALLEN  1981-02-20 
-- MANAGER    BLAKE  1981-04-01 
-- PRESIDENT  KING   1981-11-17 
-- ANALYST    FORD   1981-10-03 

-- 22 'SEOUL' 에서 근무중인 직원들의 인원을 출력하시오. ㅇ
select concat(count('SEOUL'),'명') 인원수 from emp e inner join dept d on e.deptno = d.deptno 
inner join locations l on d.loc_code = l.loc_code where city = 'SEOUL';
-- 인원수 
-- --------
--  3명    
