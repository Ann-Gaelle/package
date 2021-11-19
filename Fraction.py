#!/bin/env python3
import numpy as np

class Fraction :
    def __init__(self,*args) : #Initalisation direct via parametre
    #nd(type(args[1])==int or type(args[1])==float)and(type(args[0])==int or type(args[0])==float)
        """Si vous souhaitez mettre l'initialisation en argument, commencez par le numérateur et ensuite le denominateur"""
        if (len(args)>1):
            self._num=args[0]
            self._den = args[1]
            self._warning=False
            if self._den==0:
                x=input("Attention vous divisez par 0 ! Souhaitez vous entrez un nouveau dénominateur ?(O pour oui)")
                if x=='O':
                    self._den = int(input("Dénominateur"))
                else:
                    raise TypeError("Division par zéro")
            self.correction()
        else:
            self._num=int(input("Numérateur ?"))
            self._den = int(input("Dénominateur ?"))
            self._warning=False
            if self._den==0:
                x=input("Attention vous divisez par 0 ! Souhaitez vous entrez un nouveau dénominateur ?(O pour oui)")
                if x=='O':
                    self._den = int(input("Dénominateur"))
                else:
                   raise TypeError("Division par zéro")
            self.correction()
   
    def __str__(self):
        if self._den==1:
            return f"{int(self._num)}"
        if self._den==0:
            return f"Attention votre fraction divise {self._num} par 0 "
        if self._num<0:
            if self._den<0:
                return f"{abs(self._num)}/{abs(self._den)}"
            else:
                return f"-{abs(self._num)}/{self._den}"
        elif self._den<0:
            return f"-{self._num}/{abs(self._den)}"
        else:
            return f"{self._num}/{self._den}"
    def inverse(self):
        return Fraction(self._den,self._num)

    def PGCD(self):
        #Il faut trouver les PGDC
        a=self._num
        b=self._den
        while b!=0:
            t=b
            b=a%b
            a=t
        return a

    def __add__(self,z):
        if isinstance(z, Fraction):
            F=Fraction(self._num*z._den+self._den*z._num,self._den*z._den)
        elif isinstance(z,int) or isinstance(z,float):
            F=Fraction(self._num+z*self._den,self._den)
        return F

    def __iadd__(self,z):
        if isinstance(z, Fraction):
            self._num=self._num*z._den+self._den*z._num
            self._den=self._den*z._den
        elif isinstance(z,int) or isinstance(z,float):
            self._num=self._num*z*self._den
            self._den=self._den
        return self

    def __mul__(self,z):
        if isinstance(z, Fraction):
            return Fraction(self._num*z._num,self._den*z._den)
        elif isinstance(z,int) or isinstance(z,float):
            return Fraction(self._num*z,self._den)

    def __neg__(self):
        return Fraction(-self._num,self._den)
    def __eq__(self,z):
        return self._num==z._num and self._den==z._den

    def __sub__(self,z):
        return self + -z

    def __lt__(self,z):
        return self._num/self._den < z._num/z._den
    
    def __gt__(self,z):
        return self._num/self._den <= z._num/z._den

    def __le_(self,z):
        return self._num/self._den > z._num/z._den

    def __ge__(self,z):
        return self._num/self._den >= z._num/z._den    

    def correction(self):
        pgcd=self.PGCD()
        self._num=int(self._num/pgcd)
        self._den=int(self._den/pgcd)
