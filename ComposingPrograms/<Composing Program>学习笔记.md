---
title: <Composing Program>学习笔记
notebook: AAAA
tags:
---
# Chapter 1: Building Abstractions with functions

## 1.1 Getting Started

> fundamental ideas : representing information, specifying logic to process it, designing abstractions that manage the complexity of that logic.

> These fundamental ideas have long been taught using the classic textbook Structure and Interpretation of Computer Programs (SICP).

最基础的概念是如何表达信息（数据结构），用什么样的逻辑去运算（算法？），以及想办法用抽象去降低整个逻辑的复杂度（为了人脑能处理的复杂度考虑）。所以我的任务就是关注这几个方面到底怎样去提高，能学到什么框架和方法。


### 1.1.3 interaction

> Each session keeps a history of what you have typed. To access that history, press ctrl-P (previous) and ctrl-N (next). ctrl-D exits a session, which discards this history. 

可以用ctrl-P (previous) and ctrl-N (next). ctrl-D exits a session 去了解你曾经输入的历史命令。（以前我只会用方向键，学到了）。

### 1.1.4 First example

Broadly, computer programs consist two kinds of instructions:
1. compute some value —— expressions
2. carry out some action —— statements

在这个过程中，我们会接触到：
1. data
2. Function——chapter1
3. Object(有data，也有操作data的function)——chapter2
4. Interpreter（A program that implements such a procedure, evaluating compound expressions, is called an interpreter.）——chapter3

```python

from urllib.request import urlopen

# statements(用了一个函数)，现在shakespeare是一个object
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

# statements(用了很多个函数)，现在words是一个set()object了
words = set(shakespeare.read().decode().split())

# expression 
{w for w in words if len(w) == 6 and w[::-1] in words}

```

** 分辨expression和statements感觉有个很简单的方式，就是code会不会有返回值。**

## 1.2 Elements of Programming

Program Language = 

1. a means for instructing a computer to perform tasks.
2. a framework within which we organize our ideas about computational processes. 

So programs must be written for people to read, and only incidentally for machine to exeute.（这句话就是经典的——程序应该是写给人看去交流idea，偶尔给机器跑）

从以上这段话可以看出，最重要的是idea. We should pay attention to the means that the language provides for combining simple ideas to form complex ideas.有以下三个机制：

1. primitvie expressions and statements: simplest building blocks;
2. means of combination: combine simple ones to form complex ones
3. means of abstraction: compound elements can be named and manipulated as units.

果然是好书，我以前的感觉是学会了一堆零件，自己要设计联合运用的方式（combine）要设计抽象去解决问题，但并没有章法。其实如何更好的combine、如何更好的抽象，是有方法的。


### 1.2.1 Expressions

`-1 - -1 ——> 0` 这种是operand(numbers) and mathematical operator. 特征是infix，即operator 在 operand之间。

### 1.2.2 Call expressions

`function(operand, operand) ——> value` 

比如一些数学函数 `max(9,2), pow(2,100)` , 这个特征是opertor在括号外，括号里是operand。

### 1.2.3 Importing library functions

> An import statement designates a module name (e.g., operator or math), and then lists the named attributes of that module to import (e.g., sqrt). Once a function is imported, it can be called multiple times.

function分三种：built-in（就在environment里，无需import）, python自带库（不在environment里，需要import，但不需要安装), 第三方库(不在这个机器上，需要安装，需要import)。

### 1.2.4 Names and environment
1. the simpest means of abstraction

We use '=' to do assignment statement: binding a name to a value, then this name represents this value, and using the name we can retrieving this value.functions can also be binded to names.


```
#binding的示例
>>> max
<built-in function max>

>>> f = max
>>> f
<built-in function max>
>>> f(9,2)
9
```


We can also assign multiple values to multiple names in a single statement.

```
# = 的示例
area, circumference = pi * radius * radius, 2 * pi * radius
```

2. environment = a memory tracks names,values and bindings.

为了做到以上的binding，肯定需要一个有记忆的东西去存储names,values and bindings，那么这个memory就是environment。如果没有environment，`add(x,1)` 这个statement没有任何意义，因为我们不知道x代表什么，甚至add代表什么，所以**environment的重要性在于提供程序运行的context**。

