## ROLL: BADRI VISAAL AVVARU
### Assignment 2_a_/BADRI VISAAL AVVARU/BADRI VISAAL AVVARU_1195550_assignsubmission_file_p2a.c
```C++
//NAME:Avvaru Badri Visaal
//Roll number:19CH10013
//Dept:Chemical Engineering
//Machine number 8
#include<stdio.h>
int main()
{
  int p,q,r,s,min1,min2,max1,max2,maxb,minb,maxa,mina;
  printf("input the four values:");
  scanf("%d%d%d%d",&p,&q,&r,&s);
  if(p>q)
    {
      maxa=p;
      mina=q;
    }
  else
    {
      maxa=q;
      mina=p;
    }
  if(r>s)
    {
      maxb=r;
      minb=s;
    }
  else
    {
      maxb=s;
      minb=r;
    }
  if(maxa>maxb)
    {
    max1=maxa;
    if((maxb>mina)&&(maxb>minb))
      {
	max2=maxb;
           if(mina>minb)
	     {
              min1=minb;
	      min2=mina;
	     }
           else
	     {
              min1=mina;
	      min2=minb;
	     }
      }
    else
      {
	if((maxb>mina)&&(maxb<minb))
	  {
	    max2=minb;
	    min2=maxb;
	    min1=mina;
	  }
	else if((maxb<mina)&&(maxb>minb))
	  {
	    max2=mina;
	    min2=maxb;
	    min1=minb;
	  }
      }
    }
  else
    {
    max1=maxb;
        if((maxb>mina)&&(maxb>minb))
      {
	max2=maxb;
           if(mina>minb)
	     {
              min1=minb;
	      min2=mina;
	     }
           else
	     {
              min1=mina;
	      min2=minb;
	     }
      }
    else
      {
	if((maxb>mina)&&(maxb<minb))
	  {
	    max2=minb;
	    min2=maxb;
	    min1=mina;
	  }
	else if((maxb<mina)&&(maxb>minb))
	  {
	    max2=mina;
	    min2=maxb;
	    min1=minb;
	  }
      }                                      
    }
  printf("max1:%d\n",max1);
  printf("max2:%d\n",max2);
  printf("min1:%d\n",min1);
  printf("min2:%d\n",min2);
}

```
## ROLL: BHARGAVI ADUSUMILLI
### Assignment 2_a_/BHARGAVI ADUSUMILLI/BHARGAVI ADUSUMILLI_1195552_assignsubmission_file_assign2a.c
```C++
/*Name:A.N.V.S.Bhargavi
Rollno:19AE10004
Dept:Aerospace
Machine no:01*/
#include<stdio.h>
#include<math.h>
int main()
{
  int a,b,c,d;
  if(a>b && a>c && a>d && b>c && b>d && c>d)
  printf("Min=%d,Second min=%d,Max=%d,Second max=%d",d,c,a,b);
  if(a>b && a>c && a>d && b>c && b>d && d>c)
   printf("Min=%d,Second min=%d,Max=%d,Second max=%d",c,d,a,b);
  if(a>b && a>c && a>d && c>b && c>d && b>d)
    printf("Min=%d,Second min=%d,Max=%d,Second max=%d",d,b,a,c);
  if(a>b && a>c && a>d && c>b && c>d && b<d)
   printf("Min=%d,Second min=%d,Max=%d,Second max=%d",b,d,a,c);
  if(a>b && a>c && a>d && d>b && d>c && b>c)
 printf("Min=%d,Second min=%d,Max=%d,Second max=%d",c,b,a,d);
  if(a>b && a>c && a>d && d>b && d>c && c>b)
 printf("Min=%d,Second min=%d,Max=%d,Second max=%d",b,c,a,d);
  
  }
    

```
## ROLL: DEDIPYA YALAM
### Assignment 2_a_/DEDIPYA YALAM/DEDIPYA YALAM_1195493_assignsubmission_file_minmax.c
```C++
/*A program to read and print minimum ,maximum ,second minimum ,second maximum among 4 numbers*/
#include<stdio.h>
int main()
{
  int a,b,c,d,max1,min1,max2,min2;
  printf("\nEnter four distinct numbers:\n");
  scanf("%d%d%d%d",&a,&b,&c,&d);
  if(a>b)
    {
      max1=a;
      min1=b;
    }
  else
    {
      max1=b;
      min1=a;
    }
  if(c>d)
    {
      max2=c;
      min2=d;
    }
  else
    {
      max2=d;
      min2=c;
    }
  if(max1>max2)
     if(min2>min1)
        printf("\nMin=%d Second min=%d Max=%d Second max=%d",min1,min2,max1,max2);
     else
       if(max2>min1)
	printf("\nMin=%d Second min=%d Max=%d Second max=%d",min2,min1,max1,max2);
       else
        printf("\nMin=%d Second min=%d Max=%d Second max=%d",min2,max2,max1,min1);
  else
    if(min1>min2)
        printf("\nMin=%d Second min=%d Max=%d Second max=%d",min2,min1,max2,max1);
    else
       if(max1>min2)
	printf("\nMin=%d Second min=%d Max=%d Second max=%d",min1,min2,max2,max1);
       else
        printf("\nMin=%d Second min=%d Max=%d Second max=%d",min1,max1,max2,min2);
}
 

```
## ROLL: RAHUL CHOUDHARY
### Assignment 2_a_/RAHUL CHOUDHARY/RAHUL CHOUDHARY_1195519_assignsubmission_file_Assignment2(a).c
```C++
#include<stdio.h>
/* Name- Rahul Choudhary
   Roll No.: 19AE10024
   Department: Aerospace
   Machine No.: 02 */
int main()
{
 int i,max,min,secondmin,secondmax,num;
scanf("%d",&num);
max=min=secondmin=secondmax=num;
for(i=0;i<3;i++)  /* Here what we actually are doing is comparing numbers as soon as they are 			     entered by user and keeping trackers on numbers */
{
scanf("%d",&num); 
if(num>max)     /* This Nested 'if' not only give maximum but also the second maximum mo. */
{
 if(secondmax<max)
{
secondmax=max;
}
max=num;
}
if(num<min)  /* This Nested 'if' will give minimum also update the second minimum no. while    			execution */
{
secondmin=min;
min=num;
}
if(num>min&&num<secondmax) /* This 'if' along with just above nested 'if' gives second minimum */
{
secondmin=num;
}
}
printf("Maximum No. %d\n Minimum No. %d\n Second Maximum %d\n Second Minimum %d\n",max,min,secondmax,secondmin);
return 0;
}

```
## ROLL: RAHUL NATH
### Assignment 2_a_/RAHUL NATH/RAHUL NATH_1195529_assignsubmission_file_assignment2a.c
```C++
/*Name:Rahul Nath
roll no.:19CH10033
Dept:chemical
assignment:assignment2(a)*/
#include<stdio.h>
int main()
{
  float i,j,k,l,r,m,n,o;
  printf("enter four distinct no.:\n");
  scanf("%f%f%f%f",&i,&j,&k,&l);
  if((i!=j)&&(i!=k)&&(i!=l)&&(j!=k)&&(j!=l)&&(k!=l))
    { r=i;
      if(i>j)
	{
	  r=i;
	}
      else
	{
	  r=j;
	}
      if(r<k)
	{
	  r=k;
	}
       if(r<l)
	{
	  r=l;
	}
      printf("max=%f\n",r);
      m=i;
      if((i>j)&&(i<r))
	{
	  m=i;
	}
      else if(j<r)
	{
	  m=j;
	}
       else if((m<k)&&(k<r))
	{
	  m=k;
	}
      else if(l<r)
	{
	m=l;
	}
      printf("2nd max=%f\n",m);
      n=i;
      if((i>j)&&(i<r)&&(i<m))
	{
	  n=i;
	}
      else if((j<r)&&(j<m))
	{
	  n=j;
	}
      if((k<r)&&(k<m))
	{
	  n=k;
	}
      else if((l<m)&&(l<r))
	{
	  n=l;
	}
      printf("2nd min=%f\n",n);
      o=i;
      if((i>j)&&(i<r)&&(i<m)&&(i<n))
	{
	  o=i;
	}
      else if((j<r)&&(j<m)&&(j<n))
	{
	  o=j;
	}
       if((k<r)&&(k<m)&&(k<n))
	{
	o=k;
	}
       else if((l<n)&&(l<m)&&(l<r))
	{
	o=l;
	}
      printf("min=%f\n",o);
    }
     
  else
    {
      printf("please enter valid numbers!");
      
    }
  return (0);
}

```
## ROLL: SHIVAM LAHOTI
### Assignment 2_a_/SHIVAM LAHOTI/SHIVAM LAHOTI_1195502_assignsubmission_file_assignment2a.c
```C++
#include<stdio.h>
int main()
{
  /*name- Shivam Lahoti
roll no.- 19AG10028
machine no.- 5
department- Agriculture and food engineering*/
  int a,b,c,d,max,max1,max2,sec_max,min,min1,min2,sec_min;
  printf("enter four distinct positive numbers\n");
  scanf("%d%d%d%d",&a,&b,&c,&d);
if(a>b)
  {
    max1=a;
    min1=b;
      }
 else{
   max1=b;
   min1=a;
 }
if(c>d)
  {
    max2=c;
    min2=d;
  }
 else{
   max2=d;
   min2=c;
 }
if(max1>max2)
  {
    max=max1;
    sec_max=max2;
  }
 else{
   max=max2;
   sec_max=max1;
 }
if(min1<min2)
  {
    min=min1;
    sec_min=min2;
  }
 else
   {
     min=min2;
     sec_min=min1;
   }
printf("max = %d, second max= %d, min= %d, second min= %d \n",max,sec_max,min,sec_min);
}

```
## ROLL: SHIVANI SOREN
### Assignment 2_a_/SHIVANI SOREN/SHIVANI SOREN_1195491_assignsubmission_file_minmax.c
```C++
#include<stdio.h>
/*program to find min,2nd min,max,2nd max*/
int main()
{
  int a,b,c,d,max1,max2,min1,min2;
  printf("Enter four distinct numbers : ");
  scanf("%d %d %d %d",&a,&b,&c,&d);
  if(a>b)
    {  if(a>c)
	{  if(a>d)
	    {
	      max1=a;
	      if(b>c)
		{if(b>d)
		    { max2=b;
		         if(c>d)
		         {   min1=d;
		             min2=c;
		         }
	                 else
		         {   min1=c;
		              min2=d;
		          }
		      }
		}
	     else
	      {max2=d;
		  if(c>b)
		{   min1=b;
		    min2=c;
		}
	         else
	       	{   min1=c;
		    min2=b;
		}
	    }
	  else
	    {
	      max1=d;
	      max2=a;
	      if(c>b)
		{   min1=b;
		    min2=c;
		}
	      else
		{   min1=c;
		    min2=b;
		}
	    }
	}
      else
	{
	  if(c>d)
	    {
	      max1=c;
	      max2=d;
	      if(a>b)
		{   min1=b;
		    min2=a;
		}
	      else
		{   min1=a;
		    min2=b;
		}
	    }
	  else
	    {
	      max1=d;
	      max2=c;
	      if(a>b)
		{   min1=b;
		    min2=a;
		}
	      else
		{   min1=a;
		    min2=b;
		}
	    }
	}
    }
  else
    {
      if(b>c)
	{if(b>d)
	    {  max1=b;}
	  else
	    {  max1=d;
	       max2=b;
	       if(c>a)
		{   min1=a;
		    min2=c;
		}
	      else
		{   min1=c;
		    min2=a;
		}
	    }
	}
      else
	{  if(c>d)
	    {max1=c;}
	  else
	    {max1=d;
	      max2=c;
	      if(a<b)
		{   min1=a;
		    min2=b;
		}
	      else
		{   min1=b;
		  min2=a;
		}
	    }
	}
    }
   printf("Min=%d\nSecond Min=%d\nMax=%d\nSecond Max=%d\n",min1,min2,max1,max2);
	  
      
}

```
## ROLL: SHREE HARSHA KODI
### Assignment 2_a_/SHREE HARSHA KODI/SHREE HARSHA KODI_1195487_assignsubmission_file_Assignment 2(a).c
```C++
/*Name:Kodi Shree Harsha
Roll No:19AE30009
Machine No:3
Department:Aerospace*/

#include<stdio.h>
int main()
{
  int A,B,C,D;
  printf("Enter the values of A,B,C,D:");
  scanf("%d%d%d%d",&A,&B,&C,&D);
  if(A<B)
    {if(B<C<D)
	printf("min=%d,secondmin=%d,secondmax=%d,max=%d",A,B,C,D);}	
  else if(B<D<C)
	printf("min=%d,secondmin=%d,secondmax=%d,max=%d",A,B,D,C);}
  else if(C<D<B)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",A,C,B,D);}
    else if(D<C<B)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",A,D,C,B);} 
    else if(D<B<C)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",A,D,B,C);}
else(C<B<D)
printf("min=%d,secondmin=%d,secondmax=%d,max=%d",A,C,B,D);}}
    else if(B<C)   
{ if(C<D<A)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",B,C,D,A);}
else if(C<A<D)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",B,C,A,D);}
else if(D<C<A)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",B,D,C,A);}
else if(D<A<C)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",B,D,A,C);}
else if(A<D<C)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",B,A,D,C);}
else (A<C<D)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",B,A,C,D);}}
else if(C<D)
{if(D<A<B)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",C,D,A,B);}
else if(D<B<A)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",C,D,B,A);}
else if(B<D<A)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",C,B,D,A);}
else if(B<A<D)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",C,B,A,D);}
else if(A<B<D)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",C,A,B,D);}
else(A<D<B)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",C,A,B,D);}}
else if(D<A)
{if(A<B<C)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",D,A,B,C);}
else if(A<C<B)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",D,A,C,B);}
else if(B<C<A)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",D,B,C,A);}
else if(B<A<C)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",D,B,A,C);}
else if(C<A<B)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",D,C,A,B);}
else(C<B<A)
{printf("min=%d,secondmin=%d,secondmax=%d,max=%d",D,C,B,A);}}
return(0);

}

```
## ROLL: SOHAM ZADE
### Assignment 2_a_/SOHAM ZADE/SOHAM ZADE_1195501_assignsubmission_file_program2a.c
```C++
/* Name: Soham Zade
   Roll no: 19CH10053
   Machine no: 10
   Program to find max and min numbers*/

#include<stdio.h>

int main()

{ int a, b, c, d, swap1, swap2, swap3, swapa, swapb,swapc, k;
  
  printf("Enter four distinct numbers\n");
  scanf("%d %d %d %d", &a, &b, &c, &d);

  if(b<a)
    {swap1=a; //swap1 has original a//
     a=b; 
    }
  if(c<a)
    {swap2=a; //swap2 has original b//
     a=c;
    }
  if(d<a)
    {swap3=a; //swap3 has original c//
     a=d;
    }
  if(swap2<swap1) //original b<original a//
     {swapa=swap1; //swapa has original b//
     b=swap2; 
    }
  if(swap3<b)  //original c< original b//
    {swapb=b; //swapb has original b//
      b=swap3; 
    }
  if(d<b){swapc=b; //original d< originalc//
    b=d;
  }
  if(swapb<swapa) //original b< original b//
    {k=c;
  c=swapb;}
  if(swapc<c){
    l=c;
    c=swapc;}
  if (d<c){c=d;}
     
 }
  printf("%d, %d, %d, %d", a, b, c, d);
  

	  




}

```
## ROLL: SREEYA CHILUPURI
### Assignment 2_a_/SREEYA CHILUPURI/SREEYA CHILUPURI_1195514_assignsubmission_file_a1.c
```C++
#include <stdio.h>
int main()
{int a,b,c,d;
  printf("Enter the value of 4 numbers:\n");
  scanf("%d%d%d%d",&a,&b,&c,&d);
  if(a>b && a>c && a>d )
    printf("Max=%d\n",a);
  else if(a>b && a>c && a<d)
    printf("Second Max=%d\n",a);
  else if(a<b && a<c && a<d)
	printf("Min=%d\n",a);
  else if(a<b && a<c && a>c)
	printf("Second Min=%d\n",a);
  
  if(b>a&&b>c&&b>d)
    printf("Max=%d\n",b);
	   else if(b>a&&b>c&&b<d)
	     printf("Second Max=%d\n",b);
	   else if(b<a&&b<c&&b<d)
	     printf("Min=%d\n",b);
	   else if(b<a&&b<c&&b>d)
	     printf("Second Min=%d\n",b);
  if(c>a&&c>b&&c>d)
    printf("Max=%d\n",c);
  else if (c>a&&c>b&&c<d)
    printf("Second Max=%d\n",c);
  else if (c<a&&c<b&&c<d)
    printf("Min=%d\n",c);
  else if(c<a&&c<b&&c>d)
    printf("Second Min=%d\n",c);
  
   if (d>a&&d>b&&d>a)
	printf("Max=%d\n",d);
   else if(d<a&&d>c&&d>b)
	printf("Second Max=%d\n",d);
   else if(d<a&&d<c&&d<b)
     	printf("Min=%d\n",d);
      else if(d<a&&d<b&&d>c)
	printf("Second Min=%d\n",d);
   return 0;
}

```
