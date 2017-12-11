---
title: 学习《The AWK Programming Language》
tags: []
notebook: AAAA
---

## 阅读顺序
CP1 是 tutorial，教你怎么写awk
CP2 是 语言语法介绍
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
../data/emp.data里储存了三列数据，姓名，每小时工资，工作小时数

Beth 4.00 0

Dan 3.75 0

Kathy 4.00 10

Mark 5.00 20

Mary 5.50 22

Susie 4.25 1

#### 第一个awk程序

  * 统计所有工作小时大于0的人的工资

  `awk '$3>0 { print $1, $2*$3 } ../data/emp.data'`

  结果：

```
Kathy 40
Mark 100
Mary 121
Susie 76.
```
  * awk告诉system to run awk， ''之间是可执行的awk程序 , ../data/emp.data是input file.
  * 程序是`pattern {action} statement`： 对每一行匹配$3>0这个pattern, 匹配上就执行{}中的action。
  * 统计工作小时为0的人的姓名`awk '$3 == 0 {print $1 }' ../data/emp.data`

#### 注意

  * 可以有多个input files

假设有一个文件 ../data/emp2.data
 
```
Danny 4.00 0
Apink 5.00 20
Nine 5.50 22
Mike 4.25 18
```

输入了这个程序`awk '$3 > 0 {print $1}' ../data/emp.data e../data/mp2.data`,输出是emp 第三个field>0的第一个field，emp2 第三个field>0的第一个field。即先处理第一个文件，再处理第二个文件，最后输出

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
  `'{print "total pay for",$1, "is",$2*$3}'` ——> ','默认代表空格，可以修改，结果是：total pay for Susie is 76.5awk `'{print "total pay for"$1"is"$2*$3}' ../data/emp.data` ——> 不加逗号，就没有空格，结果是:total pay forSusieis76.5

### 1.3 fancier output

  * 使用 printf("format",value1,value2..) 来控制输出格式,format的格式和python一致。
  `awk '{ printf("total pay for %s is %.2f\n",$1,$2*$3) }' ../data/emp.data`
  `awk '{ printf("%-8s %6.2f\n", $1,$2*$3)}' ../data/emp.data` ——> %8s是8个字符的预留，右对齐；%-8s是左对齐； %6.2f是6个字符的预留，右对齐

  * 使用sort， 经试验，sort应该是按照第一个字段来排序的，所以想用什么排序，就把它放在输出的第一个字段`awk '{ printf("%6.2f %s\n",$2*$3,$1)}' ../data/emp.data | sort`
  
### 1.4 Selection
可以用在pattern里的，记住'pattern{action}'这个模式，匹配成功如果没有action就直接把匹配出的行输

  * 数字比较
  `awk '$2 >=5' ../data/emp.data` 将所有第二字段>=5的行输出`awk '$2*$3 > 50 {printf ("$%.2f for %s\n",$2*$3,$1)}' ../data/emp.data`
  * 文字匹配
  `awk '$1 == "Susie"' ../data/emp.data` 第一字段=="Susie"同时还可以用正则表达式,TODO: 见SELECTION 2.1
  * 条件组合&&-AND， ||-OR，！- NOT
  `awk '$1!="Susie" && $2 <= 4' ../data/emp.data`
  * 数据验证
  在使用数据前先通过一些测试来验证数据，把测试awk写入一个awk文件中，直接-f,如果没有error，就没有输出，就可使用。（类似测试文件）
  `NF != 3 {print $0, "number of fields is not equal to 3"}$3 < 0 {print $0, "negative hours worked"}`
  * BEGIN END 分别匹配第一个文件的第一行之前，最后一个文件的最后一行之后,注意不是同一个文件的第一行和
  最后一行可以用来生成表头和收尾语句。`awk 'BEGIN {print "NAME RATE HOURS" ; print ""} {print }' ../data/emp.data`

### 1.5 Computing
不用初始化变量，第一次使用时数字自动为0，字符串自动为nul

#### counting and computing sum/avg

  * 统计工时超过15的员工数量
  `awk '$3 > 15 {emp = emp + 1} END {printf("%d employees have workd more than 15 hours\n",emp)}' ../data/emp.data`

  * 计算平均工资(较长的程序可以写成文件执行，或用;分隔) 
  `awk '{pay = pay + $2 * $3} END { print NR, "employees";print "total pay is",pay;print "average pay is", pay/NR }' ../data/emp.data`

  * 找到最高小时工资的人
  `awk '$2 > maxrate { maxrate = $2; maxemp = $1} END { print "highest hourly rate:",maxrate,"for",maxemp }' ../data/emp.data`