本小节很好的解释了environment的意思，其实把它看做程序运行的memeroy就行，包括import进来的function.

### 1.2.5 evaluating nested expressions

**nested expressions是一种combine的方式！**

nested expressions like `sub(pow(2, add(1, 10)), pow(2, 5))`，程序的执行过程其实用到了**recursive**, 可以画一棵expression tree来看从root到node，再从node返回到root最终得到result的过程，就是递归的过程。

### 1.2.6 The Non-Pure Print Function

There are two types of functions:
1. The Pure Function : input --> output
2. The Non-Pure Function: input -- no output(Return None), e.g. Print()

这个很好懂，有返回值和没有返回值（None）的两种函数嘛。

## 1.3 Defining New Functions

As far as we know:
- numbers and arithmetic operations are **primitive built-in data values and functions**
- nested functions provides a means of **combining operations.**
- Binding names to values/functions provides a means of **abstraction.**

就像之前说的，主线是学习这三点（重点是后两者），所以这种总结帮助我把已知的东西挂到这个框架（知识树）上。

本章重点在于A new and powerful abstraction technique —— Defining New Functions.（自定义函数是另一种强大的abstraction方式，可以把一堆操作封装抽象成一个building block/unit），给它一个名字，我们就可以用这个名字，只考虑输入输出，不用考虑一堆细节。

```
def <name>(<formal parameters>):
	(body)
	return <return expression>


# e.g.
def cal_area(x,y):
	return x*y

def g():
	return 2
```

### 1.3.1 Environments

把environments想象成一个个frame/box, 它储存了所有被assignment binding的names/values，并且track the changes。

更核心的概念是：global environment和 function自己的environment。从现在来看，global box里面会存function name 指代 function, function有自己的box，**function被call几次，就会建几个local frame**。(这也提示了以前我犯的错误，local frame也是占内存的，所以如果一个function被call 太多次，内存也会溢出。)

> This example illustrates many of the fundamental ideas we have developed so far. Names are bound to values, which are distributed across many independent local frames, along with a single global frame that contains shared names. A new local frame is introduced every time a function is called, even if the same function is called twice.

### 1.3.4 Local names

>  a function's implementation that should not affect the function's behavior.

function不管使用什么name去代表参数，behavior都一样。

但，还是要学会怎么Chosing Names，因为程序大部分时间是给人读的，良好的起名能降低人面对的complexity。

### 1.3.6 Functions as Abstractions
function被抽象作为一个unit后，the details is abstracted away，大家不再关心它的具体怎么实现，所以function要体现的是：输入，输出，作用。

> For example, any square function that we use to implement sum_squares should have these attributes:
> - The domain is any single real number.
> - The range is any non-negative real number.
> - The intent is that the output is the square of the input.


### 1.3.7 Operators
Python expressions with infix operators each have their own evaluation procedures, but you can often think of them as short-hand for call expressions.

```
from operators import add,mul
# = 2+4
print(add(2,4))
# = 4*2
print(mul(4,2))  

```


## 1.4 Designing Functions

Guidelines to a good designed function:

1. Each function should have exactly one job. That job should be identifiable with a short name and characterizable in a single line of text. Functions that perform multiple jobs in sequence should be divided into multiple functions.
2. Don't repeat yourself is a central tenet of software engineering. The so-called DRY principle states that multiple fragments of code should not describe redundant logic. Instead, that logic should be implemented once, given a name, and applied multiple times. If you find yourself copying and pasting a block of code, you have probably found an opportunity for functional abstraction.
3. Functions should be defined generally. Squaring is not in the Python Library precisely because it is a special case of the pow function, which raises numbers to arbitrary powers.

### 1.4.1 Documention

如果你用"""/"""的形式增加function的文档说明，你可以使用help(name_of_function)来获取function的文档说明。

```
def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
```


### 1.4.2 default Argument Values

`def pressure(v, t, n=6):` 可以只输入前两个arguments，此时使用默认n；也可以输入三个arguments，此时n使用输入值。