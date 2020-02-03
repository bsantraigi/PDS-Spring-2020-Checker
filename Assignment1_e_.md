## ROLL: BADRI VISAAL AVVARU
### Assignment 1_e_/BADRI VISAAL AVVARU/BADRI VISAAL AVVARU_1194021_assignsubmission_file_coordinates.c
```C++
//NAME:Avvaru Badri Visaal
//Roll number:19CH10013
//Dept:Chemical Engineering
//Machine number 8
#include<stdio.h>
int main()
{
  float x1,x2,y1,y2,m,n;
  printf("enter your first point coordinates x1:");
  scanf("%f",&x1);
  printf("y1:");
  scanf("%f",&y1);
  printf("enter your second point coordinates x2:");
  scanf("%f",&x2);
  printf("y2:");
  scanf("%f",&y2);
  printf("enter the ratio's abscissa m:");
  scanf("%f",&m);
  printf("ordinate n:");
  scanf("%f",&n);
  printf("The x coordinate of the point is:%f",((m*x2)+(n*x1))/(m+n));
  printf(" and y coordinate is:%f\n",((m*y2)+(n*y1))/(m+n));
}

```
## ROLL: BHARGAVI ADUSUMILLI
### Assignment 1_e_/BHARGAVI ADUSUMILLI/BHARGAVI ADUSUMILLI_1194040_assignsubmission_file_assign1e.c
```C++
/*Name:A.N.V.S.Bhargavi
Rollno:19AE10004
Dept:Aerospace
Machine no:01*/
#include<stdio.h>
main()
{
  float x1,x2,y1,y2,m,n,a,b;
  printf("enter coordinates of point A:");
  scanf("%f%f",&x1,&y1);
  printf("\nenter coordinates of point B:");
  scanf("%f%f",&x2,&y2);
  printf("\nenter the values of m,n:");
  scanf("%f%f",&m,&n);
  a=(m*x2+n*x1)/(m+n);
  b=(m*y2+n*y1)/(m+n);
  printf("\nCoordinates of point P are(%f %f)",a,b);
  return(0);
}
  
  
	 
  

```
## ROLL: DEDIPYA YALAM
### Assignment 1_e_/DEDIPYA YALAM/DEDIPYA YALAM_1194024_assignsubmission_file_ratio.c
```C++
/*A program to read an print co ordinates of 2 points and m,n and calculate the co ordinates of the point which divides line joining those points in m:n internally */
#include<stdio.h>
int main()
{
  float x1,y1,x2,y2,m,n,x,y;
  printf("Enter co ordinates of A:\n");
  scanf("%f%f",&x1,&y1);
  printf("Enter co ordinates of B:\n");
  scanf("%f%f",&x2,&y2);
  printf("A=(%f,%f) B=(%f,%f)",x1,y1,x2,y2);
  printf("\nEnter m,n if ratio is m:n\n");
  scanf("%f%f",&m,&n);
  x=(m*x2+n*x1)/(m+n);
  y=(m*y2+n*y1)/(m+n);
  printf("Co ordinates of the point P which divides AB in m:n ratio internally=(%f,%f)",x,y);
}
  

```
## ROLL: RAHUL CHOUDHARY
### Assignment 1_e_/RAHUL CHOUDHARY/RAHUL CHOUDHARY_1194011_assignsubmission_file_Assignment1(e).c
```C++

#include<stdio.h>
/* Name- Rahul Choudhary
   Roll No.: 19AE10024
   Department: Aerospace
   Machine No.: 02 */
int main()
{
 float x1,y1,x2,y2,m,n,xp,yp;
printf("Enter the (x,y) coordinates of one endpoint of line segment.");
scanf("\n%f%f",&x1,&y1);
printf("Enter the (x,y) coordinates of other endpoint of line segment.");
scanf("\n%f%f",&x2,&y2);
printf("Enter the ratio\n");
scanf("%f%f",&m,&n);
xp=(m*x2 + n*x1)/(m+n); /* formula for calcualting x-coordinate for point lying on line  
                           and dividing the line in m:n ratio */
yp=(m*y2 + n*y1)/(m+n);/* formula for calcualting y-coordinate for point lying on line  
                           and dividing the line in m:n ratio */
printf("The (x,y) coordinates of P are: %f %f\n",xp,yp);
return 0;
}

```
## ROLL: RAHUL NATH
### Assignment 1_e_/RAHUL NATH/RAHUL NATH_1193996_assignsubmission_file_assignment1e.c
```C++
/*Name:Rahul Nath
roll no.:19CH10033
Dept:chemical
assignment:assignment1(e)*/
#include<stdio.h>
#include<math.h>
int main()
{
  float x1,y1,x2,y2;
  float m,n;
  float x3,y3;
  printf("enter all four co-ordinates:\n");   /*input of 4 co-ordinates*/
  scanf("%f%f%f%f",&x1,&y1,&x2,&y2);
  printf("enter internal dividing ratio:\n");    /*ratio input*/
  scanf("%f%f",&m,&n);
   
    x3=(m*x1+n*x2)/(m+n);
    y3=(m*y1+n*y2)/(m+n);
    printf("co-ordinates of P:%f , %f \n",x3,y3);     /*printing co-ordinates of P*/
   
     return(0);
}

```
## ROLL: SHIVAM LAHOTI
### Assignment 1_e_/SHIVAM LAHOTI/SHIVAM LAHOTI_1193986_assignsubmission_file_assignment1e.c
```C++
#include<stdio.h>
int main()
{
  /*name-Shivam Lahoti
roll no. - 19AG10028
machine no. - 5
dep. - agriculture and food engineering*/
  float x1,x2,x3,y1,y2,y3,m,n;
  printf("enter the coordinate of point A\n");
  scanf("%f%f",&x1,&y1);
  printf("enter the coordinates of point B \n");
  scanf("%f%f",&x2,&y2);
  printf("enter the ratio m:n in which AB has to be divided \n");
  scanf("%f%f",&m,&n);
  x3=((x1*n)+(x2*m))/(m+n);
  y3=((y1*n)+(y2*n))/(m+n);
  printf("the coordinate of P is (%f,%f) \n",x3,y3);
}

```
## ROLL: SHIVANI SOREN
### Assignment 1_e_/SHIVANI SOREN/SHIVANI SOREN_1194022_assignsubmission_file_ratio.c
```C++
#include<stdio.h>
int main()
{
  /*program to compute coordinates of point P from input ratio*/
  float x1,y1,x2,y2,m,n,x3,y3;
  printf("Enter coordinates of A :");
  scanf("%f %f",&x1,&y1);
  printf("Enter coordinates of B :");
  scanf("%f %f",&x2,&y2);
  printf("Enter ratio :");
  scanf("%f %f",&m,&n);
  x3=((n*x1)+(m*x2))/(m+n);
  y3=((n*y1)+(m*y2))/(m+n);
  printf("Coordinates of P : %f %f\n",x3,y3);
  
}

```
## ROLL: SHREE HARSHA KODI
### Assignment 1_e_/SHREE HARSHA KODI/SHREE HARSHA KODI_1193974_assignsubmission_file_Assignment 1(e).c
```C++
/*Name:Kodi Shree Harsha
Roll No:19AE30009
Machine No:3
Department:Aerospace*/

#include<stdio.h>
int main()
{
  float x1,x2,y1,y2,m,n,P,X,Y;
  printf("Enter the values:");
  scanf("%f %f %f %f %f %f",&x1,&x2,&y1,&y2,&m,&n);
  X=(m*x2+n*x1)/(m+n);
  Y=(m*y2+n*y1)/(m+n);
 
  printf("Coordinates of point P are X=%f,Y=%f",X,Y); 
    return(0);
}

```
## ROLL: SOHAM ZADE
### Assignment 1_e_/SOHAM ZADE/SOHAM ZADE_1194004_assignsubmission_file_assignment1e.c
```C++
/* Name: Soham Zade
   Roll no: 19CH10053
   Machine no: 10
   Program to internally divide a line segment.*/

#include <stdio.h>

int main()

{float x1, y1, x2, y2;

  printf("Enter X1, Y1, X2, Y2 in order.\n");
  scanf("%f %f %f %f", &x1, &y1, &x2, &y2);

  float m, n, x, y; //x and y are coordinates of point P//

  printf("Enter M and N\n");
  scanf("%f %f", &m, &n);

  x= (m*x2 + n*x1)/(m+n); //Formula for internal division//
  y= (m*y2 + n*y1)/(m+n);

  printf("Coordinates of P are (%f, %f)", x,y);

  return(0);




}

```
## ROLL: SREEYA CHILUPURI
### Assignment 1_e_/SREEYA CHILUPURI/SREEYA CHILUPURI_1194006_assignsubmission_file_a-1e.c
```C++
#include <stdio.h>
int main()
{float x1,x2,y1,y2,m,n,p,x,y;
  printf("Enter the values of x1,y1:\nEnter the value of x2,y2:\nEnter the value of m,n:");
  scanf("%f%f%f%f%f%f",&x1,&x2,&y1,&y2,&m,&n);
  x=(m*x2+n*x1)/m+n;
  y=(m*y2+n*y1)/m+n;
  p=(x,y);
  printf("co-ordinate of x=%f\nco-ordinate of y=%f",x,y);
  return 0;
}

```