#### string concatenation
`awk ' {names = names $1 " "} END {print names}' ../data/emp.data` 字符串拼接就直接是a b c，输出就是 ab

  * 输出最后一行两个都可以`awk 'END {pring $0}' ../data/emp.dataawk '{last = $0} END {print last}' ../data/emp.data`

#### built-in functions
length(string),length 可以处理一整行 length($0
`awk 'length($1)<4 {print $0}' ../data/emp.data`

#### counting lines, words, characters
`awk '{nw += NF; nc += length($0) - (NF-1)} END {print NR, nw, nc}' ../data/emp.data`

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

  * while 

新数据：amount rate year,每一年总金额为 amount*(1+rate)^year,求每一行每一年的总金额
这个程序是目前为止最像C语言程序的一个了，注意整个{}里是action, action里有n行，依次执行命令

```shell
{ i = 1 #初始化变量

print $0 #打印原始行

# i为年，当i小于总年数的时候，算总金额，并让i递增

while (i <= $3 ){

printf("\t%.2f\n", $1*(1+$2)^i)

i = i+1

}

}
```

  * for 用for重写上面计算总金额的程序

```shell
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

```shell
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

```shell
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
awk 自然用空格作为input field的分隔符，但在../data/countries.data里，必须用\t分隔符：`awk -F'\t' '{print $1,$4}' ../data/countries.data` 换言之，可以用`-F'分隔符'`来自行设置分隔符。

program format: 1,可以用分号作为一个action内多个statement的区分；2，在awk文件中为了提高可读性，可以用\来换行； 3，注释用#

```shell
{print $1, $3; print $2}

  


{print \

$1, #country name

$2} #area in thousands of square miles

  
```


### 2.1 Patterns

用Patterns去匹配每一行，若匹配成功执行对应action. 以下为六种type:

- `BEGIN {action}`
不是第一行，而是所有行之前;可以用来输出标题

- `END {action}`
不是最后一行，而是所有行结束后;可以用来输出结果

- `expression {action}`

- `compound pattern {action}`
&& and; || or; ! not

- `/regular expression/ {action}`
正则，在//之间

- `pattern1 , pattern2 {action}`
range patterns 符合pattern1的A行，后接符合pattern2的B行，A-B里的所有行执行action

#### BEGIN AND END 
注意：BEGIN和END不match任何一个输入行，它是一个位置匹配符；
用途：可以在BEGIN里定义分隔符，输出标题；

```
  1 BEGIN {FS = "\t";  #注意需要用双引号
  2         printf("%10s %6s %5s %s\n\n",
  3                "Country","AREA","POP","CONTINENT")}
  4       { area += $2; pop += $3;
  5         printf("%10s %6d %5d %s\n",
  6                $1,$2,$3,$4)}
  7 END   { printf("%10s %6d %5d\n",
  8                "TOTAL",area,pop)}

```

#### Expression
注意：
1。< <= > >= != ==可以用于数字比较，也可以用于字符串比较（数字自动转化为字符串，字符串自动转化为数字
2。~，!~ matched by , not matched by
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

```shell

2的例子
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

```shell
input:
awk -F'\t' 'FNR==2, FNR==5 {print FILENAME ":" $0}' ../data/countries.data ../data/test.data

output:（两个文件的第2-5行)
countries.data:Brazil	3286	134	South America
countries.data:Canada	3852	25	North America
countries.data:China	3705	1032	Asia
countries.data:USA	3615	237	North America
test.data:USA
test.data:PSA

```


### 2.2 Actions

#### 所有action类型列举
- expressions
constants,variables（built-in, user-defined),fields,function calls, arrary elements
+ operator

- print expression-list
- printf(format, expression-list)
打印，以及各种格式打印

- if (expression) statement
- if (expression) statement  else *statement*

- while (expression) *statement*
- do *statement* while (expression)
- for(expression;expression;expression) *statement*
- for(variable in array) *statement*

- break,continue,next,exit
- exit expressions {*statement*}

#### Expressions
主要分成primary expression 和 operators that combine expressions（已知，算术，条件?:，逻辑，匹配~/!~，++ -- ）

primary expression主要有：numberic and string constants, variables, fields, function calls, arrary elements

