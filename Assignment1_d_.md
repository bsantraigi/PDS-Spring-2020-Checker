## ROLL: BADRI VISAAL AVVARU
### Assignment 1_d_/BADRI VISAAL AVVARU/BADRI VISAAL AVVARU_1193952_assignsubmission_file_reversedigits.c
```C++
//NAME:Avvaru Badri Visaal
//Roll number:19CH10013
//Dept:Chemical Engineering
//Machine number 8
#include<stdio.h>
int main()
{
  int a,x,y,z,p,q;
  printf("enter your three digit number:");
  scanf("%d",&a);
  x=a/100;
  p=a%100;
  y=p/10;
  z=p%10;
  q=(100*z)+(10*y)+x;
  printf("the reversed number is:%d\n",q);
}

```
## ROLL: BHARGAVI ADUSUMILLI
### Assignment 1_d_/BHARGAVI ADUSUMILLI/BHARGAVI ADUSUMILLI_1193964_assignsubmission_file_assign1d.c
```C++
/*Name:A.N.V.S.Bhargavi
Rollno:19AE10004
Dept:Aerospace
machine no:01*/
#include<stdio.h>
int main()
{
  int num,a,b,c,d,e;
  printf("Enter a 3-digit number:");
  scanf("%d",&num);
  a=num/100;
  b=num%10;
  c=num/10;
  d=c%10;
  e=100*b+10*d+a;
  printf("Reversed number=%d",e);
  return(0);
}
  


```
## ROLL: DEDIPYA YALAM
### Assignment 1_d_/DEDIPYA YALAM/DEDIPYA YALAM_1193957_assignsubmission_file_reverse.c
```C++
/*A program to read and print a 3-digit and reverse its digits*/
#include<stdio.h>
int main()
{
  int a,rev;
  printf("Enter a 3-digit no= ");
  scanf("%d",&a);
  rev=100*(a%10)+10*((a/10)%10)+(a/100);
  printf("Reverse number= %d",rev);
}

```
## ROLL: RAHUL CHOUDHARY
### Assignment 1_d_/RAHUL CHOUDHARY/RAHUL CHOUDHARY_1193923_assignsubmission_file_Assignment1(d).c
```C++
#include<stdio.h>
/* Name- Rahul Choudhary
   Roll No.: 19AE10024
   Department: Aerospace
   Machine No.: 02 */
int main()
{
  int a,b,c,d;
printf("Enter the 3-digit number\n");
scanf("%d",&a);
b=a/100; /* we get number at Hundredth position */
c=a/10-b*10; /* we get number at tenth positon */ 
d=a%10; /* we get number ar one's postion */
printf("Reversed number is %d%d%d\n",d,c,b);
return 0;
}

```
## ROLL: RAHUL NATH
### Assignment 1_d_/RAHUL NATH/RAHUL NATH_1193962_assignsubmission_file_assignment1d.c
```C++
/*Name:Rahul Nath
roll no.:19CH10033
Dept:chemical
assignment:assignment1(d)*/
#include<stdio.h>
int main()
{
  int n,rm1,rm2,newn;
    printf("enter the 3 digit no.:\n");/*input 3 digit no.*/
    scanf("%d",&n);
    if((n>=0)&&(n<=999))
      {
	rm1=n%10;
        n=n/10;
	rm2=n%10;
	n=n/10;
	newn=rm1*100+rm2*10+n;
	printf("reverse no.:%d\n",newn);/*printing reversed no.*/
      }
      return(0);
      }

```
## ROLL: SHIVAM LAHOTI
### Assignment 1_d_/SHIVAM LAHOTI/SHIVAM LAHOTI_1193910_assignsubmission_file_assignment1d.c
```C++
#include<stdio.h>
int main()
{
  /*name-Shivam lahoti
roll no. - 19AG10028
machine no. - 5
department- agriculture and food engineering*/
  int n,u1,u2,u3,r,new_number;
  printf("enter a three digit number\n");
  scanf("%d",&n);
  u3=n/100;/*calcullating 100th place digit*/
  r=n%100;
  u2=r/10;/*calculating 10th place digit*/
  u1=r%10;/*calculating unit place digit*/
  new_number= (100*u1)+(10*u2)+u3;
  printf("the reversed number=%d \n",new_number);
}
  

```
## ROLL: SHIVANI SOREN
### Assignment 1_d_/SHIVANI SOREN/SHIVANI SOREN_1193943_assignsubmission_file_reverse.c
```C++
#include<stdio.h>
int main()
{
  /*program to reverse and print a three digit number */
  int a,rev,b,c,e;
  printf("Enter a 3-digit number  : ");
  scanf("%d",&a);
  b=a/100;
  c=(a/10)%10;
  e=a%10;
  rev=(e*100)+(c*10)+b;
  printf("Reverse number = %d\n",rev);
}

```
## ROLL: SHREE HARSHA KODI
### Assignment 1_d_/SHREE HARSHA KODI/SHREE HARSHA KODI_1193924_assignsubmission_file_Assignment1(d).c
```C++
/*Name:Kodi Shree Harsha
Roll No:19AE30009
Machine No:3
Department:Aerospace*/

#include<stdio.h>
int main()
{
  int A,B,C,n,N;
  printf("Enter the number:");
  scanf("%d",&n);
  
   A=n%10 ;
   B=(n/10)%10;
   C=(n/100);
   N=100*A+10*B+C;
  
  printf("Reverse of the number is %d",N);
  return(0);
    }

```
## ROLL: SOHAM ZADE
### Assignment 1_d_/SOHAM ZADE/SOHAM ZADE_1193934_assignsubmission_file_assignment1d.c
```C++
/* Name: Soham Zade
   Roll no: 19CH10053
   Machine no: 10
   Program to reverse digits*/

#include <stdio.h>

int main()

{
  int n, r1, r2, r3;
  /* r1 is remainder when n is divided by 10.
     r2 is remainder when quotient of n/10 is divided by 10 and so on.*/

  printf("Enter a 3-digit number\n");
  scanf("%d", &n);

  r1 = n%10;
  r2 = (n/10)%10;
  r3 = (n/100)%10;

  printf("Reverse number = %d\n", r1*100+ r2*10+ r3*1);

  return(0);
    



}

```
## ROLL: SREEYA CHILUPURI
### Assignment 1_d_/SREEYA CHILUPURI/SREEYA CHILUPURI_1193927_assignsubmission_file_a-1d.c
```C++
#include <stdio.h>
int main()
{int a,n,r,sum;
  printf("Enter a 3-digit number:\n");
  scanf("%d",&a);
  sum=0;
  n=100;
  while(a>0)
    { r=a%10;
      sum=sum+r*n;
      a=a/10;
      n=n/10;
    }
  printf("reverse of a 3-digit number=%d\n",sum);
  return 0;
}  

```
