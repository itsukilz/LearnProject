---
title: 学习《The AWK Programming Language》
tags: []
notebook: AAAA
---

## 阅读顺序
CP1 是 tutorial，教你怎么写aw
CP2 是 语言语法介
余下是awk各种应用

## 进度记录

  * 2017-10-11 1.1
  * 2017-10-11 1.2～1.5
  * 2017-10-12 1.6
  * 2017-10-13 1.7
  * 2017-10-14 1.8～1.9 CP1结束
  * 2017-10-16 CP3 开始
  * 2017-10-17 CP3尝试结束，CP2开始
  * 2017-10-18 CP2.1

  

## CP1

### 1.1 Getting Started
emp.data里储存了三列数据，姓名，每小时工资，工作小时数
Beth 4.00 0Dan 3.75 0Kathy 4.00 10Mark 5.00 20Mary 5.50 22Susie 4.25 1

#### 第一个awk程序

  * 统计所有工作小时大于0的人的工资`awk '$3>0 { print $1, $2*$3 } emp.data'`结果：Kathy 40Mark 100Mary 121Susie 76.

  * awk告诉system to run awk， ''之间是可执行的awk程序 , emp.data是input file.
  * 程序是`pattern {action} statement`： 对每一行匹配$3>0这个pattern, 匹配上就执行{}中的action。
  * 统计工作小时为0的人的姓名`awk '$3 == 0 {print $1 }' emp.data`

#### 注意

  * 可以有多个input files假设有一个文件emp2.data
 
```
Danny 4.00 0
Apink 5.00 20
Nine 5.50 22
Mike 4.25 18
```

输入了这个程序`awk '$3 > 0 {print $1}' emp.data emp2.data`,输出是emp 第三个field>0的第一个field，emp2 第三个field>0的第一个field。即先处理第一个文件，再处理第二个文件，最后输出

  * 三种执行方式第一种是常见的 `awk 'program' file1 file2`第二种是 `awk 'program'`，然后一行输入，执行，输出。第三种是`awk -f awkprogramfile file1 file2`，如果程序太长，可以将''中的内容存在awkprogramfile中，直接用-f 参数执行。
  * awk有自己的语法，如果程序出现语法错误，会报syntax error错误。

### 1.2 Simple Output
本节是各种小练习

  * Printing every line
  `'{ print }' / { print $0 } `, $0 = the whole line
  * Printing certain fields
  `{print $1, $3}`
  by default, output fields are seperated by blank, each line ends with a newline character, all this can be changed.
  * NF = numbers of fields , started by 1
  `{print NF, $NF} `即打印这一行的字段数，及输出最后一个字段`{print NF, $(NF-1)}` 即打印这一行的字段数，及输出倒数第二个字段
  * NR = number of counts lines read so far，行号
  `{print NR, $0 } `, 输出行号及该行全行
  * computing , 
  fields之间可以计算,并将计算结果输出`{print $2*$3}`
  * putting text in the output
  `'{print "total pay for",$1, "is",$2*$3}'` ——> ','默认代表空格，可以修改，结果是：total pay for Susie is 76.5awk `'{print "total pay for"$1"is"$2*$3}' emp.data` ——> 不加逗号，就没有空格，结果是:total pay forSusieis76.5

### 1.3 fancier output

  * 使用 printf("format",value1,value2..) 来控制输出格式,format的格式和python一致。
  `awk '{ printf("total pay for %s is %.2f\n",$1,$2*$3) }' emp.data`
  `awk '{ printf("%-8s %6.2f\n", $1,$2*$3)}' emp.data` ——> %8s是8个字符的预留，右对齐；%-8s是左对齐； %6.2f是6个字符的预留，右对齐

  * 使用sort， 经试验，sort应该是按照第一个字段来排序的，所以想用什么排序，就把它放在输出的第一个字段`awk '{ printf("%6.2f %s\n",$2*$3,$1)}' emp.data | sort`
  
### 1.4 Selection
可以用在pattern里的，记住'pattern{action}'这个模式，匹配成功如果没有action就直接把匹配出的行输

  * 数字比较
  `awk '$2 >=5' emp.data` 将所有第二字段>=5的行输出`awk '$2*$3 > 50 {printf ("$%.2f for %s\n",$2*$3,$1)}' emp.data`
  * 文字匹配
  `awk '$1 == "Susie"' emp.data` 第一字段=="Susie"同时还可以用正则表达式,TODO: 见SELECTION 2.1
  * 条件组合&&-AND， ||-OR，！- NOT
  `awk '$1!="Susie" && $2 <= 4' emp.data`
  * 数据验证
  在使用数据前先通过一些测试来验证数据，把测试awk写入一个awk文件中，直接-f,如果没有error，就没有输出，就可使用。（类似测试文件）
  `NF != 3 {print $0, "number of fields is not equal to 3"}$3 < 0 {print $0, "negative hours worked"}`
  * BEGIN END 分别匹配第一个文件的第一行之前，最后一个文件的最后一行之后,注意不是同一个文件的第一行和
  最后一行可以用来生成表头和收尾语句。`awk 'BEGIN {print "NAME RATE HOURS" ; print ""} {print }' emp.data`