- Variables: Built-in, fields, User-defined
例子-field_variables.awk，用于说明为什么field也是variables.

```
BEGIN {FS = "\t"; OFS = "**"}  #FS是输入分隔符，OFS输出分隔符, BEGIN事前定义
$4 == "South America" {$4 = "SA"} # 当输入进来分隔出的$4是"South America"，将$4替换成 "SA"。 这个action里$4就是field_variables, 可以把它视作输出流中的字符串变量
$4 == "North America" {$4 = "NA"}  # 同上
{print} # 输出
```

真正输出时会吓一跳(如下)，为什么OFS只作用在了前两个pattern起作用的行呢？

```
USSA  8649  275 Asia
Brazil**3286**134**SA
Canada**3852**25**NA
China 3705  1032  Asia
USA**3615**237**NA
India 1267  746 Asia
Mexico**762**78**NA
France  211 55  Europe
Japan 144 120 Asia
Germany 96  61  Europe
England 94  56  Europe
```

把中间两个pattern去掉试试（如下），可以看到，就算我改变了OFS，如果我的输出流相对于输入流没有被改变，那么OFS是不起作用的。

```
awk 'BEGIN {FS="\t";OFS="**"} {print}' ../data/countries.data
或者 awk 'BEGIN {FS="\t";OFS="**"} {print $0}' ../data/countries.data
USSA  8649  275 Asia
Brazil  3286  134 South America
Canada  3852  25  North America
China 3705  1032  Asia
USA 3615  237 North America
India 1267  746 Asia
Mexico  762 78  North America
France  211 55  Europe
Japan 144 120 Asia
Germany 96  61  Europe
England 94  56  Europe
```

假如我就是只想改变输出流的分隔符而已呢？怎么办？(如下)，可以看到，重组输入流就可以做到。

```
awk 'BEGIN {FS="\t";OFS="**"} {print $1,$2,$3,$4}' ../data/countries.data

USSA**8649**275**Asia
Brazil**3286**134**South America
Canada**3852**25**North America
China**3705**1032**Asia
USA**3615**237**North America
India**1267**746**Asia
Mexico**762**78**North America
France**211**55**Europe
Japan**144**120**Asia
Germany**96**61**Europe
England**94**56**Europe
```


fields: $1,$2， FS（输入分隔符），OFS（输出分隔符）——> FS 也可以用 `-F'\t'`来代替
built-in: 已知的有NF, NR, FILENAME, FNR
user-defined: 自定义，不用初始化。

例子-user_defined.awk，说明自定义变量怎么用

```
$4 == "Asia" {pop += $3; count += 1}
END {printf "%d Asia countries have %d population in all.",count,pop}

output:
4 Asia countries have 2173 population in all.
```

- functions: Built-in(数字的，字符串的), User-defined
  - 字符串函数： length(s), index(s,t)-*return first position of string t in s*, split(s,a)-*split s into arrary a on FS*, sub(r,s)-*$0左侧最长可匹配r的子串用s替换，返回替换次数*, substr(s,p,n)-*return substring of s of length n starting at position p*,
  - 自定义：`function isnum(n) {return n ~ /^[+-]?[0-9]+([\\.][0-9]+)?$/}`

例子：利用../data/seed.data 来说明随机数函数怎么使用

```shell
awk '{x = rand(); print $1,x,$1*x}' ../data/seed.data    #对每个数都产生一个随机数rand()（0<=x<1），并计算两者相乘的积

4 0.840188 3.36075
5 0.394383 1.97191
7 0.783099 5.48169
82 0.79844 65.4721
5 0.911647 4.55824
45 0.197551 8.88981
75 0.335223 25.1417


awk '{print $1,srand($1)}' ../data/seed.data  #利用每个数作为种子，srand(x）重新产生一个随机数
4 0
5 4
7 5
82 7
5 82
45 5
75 45
```


例子，了解内置的字符串函数

