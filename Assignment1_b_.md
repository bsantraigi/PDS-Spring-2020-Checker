## ROLL: BADRI VISAAL AVVARU
### Assignment 1_b_/BADRI VISAAL AVVARU/BADRI VISAAL AVVARU_1193762_assignsubmission_file_marks.c
```C++
//NAME:Avvaru Badri Visaal
//Roll number:19CH10013
//Dept:Chemical Engineering
//Machine number 8
#include<stdio.h>
int main()
{
  float eng,mat,phy,chem,cs,total,per;
  printf("your marks in english:");
  scanf("%f",&eng);
  printf("your marks in maths:");
  scanf("%f",&mat);
  printf("your marks in physics:");
  scanf("%f",&phy);
  printf("your marks in chemistry:");
  scanf("%f",&chem);
  printf("your marks in computer science:");
  scanf("%f",&cs);
  total=eng+mat+chem+phy+cs;
  per=(total/250)*100;
  printf("total:%f\n",total);
  printf("percentage:%f\n",per);
}

```
## ROLL: BHARGAVI ADUSUMILLI
### Assignment 1_b_/BHARGAVI ADUSUMILLI/BHARGAVI ADUSUMILLI_1193777_assignsubmission_file_assign1b.c
```C++
/*Name:A.N.V.S.Bhargavi
Rollno:19AE10004
Dept:Aerospace
Machine no:01*/
#include<stdio.h>
main()
{
  int eng,math,phy,chem,cs,total;
  float percentage;
  printf("enter the marks\n");
  printf("English:");
  scanf("%d",&eng);
  printf("Maths:");
  scanf("%d",&math);
  printf("Physics:");
  scanf("%d",&phy);
  printf("Chemistry:");
  scanf("%d",&chem);
  printf("Computer Science:");
  scanf("%d",&cs);
  total=eng+math+phy+chem+cs;
  printf("total=%d",total);
  percentage=total/2.5;
  printf("\npercentage=%f",percentage);
  return(0);
}

```
## ROLL: DEDIPYA YALAM
### Assignment 1_b_/DEDIPYA YALAM/DEDIPYA YALAM_1193765_assignsubmission_file_report.c
```C++
/*A program to read and print your subject marks out of 50 and calcuate total marks and percentage of marks*/
#include<stdio.h>
int main()
{
	float eng_marks,maths_marks,phy_marks,chem_marks,computerscience_marks,total,percentage;
	printf("Enter English marks out of 50:");
	scanf("%f",&eng_marks);
	printf("Enter Mathematics  marks out of 50:");
	scanf("%f",&maths_marks);
	printf("Enter Physics marks out of 50:");
	scanf("%f",&phy_marks);
	printf("Enter Chemistry  marks out of 50:");
	scanf("%f",&chem_marks);
	printf("Enter Computer Science marks out of 50:");
	scanf("%f",&computerscience_marks);
	total=eng_marks+maths_marks+phy_marks+chem_marks+computerscience_marks;
	percentage=total*100.00/250.00;
	printf("Total marks:%f\nPercentage of marks:%f\n",total,percentage);
}
	
	

```
## ROLL: RAHUL CHOUDHARY
### Assignment 1_b_/RAHUL CHOUDHARY/RAHUL CHOUDHARY_1193760_assignsubmission_file_Assignment1(b).c
```C++

#include<stdio.h>
/* Name- Rahul Choudhary
   Roll No.: 19AE10024
   Department: Aerospace
   Machine No.: 02 */
int main()
{
  int a,b,c,d,e;
  float f,g;
printf("Enter the English Marks\n");
scanf("%d",&a);
printf("Enter the Mathematics Marks\n");
scanf("%d",&b);
printf("Enter the Physics Marks\n");
scanf("%d",&c);
printf("Enter the Chemistry Marks\n");
scanf("%d",&d);
printf("Enter the Computer Science Marks\n");
scanf("%d",&e);
f=a+b+c+d+e;     /*total marks calculation */
g=(f/250)*100;           /*percentage calculation */
printf("Total Marks is %f\n",f);
printf("Percentage is %f\n",g);
return 0;
}

```
## ROLL: RAHUL NATH
### Assignment 1_b_/RAHUL NATH/RAHUL NATH_1193754_assignsubmission_file_assignment1b.c
```C++
/*Name:Rahul Nath
roll no.:19CH10033
Dept:chemical
assignment:assignment1(b)*/
#include<stdio.h>
int main()
{
  int E,M,CS,P,C;
  int total;
  float percent;
  printf("enter the marks of English,Maths,computer science,physics,chemistry:\n");/*input of marks*/
  scanf("%d%d%d%d%d",&E,&M,&CS,&P,&C);
  if((E<=50)&&(E>=0)&& (M<=50)&&(M>=0)&&(CS<=50)&&(CS >=0 )&&(P>=0)&&(P<=50)&&(C>=0)&&(C<=50))
    {  
  total=E+M+CS+P+C;
  percent=((float)total/250.0)*100.0;
  printf("total marks and percent:%d and %f",total,percent);/*output of total and percentage*/
    }
  
  return(0);
}
  

```
## ROLL: SHIVAM LAHOTI
### Assignment 1_b_/SHIVAM LAHOTI/SHIVAM LAHOTI_1193774_assignsubmission_file_assignment1b.c
```C++
#include<stdio.h>
int main()
{
  /*name-Shivam lahoti
roll no.-19AG10028
machin no.- 5
dep. - Agriculture and food engineering*/
  float m1,m2,m3,m4,m5,total,prcnt;
  printf("enter your marks in english, maths, physics, chemistry and computer sscience respectively:\n");
  scanf("%f%f%f%f%f",&m1,&m2,&m3,&m4,&m5);
  total=m1+m2+m3+m4+m5;
  prcnt=(total/250)*100;
  printf("our total marks is %f and obtained percentage is %f \n",total,prcnt);
}

```
## ROLL: SHIVANI SOREN
### Assignment 1_b_/SHIVANI SOREN/SHIVANI SOREN_1193741_assignsubmission_file_marks.c
```C++
#include<stdio.h>
int main()
{
  /*program to calculate total and percentage of given subjects*/
  float a,b,c,d,e,tot,per;
  printf("Enter marks for English : ");
  scanf("%f",&a);
  printf("Enter marks for Mathematics : ");
  scanf("%f",&b);
  printf("Enter marks for Physics : ");
  scanf("%f",&c);
  printf("Enter marks for Chemistry : ");
  scanf("%f",&d);
  printf("Enter marks for Computer Science : ");
  scanf("%f",&e);
  tot=a+b+c+d+e;
  per=(tot/250)*100;
  printf("Your total marks is %0.2f out of 250\n",tot);
  printf("Percentage = %0.2f \n",per);
}

```
## ROLL: SHREE HARSHA KODI
### Assignment 1_b_/SHREE HARSHA KODI/SHREE HARSHA KODI_1193806_assignsubmission_file_assignment1(b).c
```C++
/*Name:Kodi Shree Harsha
Roll No:19AE30009
Machine No:3
Department:Aerospace*/

#include<stdio.h>
int main()
{
  int Eng,Maths,Phy,Che,CS;
  float Total,Percentage;
  printf("Enter the values of Eng,Maths,Phy,Che,CS:");
  scanf("%d%d%d%d%d",&Eng,&Maths,&Phy,&Che,&CS);
  Total=Eng+Maths+Phy+Che+CS;
  Percentage=(Total/250)*100;
 
   printf("Total and percentage are %f %f,Total,Percentage"); 
    return(0);
}

```
## ROLL: SOHAM ZADE
### Assignment 1_b_/SOHAM ZADE/SOHAM ZADE_1193785_assignsubmission_file_assignment1b.c
```C++
/*Name : Soham Zade
  Roll no: 19CH10053
  Machine no: 10
  Program to calculate total and percentage of marks*/

#include <stdio.h>

int main()

{
  float eng, math, phy, chem, cs; //variables for marks//

  printf("Enter your marks in English, Maths, Physics, Chemistry and Computer Science in order.\n");
  scanf("%f %f %f %f %f", &eng, &math, &phy, &chem, &cs);

  printf("Your total marks are %f.\n", eng+math+phy+chem+cs); //total//
  printf("Your percentage is %f.\n", ((eng+math+phy+chem+cs)/250)*100); //percentage//

  return(0);



}

```
## ROLL: SREEYA CHILUPURI
### Assignment 1_b_/SREEYA CHILUPURI/SREEYA CHILUPURI_1193745_assignsubmission_file_ass-1b.c
```C++
#include <stdio.h>
int main()
{float  Eng,Mat,Phy,Chem,CS,Total, Percentage;
  printf("Enter the marks of Eng,Mat,Phy,Chem,CS\n:");
  scanf("%f%f%f%f%f",&Eng,&Mat,&Phy,&Chem,&CS);
  Total=Eng+Mat+Phy+Chem+CS;
  Percentage=(Total/250)*100;
  printf("Total marks=%f\nPercentage=%f",Total,Percentage);
  return 0;
}
    

```
