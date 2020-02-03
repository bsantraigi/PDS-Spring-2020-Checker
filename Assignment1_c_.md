## ROLL: BADRI VISAAL AVVARU
### Assignment 1_c_/BADRI VISAAL AVVARU/BADRI VISAAL AVVARU_1193885_assignsubmission_file_distance.c
```C++
//NAME:Avvaru Badri Visaal
//Roll number:19CH10013
//Dept:Chemical Engineering
//Machine number 8
#include<stdio.h>
int main()
{
  float a,u,alpha,t,d;
  printf("Enter the values of a, u, alpha in order:");
  scanf("%f%f%f",&a,&u,&alpha);
  printf("Enter the Time:");
  scanf("%f",&t);
  d=a+(u*t)+(0.5*alpha*t*t);
  printf("D:%f\n",d);
}

```
## ROLL: BHARGAVI ADUSUMILLI
### Assignment 1_c_/BHARGAVI ADUSUMILLI/BHARGAVI ADUSUMILLI_1193826_assignsubmission_file_assign1c.c
```C++
/*Name:A.N.V.S.Bhargavi
Rollno:19AE10004
Dept:Aerospace
machine no:01*/
#include<stdio.h>
main()
{
  float a,u,alpha,t,d;
  printf("enter the values of a,u,alpha in order:");
  scanf("%f %f %f",&a,&u,&alpha);
  printf("enter the time:");
  scanf("%f",&t);
  d=(u*t)+(a*t*t)/2;
  printf("Distance:%f",d);
  return(0);
}

```
## ROLL: DEDIPYA YALAM
### Assignment 1_c_/DEDIPYA YALAM/DEDIPYA YALAM_1193842_assignsubmission_file_p1c.c
```C++
/*A program to calculate the distance covered by a particle from origin using ininitial velocity,intial position,acceleration,time taken*/
#include<stdio.h>
int main()
{
  float u,a,t,alpha,d;
  printf("Enter values of a,u,alpha in order:\n");
  scanf("%f%f%f",&a,&u,&alpha);
  printf("\nEnter time:\n");
  scanf("%f",&t);
  d=u*t+0.5*alpha*t*t+a;
  printf("\nDistance:%f",d);
}

```
## ROLL: RAHUL CHOUDHARY
### Assignment 1_c_/RAHUL CHOUDHARY/RAHUL CHOUDHARY_1193881_assignsubmission_file_Assignment1(c).c
```C++

#include<stdio.h>
/* Name- Rahul Choudhary
   Roll No.: 19AE10024
   Department: Aerospace
   Machine No.: 02 */
int main()
{
  float a,u,alpha,time,distance;
 printf("Enter the values of a, u, alpha in order:");
 scanf("%f %f %f",&a, &u, &alpha);
printf("Enter the time:");
scanf("%f",&time);
distance=a+u*time + (alpha*time*time)*0.5;  /*formula for calculating distance */
printf("Distance: %f\n",distance);
return 0;
}

```
## ROLL: RAHUL NATH
### Assignment 1_c_/RAHUL NATH/RAHUL NATH_1193845_assignsubmission_file_assignment1c.c
```C++
/*Name:Rahul Nath
roll no.:19CH10033
Dept:chemical
assignment:assignment1(c)*/
#include<stdio.h>

int main()
{
  int  a, u, alpha;
  int t;
  float dist;
  printf("enter value of  a, u, alpha:\n");/*input of  a, u, alpha*/
  scanf("%d%d%d",&a,&u,&alpha);
  printf("enter time:\n");
  scanf("%d",&t);
  dist= (float)a+( (float)u*(float)t + (float)alpha/2*(float)t*(float)t);
  printf("distance covered is :%f",dist);/*printing distance*/

  return(0);
}
  

```
## ROLL: SHIVAM LAHOTI
### Assignment 1_c_/SHIVAM LAHOTI/SHIVAM LAHOTI_1193828_assignsubmission_file_p1c.c
```C++
#include<stdio.h>
int main()
{
  /*name-shivam lahoti
roll no.- 19AG10028
machine no. - 5
dep. - agriculture and food engineering*/
  float a,u,alpha,d,t;
  printf("enter the values of a,u,alpha in order:\n");
  scanf("%f%f%f",&a,&u,&alpha);
  printf("enter the time\n");
  scanf("%f",&t);
  d=a+(u*t)+(0.5*alpha*t*t);
  printf("distance=%f \n",d);
}
   

```
## ROLL: SHIVANI SOREN
### Assignment 1_c_/SHIVANI SOREN/SHIVANI SOREN_1193870_assignsubmission_file_p1c.c
```C++
#include<stdio.h>
int main()
{
  /*program to find distance from speed,acceleration and time*/
  int a,u,al;
  float t,d;
  printf("Enter values of a,u,alpha in order : ");
  scanf("%d %d %d",&a,&u,&al);
  printf("Enter the time : ");
  scanf("%f",&t);
  d=(u*t)+(0.5*al*t*t);
  printf("Distance = %f\n",d+a);
  
}

```
## ROLL: SHREE HARSHA KODI
### Assignment 1_c_/SHREE HARSHA KODI/SHREE HARSHA KODI_1193832_assignsubmission_file_Assignment 1(c).c
```C++
/*Name:Kodi Shree Harsha
Roll No:19AE30009
Machine No:3
Department:Aerospace*/

#include<stdio.h>
int main()
{
  float a,u,alpha,t,distance;
  printf("Enter the values of a,u,alpha,t:");
  scanf("%f %f %f %f",&a,&u,&alpha,&t);
  distance=a+(u*t)+(1.0/2.0)*(alpha*t*t);
 
   printf("distance is equal to %f", distance); 
    return(0);
}

```
## ROLL: SOHAM ZADE
### Assignment 1_c_/SOHAM ZADE/SOHAM ZADE_1193835_assignsubmission_file_assignment1c.c
```C++
/*Name: Soham Zade
  Roll no: 19CH10053
  Machine no: 10
  Program to find d*/

#include <stdio.h>

int main()

{float ini, speed, acc, time, d; //ini is for initial coordinate a//

  printf("Enter values of a, u, alpha in order.\n");
  scanf("%f %f %f", &ini, &speed, &acc);

  printf("Enter the time.\n");
  scanf("%f", &time);

  d= ini + speed*time + 0.5*acc*time*time; //d is distance from origin after t//
  printf("Distance = %f", d);

  return(0);




}

```
## ROLL: SREEYA CHILUPURI
### Assignment 1_c_/SREEYA CHILUPURI/SREEYA CHILUPURI_1193886_assignsubmission_file_a-1c.c
```C++
#include <stdio.h>
int main()
{float a,u,alpha,t,s,Distance;
  printf("Enter the value of a,u,alpha:\nEnter the value of t:\n");
  scanf("%f%f%f",&a,&u,&alpha);
  scanf("%f",&t);
  s=u*t+(0.5*alpha*t*t);
  Distance=s/t;
  printf("Distance=%f\n",Distance);
  return 0;
}
  
  

```