```shell
#index(s,t) 找到t字符串在s字符串中的位置，没找到输出0
awk '{print index($0,"SA")}' ../data/test.data

output:
0
2
2

#split(s,a)，将s字符串split成a 数组，此时是用默认分隔符
awk '{split($0,a); print a[2]}' ../data/countries.data

output:
8649
3286
3852
3705
3615
1267
762
211
144
96
94

# 制作分隔符为-的文件 ../data/countries_2.data
awk 'BEGIN {FS="\t";OFS="-"}  {print $1,$2,$3,$4}' ../data/countries.data > ../data/countries_2.data

# split(s,a,fs)，将s字符串split成a 数组，此时用fs作为分隔符。但神奇的是如果分隔符是"**"，尝试都失败了。换成"-"分隔符就成功了。
awk '{split($0,a,"-"); print a[2]}' ../data/countries_2.data
8649
3286
3852
3705
3615
1267
762
211
144
96
94


# substitution:  gsub-global sub  sub-sub leftmost longest; 这两个的区别就是 global sub是将该行所有匹配的都replace掉；sub是replace掉第一个碰到的匹配，然后就结束，不再往右匹配。源文件未改动，输出文件改动，返回的是改动次数
../data/substitution.data 长以下这样
USASA
USA
SAPSA

## gsub(r,s)
awk '{print gsub(/SA/,"*"); print }' ../data/substitution.data
output:
2
U**
1
U*
2
*P*

## sub(r,s)  substitution = replacement
awk '{print sub(/SA/,"*"); print }' ../data/substitution.data 
output:
1
U*SA
1
U*
1
*PSA

# sprintf 按照格式输出，但不打印，一般输出给变量
awk '{x = sprintf("%10s %6d",$1,$2); print NR ":" x}' ../data/countries.data
1:      USSA   8649
2:    Brazil   3286
3:    Canada   3852
4:     China   3705
5:       USA   3615
6:     India   1267
7:    Mexico    762
8:    France    211
9:     Japan    144
10:   Germany     96
11:   England     94


# substr(s,p,n)——> 其实就是s[p:n]，但不把分隔符算为一个字符
awk '{print substr($0,2,4)}' ../data/countries.data
output:
SSA
razi
anad
hina
SA  3
ndia
exic
ranc
apan
erma
ngla
```

- Number or String?