### 1.5 Computing
不用初始化变量，第一次使用时数字自动为0，字符串自动为nul

#### counting and computing sum/avg

  * 统计工时超过15的员工数量
  `awk '$3 > 15 {emp = emp + 1} END {printf("%d employees have workd more than 15 hours\n",emp)}' emp.data`

  * 计算平均工资(较长的程序可以写成文件执行，或用;分隔) 
  `awk '{pay = pay + $2 * $3} END { print NR, "employees";print "total pay is",pay;print "average pay is", pay/NR }' emp.data`

  * 找到最高小时工资的人
  `awk '$2 > maxrate { maxrate = $2; maxemp = $1} END { print "highest hourly rate:",maxrate,"for",maxemp }' emp.data`

#### string concatenation
`awk ' {names = names $1 " "} END {print names}' emp.data` 字符串拼接就直接是a b c，输出就是 ab

  * 输出最后一行两个都可以`awk 'END {pring $0}' emp.dataawk '{last = $0} END {print last}' emp.data`

#### built-in functions
length(string),length 可以处理一整行 length($0
`awk 'length($1)<4 {print $0}' emp.data`

#### counting lines, words, characters
`awk '{nw += NF; nc += length($0) - (NF-1)} END {print NR, nw, nc}' emp.data`

### 1.6 Control-Flow Statements
语法和C语言完全一致，可以通用，且 只能用于action

  * if-else统计所有时薪大于$6的员工的数量，输出总工资和平均工资。如果n=0，平均工资无法计算（总工资计算也无意义），所以需要条件判断一下
```
$2 > 6 {n = n +1 ; pay = pay + $2 * $3}

END { if (n > 0)

print n,"employees total pay is",pay,

"average pay is",pay/n

else

print "no employees are paid more than $6/hour"

}
```

  * while 新数据：amount rate year,每一年总金额为 amount*(1+rate)^year,求每一行每一年的总金
这个程序是目前为止最像C语言程序的一个了，注意整个{}里是action, action里有n行，依次执行命
```
{ i = 1 #初始化变量

print $0 #打印原始行

# i为年，当i小于总年数的时候，算总金额，并让i递增

while (i <= $3 ){

printf("\t%.2f\n", $1*(1+$2)^i)

i = i+1

}

}
```

  * for 用for重写上面计算总金额的程
```
{ print $0 #打印原始行

  


# i为年，当i小于总年数的时候，算总金额，并让i递增

for(i=1; i<=$3; i=i+1){

printf("\t%.2f\n", $1*(1+$2)^i)

}

}

```


### 1.7 Arrays
awk里可以用数组了，而且看样子还不用初始化，直接用就可以了。比如：以输入顺序的反向输出
需要注意的是，一个awk程序里有多个pattern-action,按顺序实现自己的作用，比如一下就有两个action
```
{

line[NR] = $0 #创建一个数组line，将每行用NR作为下标存储

}

END {

for(i=NR; i>=1; i=i-1){

print line[i]

}

}
```

### 1.8 One-liners

  * 14 交换$1 $2，然后输出交换后的每一行
这题我的思路是将3-NF的拼接在一起，最后输出2，1，拼接

  


  

```
{ a = Null;

for(i=3; i<=NF; i+=1){ 

a = a $i

} 

print $2,$1,a

}

  


书上的思路是$1 $2只是容器，可以直接交换容器内容后输出

  


  


`{temp = $1; $1 = $2; $2 = temp; print $0}`

  
```

明显书的思路比我的简单，我的比较复杂；知道了14题的操作，15题就很简单了;

  


  



  * 15 print everyline with the first field replaced by the line number
  `{$1 = NR; print}`

  * 16 print everyline after erasing the second field;
  `{$2 = Null; print}`


### 1.9 本章总结-awk的基本思想

  * 每个awk程序都是一系列pattern-action语句
  * 对每行input，检查pattern，符合就执行action，直到程序结束； pattern为空即所有行都满足，{action}也肯能为空。
  * awk自然的将每行切分为fields

## CP 2 The awk language
awk 自然用空格作为input field的分隔符，但在countries.data里，必须用\t分隔符：`awk -F'\t' '{print $1,$4}' countries.data`

program format: 1,可以用分号作为一个action内多个statement的区分；2，在awk文件中为了提高可读性，可以用\来换行； 3，注释用#

```
{print $1, $3; print $2}

  


{print \

$1, #country name

$2} #area in thousands of square miles

  
```


### 2.1 Patterns

string 的比较通常是ASCII码比较，比如"Canada" < "China"，可以通过终端的sort了解（第一个field，从小到大排序）。

#### String-Match patterns
本章重点是：回顾正则怎么写，下一本需要好好看的书是：《精通正则表达式》

1. 某一行和/正则/的匹配：'/regex/'
2. 表达式结果和/正则/的匹配: 'expression ~ /regex/'
3. 表达式结果和/正则/的不匹配: 'expression !~ /regex/'

#### Range Patterns
试了多个例子之后，了解到pat1,pat2的工作原理： 从pat1匹配成功的A行开始（包括A行）之后的每行去匹配pat2，直到B行匹配成功，输出包括A和B的AB之间的所有行；

容易误解的几种情况：

1. A行和B行是同一行：A行不仅能匹配成功pat1，也能匹配成功pat2,那么这个A-pat1,A-pat2结果就直接输出A一行；
2. A-pat1,B-pat2的模式匹配多处，比如1-pat1,2-pat2; 4-pat1,7-pat2，那么按顺序输出1-2，4-7。但第二处匹配必须从第一处匹配结束的后一行开始。

```2的例子
U
USA
PSA

pat1:/^U/
pat2:/SA$/

很明显，1-pat1,2-pat2; 但同时 2-pat1，2-pat2;
但输出直接是：1,2

```


3. pat2只在pat1匹配成功的那行开始往后匹配，所以如果无pat1匹配成功，输出为空；
4. pat1有匹配-A，pat2无匹配，那么输出为A-最后一行


另一种使用方式，对特定一系列行进行操作：FNR是目前这个文件读的行数（NR是目前为止所有读的行数）,FILENAME是当前文件的名称；

```
input:
awk -F'\t' 'FNR==2, FNR==5 {print FILENAME ":" $0}' countries.data test.data

output:（两个文件的第2-5行)
countries.data:Brazil	3286	134	South America
countries.data:Canada	3852	25	North America
countries.data:China	3705	1032	Asia
countries.data:USA	3615	237	North America
test.data:USA
test.data:PSA

```


### 2.2 Actions


## CP 3

### 3.1 Data Transformation and reduction

  * Summing columns 计算每列的和注意数组自动初始化为0；同时注意最后格式输出。
  * Sum2 check每列的fields是否和第一列一致，输出1-第一列最大列数的每列和
  `condition ? A:B `条件为真就执行A，条件为假就执行B，这段是在printf中也能条件判断



```
#sum2 - check that each line has the same fields as line one
4 NR == 1 {nfone = NF}

3 { if(NF != nfone)

2 printf("#%d does not has the same number of fields as line one\n",NR)

1 for(i=1; i<=NF; i++){

6 sum[i] += $i}}

1 END { for(j=1; j<=nfone; j++){

2 printf("%g%s",sum[j], j < nfone ? "\t":"\n")}}

```
 
  * Sum3 function，正则判断n是否是数字的函数（书上是整数判断，我改成了整数+小数的）`function isnum(n) {return n ~ /^[+-]?[0-9]+(\\.[0-9]+)?$/)`

题意是每一行格式都和第一行一致，那么判断哪一列不是数字，输出--，哪一列是数字，输出该列的

```
18 # sum3 - print sums of numberic columns

17 NR == 1 {nfone = NF

16 for(i=1; i<=nfone; i++){

15 numcol[i] = isnum($i)}}

14

13 {for(j=1;j<=nfone;j++){

12 if(numcol[j])

11 sum[j] += $j

10 }

9 }

8

7 END {for(i=1;i<=nfone; i++){

6 if(numcol[i])

5 printf("%d",sum[i])

4 else

3 printf("\--")

2 printf(i < nfone ? "\t":"\n")}

1 }

19 function isnum(n) {return n ~ /^[+-]?[0-9]+([\\.][0-9]+)?$/}
```

  * Exercise 
    * 3-1 ignore the blank lines NF != 0 {..}
    * 3-2 add more general regular expression for a number. how does it affect the running time ?todo
    * 3-3 去掉第二个for循环的numcol判断有何影响？ 没有影响；
    * 3-4 假设有个文件每行是 item-quantities的pair, 要求输出每单个item的总重量并按字母序排序。？todo 决定回去先看cp2

  