awk中不需要手动转类型，数字和字符串会以当下需求**自动转类型**。
例子1: number -> string  比如concatenated `{print $1 "-" $2}` 本来是作用在string上，但如果$1,$2是数字，会自动转成字符串。
例子2: string -> number  比如+，-这种算数运算符，如果 `{print "100"+$2}` 中$1为string, 它会自动转为数字。(如果是”100“这样的，就直接转成100，如果是”asia"这样的，就转化为0)
例子3: **==**作为比较，如果两方有一方是string，就会按照string 的比较来；如果两方都是number，才会按照number来比较。可以强制通过例1和例2的方式来转换：`$1 "" ——>将$1强制转成string； $1 + 0 ——>将$1强制转化为number.`
变量自动初始化为**null/0**,视第一次用到的方式定。

- Summary of Operator
几个不怎么熟悉的重点：
**in**, `i in arr`, if a[i] exists, 0 otherwise;
例子：`awk '$4 =="Asia" {a[i] = $1;i++} END {print 5 in a}' ../data/countries.data` 将亚洲的国家名都放在一个数组里，并测试数组的长度（是否有a[5]）

**||,&&,!**, OR, and , NOT
**()**, `($1)++`，为什么要用括号呢？ 一个返回负数绝对值的语句 `$1<0 {print "abs($1)= " -$1}`，很容易被看作是concatenate; 如果这时候改成 `$1<0 {print "abs($1)= " (-$1)}` 就消除歧义了。

- Control-Flow Statements
> 试过了几个例子之后，发现有一点特别需要注意，变量不需要初始化，第一次使用时就自动为 0/null，但awk里的数组是从1开始的，换言之，在未初始化i时你不能直接用a[i],此时i=0, 在涉及到数组时，必须在BEGIN里初始化i=1，再用在数组上。


**if (expression) statement1 ;else statement2**, 注意**else 跟紧最近的那个if**,如`if (e1)  if(e2) s =1 ; else s = 2`, 那么else 是和第二个if跟紧的。第二个if和else是属于第一个if的statement1。(为了消除歧义，复杂的awk程序最好还是写成文件，使用缩进。)

例子：`awk 'BEGIN {i=1} $4 =="Asia" {a[i] = $1;i++} END {if (3 in a) if (5 in a) print "ok"; else print "no" }' ../data/countries.data`

**while (e1) statement1**

例子：`awk 'BEGIN {i=1} $4 =="Asia" {a[i] = $1;i++} END { while (j in a) {print a[j];j++} }' ../data/countries.data`
注意，多行statement可以用{}包裹，用;分隔。

**for(e1;e2;e3) statement1**
例子: `awk 'BEGIN{i=1} $4 =="Asia" {a[i] = $1;i++} END { for(j=1;j<i;j++) print a[j] }' ../data/countries.data`

**do statement1 while(e1)**
例子: `awk 'BEGIN {i=1;j=1} $4 =="Asia" {a[i] = $1;i++} END { do {print a[j];j++} while (j<i)} ' ../data/countries.data`


**for(variable in array) statement1， variable是下标，不是python里的element**
例子：`awk 'BEGIN {i=1} $4 =="Asia" {a[i] = $1;i++} END { for (j in a) {print a[j]} }' ../data/countries.data`

**重点 next, exit**
next是直接输入下一行，exit是停止输入。
exit例子：属于Asia的有四个国家：USSA、China、India、Japan，但程序设计为有三个后就停止输入，输出最后一个国家名称。
`awk 'BEGIN {i=1} $4 =="Asia" {k = $1; i++; if(i>3) exit} END{print k} ' ../data/countries.data`
输出为：India

next的例子：碰到属于Asia的有四个国家就直接输入下一行，并且输出.(有点像if的break一样)
`awk '{if($4 =="Asia") next;print $0} ' ../data/countries.data`
输出为：

```
Brazil  3286  134 South America
Canada  3852  25  North America
USA 3615  237 North America
Mexico  762 78  North America
France  211 55  Europe
Germany 96  61  Europe
England 94  56  Europe

```

- Empty Statement
直接用;表示empty statement，仅占位，没有其他意义。猜测和python中的pass类似。
无法直接复现书中的例子，将FS改成","后能够复现：打印出有空field的行

```
BEGIN {FS=","}  #将分隔符改成,
{for(i=1; i<=NF && $i != ""; i++)  #遍历每行的field，如果遇到行尾或该field是空，跳出
    ;                              # 仅仅是遍历，什么也不执行
  if(i<=NF)                        # 如果跳出了，说明有field为空，就打印该行
    print }
```

- Arrays
普通意义上的理解：一维数组，无需事先声明，可以储存string和number（但注意不要用0作为下标）

```
#逆转输出各行
{a[NR] = $0}
END {for (i=NR; i>0; i--) print a[i]}

```

**高级的地方在于：它的下标可以是string！！！**

```
# 用string作为subscript的例子
/Asia/ {pop["Asia"] += $3}
/Europe/ {pop["Europe"] += $3}
END {print "Asia population is ",pop["Asia"],"million."
     print "Europe population is ",pop["Europe"],"million."
     }


# 一个和上面完全相同的作用的例子
{pop[$4] += $3}  #直接用$4的值作为subscript
END {for (name in pop) #遍历数组的所有subscript
        print name,pop[name]}

# 使用if (element in array)
awk '{pop[$4] += $3} END {if ("Asia" in pop) print pop["Asia"]}' ../data/countries.data
output
South 134
Asia 2173
North 340
Europe 172


# 使用 delete pop[element]
awk '{pop[$4] += $3} END {if ("Asia" in pop) delete pop["Asia"]; for (name in pop) print name,pop[name]}' ../data/countries.data
=====
outupt
South 134
North 340
Europe 172
```


**利用split(string,arr,fs)来创建数组**
需要注意的是, "aaa,bbb,vvv"作为split($0,arr,",")的输入时，arr的下标是"1"-aaa,"2"-bbb,"3"-vvv；即自动生成数字下标
如果是多行一起用arr的话，arr只会保存最后一行的split结果。

```
awk '{split($0,arr,","); for (name in arr) print name,arr[name]}'
input:aa,bb,cc
output:
2 bb
3 cc
1 aa
```

**不支持多维数组时的一种代替方法**
使用两个下标拼接作为一个下标使用: "i,j" 作为arr的下标。(注意，拼接后是12，32，而不是"1,2")

```
#将每行用,分隔存入数组，下标为行数列数
BEGIN {FS = ","}
{for(i=1;i<=NF;i++)
    a[NR,i] = $i}
#打印第二行的数据
END {for (name in a) {
        split(name,k,SUBSEP) #将拼接的下标拆出来
        if(k[1] == "2")
            print a[name]}}
```

### 2.3 User-Defined Functions
自己创建函数，通过例子来说明。 **注意: function中是local variables，必须涵盖在函数名后括号里的参数表内，仅在函数之内生效,如果没有在参数表中声明，那么就是全局变量**

```
#input:m,n
#output:max(m,n)

function max(m,n) {
  return m>n ? m:n     #也可以用 if(m>n) return m; else return n来代替
}

#试一下不在参数表的函数
#如果$1 > $2 ，那么返回$1；不然就返回0
{print max($1)}
function max(m) {
  return m>$2 ? m:0     
}

```

### 2.4 Output(print,printf)
The *print* and *printf* generate output. The *print* statement is used for simple output; the *printf* statement is used when careful formatting is required.

- 注意
1. 直接打印在终端内：`print ....   printf(...) `;
2. 输出给文件：`print.. > filename; printf(...) > filename`
3. 添加到文件后面（而不是overwritting)：`print... >> filename' printf(...) >> filename`
4. 输出给管道，作为另一个command的输入:`print... | command; printf(...) | command`
5. 当同一个文件中需要写入file/pipe，之后又需要read的时候，需要关闭file/pip: `close(expr)`


例子2： 所有>和>>后的被视作文件名,`{print $1,$2 > $3}` 意味着打印$1,$2到$3命名的文件中，也可以用"> / >> filename"直接输出 `{print $1,$2 > ($3 > 100 ? "bigpop.data" : "smallpop.data")}`

```
awk 'BEGIN{FS = "-";OFS="\t"}  {print $1,$2,$3 >> $4}' ../data/countries_2.data
# 将1，2，3添加到以4为命名的文件后
# 换言之，直接就可以用4去分类生成文件。

输出为：
文件：Asia
USSA    8649    275
China   3705    1032
India   1267    746
Japan   144 120
```

例子4: 输出给管道, **注意是直接跟在print后面|，command需要加双引号**
`awk -F="," '{print $1,$2 | "sort"}' ../data/empty_statement.data`

- OFS and ORS
OFS 是输出的field分隔符(Output field seperator)； ORS 是输出的行分隔符(Output record seperator), 一般在BEGIN里定义
**输入的field分隔符是FS**
`awk 'BEGIN{FS = "-"; OFS="\t" ; ORS = "\n\n"}  {print $1,$2}' ../data/countries_2.data`

- *print*
print expr1,expr2,...,exprn
print (expr1,expr2,...,exprn) (**当有operator时可以优先用括号**)

- *printf*
printf format,expr1,expr2,...,exprn
printf (format,expr1,expr2,...,exprn) 

**format**
- %c ASCII
- %d decimal
- %e d.dddde+1
- %f float
- %s string
- %o octal number; %x hexadecimal number

- %-a.b a代表空档有几格；- 代表左对齐，没有-代表右对齐； .b代表小数点后几位，用0补齐，不想用0补齐可以用%.6g

### 2.5 Input

awk 接受几种input：
- 直接输入data／file  `awk 'program' data`
- pipe 输入data  `command | awk 'program' `
- 一行接受一行接受 `awk 'program' `

**输入的field分隔符是FS, 输入的行分隔符是RS**

- FS默认是blank，可以设置FS = "\t", 但如果FS被设置成为超过一个字符的字符串，这个字符串就被视作是正则。

```
示例：如果FS被设置成为超过一个字符的字符串，这个字符串就被视作是正则。
../data/fs.data 被设置成通过两个连续数字进行分隔的文件

sdasf12dfafas34ada2sdfa44
afdasgasdg11dsfadsg33dfa2adfag33

awk 'BEGIN { FS = "[0-9][0-9]" } {print $1,$2,$3}' ../data/fs.data  #但\d\d就错了，奇怪

结果：
sdasf dfafas ada2sdfa
afdasgasdg dsfadsg dfa2adfag
```


- RS是行分隔符，默认是newline(\n)， 但也可以设置成其他的分隔符（比如\t,\3)，这样每一行就变了，然后再设FS也可。

```
示例：原来这个数据行分隔符是\n，列分隔符是\t，将行分隔符改成\t，即将每个field都变成一行

awk 'BEGIN {RS = "\t"} {print  }' ../data/countries.data

结果：
USSA
8649
275
Asia
Brazil
3286
134
South America
Canada

```

## CP 3

### 3.1 Data Transformation and reduction

  * Summing columns 计算每列的和注意数组自动初始化为0；同时注意最后格式输出。
  * Sum2 check每列的fields是否和第一列一致，输出1-第一列最大列数的每列和

  `condition ? A:B `条件为真就执行A，条件为假就执行B，这段是在printf中也能条件判断。 **注意，python中不可用**



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

  

